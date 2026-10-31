<!-- source: https://m3.material.io/foundations/layout/breakpoints/medium -->
# Breakpoints – Material Design 3

# Breakpoints

Layouts for medium breakpoints are for screen widths from 600dp to 839dp.

[image: A medium breakpoint with a video call app in full-screen mode.]

Single-pane layouts can focus attention on one action or view, such as a video call

## Navigation

Place navigation components close to edges of the window where they’re easier to reach:

- Single-pane layouts: Navigation rail

- Two-pane layouts: Navigation bar

The navigation rail can be hidden in secondary destinations as long as the primary destination can still be accessed using a back button.

[image: The navigation area of a medium breakpoint is a vertical bar at the leading edge, beside a single pane.]

- Navigation area

- Single pane

## Panes

### Single-pane layout

In a medium layout, a single pane is recommended because of limited screen width.

[image: A single pane uses most of the space in a medium window.]

- A single-pane layout is recommended for medium breakpoints

### Two-pane layout

Limit use of two panes for content with lower information density, such as a settings screen.

Each pane in a two-pane layout should take up 50% of the window width. Avoid setting custom widths. A drag handle can be used to expand or collapse panes to be 100% of the window width.

[image: 2-pane layout in a medium window. Both panes fit 50% of the window width by default.]

Two-pane layouts should use 50% widths for each pane by default

When adding navigation to a two-pane layout, use a navigation bar. This allows the panes to fully use the available window width.

[image: A navigation bar extends over 2 panes at the bottom of a medium window.]

Two-pane layout with:

- Navigation bar

## Spacing

Medium layouts have margins of 24dp.

The spacer between panes is also 24dp.

[image: 2 pane layout with 24dp margins and 24dp space between panes.]

Use 24dp for margins and spacer in a medium layout

## Special considerations

A medium layout will need to transition dynamically to a compact or expanded layout when:

- A foldable device is folded

- A tablet is rotated from portrait to landscape

- A product goes from full-screen to split-screen

- Multi-window mode is initiated

- A free-form window is resized

[image: Email app with 2 panes at  a medium breakpoint.]

Think of how a medium layout should change to a compact or expanded layout

### Reachability

For horizontal tablets and unfolded foldables, the top 25% of the screen is likely out of reach, unless the grip is adjusted. To accommodate device and hand sizes, limit the amount of interactions that are placed in the upper 25% of the screen.

[image: The hard-to-reach top quarter of a medium breakpoint in landscape mode.]

- Limit interactions in the upper quarter of a screen, as they can be hard to reach

Avoid placing essential interactive elements too close to the bottom edge of the screen. Some users, particularly those with larger hands, might struggle to reach this area.

Specify interactions in a layout with these ergonomic regions in mind:

- Users can reach this area by extending their fingers, which makes it inconvenient

- Users can reach this area comfortably

- Reaching this area is challenging when holding the device

[image: The 3 ergonomic regions of a medium breakpoint.]

Medium breakpoint ergonomic regions:

- Inconvenient

- Comfortable

- Challenging
