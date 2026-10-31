<!-- source: https://m3.material.io/components/button-groups/specs -->
# Button groups

# Button groups

## Variants

[image: Various colors and shapes of standard and connected button groups.]

- Standard button group

- Connected button group

| Variant | M3 | M3 Expressive |

|---|---|---|

| Standard button group | -- | Available |

| Connected button group | Available as segmented button | Available |

## Configurations

[image: Five sizes of button groups and two shapes of button groups.]

Configurations for both variants of button groups:

- Extra small

- Small

- Medium

- Large

- Extra large

- Single-select and multi-select

- Round and square

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Size | XS, S, M, L, XL | -- | Available |

| Default shape | Round, square | -- | Available |

| Selection | Single-select, multi-select, selection-required | Available as segmented button | Available |

## Tokens & specs

Standard and connected button group tokens are organized by size. Select the variant and size from the token set menu. Go to the button and icon button pages to view their tokens. Learn about design tokens

## Anatomy

Button groups are invisible containers that add padding between buttons and modify button shape. They don’t contain any buttons by default.

[image: The container outlined on both variants of button groups.]

[image: The container outlined on both variants of button groups.]

- Container

### Common layouts

Mix and match buttons and icon buttons for different scenarios.

[image: 4 common layouts of button groups.]

[image: 4 common layouts of button groups.]

- Label buttons

- Label buttons and icon buttons

- Extra small icon buttons

- Large icon buttons

### Color

Button groups have no color properties. They can use the default button or toggle button color styles, like filled, tonal, and outlined. Avoid using standard icon buttons or text buttons, as they have no container treatment.

[image: The container outlined on both variants of button groups.]

- Filled

- Tonal

- Outlined

- Elevated

## Selection & activation

Standard button groups add interaction between adjacent buttons when a button is selected or activated. This interaction changes the width, shape, and padding of the selected or activated button, which adjusts the width of buttons directly next to it.

A selected button changes shape, and briefly changes the width of itself and adjacent buttons

Connected button groups don’t add any interaction between buttons when selected or activated.

They only affect the shape of the button being selected or activated.

A selected button changes shape without affecting adjacent buttons

## States

### Standard button group

When a button is pressed, standard button groups modify the width and shape of that button and adjacent buttons.

[image: 5 states of a standard button group.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

When a toggle button is selected in a standard button group, its shape should change between square and round. The color should change according to the button specs.

[image: 5 states of a standard button group with toggle buttons.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

### Connected button group

Connected button groups have different shape changes than standard button groups. Selecting a button does not affect adjacent buttons.

[image: 5 states of a segmented button group.]

Connected button group unselected states:

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

[image: 4 states of a segmented button group with toggle buttons.]

Connected button group selected states:

- Enabled

- Hovered

- Focused

- Pressed

## Measurements

### Standard button group

Standard groups apply padding between all buttons. The amount of padding changes based on button size to ensure a minimum accessible target size of 48dp. More details on padding: Button specs, icon button specs

[image: Standard button group padding measurements.]

Standard button group inner padding:

- XS: 18dp

- S: 12dp

- M: 8dp

- L: 8dp

- XL: 8dp

### Connected button group

For all connected button groups, use 2dp padding. This provides visual consistency at scale.

[image: Connected button group padding and corner radius measurements.]

Round connected button group inner padding is 2dp at every size. The outer shape is fully round, and the inner shape remains square with the following corner sizes:

- XS: 4dp

- S: 8dp

- M: 8dp

- L: 16dp

- XL: 20dp

[image: Connected button group padding and corner radius measurements for square buttons.]

Square connected button group inner padding is 2dp at every size. The outer shape has the following corner sizes:

- XS: 4dp

- S: 8dp

- M: 8dp

- L: 16dp

- XL: 20dp

### Minimum widths

Extra small and small connected button groups have 48dp target areas and a minimum width of 48dp.

[image: 48x48dp accessible target areas on the XS and S connected button groups.]

- Extra small

- Small

## Density

Button groups adapt to density of the buttons inside. More on density

[image: Connected button groups at 0, -1, -2, and -3 density.]

Button groups adapt to the height of the buttons inside, including when density is applied
