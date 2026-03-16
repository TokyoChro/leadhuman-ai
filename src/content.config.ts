import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const postSchema = z.object({
  title: z.string(),
  description: z.string(),
  pubDate: z.coerce.date(),
  tags: z.array(z.string()),
  author: z.string().default("Jay Vergara"),
  image: z.string().optional(),
  imagePosition: z.string().optional(),
  draft: z.boolean().default(false),
});

const build = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/build" }),
  schema: postSchema,
});

const lead = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/lead" }),
  schema: postSchema,
});

export const collections = { build, lead };
