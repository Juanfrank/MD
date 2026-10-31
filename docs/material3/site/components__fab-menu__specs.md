<!-- source: https://m3.material.io/components/fab-menu/specs -->
# FAB menu - Material Design 3

# FAB menu

## Variants

[image: The FAB menu in its single variant.]

There’s one variant of FAB menu

| Variant | M3 | M3 Expressive |

|---|---|---|

| FAB menu | -- | Available |

## Configurations

[image: 3 color configurations of FAB menus.]

Three color sets:

- Primary

- Secondary

- Tertiary

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Color | Primary set, secondary set, tertiary set | -- | Available |

## Tokens & specs

Use the table's menu to switch token sets. The FAB menu has a common token set and six color sets, three for each element (close button and menu item). Learn about design tokens

## Anatomy

[image: 2 elements of a FAB menu.]

[image: 2 elements of a FAB menu.]

- Close button

- Menu item

[image: 5 FAB menus showing the range of 2–6 items.]

[image: 5 FAB menus showing the range of 2–6 items.]

The FAB menu can have up to six items

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 12 colors of the FAB menu.]

- On primary container

- Primary container

- On primary

- Primary

- On secondary container

- Secondary container

- On secondary

- Secondary

- On tertiary container

- Tertiary container

- On tertiary

- Tertiary

## States

States are visual representations used to communicate the status of a component or interactive element. Learn more about interaction states

### Close button

[image: 4 states of the FAB menu close button.]

Close button states in light and dark themes:

- Enabled

- Hovered

- Focused

- Pressed

### Menu item

[image: 4 states of the FAB menu items.]

Menu item states in light and dark themes:

- Enabled

- Hovered

- Focused

- Pressed

## Measurements

FAB menu items share the same measurements as the medium button specs.

The close button should always be 56dp.

[image: FAB menu size measurements.]

FAB menu size measurements

The FAB menu animates from the top trailing edge of the FAB to ensure a smooth animation.

[image: FAB on a mobile screen with 16dp margins annotated.]

The FAB should always have 16dp margins

[image: FAB menu opened from a FAB has matching margins of 16dp.]

The close button and FAB share the top trailing corner as an anchor and appear in the same place

Larger FABs will place the FAB menu slightly higher, with larger margins underneath.

[image: Medium FAB on a mobile screen with 16dp margins annotated.]

The medium FAB placement has 16dp margins

[image: FAB menu opened from the medium FAB has a 40dp margin from bottom of screen.]

The close button is placed higher to align with the top of the medium FAB

[image: Large FAB on a mobile screen with 16dp margins annotated.]

The large FAB placement has 16dp margins

[image: FAB menu opened from the large FAB has a 56dp margin from bottom of screen.]

The close button is placed higher to align with the top of the large FAB

On web, the FAB menu opens from the FAB, and inherits its states and specs from the baseline menu component.

The gap between the FAB and menu can vary, but 4dp is recommended.

[image: FAB menu on web states and specifications.]

Spacing and interaction on FAB menu for web:

- Enabled

- Hovered

- Selected
