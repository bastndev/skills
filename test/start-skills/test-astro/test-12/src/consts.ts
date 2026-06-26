import type { Route, SiteConfig } from '@/types';

// Single source of truth for the site's name. Rename the project here once and
// the browser tab, the header brand, and the footer all follow.
export const SITE: SiteConfig = {
  name: 'test-12',
  description: 'A simple, scalable Astro base — ready to grow from a portfolio to a full app.',
  url: 'https://example.com',
};

// The "connected routes" registry. Header builds its nav from this, and 404.astro
// links home from it — add a top-level page in ONE place and both update.
//
// Detail routes (e.g. /project/[slug]) are generated from Content Collections,
// not hand-listed here. See ARCHITECTURE.md → "Routing convention".
export const ROUTES: Route[] = [
  { href: '/', label: 'Home' },
  { href: '/work', label: 'Work' },
  { href: '/contact', label: 'Contact' },
];
