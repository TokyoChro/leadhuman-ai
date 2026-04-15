---
title: "Claudeで30分で個人ナレッジシステムを構築する方法"
description: "ほとんどの人はAIを検索エンジンのように使っています。私はClaudeを、自分のコンテキスト、キャリア目標、そして書き方の癖を記憶するパーソナルナレッジ管理システムに変えました。そのアーキテクチャをお伝えします。"
pubDate: 2026-03-20
tags: ["ai-tools", "claude", "tutorial", "workflow", "beginner"]
author: "Jay Vergara"
image: "../../assets/images/posts/claude-personal-knowledge-system.png"
draft: false
---

ほとんどの人はAIとの会話を使い捨てのテキストメッセージのように扱っています。質問して、回答をもらって、タブを閉じて、次に開くときにはAIが自分のことを全く知らないという状態です。

私も何カ月もそうしていました。毎朝同じ優秀な同僚に自己紹介をしているのに、なぜアウトプットが汎用的に感じるのか不思議に思っていたんです。

もっといい方法があります。セットアップには約30分しかかかりません。

---

## 何を作るのか

Claudeがすべての会話で参照できる、パーソナルコンテキストドキュメントです。毎回自分の状況を説明し直すのではなく、前回の続きから始められます。AIがすでにあなたが誰で、何に取り組んでいて、どう考えるかを理解しているのです。

---

## ステップ1：コンテキストドキュメントを書く（10分）

ドキュメントを開きましょう。Notion、Google Docs、プレーンテキスト、普段使っているものなら何でもOKです。4つのことをカバーします。

**自分が誰か。** 役職、業界、所在地。2文で。

**今取り組んでいること。** 今四半期のトップ3から5の優先事項。具体的に書きましょう。「ビジネスを成長させる」ではなく「Q2に向けた新任マネージャー育成プログラムをローンチする」のように。

**自分の働き方の好み。** チャレンジされたいのか、サポートされたいのか？フレームワークで考えるタイプか、ナラティブで考えるタイプか？ここが最も大きな違いを生む部分で、ほとんどの人がスキップしてしまいます。

**プロフェッショナルとしてのコンテキスト。** AIの回答を改善するために知っておくべき、自分の業界やオーディエンスやフレームワークについての情報。

私のものを簡略化したバージョンがこちらです：

```
I'm Jay Vergara. L&D strategist and cross-cultural communication
specialist based in Tokyo. I run leadhuman.ai and consult on
leadership development and intercultural communication.

Priorities: 3-5 content pieces per week. New
cross-cultural workshops for Q2.

How I work: Challenge me. I think in frameworks. Keep it practical.

Pillars: cross-cultural (32%), L&D (29%), AI (29%), leadership (11%)
```

1ページです。後からいつでも拡張できます。

---

## ステップ2：ドメインページを作成する（15分）

知識を2つから3つのドメインに分けましょう。それぞれについて以下を記録します。

**実際に使っているフレームワーク。** 学校で習ったものではなく、実際に手が伸びるもの。Kirkpatrick、70/20/10、MEDDIC、自分の実際のツールキットに入っているもの。

**自分の意見。** 他の人が反対するかもしれないけど、自分が信じていることは何か？これがAIのアウトプットを「自分らしい」ものにします。他の人と同じに聞こえなくなるんです。

**助けが必要なタスク。** AIが最も価値を発揮する繰り返しの作業。

---

## ステップ3：接続する（5分）

**[Claude.ai](https://claude.ai):** Projectsを使いましょう。ドキュメントをプロジェクトナレッジとしてアップロードします。そのプロジェクト内のすべての会話で、フルコンテキストが自動的に適用されます。

**Claude CodeまたはMCP付きDesktop:** ClaudeをNotionやGoogle Driveに直接接続します。セッション開始時にドキュメントを読み込みます。

**どのプラットフォームでも:** 新しい会話の最初にコンテキストドキュメントを貼り付けるだけです。10秒で済みますが、すべてが変わります。

---

## ステップ4：生かし続ける（週5分）

毎週：優先事項と最近の判断を更新。毎月：ドメインページを見直してフレームワークを進化させる。大きな変化の後：すぐに更新。

このシステムは、自分の実際の現状を反映している場合にのみ機能します。

---

## 何が変わるか

コンテキストがあると、Claudeは自分らしく聞こえるコンテンツを下書きし、自分の具体的な状況に合った提案をし、関連する反論で押し返してくれて、仕事全体のつながりを見つけてくれます。

コンテキストなしだと賢いけど汎用的です。コンテキストがあると、本当の思考パートナーになります。

そして、最も驚いたことがあります。このシステムを構築するプロセスそのものが、自分の仕事について一度も書き出したことのないことを明確にさせてくれました。自分のフレームワークや意見や優先事項です。AIに渡す前の段階で、それだけで価値がありました。

30分です。今日から始めましょう。

---

**出典:**

- [Claude Projects Documentation](https://docs.anthropic.com/en/docs/about-claude/models) — Claudeで持続的なコンテキストのためにProjectsを使う方法。
- [Tiago Forte's "Building a Second Brain"](https://www.buildingasecondbrain.com/) — このシステムの背後にあるナレッジマネジメントアプローチに影響を与えたフレームワーク。
- [How I Built a Council of AI Advisors](https://leadhuman.ai/build/council-of-ai-advisors) — このコンセプトをさらに発展させ、深いドメインコンテキストを持つ専門AIペルソナを作成する方法。
- [Why Every Leader Needs to Understand AI](https://leadhuman.ai/lead/why-leaders-need-ai) — こうしたシステムの構築から始まる、AIリテラシーのリーダーシップ的意義。

---

*[leadhuman.ai](https://leadhuman.ai)のBuild with AIシリーズの一部です。*
