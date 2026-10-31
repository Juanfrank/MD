<!-- source: https://m3.material.io/components/switch/accessibility -->
# Switch – Material Design 3

# Switch

## Use cases

People should be able to do the following with assistive technology:

- Navigate to a switch with a keyboard or switch input

- Toggle the switch on and off

- Get appropriate feedback based on input type documented under Interaction & style

## Interaction & style

The switch handle increases in size to indicate interactivity for both touch and cursor control interactions.

Touch When tapped or dragged, the handle size grows, providing interaction feedback.

Cursor When hovered (in both on and off states), the hover area grows, providing a visual cue that the handle is interactive. When clicked, the handle size grows.

[image: The switch handle increases in size when tapped and dragged.]

Touch: Tap, Drag

[image: The cursor changes from an arrow to a hand pointer when hovering over and clicking the switch.]

Cursor: Hover, Click

### Avoid applying density by default

Don't apply density to switches by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.

To ensure that this density setting can easily be reverted when it's active, keep all targets to change it at a minimum 48x48 CSS pixels each.

## Initial focus

Initial focus lands directly on the switch’s handle, since it’s the primary interactive element of the component.

[image: The focus is on the switch handle, which is toggled on.
]

Focus lands on the switch handle

[image: Space or Enter is used to toggle the switch off.]

The switch is toggled using Space or Enter

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab | Focus lands on the switch handle |

| Space or Enter | Toggles the handle on and off |

## Labeling elements

The accessibility label for a switch uses the adjacent label text if implemented correctly.

Assistive tech such as a screen reader will read the UI text followed by the component’s role.

[image: “Dark theme” is the switch’s adjacent label text and the accessibility label.]

[image: “Dark theme” is the switch’s adjacent label text and the accessibility label.]

A switch’s accessibility label can incorporate its adjacent UI text

When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a switch visibly labelled Photo album would benefit from additional information to clarify the switch’s function.

Consider making the adjacent label text more descriptive when possible. This reduces the need for different accessibility text.

[image: The accessibility label for the switch is “Photo album access” though the label text is “photo album.”]

[image: The accessibility label for the switch is “Photo album access” though the label text is “photo album.”]

While the visible label text reads Photo album, the accessibility label for this switch clarifies its function: Photo album access
