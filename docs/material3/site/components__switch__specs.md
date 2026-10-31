<!-- source: https://m3.material.io/components/switch/specs -->
# Switch – Material Design 3

# Switch

[image: 3 elements of a switch.]

- Track

- Handle (formerly "thumb")

- Icon

## Tokens & specs

Browse the component elements, attributes, tokens, and their values. Learn more about design tokens

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 6 color roles of a switch in light and dark themes.]

Switch color roles used for light and dark themes:

- Surface container highest

- Outline

- Outline

- Primary

- On primary

- On primary container

### Adjacent text label color

Use the color role on surface for adjacent text labels. This remains the same even if interacting with the label or component.

[image: The large body text adjacent to switches uses "on surface" color and the body text uses "on surface variant."]

The text label uses on surface. Supporting text may use on surface variant.

## States

States are visual representations used to communicate the status of a component or interactive element. Learn more about interaction states

[image: 5 states of a switch shown in light and dark themes.]

[image: 5 states of a switch shown in light and dark themes.]

- Enabled

- Hovered

- Focused

- Pressed

- Disabled

State specs are in the token module above

## Measurements

[image: Measurements of switches without icons.]

Switches without icons

[image: Measurements of pressed switches without icons.]

Pressed switches without icons

[image: Measurements of switches with icons.]

Switches with icons

[image: Measurements of pressed switches with icons.]

Pressed switches with icons

| Element | Attribute | Value |

|---|---|---|

| Track | Height | 32dp |

| Width | 52dp |

| Outline width | 2dp |

| Shape | md.sys.shape.corner.full |

| Handle | Height (unselected) | 16dp |

| Height - with icon | 24dp |

| Height (selected) | 24dp |

| Height (pressed) | 28dp |

| Width (unselected) | 16dp |

| Width - with icon | 24dp |

| Width (selected) | 24dp |

| Width (pressed) | 28dp |

| Shape | md.sys.shape.corner.full |

| State layer | Size | 40dp |

| Shape | md.sys.shape.corner.full |

| Target | Size | 48dp |

| Icon | Size (selected) | 16dp |

| Icon | Size (unselected) | 16dp |

## Configurations

- Without icons

- Icon on selected switch

- Icon on selected and unselected switch

[image: 3 example switches with and without icons in on and off states. ]
