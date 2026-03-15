// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

import vercel from '@astrojs/vercel';

import rehypeNumberedCallouts from './src/plugins/rehype-numbered-callouts.mjs';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()]
  },

  markdown: {
    rehypePlugins: [rehypeNumberedCallouts],
  },

  adapter: vercel()
});
