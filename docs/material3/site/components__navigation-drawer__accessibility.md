<!-- source: https://m3.material.io/components/navigation-drawer/accessibility -->
# Navigation drawer – Material Design 3

# Navigation drawer

## Use cases

Users should be able to:

- Move between navigation destinations with assistive technology

- Select a particular navigation destination from a set

- Get appropriate feedback based on input type

## Interaction & style

Touch

- When a navigation item is tapped, the active indicator appears in place, providing feedback to the user that it is selected

- A touch ripple passes through the indicator

- The icon switches from outlined to filled

- The icon changes color, becoming darker

Touch: Tap

Cursor

- When hovered, the hover indicator appears providing a visual cue that the destination is interactive

- When clicked, a ripple passes through the indicator

- The icon switches from outlined to filled

- The icon changes color, becoming darker in light theme and lighter in dark theme, to increase the contrast

Cursor: Hover, Click

## Initial focus

Initial focus lands directly on the first navigation item, since that is the first interactive element of the component.

[image: 1. Tab lands on the first navigation item, Inbox. 2. Down arrow to get to the second navigation item, Outbox.]

Focus lands on first navigation item

## Closing

The modal navigation drawer can be dismissed by selecting the scrim that covers the rest of the screen.

[image: A navigation drawer with a scrim covering the body content. A touch target is selecting the scrim.]

Select the scrim to close the navigation drawer

## Visual indicators

Icons are the primary focus of the navigation and such give the dominant cue of its state. Use a filled icon for the selected destination to differentiate from the outlined icons of non-selected destinations.

[image: Space + enter is used to select the navigation item inbox.]

The navigation item is selected via Space/Enter

[image: A navigation drawer with the home destination using a filled icon.]

Use a filled icon for the selected navigation destination to differentiate from the other destinations

[image: A navigation drawer with the home destination using an outlined icon.]

Avoid keeping the icon style for the selected navigation destination the same as unselected destination's icons. This removes an important visual indicator of which destination is active.

[image: A selected home icon using a filled icon and active indicator and a unselected home icon using an outlined icon.]

When selected, the icon fills, darkens in light theme (or lightens in dark theme), and is backed by an active indicator shape

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab | Focus lands on the first navigation destination |

| Space or Enter | Selects the focused navigation destination, and focus moves to the newly opened section (if applicable) |

| Arrow | Navigate between destinations within the navigation drawer |

## Labeling elements

The accessibility label for a navigation item is typically the same as the destination name. If the UI text is correctly linked, assistive tech (such as a screenreader) will read the UI text followed by the component’s role. For Android Views (MDC-Android), a more descriptive accessibility label is not available to be set and the role is not announced.

[image: A navigation drawer item’s label text and accessibility label both read “photos.” The role is “tab.”]

A navigation drawer’s accessibility label can incorporate its adjacent UI text

When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a navigation destination visibly labeled Recents would benefit from additional information in its accessibility label to clarify the destination’s intent.

[image: A navigation drawer item’s label text is “recents”, the accessibility label is “recent images.” The role is “tab.”]

While the visible label text reads Recents, the accessibility label for this destination clarifies its function: Recent images
