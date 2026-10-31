<!-- source: https://m3.material.io/components/segmented-buttons/specs -->
# Segmented button – Material Design 3

# Segmented buttons

[image: Diagram of segmented button indicating 3 parts of its anatomy.]

- Container

- Icon (optional for unselected state)

- Label text

## Tokens and specs

Browse the component elements, attributes, tokens, and their values. Learn more about design tokens

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

[image: Diagram of segmented button indicating its color mappings]

Segmented button color roles used for light and dark schemes:

- On surface

- Outline

- Secondary container

- On secondary container

## States

States are visual representations used to communicate the status of a component or interactive element. Learn more about interaction states

### Unselected

[image: Side by side view of segmented buttons with 5 unselected states.]

[image: Side by side view of segmented buttons with 5 unselected states.]

Unselected button states:

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

### Selected

[image: Side by side view of segmented buttons with 4 selected states.]

Selected button states:

- Selected

- Hovered on selected

- Focused on selected

- Pressed on selected

## Measurements

[image: Diagram indicating layout values, paddings, and target size for segmented buttons]

- Padding and container size

- Target size

| Attribute | Value |

|---|---|

| Container width | Dynamic based on labels |

| Segment width | Container width / total segments (Example: 1/3) |

| Height | 40dp |

| Outline width | 1dp |

| Label alignment | Center |

| Left/right padding | Min 12dp |

| Padding between elements | 8dp |

| Target size | 48dp |

### Density

Density can be used in denser UIs where space is limited. Density is only applied to the height.

[image: Side by side view of segmented buttons with 4 different density heights]

Each step down in density removes 4dp from the height
