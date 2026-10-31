<!-- source: https://m3.material.io/foundations/watches/layout -->
# Watches – Material Design 3

# Design for watches

## Resources

| Type | Resource |

|---|---|

| Design | Wear OS common design layouts |

| Adaptive layout for Wear OS |

| Figma Design Kit for Wear OS Apps |

| Figma Design Kit for Wear OS Tiles |

| Implementation | Android Developers: Wear OS |

## Layout principles

[image: A social networking scrolling screen showing Followers, sorting and search.]

Prioritize content

Place the most important information at the top of the screen.

[image: An audio interface showing headphones are connected with volume indicator and controls.]

Limit choices

Reduce the number of actions to prevent decision fatigue. Focus on critical tasks to help people get things done within seconds.

[image: A dialog confirming device access to call log and contacts.]

Simplify navigation

Use a clear, shallow hierarchy so people don't get lost in complex menus. Aim to display content and navigation inline.

## Standard layouts

For scrolling and non-scrolling apps:

- The time is shown on most app screens

- Edge-hugging buttons are used for round screens

- Show an indicator if more content is available on a scrolling apps

Wear OS offers Figma Design Kits for standard layouts, with components, styles, and variables.

[image: A watch screen showing a social media app and a watch screen showing a timer with element indicators.]

- Time text

- Page title

- Scroll indicator

- Action button

### Non-scrolling layouts

Non-scrolling layouts are for focused tasks or single-screen interactions where all content fits within the display, such as:

- Media players

- Pickers and switchers

- Fitness tracking screens

- Confirmation dialogs

More on non-scrolling layouts for Wear OS

[image: A non-scrollable timer with current time 9:30, timer set for 00:25:52, and a start button.]

Use non-scrolling layouts for focused tasks like a timer

### Scrolling layouts

Scrolling layouts can show content that exceeds the screen height, such as lists or dialogs. These might include:

- Message threads

- Contact lists

- Menu options

More on scrolling layouts for Wear OS

[image: A scrollable layout with current time, search button, 1st follower and avatar on screen, and two followers off screen.]

Lists use scrolling layouts to show additional options

### Tiles

Tiles (or widgets) are designed for glanceability. Use them to show timely updates or to help people perform frequent tasks quickly, such as checking progress towards a goal or viewing the weather.

Tiles are accessible with a swipe from the watch face. They have a fixed screen height and don't scroll.

More on tiles for Wear OS

[image: Icon buttons for meditation, running, cycling, and a More button]

Use tiles for quick access to to a few key options

### Notifications

Notifications can be expanded to offer more interactions, such as replying to a message, opening a location on a map, or playing a song.

Wear OS provides notification templates for instant messaging and calendar events.

More on notifications for Wear OS

[image: A message notification shown in a drawer with dimmed notifications above and below.]

Notifications should offer easy access to more interactions

### Adaptive layout

Adaptive design allows apps to adapt to different screen sizes and device contexts. On Wear OS, this means apps scale and reorganize to maximize the available space on both small and large round displays. The Material 3 Compose component library has built-in adaptive behavior.

- Design for small screens first: Start by designing for the smallest common screen size

- Use percentages: Define margins and padding using percentages rather than fixed pixel values. This prevents clipping and ensures content remains centered and proportional as the screen size increases.

- Add value on larger screens: Use the extra space on screens larger to show more content, such as additional buttons, text lines, or data visualizations

- Test all font sizes: Font scaling and accessibility settings such as bold text may cause changes in the size of UI elements

More on adaptive layout for Wear OS

[image: 5, 10, and 15 minute alarm buttons plus an edge-hugging more button.]

Design for small screens first, starting with a 192dp size watch

[image: 5, 10, 15, 20 &amp; 30 minute alarm buttons plus an edge-hugging more button.]

Show more content on devices that are larger than 225dp
