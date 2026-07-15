import { defineConfig } from 'tsdown';

export default defineConfig({
  entry: { index: 'src/index.ts' },
  format: ['esm', 'cjs'],
  fixedExtension: false,
  dts: true,
  shims: true,
  publint: { strict: true },
  attw: { level: 'error' },
});
