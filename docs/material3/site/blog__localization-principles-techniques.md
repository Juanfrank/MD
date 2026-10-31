<!-- source: https://m3.material.io/blog/localization-principles-techniques -->
# Principles and Techniques for Effective Localization - Material Design

# Principles and Techniques for Effective Localization

Posted by

Localization is the process of adapting messages, imagery, brand voice, features, and products to achieve a linguistic, cultural, and geographic fit for a given audience. The goal is to make user experiences for everyone as comfortable as possible across different cultural and regional contexts. It is important to consider localization if your product will be used globally, since a poorly or insufficiently localized product or content could create confusion.

The process of localization is often misunderstood to mean translation, but in fact localization deals with much more than word-by-word translation of text and content. Translation strives for a linguistic equivalent, while localization broadly considers adaptation for a market or cultural context.

Localization is also different from internationalization, a practice and procedure for applications to support different local conventions, such as time, date and phone number formats, currency, measurement, and other data.

This post introduces principles and techniques to ensure that your products and experiences will work well across different contexts. Get to know the considerations and best practices for adapting content, imagery, and more.

## Design flexible and concise messages

Expect messages to shrink or expand after translation and localization. For some languages, length can expand by 30% or might even double when rendered in a different language. For others, the localized text may be shorter but take up more vertical space. Lengthy text can get cut off, overlap, and lead to an overall poor experience.

To avoid text being cut off or overlapping, consider keeping messages concise while designing an interface that’s flexible enough to accommodate different languages.

Learn more: For help with flexible size constraints, see our guidance on component behavior and making apps compatible with different devices. For ideas on how to make your app as easy-to-understand as possible, read about improving comprehension through intuitive actions.

If you already know the languages that your product will be translated into, it helps to design for the longest possible translation of a given text. Consider using Google Translate for a quick test of translated text length, or consult a localization specialist.

Leave open space around condensed UI components, such as buttons and tabs. Consider building extra room or a buffer into your design to accommodate the overflow of text. For longer text, establish a component’s maximum width that allows lengthier passages to wrap.

## Ensure that language and imagery are inclusive

Whenever possible, edit any jargon, slang, or language that’s used by a narrow or specialized group.

When designing for many cultures, use imagery and avatars that display various cultures, backgrounds, ethnicities, and demographic groups.

Avoid imagery and avatars that represent a single culture, gender, or demographic characteristic.

Learn more: For help with communicating with international users, see our guidance on writing for a global audience.

#### Icons and emoji

Although icons and emoji are widely used for applications and websites, not all visual elements are interpreted in the same way across cultures. An icon or emoji might have a positive impact in one culture, but could be offensive in another.

To ensure that the icons you use are understandable for your audience, consult a localization specialist if available, or someone who can serve as a subject matter expert for the target culture or market, such as a local user, an in-market support team, or a translator.

To make text with emoji appropriate for a local context, you may need to move emoji around in the UI, add explanatory text, or change the icon or emoji to one that’s better suited for the target region.

For example, in the United States the icons that look like a flame or fire 🔥 might connote “trending” or “exciting.” However, fire iconography as a positive value isn’t universally understood. For a Polish audience, the up arrow is a more appropriate way to signal “trending.” It will aid overall comprehension if the trending icon is paired with the word “trending.”

When words are replaced with many emoji in a single line, it increases the difficulty for someone from a different culture with a different mental model to interpret the meaning. The translation effort becomes more challenging as well. As a result, users may get something that deviates from the original intention of the emoji. Additionally, multiple emoji in a single line can appear cluttered and visually distracting.

#### Fonts

Choosing the right typography can impact how your product text appears in different languages.

System fonts usually support a limited range of weights. However, if your chosen font doesn’t support various scripts, text in those scripts may be rendered differently depending upon the operating system and platform. The system default fonts also vary across operating systems. Chinese, Japanese, and Korean (CJK) system fonts (the typefaces that are pre-installed on computers and devices) typically use different font weights when compared to Latin characters.

It’s recommended to use Google’s Noto fonts if your product uses CJK or other scripts. Noto’s name comes from the phrase “no more tofu,” because the fonts eliminate the tofu-like boxes (𛲢𛲡𛲠) for missing glyphs that appear when a font is not available for a user’s text. Noto CJK, for example, provides full coverage for CJK characters in four scripts with seven weights: Simplified Chinese, Traditional Chinese, Japanese, and Korean.

Learn more about Noto fonts.

#### Line breaks

Line breaks can appear incorrectly in languages that do not use spaces between words, such as many CJK languages.

Budou is an open-source tool that automatically creates line breaks for CJK languages, which improves text readability.

Learn more: Language enablement line breaks and approaches to line breaks.

## Account for local design practices

#### Color

Color choice can directly influence an individual’s brand perception, While some colors are interpreted across many cultures with relative consistency, others convey a wide variety of symbolic meanings across cultures.

Learn more about applying color in the Material Design color guidelines.

#### Information density

Preferences for information density and design styles vary across regions and cultures. Density and style preferences can be explored with help from a localization specialist or expert in the culture. Within the same product or brand, designs may be changed to better serve audiences with different backgrounds or needs.

#### Bidirectionality

Languages such as Arabic, Hebrew, and Farsi are read from right-to-left (RTL). If you’re designing for left-to-right languages as the default, take time to ensure that your design is optimally mirrored for RTL languages. Learn more about bidirectionality.

#### Data formats

Different regions have varying conventions for data formats, including addresses, phone numbers, names, calendars, measurements, currencies, payment methods, and more.

Learn more:

- CLDR (Unicode Common Locale Data Repository): The international standard for automatic formatting of numbers, currency, and more.

- Material Design Data Formats guidance

## Create and share guidance or visual references

If you work with a translator or localization team, creating and sharing documentation around your goals will empower their work. Some examples of helpful documentation include:

- Product goals, intent, and details

- User personas and demographic features

- User journeys

- Target markets

- Brand voice guidelines

- Tone and style considerations

- Design mocks or sketches at any stage

- How much freedom the translator can have in adapting your content. (You may consider transcreation, a process to rewrite messages to fit the target culture.)

## Don’t forget to test!

Standard research and testing, such as functional testing done by a professional tester and native speaker, will help reveal technical and functional errors in localized content.

To learn if your product, content, or design is effective and enjoyable across locales, test localized mocks with a small group of your potential users. Ask them to walk through a user journey and learn from their struggles or successes with task completion. Testing provides a better understanding of how likely your product or content resonates with a region or culture, and where any potential risks lie.

Even after launching a product, it’s best to continue testing or user interviews to gather feedback as the product evolves. Distill those findings and insights and incorporate them into the next iteration of the product and content. Establish a cycle of research and embrace regional and cultural inclusion when designing and writing for international audiences.
