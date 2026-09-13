import { ThemeToggle } from "@/components/theme-toggle";
import { SITE } from "@/consts";

export default function Home() {
  return (
    <main className="mx-auto flex min-h-svh max-w-3xl flex-col gap-12 px-6 py-8 sm:px-10">
      <header className="flex items-center justify-between gap-4">
        <span className="text-sm font-medium">{SITE.name}</span>
        <ThemeToggle />
      </header>
      <section className="flex flex-1 flex-col justify-center gap-4 pb-16">
        <h1 className="text-4xl font-semibold tracking-tight sm:text-5xl">
          {SITE.name}
        </h1>
        <p className="max-w-lg text-base text-muted-foreground">
          Una base simple para tu próximo proyecto.
        </p>
      </section>
    </main>
  );
}
