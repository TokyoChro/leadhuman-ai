import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";

export async function GET(context: APIContext) {
  const buildPosts = await getCollection("build", ({ data }) => !data.draft);
  const leadPosts = await getCollection("lead", ({ data }) => !data.draft);
  const allPosts = [...buildPosts, ...leadPosts].sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
  );

  return rss({
    title: "leadhuman.ai",
    description: "Jay Vergara writes about AI, leadership, and how people actually grow at work. Practical tutorials, cross-cultural insights, and L&D strategy from Tokyo.",
    site: context.site!,
    items: allPosts.map((post) => {
      const collection = buildPosts.includes(post) ? "build" : "lead";
      return {
        title: post.data.title,
        pubDate: post.data.pubDate,
        description: post.data.description,
        link: `/${collection}/${post.id}/`,
        content: post.body,
      };
    }),
  });
}
