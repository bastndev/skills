#!/usr/bin/env bash
# start-egui: copies the template into the current folder (the project root) and fills it in.
#
#   bash <skill>/scripts/scaffold.sh --defaults
#       Writes nothing. Prints each value's default as KEY=VALUE, an INVALID= line for a value
#       that breaks a rule, and a FOLDER= line saying whether the folder is ready.
#
#   bash <skill>/scripts/scaffold.sh [--display-name "Photo Lab"] [--machine-name photo-lab]
#                                    [--crate-prefix app] [--github-repo owner/repo]
#                                    [--description "One sentence."] [--author "Name"]
#                                    [--year 2026] [--overwrite]
#       Writes every template file, named after MACHINE_NAME, with every placeholder filled in,
#       and makes the scripts executable. A value left out uses its default. Never touches files
#       that are not in the template. Ends with "scaffold: ok" and the values used, as KEY=VALUE.
#
# Exit codes: 0 done; 1 a value is invalid (the message says which); 2 the folder needs the
# person's decision: rerun with --overwrite only after they agree.
set -euo pipefail

die() { # die <exit code> <message>
    local code="$1"
    shift
    echo "scaffold: $*" >&2
    exit "$code"
}

need() { # need <option> [value]: the option must be followed by a value
    if [ $# -lt 2 ]; then die 1 "$1 needs a value"; fi
}

# Escapes a value for the replacement side of a sed `s|...|...|` command.
esc() { printf '%s' "$1" | sed -e 's/[\\|&]/\\&/g'; }

github_repo() { # github_repo <root> <machine name>: owner/repo from the origin remote, if GitHub
    local url
    url="$(git -C "$1" remote get-url origin 2>/dev/null || true)"
    case "$url" in
        *github.com:*/* | *github.com/*/*)
            printf '%s' "$url" | sed -e 's#^.*github\.com[:/]##' -e 's#/*$##' -e 's#\.git$##'
            ;;
        *) printf 'bastndev/%s' "$2" ;;
    esac
}

problems() { # prints one line per invalid value; reads the values from main
    local re pair key value
    re='^[a-z][a-z0-9-]*$'
    if ! [[ $machine =~ $re ]]; then
        echo "MACHINE_NAME \"$machine\" must start with a-z and use only a-z, 0-9 and -"
    fi
    re='^[a-z][a-z0-9]*$'
    if ! [[ $prefix =~ $re ]]; then
        echo "CRATE_PREFIX \"$prefix\" must start with a-z and use only a-z and 0-9 (no -)"
    fi
    if [ "$machine" = "$prefix-brand" ] || [ "$machine" = "$prefix-ui" ]; then
        echo "MACHINE_NAME must differ from $prefix-brand and $prefix-ui"
    fi
    re='^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$'
    if ! [[ $repo =~ $re ]]; then
        echo "GITHUB_REPO \"$repo\" must look like owner/repo"
    fi
    re='^[0-9]{4}$'
    if ! [[ $year =~ $re ]]; then
        echo "YEAR \"$year\" must be four digits"
    fi
    for pair in "DISPLAY_NAME=$display" "DESCRIPTION=$description"; do
        case "${pair#*=}" in
            *\"* | *\\*) echo "${pair%%=*} must not contain \" or \\ (it goes inside Rust and TOML strings)" ;;
        esac
    done
    for pair in "DISPLAY_NAME=$display" "MACHINE_NAME=$machine" "CRATE_PREFIX=$prefix" \
        "GITHUB_REPO=$repo" "DESCRIPTION=$description" "AUTHOR=$author" "YEAR=$year"; do
        key="${pair%%=*}"
        value="${pair#*=}"
        case "$value" in
            "") echo "$key is empty" ;;
            *$'\n'*) echo "$key must be one line" ;;
            *'{{'* | *'}}'*) echo "$key must not contain {{ or }}" ;;
        esac
    done
}

