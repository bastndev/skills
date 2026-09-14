## Structure and routes

```text
src/
├── app/
│   ├── layout.tsx              Root document, font, and default metadata
│   ├── globals.css             Shared theme colors and base styles
│   ├── favicon.ico
│   ├── (workspace)/
│   │   ├── layout.tsx          Shared header and footer for public pages
│   │   ├── page.tsx            / — Home with GXB and social links
│   │   ├── work/page.tsx       /work — example project page
│   │   └── contact/page.tsx    /contact — example contact page
│   └── (auth)/
│       ├── login/page.tsx      /login — placeholder
│       └── register/page.tsx   /register — placeholder
├── components/
│   ├── ThemeToggle.tsx
│   ├── icons/social-media.tsx
│   └── ui/
│       ├── Header.tsx
│       ├── Footer.tsx
│       └── GXB.tsx
└── consts.ts                   Site metadata and navigation
```

## Responsibilities

- The root layout owns the document language, font, metadata defaults, initial theme, and skip link.
- Workspace pages share the header and footer. Auth examples only use the root layout. Route groups do not enforce authentication.
- Pages and layouts remain Server Components. Header uses `usePathname` for active navigation; ThemeToggle handles the browser theme and persistence.
- `consts.ts` contains public site configuration. GXB keeps its own social URLs and imports only the icons it renders.
- `globals.css` contains theme tokens and document styles. Tailwind utilities for individual components stay in their TSX files.

## Growing the template

Add pages beside the existing examples or introduce a route group when pages need a different shared layout. Each page should define its title and render one `main` with `id="main-content"`, `tabIndex={-1}`, and a descriptive heading.

Replace example pages and GXB as the product takes shape. Add feature-specific components, data access, authentication, and loading/error UI when the feature requires them.

Theme persistence uses the `theme` storage key with `light` and `dark` values. The root script validates the saved value before hydration; only the HTML element suppresses the expected attribute mismatch. The default remains dark when no valid preference is saved.
