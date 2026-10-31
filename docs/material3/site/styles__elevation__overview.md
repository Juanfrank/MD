<!-- source: https://m3.material.io/styles/elevation/overview -->
# Elevation – Material Design 3

# Elevation

- Elevation is applied to all surfaces and components

- Tokens codify the distance on the z-axis to ensure components appear consistently relative to each other

- Tokens have no shadows or color; each platform determines the specific shadows and values to use at each elevation level

- Elevation can be shown as tonal surface colors or shadows

- Avoid changing the default elevation of Material 3 components

- Stick to using a small amount of elevation levels

Elevation is measured as the distance between components along the z-axis in density-independent pixels (dps).

[image: 1 diagram shows a light purple square and a darker purple square. A second one shows a side view of the squares in elevation, showing that the light square is lower in elevation than the dark square.]

Elevation represents the distance between elements. The product applies color to represent elevation.

- One surface at 1dp elevation and another surface at 8dp elevation, as viewed from the front

- The difference in elevation between the two surfaces is 7dp, as viewed from the side

## Availability & resources

|  | Resource | Status |

|---|---|---|

| Design | Design Kit (Figma) | Available |

| Implementation | Flutter | Available |

|  | Jetpack Compose | Available |

|  | MDC - Android | Available |

|  | MWC - Web | Available |

## Differences from M2

- Shadows: Instead of applying shadows by default to all levels, use shadows only when required to create additional protection against a background or to encourage interaction

- Color: New color mappings and compatibility with dynamic color

- Levels: Elevation is now described in terms of levels

[image: Diagram of 2 concentric squares. The inner square is at 12dp and has a larger shadow than the outer square, which is at 3dp.]

M2: Shadows applied at all levels

[image: Diagram of 2 concentric squares without shadows. Instead, the inner square is at level and tonally darker than the outer square, which is at level 2.]

M3: Using color instead of shadows to communicate elevation

## All surfaces and components have elevation values

Surfaces at different elevations do the following:

- Allow surfaces to move in front of and behind other surfaces, such as content scrolling behind app bars

- Reflect spatial relationships, such as how a FAB's shadow indicates it's separate from a card collection

- Focus attention on the highest elevation, such as a dialog temporarily appearing in front of other surfaces

Elevation can be depicted using shadows or other visual cues, such as surface fills with a tone difference

### Resting elevation (default)

All components have a default resting elevation. Avoid changing the default elevation of Material components.

[image: A floating action button with a shadow.]

All components have a default elevation which should be used

### Changing elevation

Components should change elevation in response to system events or user interaction, like hovering. This elevation change should be consistent across all similar elements.

For example, hovering a FAB temporarily increases the elevation by 1 level, from level 3 to level 4. All Material buttons increase elevation by 1 level when hovered.

Hovering over a button increases its elevation to show user interaction