folder_state() { # sets blockers, conflicts and replaced; reads root, files and machine from main
    local p rel dest
    blockers=""
    conflicts=""
    replaced=""
    for p in Cargo.toml apps crates; do
        if [ -e "$root/$p" ]; then blockers="$blockers $p"; fi
    done
    while IFS= read -r rel; do
        dest="${rel//"$ph_machine"/$machine}"
        if [ -e "$root/$dest" ]; then
            case "$dest" in
                # Left by GitHub's "Initial commit": replaced without asking.
                README.md | LICENSE | .gitignore) replaced="$replaced $dest" ;;
                Cargo.toml | apps/* | crates/*) ;; # already reported as blockers
                *) conflicts="$conflicts $dest" ;;
            esac
        fi
    done <<<"$files"
}

folder_line() {
    if [ -n "$blockers" ]; then
        echo "FOLDER=stop: already here:$blockers. Ask the person before going on."
    elif [ -n "$conflicts" ]; then
        echo "FOLDER=ask: would overwrite:$conflicts. Ask the person before going on."
    elif [ -n "$replaced" ]; then
        echo "FOLDER=ok, replaces:$replaced (left by GitHub's initial commit)"
    else
        echo "FOLDER=ok"
    fi
}

print_values() {
    printf 'DISPLAY_NAME=%s\nMACHINE_NAME=%s\nCRATE_PREFIX=%s\nGITHUB_REPO=%s\n' \
        "$display" "$machine" "$prefix" "$repo"
    printf 'DESCRIPTION=%s\nAUTHOR=%s\nYEAR=%s\n' "$description" "$author" "$year"
}

main() {
    local skill_dir template root folder files probs script rel dest left="" count=0
    local blockers conflicts replaced
    local defaults_only=0 overwrite=0
    local display="" machine="" prefix="" repo="" description="" author="" year=""
    local ph_machine='{{MACHINE_NAME}}'

    skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    template="$skill_dir/assets/template"
    root="$(pwd)"
    if [ ! -d "$template" ]; then die 1 "template not found: $template"; fi

    while [ $# -gt 0 ]; do
        case "$1" in
            --defaults) defaults_only=1 ;;
            --overwrite) overwrite=1 ;;
            --display-name) need "$@"; display="$2"; shift ;;
            --machine-name) need "$@"; machine="$2"; shift ;;
            --crate-prefix) need "$@"; prefix="$2"; shift ;;
            --github-repo) need "$@"; repo="$2"; shift ;;
            --description) need "$@"; description="$2"; shift ;;
            --author) need "$@"; author="$2"; shift ;;
            --year) need "$@"; year="$2"; shift ;;
            *) die 1 "unknown option: $1" ;;
        esac
        shift
    done

    # Defaults, for every value not given.
    folder="$(basename "$root")"
    if [ -z "$display" ]; then
        display="$(printf '%s' "$folder" | tr '_-' '  ' |
            awk '{ for (i = 1; i <= NF; i++) $i = toupper(substr($i, 1, 1)) substr($i, 2); print }')"
    fi
    if [ -z "$machine" ]; then
        machine="$(printf '%s' "$folder" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')"
    fi
    if [ -z "$prefix" ]; then prefix="app"; fi
    if [ -z "$repo" ]; then repo="$(github_repo "$root" "$machine")"; fi
    if [ -z "$description" ]; then description="A desktop app built with Rust and egui."; fi
    if [ -z "$author" ]; then author="Gohit X (bastndev)"; fi
    if [ -z "$year" ]; then year="$(date +%Y)"; fi
    case "$description" in
        *. | *! | *\? | "") ;;
        *) description="$description." ;;
    esac

    files="$(cd "$template" && find . -type f | sed 's#^\./##' | LC_ALL=C sort)"
    probs="$(problems)"
    folder_state

    if [ "$defaults_only" = 1 ]; then
        print_values
        if [ -n "$probs" ]; then printf '%s\n' "$probs" | sed 's/^/INVALID=/'; fi
        folder_line
        exit 0
    fi

    if [ -n "$probs" ]; then die 1 "$(printf '%s\n' "$probs" | sed '2,$s/^/scaffold: /')"; fi
    if [ "$overwrite" = 0 ] && [ -n "$blockers$conflicts" ]; then
        die 2 "$(folder_line) Rerun with --overwrite only if they agree."
    fi

    script="s|{{DISPLAY_NAME}}|$(esc "$display")|g
s|{{MACHINE_NAME}}|$(esc "$machine")|g
s|{{CRATE_PREFIX}}|$(esc "$prefix")|g
s|{{GITHUB_REPO}}|$(esc "$repo")|g
s|{{DESCRIPTION}}|$(esc "$description")|g
s|{{AUTHOR}}|$(esc "$author")|g
s|{{YEAR}}|$(esc "$year")|g"

    # One pass: copy each file to its final name, filling in the text files that hold a
    # placeholder. Binary files (the PNG icons) are copied as they are.
    while IFS= read -r rel; do
        dest="${rel//"$ph_machine"/$machine}"
        mkdir -p "$root/$(dirname "$dest")"
        if LC_ALL=C grep -qI '{{' "$template/$rel"; then
            LC_ALL=C sed -e "$script" "$template/$rel" >"$root/$dest"
            if LC_ALL=C grep -q '{{[A-Z_]*}}' "$root/$dest"; then left="$left $dest"; fi
        else
            cp "$template/$rel" "$root/$dest"
        fi
        case "$dest" in *'{{'*) left="$left $dest" ;; esac
        count=$((count + 1))
    done <<<"$files"

    # Whatever the copy or the skill installer did to permissions.
    chmod +x "$root"/scripts/*.sh

    if [ -n "$left" ]; then die 1 "placeholders left in:$left"; fi
    echo "scaffold: ok, $count files written to $root"
    print_values
    if [ -n "$replaced" ]; then echo "REPLACED=${replaced# }"; fi
}

main "$@"
