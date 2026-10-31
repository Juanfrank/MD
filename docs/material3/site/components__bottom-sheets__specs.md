<!-- source: https://m3.material.io/components/bottom-sheets/specs -->
# Bottom sheets – Material Design 3

# Bottom sheets

Modal bottom sheets are above a scrim while standard bottom sheets don't have a scrim. Besides this, both variants of bottom sheets have the same specs.

[image: Diagram of container, drag handle, scrim]

- Container

- Drag handle (optional)

- Scrim

## Tokens and specs

Browse the component elements, attributes, tokens, and their values. Learn more about design tokens

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

[image: Two diagrams featuring color opposites of scrim, container, drag handle]

Bottom sheet color roles used for both light and dark schemes:

- Scrim*

- On surface variant

- Surface container low

*On Android platforms, the scrim color and opacity is automatically handled by the system UI.

## Measurements

[image: Bottom sheet on larger device with 56dp top and 56dp side margins]

[image: Bottom sheet on larger device with 56dp top and 56dp side margins]

Bottom sheet padding and size measurements

Bottom sheets span the full window width up to 640dp. When the window width exceeds 640dp, bottom sheets adjust to have a top margin of 56dp and side margins of 56dp.

| Attribute | Value |

|---|---|

| Drag handle alignment (horizontal) | Center |

| Drag handle padding top/bottom | 22dp |

| Top margin | 72dp |

| Top margin (window width > 640dp) | 56dp |

| Start/end margin (window width > 640dp) | 56dp |

| Width | Full width, up to max-width 640dp |

| Height | Variable |
