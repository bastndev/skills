import { SITE } from "@/src/consts";

const year = new Date().getFullYear();

export default function Footer() {
  return (
    <footer className="shrink-0 border-t border-transparent [border-image:linear-gradient(to_right,transparent,var(--color-border)_40%,var(--color-border)_60%,transparent)_1]">
      <p className="m-0 px-6 py-5 text-center text-[0.9rem] text-foreground/65">
        {SITE.name} © {year}
      </p>
    </footer>
  );
}
