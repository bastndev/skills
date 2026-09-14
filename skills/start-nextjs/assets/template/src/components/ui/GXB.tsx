import { SocialMedia } from "@/src/components/icons/social-media";

interface GXBProps {
  text: string;
}

const socials = [
  {
    href: "https://x.com/intent/follow?screen_name=gohitx",
    icon: SocialMedia.Twitter,
    label: "X (Twitter)",
  },
  {
    href: "https://github.com/gohitx",
    icon: SocialMedia.GitHubThin,
    label: "GitHub",
  },
  {
    href: "https://linkedin.com/in/gohitx",
    icon: SocialMedia.Linkedin,
    label: "LinkedIn",
  },
  {
    href: "https://instagram.com/gohitx",
    icon: SocialMedia.Instagram,
    label: "Instagram",
  },
  {
    href: "https://www.youtube.com/@gohitx?sub_confirmation=1",
    icon: SocialMedia.YouTube,
    label: "YouTube",
  },
  {
    href: "https://tiktok.com/@gohitx",
    icon: SocialMedia.Tiktok,
    label: "TikTok",
  },
  {
    href: "https://facebook.com/gohitx",
    icon: SocialMedia.Facebook,
    label: "Facebook",
  },
];

const logo = ` ██████╗ ██╗  ██╗██████╗
██╔════╝ ╚██╗██╔╝██╔══██╗
██║  ███╗ ╚███╔╝ ██████╔╝
██║   ██║ ██╔██╗ ██╔══██╗
╚██████╔╝██╔╝ ██╗██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝ `;

export default function GXB({ text }: GXBProps) {
  return (
    <section className="flex flex-1 flex-col items-center justify-center gap-6 px-6 py-8 text-center">
      <pre
        className="m-0 max-w-full whitespace-pre font-mono text-[clamp(0.45rem,2.2vw,0.95rem)] leading-[1.1] text-[#f5f5f5] group-data-[theme=light]/theme:text-[#2d2d2d]"
        aria-hidden="true"
      >
        {logo}
      </pre>

      <p className="m-0 text-[1.05rem] text-[#9b9b9b] group-data-[theme=light]/theme:text-[#6b6b6b]">
        {text}
      </p>

      <div className="mt-2 flex items-center justify-center gap-8 max-[400px]:gap-4">
        {socials.map(({ href, icon: Icon, label }) => (
            <a
              key={href}
              className="flex size-6 items-center justify-center text-[#9b9b9b] transition-transform duration-200 ease-in-out hover:[transform:translateY(-2px)] hover:text-foreground focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-4 group-data-[theme=light]/theme:text-[#6b6b6b] group-data-[theme=light]/theme:hover:text-foreground motion-reduce:transition-none"
              href={href}
              target="_blank"
              rel="noopener noreferrer"
              aria-label={label}
            >
              <Icon className="size-full" aria-hidden="true" focusable="false" />
            </a>
        ))}
      </div>
    </section>
  );
}
