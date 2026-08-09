export const SITE = {
  name: '{{PROJECT_NAME}}',
  description: 'A clean Astro base with a focused structure, accessible theme, and room to grow.',
} as const;

export const ROUTES = [
  { href: '/', label: 'Home' },
  { href: '/work', label: 'Work' },
  { href: '/contact', label: 'Contact' },
] as const;
