// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

import vercel from '@astrojs/vercel';

import rehypeNumberedCallouts from './src/plugins/rehype-numbered-callouts.mjs';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://leadhuman.ai',
  vite: {
    plugins: [tailwindcss()]
  },

  markdown: {
    rehypePlugins: [rehypeNumberedCallouts],
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ja'],
    fallback: { ja: 'en' },
    routing: {
      prefixDefaultLocale: false,
      fallbackType: 'rewrite',
    },
  },

  adapter: vercel(),
  integrations: [
    sitemap({
      i18n: {
        defaultLocale: 'en',
        locales: {
          en: 'en',
          ja: 'ja',
        },
      },
    }),
  ]
});