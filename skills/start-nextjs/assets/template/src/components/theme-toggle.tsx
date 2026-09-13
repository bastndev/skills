"use client";

import { Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";
import { Button } from "@/components/ui/shadcn/button";

export function ThemeToggle() {
  const { resolvedTheme, setTheme } = useTheme();

  return (
    <Button
      type="button"
      variant="outline"
      size="icon"
      aria-label="Cambiar tema"
      className="relative cursor-pointer transition-none"
      onClick={() => {
        if (!resolvedTheme) return;
        setTheme(resolvedTheme === "dark" ? "light" : "dark");
      }}
    >
      <Sun
        aria-hidden="true"
        className="size-5 rotate-0 scale-100 transition-transform dark:-rotate-90 dark:scale-0 motion-reduce:transition-none"
      />
      <Moon
        aria-hidden="true"
        className="absolute size-5 rotate-90 scale-0 transition-transform dark:rotate-0 dark:scale-100 motion-reduce:transition-none"
      />
    </Button>
  );
}
