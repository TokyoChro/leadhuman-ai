# AI Crawler Access Report: leadhuman.ai

**Analysis Date:** 2026-04-15
**Domain:** leadhuman.ai (including /ja/ Japanese localization)
**robots.txt Status:** Found, permissive

---

## Crawler Access Summary

| Crawler | Operator | Tier | Status | Impact |
|---|---|---|---|---|
| GPTBot | OpenAI | 1 | Allowed (wildcard) | Visible in ChatGPT Search |
| OAI-SearchBot | OpenAI | 1 | Allowed (wildcard) | Visible in ChatGPT search results |
| ChatGPT-User | OpenAI | 1 | Allowed (wildcard) | Users can browse via ChatGPT |
| ClaudeBot | Anthropic | 1 | Allowed (wildcard) | Visible in Claude web search |
| PerplexityBot | Perplexity | 1 | Allowed (wildcard) | Visible in Perplexity (referral traffic) |
| Google-Extended | Google | 2 | Allowed (wildcard) | Content available for Gemini/AI Overviews |
| GoogleOther | Google | 2 | Allowed (wildcard) | Available for Google AI research |
| Applebot-Extended | Apple | 2 | Allowed (wildcard) | Available for Apple Intelligence |
| Amazonbot | Amazon | 2 | Allowed (wildcard) | Available for Alexa answers |
| FacebookBot | Meta | 2 | Allowed (wildcard) | Available for Meta AI |
| CCBot | Common Crawl | 3 | Allowed (wildcard) | Training data inclusion |
| anthropic-ai | Anthropic | 3 | Allowed (wildcard) | Claude training data |
| Bytespider | ByteDance | 3 | Allowed (wildcard) | ByteDance AI products |
| cohere-ai | Cohere | 3 | Allowed (wildcard) | Cohere training data |

## AI Visibility Score: 95/100

**Tier 1 Access:** 5/5 crawlers allowed
**Tier 2 Access:** 5/5 crawlers allowed
**Tier 3 Access:** 4/4 crawlers allowed (Bytespider should be blocked)

---

## Current robots.txt

```
User-agent: *
Allow: /

Sitemap: https://leadhuman.ai/sitemap-index.xml
```

## Critical Issues

None. All Tier 1 and Tier 2 crawlers have full access.

## Findings

### Meta Robots Tags
No blocking meta tags found on any page. No noindex, noai, or noimageai directives.

### HTTP Headers
No X-Robots-Tag headers detected.

### JavaScript Rendering
Not a concern. Astro generates static HTML (SSG). All content is in the HTML source, fully readable by all crawlers regardless of JS rendering capability.

### llms.txt
**NOT FOUND.** This is the primary gap. llms.txt is the emerging standard for helping AI systems understand site structure and content. Creating one would improve AI discoverability.

### Sitemap
Fully accessible. 46 URLs with xhtml:link hreflang alternates on 45/46 URLs. Language relationship between EN and JA pages is clearly mapped.

### hreflang Tags
Bidirectional hreflang tags present on all pages (EN <-> JA, x-default -> EN).

### Structured Data
Schema.org JSON-LD with inLanguage property on all pages. FAQ schema translated to Japanese. Breadcrumb schema with Japanese labels.

## Recommendations

### 1. Create llms.txt (HIGH PRIORITY)
Create a /public/llms.txt file describing the site's content and structure for AI systems.

### 2. Enhance robots.txt (MEDIUM PRIORITY)
Add explicit AI crawler entries and block Bytespider. While the current wildcard allows all crawlers, explicit entries provide clarity and allow selective blocking.

### 3. Submit sitemap to Google Search Console (MANUAL STEP)
Resubmit https://leadhuman.ai/sitemap-index.xml and use URL Inspection tool on key /ja/ pages.
