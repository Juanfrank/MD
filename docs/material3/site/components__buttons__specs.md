<!-- source: https://m3.material.io/components/buttons/specs -->
# Buttons – Material Design 3

# Buttons

## Variants

[image: Diagram comparing buttons with toggle buttons.]

- Default button

- Toggle button

| Variant | M3 | M3 Expressive |

|---|---|---|

| Default | Available | Available |

| Toggle (selection) | -- | Available |

## Configurations

[image: Diagram showing configurations of buttons.]

- Size

- Shape

- Color

- Small button padding

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Size | Small (default) | Available | Available |

| XS, M, L, XL | -- | Available |

| Shape | Round (default) | Available | Available |

| Square | -- | Available |

| Color | Elevated, filled (default), tonal, outlined, text | Available | Available |

| Small button padding | 24dp | Available | Not recommended. Use 16dp |

| 16dp | -- | Available |

## Tokens & specs

Use the table's menu to select a token set. Button token sets are separated into common tokens, color, and size. View baseline tokens

## Anatomy

[image: Diagram labeling 3 parts of a button.]

[image: Diagram labeling 3 parts of a button.]

- Container

- Label text

- Icon (optional)

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.

- There are five built-in button color styles: elevated, filled, tonal, outlined, and text

- The default and toggle buttons use different colors

- Toggle buttons don’t use the text style

[image: Diagram shows dark and light color schemes for buttons.]

A. Elevated, B. Filled, C. Tonal, D. Outlined, E. Text

- Default

- Toggle: unselected

- Toggle: selected

|  | 1. Default | 2. Toggle unselected | 3. Toggle selected |

|---|---|---|---|

| Elevated container Elevated icon & label | Surface container low Primary | Surface container low Primary | Primary On primary |

| Filled container Filled icon & label | Primary On primary | Surface container On surface variant | Primary On primary |

| Tonal container Tonal icon & label | Secondary container On secondary container | Secondary container On secondary container | Secondary On secondary |

| Outlined container Outlined icon & label | Outline variant (outline) On surface variant | Outline variant (outline) On surface variant | Inverse surface Inverse on surface |

| Text icon & label | Primary | -- | -- |

## States

States are visual representations used to communicate the status of a component or interactive element.

### Elevated button states

The elevated button style has an elevation of 1 by default and 0 when disabled.

#### Default

[image: Elevated button states.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

#### Toggle

[image: Toggle elevated button states.]

A. Unselected, B. Selected

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

### Filled button states

#### Default

[image: Filled button states.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

#### Toggle

[image: Toggle filled button states.]

A. Unselected, B. Selected

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

### Tonal button states

#### Default

[image: Tonal button states.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

#### Toggle

[image: Toggle tonal button states.]

A. Unselected, B. Selected

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

### Outlined button states

The outlined button’s container fill is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed.

#### Default

[image: Outlined button states.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

#### Toggle

[image: Outlined button states.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

### Text button style states

The text button’s container is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed. There is no toggle text button.

[image: Default text button style states.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

## Shape morph

### Pressed state

When pressed, buttons can morph to become more square. Both round and square buttons should have the same pressed shape.

The corner radius value differs for each button size. See full button corner measurements

[image: Shape changes of a button.]

A. Round button, B. Square button

- Enabled

- Hovered

- Pressed

### When selected

In addition to changing shape when pressed, toggle buttons also change the resting shape from round (unselected) to square (selected).

If the resting unselected shape is square, the selected shape should be round.

[image: Shape changes of a toggle button.]

A. Round button, B. Square button

- Enabled

- Hovered

- Pressed

- Selected

## Measurements

[image: Diagram of measurements of all button sizes.]

Padding and size measurements of each button size

- Extra small

- Small

- Medium

- Large

- Extra large

### Target areas

Extra small and small icon buttons must have a target size of 48x48dp or larger to be accessible.

[image: Diagram of small button target areas.]

A. Extra small B. Small

- Round button

- Button with icon

- Square button

### Corner sizes

[image: Diagram of corner radii of buttons.]

|  | XS | S | M | L | XL |

|---|---|---|---|---|---|

| A. Round button | Full | Full | Full | Full | Full |

| B. Square button | 12dp | 12dp | 16dp | 28dp | 28dp |

| C. Pressed state | 8dp | 8dp | 12dp | 16dp | 16dp |

## Baseline tokens

Use the table's menu to switch token sets. The baseline button token sets are organized by color.
