"use client";

import { Moon, Sun } from "lucide-react";

export default function ThemeToggle() {
  function toggleTheme() {
    const root = document.documentElement;
    root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";

    try {
      localStorage.setItem("theme", root.dataset.theme);
    } catch {
      // Theme switching still works when browser storage is unavailable.
    }
  }

  return (
    <button
      className="relative grid size-[37px] shrink-0 cursor-pointer place-items-center rounded-full border border-border bg-transparent text-foreground transition-transform duration-150 ease-in-out hover:-translate-y-px hover:bg-[color-mix(in_srgb,var(--foreground)_9%,transparent)] hover:text-[#f3f3f3] active:scale-[0.94] focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-4 group-data-[theme=light]/theme:hover:text-[#171717] motion-reduce:transition-none max-[600px]:size-8"
      type="button"
      onClick={toggleTheme}
    >
      <span className="sr-only group-data-[theme=light]/theme:hidden">
        Switch to light theme
      </span>
      <span className="sr-only hidden group-data-[theme=light]/theme:inline">
        Switch to dark theme
      </span>
      <span
        className="absolute grid place-items-center opacity-100 [transform:rotate(0deg)_scale(1)] [transition:opacity_100ms_ease,transform_150ms_ease] group-data-[theme=light]/theme:opacity-0 group-data-[theme=light]/theme:[transform:rotate(75deg)_scale(0.5)] motion-reduce:transition-none"
        aria-hidden="true"
      >
        <Sun size={19} strokeWidth={1.8} />
      </span>
      <span
        className="absolute grid place-items-center opacity-0 [transform:rotate(-75deg)_scale(0.5)] [transition:opacity_100ms_ease,transform_150ms_ease] group-data-[theme=light]/theme:opacity-100 group-data-[theme=light]/theme:[transform:rotate(0deg)_scale(1)] motion-reduce:transition-none"
        aria-hidden="true"
      >
        <Moon size={19} strokeWidth={1.8} />
      </span>
    </button>
  );
}
