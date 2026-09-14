"use client";

import Image from "next/image";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { SITE, authNavigation, navigation } from "@/src/consts";
import ThemeToggle from "@/src/components/ThemeToggle";

export default function Header() {
  const pathname = usePathname();

  return (
    <header className="shrink-0 border-t border-border">
      <div className="mx-auto grid min-h-[72px] w-[min(calc(100%-40px),1152px)] grid-cols-[auto_1fr] items-center gap-x-4 py-2 md:grid-cols-[1fr_auto_1fr] md:py-0 max-[600px]:w-[min(calc(100%-24px),1152px)]">
        <Link
          className="flex w-fit items-center gap-[11px] text-base font-bold text-foreground hover:text-[#f3f3f3] focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-4 group-data-[theme=light]/theme:hover:text-[#171717] max-[600px]:gap-[5px] max-[600px]:text-[13px]"
          href="/"
          aria-label={`${SITE.name} home`}
        >
          <Image
            className="h-auto shrink-0 group-data-[theme=light]/theme:brightness-0 max-[600px]:w-[17px]"
            src="/vercel.svg"
            alt=""
            width={22}
            height={19}
            loading="eager"
          />
          <span>{SITE.name}</span>
        </Link>

        <nav
          className="col-span-2 row-start-2 flex items-center justify-center gap-7 md:col-span-1 md:col-start-2 md:row-start-1 max-[600px]:gap-3"
          aria-label="Main navigation"
        >
          {navigation.map(({ href, label }) => {
            const isActive = pathname === href;

            return (
              <Link
                key={href}
                className={`flex min-h-11 items-center text-base font-medium hover:text-foreground focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-4 max-[600px]:text-[13px] ${
                  isActive ? "text-foreground" : "text-foreground/65"
                }`}
                href={href}
                aria-current={isActive ? "page" : undefined}
              >
                {label}
              </Link>
            );
          })}
        </nav>

        <div className="col-start-2 row-start-1 flex items-center justify-end gap-4 md:col-start-3 max-[600px]:gap-3">
          {authNavigation.map(({ href, label }) => (
            <Link
              key={href}
              className="flex min-h-11 items-center text-sm font-medium text-foreground/65 hover:text-foreground focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-4 max-[600px]:text-[13px]"
              href={href}
            >
              {label}
            </Link>
          ))}
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}
