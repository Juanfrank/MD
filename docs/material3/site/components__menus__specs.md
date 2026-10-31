<!-- source: https://m3.material.io/components/menus/specs -->
# Menus – Material Design 3

# Menus

## Variants

### Vertical menus

Use vertical menus for a more expressive look and feel, including rounded corners, standard and vibrant color styles, more selection states, and submenu motion.

[image: 2 vertical menus use shape and color to indicate selected state.]

- Vertical menu with gap

- Vertical menu with divider

### Baseline variant

In M3 Expressive, baseline menu is still available to use, but doesn’t have the latest shapes, color styles, selection states, and motion. See baseline menu specs

[image: A baseline menu variant with square corners and standard colors.]

A baseline menu has square corners, as compared to a vertical menu’s round corners and expressive styling

| Variant | M3 | M3 Expressive |

|---|---|---|

| Vertical menus | -- | Available |

| Menu ( baseline) | Available | Available |

## Configurations

### Vertical menus layout

[image: 2 menus: 1 standard, and 1 with a gap, creating groups.]

[image: 2 menus: 1 standard, and 1 with a gap, creating groups.]

- Standard

- Grouped

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Color | Standard | Available | Available |

| Vibrant | -- | Available |

| Layout | Standard | Available | Available |

| Grouped | -- | Available |

## Tokens & specs

Browse the component elements, attributes, tokens, and their values. Learn about design tokens

## Anatomy

### Vertical menus

[image: A diagram of a vertical menu.]

[image: A diagram of a vertical menu.]

- Menu item

- Leading icon (optional)

- Menu item text

- Trailing icon (optional)

- Badge (optional)

- Trailing text (optional)

- Container

- Supporting text (optional)

- Label text (optional)

- Gap (optional)

- Divider (optional)

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. Learn more about design tokens

Menus have two color mappings:

- Standard: Surface-based

- Vibrant: Tertiary-based

These mappings provide options for lower or higher visual emphasis. Vibrant menus are more prominent so should be used sparingly.

[image: 2 vertical menus: 1 with lower visual emphasis, and 1 vibrant menu with bold shades.]

- Standard color scheme

- Vibrant color scheme

### Standard colors

[image: 2 vertical menus with standard color roles mapped to 11 elements.]

Vertical menus color roles used for light and dark themes:

- On surface variant

- On surface

- On surface (state layer)

- Surface container low

- On surface variant

- On surface variant

- Tertiary container (selected)

- On tertiary container (selected)

- On surface variant

- On surface variant

- On tertiary container (selected)

### Vibrant colors

[image: 2 vertical menus with vibrant color roles mapped to 11 elements.]

Vertical menus color roles used for light and dark themes:

- On tertiary container

- On tertiary container

- On tertiary container (state layer)

- Tertiary container

- On tertiary container

- On tertiary container

- Tertiary (selected)

- On tertiary (selected)

- On tertiary container

- On tertiary container

- On tertiary (selected)

## States

States are visual representations used to communicate the status of a component or an interactive element. More on interaction states Shape morphing in vertical menus creates an expressive active state. As focus moves between submenus, the corner shape changes to highlight the active menu. More on menu focus

[image: 6 vertical menu states in light and dark themes.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

- Active (main menu reveals submenu)

## Measurements

[image: Vertical menu marked with spacing and padding measurements.]

Vertical menu padding and size measurements

## Menu (baseline)

The baseline menu variant is available and continues to work in existing products. However, M3 expressive vertical menus are recommended for new designs.

### Baseline tokens & specs

Browse the component elements, attributes, tokens, and their values. Learn about design tokens

### Anatomy

[image: Diagram of 6 elements of a baseline menu.]

- List item

- List item leading icon

- List item trailing icon

- Container

- List item trailing text

- Divider

### Color

[image: 9 color roles of a baseline menu in light and dark themes.]

Baseline menu color roles used for light and dark themes:

- On surface variant

- On surface

- On surface - opacity: 0.08

- Surface container

- On surface variant

- On surface variant

- On surface variant

- Surface container highest

- Outline variant

### States

#### Default menu items

[image: Diagram numbering the 5 default states of a baseline menu.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

#### Selected menu items

[image: 5 states of a selected baseline menu item.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

State specs are in the token module above

### Measurements

[image: Diagram of a baseline menu’s padding, text alignment, height, and width.]

Baseline menu padding and size measurements

| Attribute | Value |

|---|---|

| Container width | 112dp min, 280dp max |

| Corner radius | 4dp |

| Vertical label text alignment | Center-aligned |

| Horizontal label text alignment | Start-aligned |

| Left/right padding | 12dp |

| Left/right padding with-icon | 12dp |

| List item height | 48dp |

| Padding between elements within a list item | 12dp |

| Divider top/bottom padding | 8dp |

| Divider height | 1dp |

| Divider width | Dynamic |

| Leading/trailing icon size | 24dp |

### Configurations

A baseline menu appears when a person interacts with a button, action, or other control.

A few examples:

- Button

- Text field

- Icon button

- Selected text

[image: Examples of 4 baseline menu inputs.]
