<!-- source: https://m3.material.io/components/split-button/specs -->
# Split buttons

# Split buttons

## Variants

[image: 1 type of split button.]

| Variant | M3 | M3 Expressive |

|---|---|---|

| Split button | -- | Available |

## Configurations

[image: 4 colors and 5 sizes of split buttons.]

- Color configurations: Elevated, filled, tonal, outlined

- Size configurations: XS, S, M, L, XL

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Size | XS, S, M, L, XL | -- | Available |

| Color | Elevated, filled, tonal, outlined | -- | Available |

## Tokens & specs

Use the table's menu to select a token set. Split button token sets are organized by size. Learn about design tokens

## Anatomy

[image: 4 elements of a split button.]

[image: 4 elements of a split button.]

- Leading button

- Icon

- Label text

- Trailing button

The leading button in split buttons can have an icon, label text, or both. The trailing button should always have a menu icon.

[image: 3 customizations of the leading button in the split button.]

- Label + icon

- Label

- Icon

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value.

Split buttons use the same color schemes as standard buttons. However, unlike toggle buttons, the split button color doesn’t change when selected—only a state layer is applied.

Split buttons use the same colors and state layers as buttons, shown in the following token module. Go to buttons for more details.

[image: 4 color roles of the split button when unselected and selected in light and dark theme.]

A: Unselected, B: Selected trailing icon

- Elevated

- Filled

- Tonal

- Outlined

## States

States are visual representations used to communicate the status of a component or an interactive element.

Split button states use the same colors and state layers as buttons and icon buttons. Go to those specs for details.

### Leading button shape

The inner corners change shape for hovered, focused, and pressed states.

[image: 5 states of the leading button in the split button.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed, pressed with focus

### Trailing button shape

The inner corners change shape for hovered, focused, and pressed states, and the icon becomes centered when selected.

[image: 6 states of the trailing menu button in the split button.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed, pressed with focus

- Selected, selected with focus

## Measurements

Text and icons are optically centered when the buttons are asymmetrical. They’re centered normally when symmetrical.

[image: Padding and size measurements of the split button.]

Menu icon offset when unselected:

- XS: -1dp from center

- S: -1dp from center

- M: -2dp from center

- L: -3dp from center

- XL: -6dp from center

The inner corner radius changes depending on button sizing. The space should always be 2dp.

[image: Inner padding and inner corner measurements of the split button.]

- Extra small 4dp

- Small 4dp

- Medium 4dp

- Large 8dp

- Extra large 12dp
