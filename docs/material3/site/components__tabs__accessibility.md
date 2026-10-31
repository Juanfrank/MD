<!-- source: https://m3.material.io/components/tabs/accessibility -->
# Tabs – Material Design 3

# Tabs

## Use cases

Users should be able to:

- Undertake actions or invoke navigation to a new destination with assistive tech

- Select an action or destination from an off screen tab with assistive tech

- Maintain access of primary actions when the content is in a scrolled state

## Interaction & style

Touch

- When a user taps on an icon button, a touch ripple appears, indicating interaction feedback

- The selected indicator becomes active and shifts into position once the touch has been engaged

Touch: Tap

Scrollable

- When a set of tabs cannot fit on screen, scrollable tabs are used. They are best used for browsing on touch interfaces.

- To navigate between scrollable tabs, users swipe the set left or right. Users can also use arrow/tab to navigate through.

- It's not recommended to loop a tab set where it scrolls infinitely. This can trap users who are navigating linearly with a screen reader.

- To select an individual tab, users tap or press space/enter.

- Horizontal scrolling tabs meet accessibility requirements because they need to increase in width to respond to label text without affecting the layout, and horizontal scrolling is necessary to view those labels.

Scrollable: Scrollable Tabs

Cursor

- When hovered, the hover state appears, providing a visual cue that the icon button is interactive. When clicked (in both active and inactive states), a ripple appears and the indicator shifts into position, showing the user feedback.

Cursor: Hover, Click

Keyboard/Switch

- When tabbed, a focus indicator appears, providing a visual cue to the user that the destination is now selected

- When the user engages with the selected tab via Space/Enter in active states, the user is taken to a new destination

- Within the tab menu, the user is able to arrow/tab through the menu items, Space/Enter to select an item, or tab to exit the active state

Keyboard/Switch: Tab, Space/Enter, Arrow

### Avoid applying density by default

Don't apply density to tabs by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.

To ensure that this density setting can be easily reverted when it's active, keep all the targets to change it at minimum 48x48 CSS pixels each.

## Initial focus

On arrow/tab in a tab menu, the active indicator appears on the first interactive element, providing feedback to the user that it is selected. The user is then able to tab to additional interactive elements until all available items are complete within the tab menu.

Use Arrow/Tab to navigate through items

Don't use Space/Enter for navigating tabs. Space/Enter is only used for completing actions.

## Keyboard navigation

| Keys | Actions |

|---|---|

| Arrow | Focus lands on the next available navigation destination |

| Space / Enter | Activates the focused navigation destination |

| Arrow | Allows navigation through menu items |

## Labeling elements

When the visible UI text is ambiguous, or there is no visible UI text, accessibility labels need to be more descriptive. For example, an icon button that visually represents a “video camera” requires additional information in its accessibility label to clarify the icon’s intent.

[image: Small device screen  with the tab highlighted and the label and role illustrated.]

While the icon visually represents a “Video camera,” the accessibility label for this tab clarifies its function: “Video format media content”
