#!/usr/bin/env bash
# start-egui: checks the new project, then removes what the skill installer left behind.
#
#   bash <skill>/scripts/finish.sh        from the project root, after `cargo build`
#
# Runs, stopping at the first failure: cargo fmt (then --check), cargo clippy --all-targets
# -- -D warnings, cargo test, cargo build, a 5-second smoke run (the window must stay open;
# skipped without a display) and, in a Git repository, git diff --check.
# When every step passes, it deletes .agents/ and skills-lock.json, unless .agents/ holds
# something besides this skill.
# Prints one line per step, then RESULT ok, or the error and RESULT failed: <step>.
set -uo pipefail

logs=""

fail() { # fail <step> <reason> [log file]
    printf '%-8s FAILED  %s\n' "$1" "$2"
    if [ -n "${3:-}" ]; then
        echo "--- last lines of the output:"
        tail -n 40 "$3"
    fi
    echo "RESULT failed: $1"
    exit 1
}

step() { # step <name> <command...>: runs the command, output to a log
    local name="$1" start=$SECONDS code
    shift
    if "$@" >"$logs/$name.log" 2>&1; then
        printf '%-8s ok      %ss\n' "$name" "$((SECONDS - start))"
    else
        code=$?
        fail "$name" "$* (exit $code)" "$logs/$name.log"
    fi
}

format() { cargo fmt && cargo fmt --check; }

window() { # the app must still be running after 5 seconds; then it is closed
    local pid waited=0 code
    case "$(uname -s)" in
        Linux | *BSD)
            if [ -z "${DISPLAY:-}" ] && [ -z "${WAYLAND_DISPLAY:-}" ]; then
                printf '%-8s skipped (no display)\n' window
                return
            fi
            ;;
    esac
    cargo run --quiet >"$logs/window.log" 2>&1 &
    pid=$!
    while [ "$waited" -lt 5 ]; do
        sleep 1
        waited=$((waited + 1))
        if ! kill -0 "$pid" 2>/dev/null; then
            wait "$pid"
            code=$?
            fail window "the app closed after ${waited}s (exit $code)" "$logs/window.log"
        fi
    done
    kill "$pid" 2>/dev/null
    wait "$pid" 2>/dev/null
    printf '%-8s ok      stayed open 5s\n' window
}

cleanup() { # deletes .agents/ and skills-lock.json when they hold only this skill
    local entry extra="" skills
    if [ ! -e .agents ] && [ ! -e skills-lock.json ]; then
        printf '%-8s ok      nothing to remove\n' cleanup
        return
    fi
    for entry in .agents/* .agents/.[!.]* .agents/skills/* .agents/skills/.[!.]*; do
        [ -e "$entry" ] || continue
        case "$entry" in
            .agents/skills | .agents/skills/start-egui) ;;
            *) extra="$extra ${entry#.agents/}" ;;
        esac
    done
    if [ -f skills-lock.json ]; then
        skills="$(grep -c '"skillPath"' skills-lock.json || true)"
        if [ "${skills:-0}" -gt 1 ]; then extra="$extra (skills-lock.json lists $skills skills)"; fi
    fi
    if [ -n "$extra" ]; then
        printf '%-8s skipped: .agents/ also holds:%s. Ask before deleting .agents/ and skills-lock.json\n' \
            cleanup "$extra"
        return
    fi
    rm -rf .agents skills-lock.json
    printf '%-8s ok      removed .agents/ and skills-lock.json\n' cleanup
}

main() {
    if [ ! -f Cargo.toml ] || [ ! -d apps ]; then
        fail start "run it from the project root (no Cargo.toml and apps/ here)"
    fi
    logs="$(mktemp -d)"
    trap 'rm -rf "$logs"' EXIT

    step fmt format
    step clippy cargo clippy --all-targets -- -D warnings
    step test cargo test
    step build cargo build
    window
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        step git git diff --check
    else
        printf '%-8s skipped (not a Git repository)\n' git
    fi
    # The very last change to the folder. This script may live inside .agents/: bash has
    # already read all of main, so deleting the file does not stop it.
    cleanup
    echo "RESULT ok"
}

main "$@"
