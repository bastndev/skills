import type { Metadata } from "next";
import { Geist } from "next/font/google";
import { SITE } from "@/src/consts";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: {
    default: SITE.name,
    template: `%s | ${SITE.name}`,
  },
  description: SITE.description,
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang={SITE.lang}
      data-theme="dark"
      suppressHydrationWarning
      className={`${geistSans.variable} group/theme antialiased`}
    >
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){try{var theme=localStorage.getItem("theme");if(theme==="light"||theme==="dark")document.documentElement.dataset.theme=theme}catch{}})()`,
          }}
        />
      </head>
      <body className="flex min-h-dvh flex-col">
        <a
          href="#main-content"
          className="sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:w-auto focus:h-auto focus:overflow-visible focus:[clip:auto] focus:whitespace-normal focus:rounded-md focus:bg-background focus:p-3 focus:text-foreground focus:outline-2 focus:outline-offset-2"
        >
          Skip to content
        </a>
        {children}
      </body>
    </html>
  );
}
