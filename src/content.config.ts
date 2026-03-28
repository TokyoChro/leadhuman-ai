import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const postSchema = ({ image }: { image: Function }) =>
  z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    tags: z.array(z.string()),
    author: z.string().default("Jay Vergara"),
    image: image().optional(),
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
