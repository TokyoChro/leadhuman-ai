import { visit } from 'unist-util-visit';

const emojiToNumber = {
  '1️⃣': '1', '2️⃣': '2', '3️⃣': '3', '4️⃣': '4',
  '5️⃣': '5', '6️⃣': '6', '7️⃣': '7', '8️⃣': '8', '9️⃣': '9',
};

export default function rehypeNumberedCallouts() {
  return (tree) => {
    visit(tree, 'element', (node, index, parent) => {
      if (node.tagName !== 'blockquote' || !parent) return;

      // Get text content of the first paragraph
      const firstP = node.children.find(c => c.tagName === 'p');
      if (!firstP) return;

      const firstText = firstP.children.find(c => c.type === 'text' || c.tagName === 'strong');
      let textContent = '';
      if (firstText && firstText.type === 'text') {
        textContent = firstText.value;
      } else if (firstText && firstText.tagName === 'strong') {
        const inner = firstText.children.find(c => c.type === 'text');
        if (inner) textContent = inner.value;
      }

      // Check if it starts with a number emoji
      let matchedEmoji = null;
      let matchedNumber = null;
      for (const [emoji, num] of Object.entries(emojiToNumber)) {
        if (textContent.trimStart().startsWith(emoji)) {
          matchedEmoji = emoji;
          matchedNumber = num;
          break;
        }
      }

      if (!matchedNumber) return;

      // Remove the emoji from the text
      if (firstText && firstText.type === 'text') {
        firstText.value = firstText.value.replace(matchedEmoji, '').trimStart();
      } else if (firstText && firstText.tagName === 'strong') {
        const inner = firstText.children.find(c => c.type === 'text');
        if (inner) inner.value = inner.value.replace(matchedEmoji, '').trimStart();
      }

      // Wrap in callout structure
      const calloutDiv = {
        type: 'element',
        tagName: 'div',
        properties: { className: ['callout-numbered'] },
        children: [
          {
            type: 'element',
            tagName: 'span',
            properties: { className: ['callout-number'] },
            children: [{ type: 'text', value: matchedNumber }],
          },
          {
            type: 'element',
            tagName: 'div',
            properties: { className: ['callout-body'] },
            children: node.children,
          },
        ],
      };

      parent.children[index] = calloutDiv;
    });
  };
}
