<!-- source: https://m3.material.io/components/carousel/specs -->
# Carousel – Material Design 3

# Carousel

[image: 4 elements of a carousel.]

- Container

- Large carousel item

- Medium carousel item

- Small carousel item

## Tokens & specs

Browse the component elements, attributes, tokens, and their values.

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 2 color roles of a carousel.]

Carousel color roles used for light and dark schemes:

- Container

- Surface

## States

States are visual representations used to communicate the status of a component or interactive element. Learn more about interaction states

[image: 5 states of a carousel in light and dark schemes.]

[image: 5 states of a carousel in light and dark schemes.]

- Enabled

- Hovered

- Focused

- Pressed

- Disabled

## Carousel item dynamic widths

All kinds of carousel items dynamically adapt to the width of the container.

Large items have a customizable maximum width that's used to optimally fit carousel items into the available space.

Small carousel items have a minimum width of 40dp and a maximum width of 56dp.

Items change size as they move through the carousel layout.

[image: Measurements for a small carousel item.]

[image: Measurements for a small carousel item.]

Small carousel items have a minimum and maximum width

## Multi-browse

The multi-browse layout shows at least one large, medium, and small carousel item.

[image: 4 elements of a multi-browse carousel layout.]

- Container

- Large carousel item

- Medium carousel item

- Small carousel item

### Measurements

[image: Measurements of a multi-browse carousel layout.]

Multi-browse carousels have padding on both sides of the container

| Attribute | Value |

|---|---|

| Alignment | Vertically centered |

| Leading/trailing padding | 16dp |

| Top/bottom padding | 8dp |

| Padding between elements | 8dp |

| Large item width | Dynamic, or user-set |

| Medium item width | Dynamic |

| Small item width | 40–56dp, dynamic |

| Item corner radius | 28dp |

## Uncontained

The uncontained layout shows items that scroll to the edge of the container.

[image: 4 elements of an uncontained carousel layout.]

- Container

- Large carousel item

### Measurements

[image: Measurements of an uncontained carousel layout.]

Uncontained carousel items bleed over the padding on each side when scrolling

| Attribute | Value |

|---|---|

| Alignment | Vertically centered |

| Leading padding | 16dp |

| Top/bottom padding | 8dp |

| Padding between elements | 8dp |

| Item corner radius | 28dp |

## Uncontained mutli-aspect ratio

The uncontained multi-aspect ratio layout shows carousel items of various widths.

[image: 4 elements of an uncontained carousel layout]

- Container

- Carousel item (16:9)

- Carousel item (9:16)

- Carousel item (1:1)

- Carousel item (3:4)

### Measurements

Uncontained multi-aspect ratio carousels only have leading padding, with 8dp of padding between items.

| Attribute | Value |

|---|---|

| Alignment | Vertically centered |

| Leading padding | 16dp |

| Top/bottom padding | 8dp |

| Padding between elements | 8dp |

| Item corner radius | 28dp |

## Hero

The hero layout shows at least one large item and one small item.

[image: 3 elements of a hero carousel layout.]

- Container

- Large carousel item

- Small carousel item

### Measurements

[image: Measurements of a hero carousel layout.]

Hero carousels have padding on both sides of the container

| Attribute | Value |

|---|---|

| Alignment | Vertically centered |

| Leading/Trailing padding | 16dp |

| Top/bottom padding | 8dp |

| Padding between elements | 8dp |

| Large item width | Dynamic |

| Small item width | 40-56dp, dynamic |

| Item corner radius | 28dp |

## Center-aligned hero

The center-aligned hero layout shows at least one large item and two small items.

[image: 3 elements of a center-aligned hero carousel layout.]

- Container

- Large carousel item

- Small carousel item

### Measurements

[image: Measurements of a center-aligned hero carousel layout.]

Center-aligned hero carousels have padding on both sides of the container

| Attribute | Value |

|---|---|

| Alignment | Vertically centered |

| Leading/Trailing padding | 16dp |

| Top/bottom padding | 8dp |

| Padding between elements | 8dp |

| Large item width | Dynamic |

| Small item width | 40-56dp, dynamic |

| Item corner radius | 28dp |

## Full-screen

The full-screen layout shows one edge-to-edge large item.

[image: 2 elements of a full-screen carousel layout.]

- Container

- Large carousel item

### Measurements

[image: Measurements of a full-screen carousel layout.]

Full-screen carousels fill the window edge-to-edge

| Attribute | Value |

|---|---|

| Alignment | Centered |

| Leading/Trailing padding | 0dp |

| Top/bottom padding | 0dp |

| Padding between elements | 16dp |
