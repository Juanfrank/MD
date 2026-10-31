<!-- source: https://m3.material.io/components/toolbars/specs -->
# Toolbars – Material Design 3

# Toolbars

## Variants

[image: 2 variants of toolbars.]

- Docked toolbar

- Floating toolbar

### Baseline variant

The baseline bottom app bar is no longer recommended. It should be replaced with the docked toolbar, which is very similar and more flexible.

[image: Baseline bottom app bar, which looks like the docked toolbar, but is not recommended.]

- Bottom app bar (not recommended)

| Variant | M3 | M3 Expressive |

|---|---|---|

| Docked toolbar | -- | Available |

| Floating toolbar | -- | Available |

| Bottom app bar | Available | Not recommended. Use docked toolbar. |

## Configurations

[image: Color configuration of toolbars.]

[image: Color configuration of toolbars.]

- Standard and vibrant toolbars

- Vertical floating toolbar

- Floating toolbar with FAB

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Color | Standard (default) | Available as bottom app bar | Available |

| Vibrant | -- | Available |

| Floating toolbar layout | Horizontal (default) | -- | Available |

| Vertical | -- | Available |

| Other elements | With FAB | Available as bottom app bar | Available* |

## Tokens & specs

Browse the component elements, attributes, tokens, and their values. Jump to baseline bottom app bar specs

## Anatomy

[image: 2 elements of a toolbar.]

- Container

- Placed components

### Flexibility & slots

When configuring a toolbar, think of it as a container with several slots.

Each slot can be a different element. The most common elements are icon buttons, buttons, and text fields.

[image: A toolbar with 5 slots, conceptual spaces for UI elements, next to each other.]

A toolbar is essentially a container with configurable slots

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

### Standard

[image: 4 color roles in the standard color scheme  of the floating toolbar in light and dark scheme.]

Standard color schemes and icon button types:

- Surface container

- Filled button (Primary, On primary)

- Toggle tonal button (Secondary container, On secondary container)

- Standard button (Primary)

### Vibrant

[image: 4 color roles in the vibrant color scheme of the floating toolbar in light and dark scheme.]

Vibrant color scheme and icon button types:

- Primary container

- Filled button (Primary, On primary)

- Toggle tonal button: (Surface container, On surface)

- Standard button (On primary container)

## Measurements

By default all toolbars are 64dp high, center-aligned, have equal padding between items, and have a minimum outside padding of 16dp.

### Docked toolbar

[image: Default internal padding of a docked toolbar.]

- Default margins and padding

- Margins and padding with leading, middle, and trailing content

[image: 2 docked toolbars with different margins and alignment.]

Alignment and padding can be configured to create unique layouts:

- Left and right alignment

- Center-aligned, 8dp padding between items

### Floating toolbar

[image: Diagram noting margin around edge of floating toolbar.]

Default padding of floating toolbar

[image: Diagram noting layout measurements.]

Floating toolbar size and padding measurements

[image: Diagram noting layout margins.]

Floating toolbar margins

## Bottom app bar (baseline)

[image: Diagram of bottom app bar indicating the container.]

- Container

### Tokens & specs

Bottom app bar tokens are in one token set.

### Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. Learn more about design tokens

[image: Diagram of bottom app bar indicating its color mappings.]

Bottom app bar color role used for light and dark themes:

- Surface container

### Measurements

[image: Diagram showing layout values and paddings for bottom app bar.]

Bottom app bar padding and size measurements

### Common layouts

[image: Side by side view of bottom app bars in different configurations.]

- Icon buttons and FAB

- Icon buttons and no FAB
