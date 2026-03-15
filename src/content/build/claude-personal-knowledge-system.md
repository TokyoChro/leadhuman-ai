---
title: "How to Use Claude to Build a Personal Knowledge System in 30 Minutes"
description: "Most people use AI like a search engine. I turned Claude into a personal knowledge management system that remembers my context, my career goals, and my writing voice. Here's the architecture behind it."
pubDate: 2026-03-14
tags: ["ai-tools", "claude", "tutorial", "workflow", "beginner"]
author: "Jay Vergara"
draft: false
---

Most people treat AI conversations like disposable text messages. Ask a question, get an answer, close the tab, and next time you open it the AI has no idea who you are.

I did this for months before I realized I was introducing myself to the same brilliant colleague every morning and wondering why the output felt generic.

There's a better way. It takes about 30 minutes to set up.

---

## What you're building

A personal context document that Claude can reference in every conversation. Instead of re-explaining your situation each time you start where you left off. The AI already knows who you are and what you're working on and how you think.

---

## Step 1: Write your context document (10 minutes)

Open a doc. Notion, Google Docs, plain text, whatever you actually use. Cover four things.

**Who you are.** Role, industry, location. Two sentences.

**What you're working on now.** Top 3 to 5 priorities this quarter. Be specific. Not 'grow the business' but 'launch the new manager development program for Q2.'

**How you like to work.** Do you want to be challenged or supported? Do you think in frameworks or narratives? This part makes the biggest difference and most people skip it.

**Your professional context.** Anything the AI should know about your industry and audience and frameworks that would improve its answers.

Here's a simplified version of mine:

```javascript
I'm Jay Vergara. L&D strategist and cross-cultural communication
specialist based in Tokyo. I run Peak Potential Consulting and I'm
building leadhuman.ai.

Priorities: 3-5 content pieces per week. MBA at GLOBIS. New
cross-cultural workshops for Q2.

How I work: Challenge me. I think in frameworks. Keep it practical.

Pillars: cross-cultural (32%), L&D (29%), AI (29%), leadership (11%)
```

One page. You can always expand later.

---

## Step 2: Create domain pages (15 minutes)

Break your knowledge into 2 to 3 domains. For each one capture:

**Frameworks you actually use.** Not the ones from school. The ones you reach for. Kirkpatrick, 70/20/10, MEDDIC, whatever lives in your real toolkit.

**Your opinions.** What do you believe that others might disagree with? These make your AI output sound like you instead of like everyone else.

**Tasks where you need help.** The recurring stuff where AI would be most valuable.

---

## Step 3: Connect it (5 minutes)

**[Claude.ai](http://Claude.ai):** Use Projects. Upload your docs as project knowledge. Every conversation in that project gets your full context automatically.

**Claude Code or Desktop with MCP:** Connect Claude directly to your Notion or Google Drive. It reads the docs at session start.

**Any platform:** Paste your context doc at the start of a new conversation. Takes 10 seconds and changes everything.

---

## Step 4: Keep it alive (5 min/week)

Weekly: update priorities and recent decisions. Monthly: review domain pages and evolve your frameworks. After major changes: update immediately.

The system only works if it reflects your actual current reality.

---

## What changes

With context Claude drafts content that sounds like you and makes recommendations for your specific situation and pushes back with relevant counterarguments and connects dots across your work.

Without context it's smart but generic. With context it's a genuine thinking partner.

And here's what surprised me most. Building the system forced me to articulate things about my own work I'd never written down. My frameworks and my opinions and my priorities. That was valuable before I even gave it to the AI.

30 minutes. Start today.

---

**Further reading:**
- [Claude Projects Documentation](https://docs.anthropic.com/en/docs/build-with-claude/projects) explains how to use Projects for persistent context in Claude.
- [Tiago Forte's "Building a Second Brain"](https://www.buildingasecondbrain.com/) is the framework that inspired the knowledge management approach behind this system.
- [How I Built a Council of AI Advisors](https://leadhuman.ai/build/council-of-ai-advisors) takes this concept further by creating specialized AI personas with deep domain context.
- [Why Every Leader Needs to Understand AI](https://leadhuman.ai/lead/why-leaders-need-ai) covers the leadership case for building AI fluency, starting with systems like this one.

---

*Part of the Build with AI series on [leadhuman.ai](http://leadhuman.ai). Difficulty: beginner.*
