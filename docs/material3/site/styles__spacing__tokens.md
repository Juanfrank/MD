<!-- source: https://m3.material.io/styles/spacing/tokens -->
# Spacing - Material Design 3

# Spacing

## System spacing tokens

System spacing tokens are a linear range of spacing values recommended by Material. They’re intended to cover the majority of spacing needs within the design system. The base unit of measurement md.sys.measurement.space100 is 8dp. Learn more about design tokens

[image: The spacing system tokens, built from 8dp (1x). The range covers 0x to 9x.]

The main spacing units are multiples of 8dp

### Nested units

Values other than multiples of 8 are also used in layouts and Material components, like 2dp, 4dp, 6dp, and 10dp. Material only defines the most recommended nested units.

[image: The spacing system defines tokens for 0.25x, 0.5x, 0.75x. 1.25x nested units.]

Material only defines nested units that are actively used in common layouts or Material components

## Component spacing

Most Material component spacing attributes will map to system spacing tokens. Spacing logic, like adaptive design or density, should be applied to the component attribute.

Component attributes follow a new naming strategy:

- Going forward, all component spacing attributes will use padding, margin, and gap, and positional language: horizontal, vertical, leading, trailing, top, and bottom Example: “Medium button: leading padding”

- Past component spacing tokens use “space” to describe all padding, gaps, and margins, like leading-space, trailing-space, top-space, bottom-space, and between-space. Example: “Medium button: leading space”
