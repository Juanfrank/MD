<!-- source: https://m3.material.io/components/extended-fab/specs -->
# Extended FAB – Material Design 3

# Extended FABs

## Variants

[image: 3 variants of extended FABs.]

- Small extended FAB

- Medium extended FAB

- Large extended FAB

### Baseline variants

The baseline extended FAB is no longer recommended in the M3 expressive update. Use a small extended FAB; the type style was updated from label large to title medium, and the inner padding was reduced. View baseline extended FAB specs

[image: 1 baseline extended FAB.]

- Extended FAB

| Variant | M3 | M3 Expressive |

|---|---|---|

| Small extended FAB | -- | Available |

| Medium extended FAB | -- | Available |

| Large extended FAB | -- | Available |

| Extended FAB (baseline) | Available | Not recommended. Use small extended FAB. |

## Tokens & specs

Use the table's menu to select a token set. Extended FAB tokens are organized by size and color.

## Anatomy

[image: 3 elements of extended FABs.]

- Container

- Label text

- Icon

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

### Color styles

Extended FABs can use several combinations of color and on color styles, such as primary and on primary. The following color mappings provide the same level of contrast and functionality, so choose a color mapping based on visual preference.

[image: 6 extended FAB color styles.]

[image: 6 extended FAB color styles.]

Extended FAB color roles used for light and dark schemes:

- Primary container & on primary container (default)

- Secondary container & on secondary container

- Tertiary container & on tertiary container

- Primary & on primary

- Secondary & on secondary

- Tertiary & on tertiary

### Baseline color styles

Extended FABs should no longer use surface color styles. They’re still available, but not recommended.

[image: 1 baseline extended FAB color style.]

- Surface container FAB

## States

States are visual representations used to communicate the status of a component or interactive element. Learn more about interaction states

When using a non-default color mapping for extended FABs, make sure the state layer color is the same as the icon color. For example, the state layer color for primary mapping should be md.sys.color.primary.

[image: 4 states of extended FABs.]

- Enabled

- Hovered - elevation 4

- Focused

- Pressed

## Measurements

[image: Extended FAB padding and size measurements.]

Size and padding measurements of the small, medium, and large extended FABs

[image: Extended FAB margin measurements.]

Extended FABs should have margins of 16dp

## Baseline extended FAB

[image: 3 elements of baseline extended FAB.]

- Container

- Label text

- Icon

### Baseline configurations

[image: Baseline extended FAB with icon.]

With icon

[image: Baseline extended FAB without icon.]

Without icon

### Baseline tokens

Use the table's menu to select a token set. The baseline extended FAB token sets are organized by common tokens, then by surface and branded color styles. Other color styles like primary, secondary, and tertiary are still used by the latest extended FABs.

### Baseline colors

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 3 baseline extended FAB color roles.]

Extended FAB color roles used for light and dark schemes:

- Primary container + shadow

- On primary container

- On primary container

#### Additional color mappings

Extended FABs can use other combinations of container and icon colors. The color mappings below provide the same legibility and functionality as the default, so the color mapping you use depends on style alone.

[image: 3 deprecated extended FABs with different container and icon colors.]

Extended FABs can use different combinations of container and icon colors

### Baseline states

States are visual representations used to communicate the status of a component or interactive element. Learn more about interaction states

[image: 4 states of baseline extended FAB.]

- Enabled

- Hovered

- Focused

- Pressed

### Baseline measurements

[image: Margins of baseline extended FAB.]

Extended FABs have a padding of 16dp

[image: Size of baseline extended FAB while on screen.]

Extended FAB height, width, and icon size

| Attribute | Value |

|---|---|

| Container height | 56dp |

| Container width | Dynamic, 80dp min |

| Container shape | 16dp corner radius |

| Icon size | 24dp |

| Padding | 16dp |
