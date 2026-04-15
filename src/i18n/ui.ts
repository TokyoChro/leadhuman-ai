export const languages = {
  en: 'English',
  ja: '日本語',
} as const;

export type Lang = keyof typeof languages;

export const defaultLang: Lang = 'en';

export const ui = {
  en: {
    // Nav
    'nav.home': 'Home',
    'nav.build': 'Build with AI',
    'nav.lead': 'Lead Humanly',
    'nav.videos': 'Videos',
    'nav.about': 'About',

    // Hero
    'hero.location1': 'Tokyo, Japan',
    'hero.location2': 'Vancouver, Canada',
    'hero.tagline': 'Lead humanly. Learn constantly. Build with AI.',
    'hero.subtitle': 'L&D Strategist · Leadership Development · AI Trainer',
    'hero.subtitle2': 'Cross-Cultural Communications · Corporate Learning · MBA',
    'hero.body': 'I help organizations <a href="/lead/" class="text-ivy hover:text-ivy-light transition-colors underline decoration-ivy/30">build leaders</a>, design corporate training programs, and develop <a href="/build/" class="text-ivy hover:text-ivy-light transition-colors underline decoration-ivy/30">AI fluency</a> that works across borders. Over a decade of experience in learning and development, manager coaching, and building teams across cultures.',
    'hero.cta': 'Connect on LinkedIn',

    // Section headings
    'section.latestBuild': 'Latest from Build with AI',
    'section.latestLead': 'Latest from Lead Humanly',
    'section.expertise': 'Leadership, L&D, AI, and Cross-Cultural Insights',
    'section.expertiseDesc': 'I write about what I work on every day: building corporate training programs, developing managers, using AI in people development, and communicating across cultures.',
    'section.aboutJay': 'About Jay Vergara',
    'section.videos': 'AI Tutorials, Leadership Talks, and Quick Takes',
    'section.videosDesc': 'I make videos about using AI in corporate training, leading teams across cultures, and building real tools with AI. New tutorials drop weekly.',
    'section.ctaDesc': 'Find me on LinkedIn for L&D and leadership insights, YouTube for AI tutorials, and TikTok for quick takes.',

    // About section on homepage
    'home.about1': 'I grew up in Vancouver, B.C. and I\'ve been in Tokyo for over a decade now. My career has been in learning and development at companies like Indeed, Rakuten, and TELUS, building training programs and leading L&D teams across borders.',
    'home.about2': 'I\'m finishing an MBA at GLOBIS University and I use AI every single day to build systems, create content, and figure out how it all fits into developing people.',
    'home.aboutLink': 'Read the full story',

    // Expertise pillars
    'pillar.learning.title': 'Corporate Learning & L&D Strategy',
    'pillar.learning.desc': 'How to design training programs that actually change behavior. Instructional design, learning measurement, onboarding frameworks, and why most corporate L&D programs don\'t stick.',
    'pillar.leadership.title': 'Manager & Leadership Development',
    'pillar.leadership.desc': 'Practical frameworks for developing first-time managers and senior leaders. Coaching, feedback, psychological safety, and building high-performing teams across levels.',
    'pillar.ai.title': 'AI for HR & L&D Teams',
    'pillar.ai.desc': 'Hands-on tutorials for using AI in corporate training, talent development, and people operations. Real tools, real workflows, no hype.',
    'pillar.crosscultural.title': 'Cross-Cultural Business Communication',
    'pillar.crosscultural.desc': 'Working across cultures, languages, and time zones. What a decade in Tokyo taught me about Japanese business culture, global teams, and the communication gaps no textbook covers.',

    // Common
    'common.viewAll': 'View all',
    'common.browseVideos': 'Browse all videos',
    'common.readArticles': 'Read articles',
    'common.readMore': 'Read more',
    'common.minRead': 'min read',
    'common.skipToContent': 'Skip to content',
    'common.backToBuild': 'Build with AI',
    'common.backToLead': 'Lead Humanly',
    'common.youMightAlsoLike': 'You might also like',
    'common.noPosts': 'No posts yet. Check back soon.',

    // Build hub
    'build.title': 'Build with AI',
    'build.description': 'Tools, workflows, and experiments in building with AI.',
    'build.badge': 'BUILD WITH AI',

    // Lead hub
    'lead.title': 'Lead Humanly',
    'lead.description': 'Leadership, learning, and cross-cultural communication.',
    'lead.badge': 'LEAD HUMANLY',

    // Videos page
    'videos.title': 'Videos',
    'videos.description': 'Practical AI tutorials, leadership insights, and workflow breakdowns — everything I publish on the leadhuman.ai YouTube channel, organized in one place.',
    'videos.longForm': 'Long Form',
    'videos.longFormDesc': 'Full-length tutorials, deep dives, and commentary on AI, leadership, and learning development.',
    'videos.shortForm': 'Short Form',
    'videos.shortFormDesc': 'Quick tips, clips, and takeaways — bite-sized insights you can use right away.',
    'videos.longFormSoon': 'Long form videos coming soon.',
    'videos.shortFormSoon': 'Short form videos coming soon.',
    'videos.error': 'Something went wrong loading videos. Please try again later.',

    // Author bio
    'author.bio': '<strong>Jay Vergara</strong> is an L&D strategist and cross-cultural communication specialist based in Tokyo. He writes about leadership, learning, and building with AI at <a href="https://leadhuman.ai" class="text-ivy hover:text-ivy-light transition-colors underline">leadhuman.ai</a> and on <a href="https://linkedin.com/in/vergarajay/" class="text-ivy hover:text-ivy-light transition-colors underline">LinkedIn</a>.',

    // Footer
    'footer.tagline': 'Jay Vergara · Tokyo · Lead humanly. Learn constantly. Build with AI.',

    // Language switcher
    'lang.switch': '日本語',
  },
  ja: {
    // Nav
    'nav.home': 'ホーム',
    'nav.build': 'AIで創る',
    'nav.lead': '人間らしく導く',
    'nav.videos': '動画',
    'nav.about': 'プロフィール',

    // Hero
    'hero.location1': '東京',
    'hero.location2': 'バンクーバー、カナダ',
    'hero.tagline': '人間らしく導く。学び続ける。AIで創る。',
    'hero.subtitle': 'L&D戦略家 · リーダーシップ開発 · AIトレーナー',
    'hero.subtitle2': '異文化コミュニケーション · 企業研修 · MBA',
    'hero.body': '組織の<a href="/ja/lead/" class="text-ivy hover:text-ivy-light transition-colors underline decoration-ivy/30">リーダー育成</a>、企業研修プログラムの設計、国境を越えて機能する<a href="/ja/build/" class="text-ivy hover:text-ivy-light transition-colors underline decoration-ivy/30">AI活用力</a>の開発を支援しています。人材開発、マネージャーコーチング、異文化チームビルディングの分野で10年以上の経験があります。',
    'hero.cta': 'LinkedInでつながる',

    // Section headings
    'section.latestBuild': 'AIで創る 最新記事',
    'section.latestLead': '人間らしく導く 最新記事',
    'section.expertise': 'リーダーシップ、L&D、AI、異文化コミュニケーション',
    'section.expertiseDesc': '日々の仕事で取り組んでいることについて書いています。企業研修プログラムの構築、マネージャーの育成、人材開発におけるAI活用、そして異文化間のコミュニケーション。',
    'section.aboutJay': 'Jay Vergaraについて',
    'section.videos': 'AIチュートリアル、リーダーシップ、ショート動画',
    'section.videosDesc': '企業研修でのAI活用、異文化チームのリーダーシップ、実用的なAIツールの構築について動画を制作しています。毎週新しいチュートリアルを公開中。',
    'section.ctaDesc': 'L&Dとリーダーシップに関する知見はLinkedInで、AIチュートリアルはYouTubeで、ショート動画はTikTokでご覧いただけます。',

    // About section on homepage
    'home.about1': 'バンクーバー出身で、東京に住んで10年以上になります。Indeed、楽天、TELUSなどの企業でL&D（人材開発）のキャリアを積み、研修プログラムの構築や国境を越えたL&Dチームのリーダーシップに携わってきました。',
    'home.about2': 'グロービス経営大学院でMBAを取得中で、毎日AIを使ってシステムを構築し、コンテンツを制作し、人材開発にどう活かせるかを模索しています。',
    'home.aboutLink': '詳しいプロフィールを読む',

    // Expertise pillars
    'pillar.learning.title': '企業研修・L&D戦略',
    'pillar.learning.desc': '実際に行動を変える研修プログラムの設計方法。インストラクショナルデザイン、学習効果の測定、オンボーディングの仕組み、そしてなぜほとんどの企業研修が定着しないのか。',
    'pillar.leadership.title': 'マネージャー・リーダーシップ開発',
    'pillar.leadership.desc': '新任マネージャーからシニアリーダーまで実践的なフレームワーク。コーチング、フィードバック、心理的安全性、そしてあらゆる階層で高パフォーマンスチームを構築する方法。',
    'pillar.ai.title': 'HR・L&DチームのためのAI',
    'pillar.ai.desc': '企業研修、タレント開発、ピープルオペレーションにおけるAI活用の実践的チュートリアル。本物のツール、本物のワークフロー、誇大広告なし。',
    'pillar.crosscultural.title': '異文化ビジネスコミュニケーション',
    'pillar.crosscultural.desc': '文化、言語、タイムゾーンを越えて働くこと。東京での10年間が教えてくれた日本のビジネス文化、グローバルチーム、そして教科書には載っていないコミュニケーションのギャップ。',

    // Common
    'common.viewAll': 'すべて見る',
    'common.browseVideos': '動画一覧を見る',
    'common.readArticles': '記事を読む',
    'common.readMore': '続きを読む',
    'common.minRead': '分で読める',
    'common.skipToContent': 'メインコンテンツへスキップ',
    'common.backToBuild': 'AIで創る',
    'common.backToLead': '人間らしく導く',
    'common.youMightAlsoLike': 'こちらもおすすめ',
    'common.noPosts': 'まだ記事がありません。もうしばらくお待ちください。',

    // Build hub
    'build.title': 'AIで創る',
    'build.description': 'AIを使ったツール、ワークフロー、実験の記録。',
    'build.badge': 'AIで創る',

    // Lead hub
    'lead.title': '人間らしく導く',
    'lead.description': 'リーダーシップ、学び、異文化コミュニケーション。',
    'lead.badge': '人間らしく導く',

    // Videos page
    'videos.title': '動画',
    'videos.description': '実践的なAIチュートリアル、リーダーシップの知見、ワークフロー解説。leadhuman.ai YouTubeチャンネルで公開中の全コンテンツをまとめています。',
    'videos.longForm': 'ロングフォーム',
    'videos.longFormDesc': 'フルレングスのチュートリアル、深掘り解説、AI・リーダーシップ・人材開発に関するコメンタリー。',
    'videos.shortForm': 'ショートフォーム',
    'videos.shortFormDesc': 'すぐに使えるクイックヒント、クリップ、要点まとめ。',
    'videos.longFormSoon': 'ロングフォーム動画は近日公開予定です。',
    'videos.shortFormSoon': 'ショートフォーム動画は近日公開予定です。',
    'videos.error': '動画の読み込み中にエラーが発生しました。しばらくしてからもう一度お試しください。',

    // Author bio
    'author.bio': '<strong>Jay Vergara（ジェイ・ベルガラ）</strong>は東京を拠点とするL&D戦略家、異文化コミュニケーションスペシャリスト。リーダーシップ、学び、AIとの共創について<a href="https://leadhuman.ai/ja/" class="text-ivy hover:text-ivy-light transition-colors underline">leadhuman.ai</a>と<a href="https://linkedin.com/in/vergarajay/" class="text-ivy hover:text-ivy-light transition-colors underline">LinkedIn</a>で発信中。',

    // Footer
    'footer.tagline': 'Jay Vergara · 東京 · 人間らしく導く。学び続ける。AIで創る。',

    // Language switcher
    'lang.switch': 'English',
  },
} as const;
