<!-- source: https://m3.material.io/components/navigation-rail/accessibility -->
# Navigation rail – Material Design 3

# Navigation rail

## Use cases

People should be able to do the following using the assistive technology:

- Navigate between navigation destinations

- Select a particular navigation destination from a set

- Get appropriate feedback based on input type

## Interaction & style

When a navigation item is tapped, the active indicator appears, providing the following feedback to the user that it is selected:

- A ripple passes through the indicator

- The icon switches from outlined to filled

- The icon and text change color

When hovered, the hover state appears, providing a visual cue that the destination is interactive.

[image: Colorful, purple navigation rail shown collapsed and expanded.]

Touch: Tap

[image: Tap indicator on a collapsed nav rail.]

Cursor: Hover, Click

The target area for expanded navigation rails spans the full width of the container, even though the active indicator visually hugs the content.

[image: Touch indicator on a nav rail.]

Touch: Tap

Use a filled icon for the active destination and outlined icons for inactive destinations. Active and inactive icon colors need sufficient contrast against the container.

[image: Navigation rail with filled element.]

Use the default color scheme to ensure proper contrast and emphasis on the active destination

[image: Nav rail with multiple navigation destinations and multi-colored contrast.]

Don’t use more than two colors for destinations or low-contrast colors in the navigation rail. This will make distinguishing active items difficult.

If an icon doesn’t have a filled style, use the semibold icon weight instead.

[image: Icon button with semibold weight, without filled options.]

An icon with no filled option should use the semibold weight when active

### Text scaling and truncation

When someone sets their device to show a larger text size, the navigation rail items should grow vertically to accommodate larger labels while retaining the default padding. It’s okay for scaled text to wrap in navigation items.

To remain accessible, ensure the full label is always visible on-screen at up to 2x text sizing. Beyond this size, text can truncate.

[image: Nav rail with text scaled to 1.5x size. All labels are on one line.]

Text scaled to 1.5 size

[image: Nav rail with text scaled to 2x size. Some labels wrap to two lines.]

Text scaled to 2x size

### Initial focus

Initial focus lands directly on the first interactive item, whether it’s the menu, the FAB, or the first navigation item. From the FAB or menu, Tab brings the person to the navigation items. Tab or Arrows then navigate between items.

[image: Arrows help people move between pages.]

Use arrows to move between navigation items

[image: Space/enter help people choose a navigation destination.]

Use space/enter to activate the focused navigation item

### Visual indicators

Icons give the dominant cue of the navigation state. Use a filled icon for the selected destination to contrast with outlined icons for the non-selected destinations.

[image: Nav bar with an active, filled icon button.]

Use a filled icon variant on the selected navigation item to differentiate from inactive navigation items

[image: Selected navigation item without filled icon style.]

Avoid using the same unfilled icon style for both selected and unselected items because it lacks important visual feedback cue

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab / Arrows | Navigate between interactive elements |

| Space / Enter | Selects an interactive element |

## Labeling elements

The accessibility label for a navigation item is typically the same as the adjacent text label. When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a navigation item visibly labeled Recent would benefit from additional information in its accessibility label to clarify the destination's intent. Note: On Android Views (MDC-Android), a more descriptive accessibility label is not available and the role is not announced.

[image: “Maps” is both the icon label text and the accessibility label.]

While the visible label text reads Recent, the accessibility label for this switch clarifies its function: Recent images
