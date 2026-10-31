<!-- source: https://m3.material.io/components/icon-buttons/specs -->
# Icon buttons – Material Design 3

# Icon buttons

## Variants

[image: Side by side view of default and toggle icon buttons.]

- Default icon button

- Toggle icon button

| Variant | M3 | M3 Expressive |

|---|---|---|

| Default | Available | Available |

| Toggle (selection) | Available | Available |

## Configurations

[image: Side by side view of size, shape, color, and width variations.]

- Five sizes

- Two shapes

- Four color styles

- Three widths

| Category | Options | M3 | M3 Expressive |

|---|---|---|---|

| Size | Small (default) | Available | Available |

| XS, M, L, XL | -- | Available |

| Shape | Round (default) | Available | Available |

| Square | -- | Available |

| Color | Filled (default), tonal, outlined, standard | Available | Available |

| Width | Default | Available | Available |

| Narrow, wide | -- | Available |

## Tokens & specs

Icon button token sets are organized by common tokens, color, and size. Select the token set from the table’s menu. Learn about design tokens

## Anatomy

[image: Diagram indicating anatomy of filled icon button.]

[image: Diagram indicating anatomy of filled icon button.]

- Icon

- Container

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value.

There are four built-in color styles: filled, tonal, outlined, and standard. Default and toggle buttons use different color roles per style.

[image: Color roles of default and toggle buttons in 4 visual styles.]

A: Filled, B: Tonal, C: Outlined, D: Standard

- Default

- Toggle, unselected

- Toggle, selected

|  | 1. Default | 2. Toggle, unselected | 3. Toggle, selected |

|---|---|---|---|

| Filled container Filled icon | Primary On primary | Surface container On surface variant | Primary On primary |

| Tonal container Tonal icon | Secondary container On secondary container | Secondary container On secondary container | Secondary On secondary |

| Outlined container Outlined icon | Outline variant (outline) On surface variant | Outline variant (outline) On surface variant | Inverse surface Inverse on surface |

| Standard icon | On surface variant | On surface variant | Primary |

## States

States are visual representations used to communicate the status of a component or interactive element. State layers slightly change button color. Disabled states have different base colors. View tokens for details

### Filled button states

#### Default

[image: 5 states of filled icon button.]

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

#### Toggle

[image: 5 states of filled toggle icon button.]

A: Unselected. B: Selected

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

### Tonal button states

#### Default

[image: 5 states of tonal icon button.]

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

#### Toggle

[image: 5 states of tonal toggle icon button.]

A: Unselected. B: Selected

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

### Outlined button states

#### Default

[image: 5 states of outlined icon button.]

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

#### Toggle

[image: 5 states of outlined toggle icon button.]

A: Unselected. B: Selected

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

### Standard icon button states

The standard icon button’s container is invisible at rest, but visible when the state layer is applied.

#### Default

[image: 5 states of standard icon button.]

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

#### Toggle

[image: 5 states of standard toggle icon button.]

A: Unselected. B: Selected

- Enabled

- Disabled (10% state layer)

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

## Shape morph

### Pressed state

While pressed, icon buttons can morph to become more square.

Both round and square icon buttons should have the same pressed shape radius. The corner radius value differs for each button size. See full icon button corner measurements

[image: Shape changes for round and square icon buttons in 3 states.]

A. Round, B. Square

- Enabled

- Hovered

- Pressed

### When selected

In addition to changing shape when pressed, toggle icon buttons also change the resting shape from round (unselected) to square (selected) by default. If the resting shape is square, the selected shape should be round.

[image: Shape changes for round and square toggle icon buttons in 3 states.]

A. Round, B. Square

- Enabled

- Hovered

- Pressed

- Selected

## Measurements

[image: Diagram of 5 sizes of icon buttons in 4 widths.]

A. Extra small B. Small C. Medium D. Large E. Extra large

- Icon size

- Default width size

- Narrow width size

- Wide width size

### Target sizes

Extra small and small icon buttons must have a target size of 48x48dp or larger to be accessible.

[image: Diagram of target sizes.]

A. Extra small icon button size B. Small icon button size

- Narrow width

- Default width

- Wide width

### Button corner radius

[image: Diagram of icon button corner radius.]

|  | XS | S | M | L | XL |

|---|---|---|---|---|---|

| A. Round button | Full | Full | Full | Full | Full |

| B. Square button | 12dp | 12dp | 16dp | 28dp | 28dp |

| C. Pressed state | 8dp | 8dp | 12dp | 16dp | 16dp |

## Baseline tokens

Use the table's menu to select a token set. Filled, tonal, and outlined icon button tokens are now deprecated in favor of the new token sets. All other tokens are still available in the module at the top of the page.
