export const SITE = {
  name: "{{PROJECT_NAME}}",
  description: "A starting point for your next project.",
  lang: "en",
} as const;

export const navigation = [
  { href: "/", label: "Home" },
  { href: "/work", label: "Work" },
  { href: "/contact", label: "Contact" },
] as const;

export const authNavigation = [
  { href: "/login", label: "Login" },
  { href: "/register", label: "Register" },
] as const;
