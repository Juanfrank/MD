<!-- source: https://m3.material.io/components/navigation-bar/specs -->
# Navigation bar – Material Design 3

# Navigation bar

## Variants

[image: The recommended flexible navigation bar.]

- Flexible navigation bar

### Baseline variants

The baseline nav bar is no longer recommended, and should be replaced by the flexible nav bar, which is shorter and supports horizontal navigation items in medium windows. View baseline nav bar specs

[image: 1 baseline navigation bar.]

- Navigation bar (not recommended)

| Variant | M3 | M3 Expressive |

|---|---|---|

| Flexible navigation bar | -- | Available |

| Navigation bar | Available | Not recommended. Use flexible navigation bar. |

## Configurations

In compact windows, navigation bars use vertical items. In medium windows, navigation bars should use horizontal items.

[image: Two size configurations for navigation bar and items.]

- Vertical navigation items

- Horizontal navigation items

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Navigation item layout | Vertical (default) | Available | Available |

| Horizontal | -- | Available |

## Tokens & specs

Use the table's menu to switch between token sets for the navigation bar and the nav items. Learn about design tokens

## Anatomy

[image: Seven elements of the navigation bar.]

[image: Seven elements of the navigation bar.]

- Container

- Icon

- Label text

- Active indicator

- Small badge (optional)

- Large badge (optional)

- Large badge label

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value. Learn more about design tokens

[image: Six color roles of the navigation bar.]

Navigation bar color roles used for light and dark schemes:

- Surface container

- On-secondary container

- Secondary

- Secondary container

- On-surface variant

- On-surface variant

For badge color roles, go to badge specs.

## States

States are visual representations used to communicate the status of a component or an interactive element.

[image: Four states of the navigation bar items.]

- Enabled

- Hovered (8% state layer)

- Focused (10% state layer)

- Pressed (10% state layer)

## Measurements

The navigation bar stretches the full window width.

[image: Navigation bar padding and size measurements.]

Navigation bar padding and size measurements

Vertical navigation items dynamically change width to equally fit the container. Horizontal navigation items have a fixed width, so extra space is added to the ends of the navigation bar instead.

[image: Navigation bar and item widths.]

Navigation bar width and margins for compact and medium windows.

- Vertical navigation item

- Margin from window edge

- Horizontal navigation item

## Baseline navigation bar

[image: 7 elements of baseline navigation bar.]

- Container

- Icon

- Label text

- Active indicator

- Small badge

- Large badge

- Large badge label

### Tokens & specs

These tokens are for the baseline navigation bar.

### Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 6 color roles of baseline navigation bar.]

Navigation bar color roles used for light and dark schemes:

- Surface

- On secondary container

- On surface

- Secondary container

- On surface variant

- On surface variant

For badge color roles, go to badge specs.

### States

States are visual representations used to communicate the status of a component or an interactive element.

[image: 4 states of baseline navigation bar.]

Navigation bar states:

- Enabled

- Hovered

- Focused

- Pressed

## Measurements

[image: Baseline navigation bar padding and size measurements.]

Navigation bar padding and size measurements

[image: Baseline navigation bar target size and margins.]

Navigation bar target size and margins

## Configurations

[image: 3 configurations of the baseline navigation bar.]

- 3 destinations

- 4 destinations

- 5 destinations
