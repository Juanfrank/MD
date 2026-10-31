<!-- source: https://m3.material.io/foundations/layout/breakpoints/large-extra-large -->
# Breakpoints – Material Design 3

# Breakpoints

These breakpoints are most useful for creating web experiences tailored to laptop and desktop devices. Some products may not need large and extra-large breakpoints. Consider your platform’s conventions and users when making decisions on which breakpoints to design for.

- Layouts for large breakpoints are for screen widths from 1200dp to 1599dp

- Layouts for extra-large breakpoints are for screen widths of 1600dp and larger

[image: Large window with a video app in 2 pane layout.]

A two-pane layout is recommended for large and extra-large breakpoints

## Navigation

Use a navigation rail, either collapsed or expanded, depending on the amount of content.

For sorting, filtering, or secondary navigation, use tabs or other components directly in the pane.

[image: Large web browser with a small navigation area on the leading edge with 1 pane filling the rest of the window.]

- Collapsed navigation area

- Single-pane layout

An expanded navigation rail is best suited for extra-large windows, where there's still plenty of room for content. Consider collapsing the navigation rail when space is needed, or when on pages deeper in the page hierarchy.

[image: Extra-large web browser with an expanded navigation area and 1 pane filling the rest of the window.]

- Expanded navigation area

- Single-pane layout

## Panes

A two-pane layout is often best for large and extra-large breakpoints.

However, a single-pane layout can work when displaying visually- or information-dense content, such as videos.

[image: The single pane covers most of a large screen except for the navigation area and margins.]

Only use a single-pane layout for dense content or media

When using a fixed-and-flexible layout, the fixed pane should have a width of 412dp by default.

[image: A 2-pane layout with 1 pane fixed at 412dp.]

Fixed panes should be 412dp in large and extra-large layouts

When using a split-pane layout, the spacer should be visually centered by default, even when using an expanded navigation rail.

[image: An expanded nav rail and the first pane take up 50% of the window, and the second pane takes up 50%. ]

In split-pane layouts, navigation components shrink the leading pane, so the spacer remains centered

## Additional panes

The extra-large breakpoint supports using a standard side sheet as a third pane. When the side sheet is present, the navigation rail can remain visible, collapse, or hide completely. Don't use more than three panes.

Note: Fixed panes in this window size are recommended to be 412dp, but side sheets have a default maximum width of 400dp.

[image: Extra-large window with 2 panes and a side sheet acting as a third pane.]

- Standard side sheet (third pane)

## Spacing

Large and extra-large layouts have a leading and trailing margin of 24dp.

The spacer between panes is 24dp.

[image: 2 pane layout with 24dp margins and 24dp space between panes.]

Use 24dp for margins and spacers in large and extra-large layouts

## Special considerations

Large and extra-large layouts will need to transition dynamically to a smaller layout when:

- The app goes from full-screen to split-screen

- Multi-window mode is initiated

- A free-form window is resized

Pay attention to typographic elements such as line length to ensure readability on large and extra-large layouts.

[image: An email app with 2 panes in a large layout.]

Consider how a large layout should change at smaller breakpoints
