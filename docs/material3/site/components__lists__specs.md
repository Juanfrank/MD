<!-- source: https://m3.material.io/components/lists/specs -->
# Lists – Material Design 3

# Lists

## Variants

### Expressive lists

Use the expressive list variant for more flexible styling, highlighted selection states, and customizable slots.

[image: 2 expressive lists: a photos list on a tablet, and a song list on mobile.]

An expressive list has a segmented style and round corners

### Baseline lists

Baseline lists are still available to use, but don’t have the latest visual style, selection treatment, and slot functionality. On web, expressive lists are built on top of baseline lists.

See baseline list specs

[image: 3 baseline list items with square corners.]

Baseline list items have square corners and standard colors

| Variants | M3 | M3 Expressive |

|---|---|---|

| Lists (expressive) | -- | Available |

| Lists (baseline) | Available | Not recommended. Use expressive lists instead. |

## Configurations

### Styles

The standard and segmented styles are a visual choice, and don’t affect a list’s behavior.

[image: A standard list and segmented list in dark mode.]

[image: A standard list and segmented list in dark mode.]

- Standard

- Segmented

### List selection

A list can have only one selection mode at a time. For example, a single-action list can change to a multi-select list, but can’t be both at once.

[image: A single-action list with 4 items and no additional actions.]

In a single-action list, each item is a single tappable area

[image: A list with 4 items. Each item has 2 trailing icons for additional actions.]

Multi-action list items include a primary action, and one or more secondary actions

[image: A list with 1 item selected.]

A single-select list

[image: A list with 2 items selected.]

A multi-select list

### List interactions

Lists can:

- Expand and collapse

- Swipe to reveal*

More on list interaction accessibility

A list can expand to include multiple items

[image: A list item is swiped, and reveals 3 more actions.]

A list item can be swiped to reveal more actions

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Styles | Standard | Available | Available |

| Segmented | -- | Available |

| Selection modes | Single-action, multi-action, single-select, multi-select | Available | Available |

| Interactions | Expand, swipe* | Available | Available |

* Swipe-to-reveal interactions are only available on Android Views

## Tokens & specs

Use the table's menu to select a token set. The common set combines baseline tokens with new expressive shapes and sizes. The expand set has tokens for the expand interaction. Learn about design tokens

## Anatomy

[image: Diagram with 10 elements that can be included in lists.]

Container and label text are required. All other elements are optional:

- Container

- Overline

- Label text

- Trailing text

- Supporting text

- Trailing icon

- Divider

- Leading avatar

- Leading icon

- Leading media - image or video

### Flexibility & slots

The M3 Design Kit includes lists with custom slots for designing flexible item layouts. Think of a custom list as a container with three different slots: leading, content, and trailing. Each slot can hold a different element.

#### Slot accessibility

Slots are not accessible by default. Consider the following:

- Elements must follow the rules, structure, and interaction patterns for lists

- Use standard list item padding

- Target size must be at least 48x48dp

- Don't add interactive elements that make the list item difficult to navigate, especially for people using screen readers

More on required accessibility guidelines

[image: A diagram with leading, content, and trailing slots.]

Reserve the use of slots for use cases that maintain the list’s accessibility and functionality

- Leading slot

- Content slot

- Trailing slot

The leading and trailing slot positions must be a smaller width than the content section.

1. Leading slots can contain:

- Visual elements: Avatar, icon, image, or video thumbnail

- Selection controls: Checkbox, radio button, or switch

- Customizations: Badge or larger image

2. Content slots must be the largest-width slot and can contain:

- Default content: Label text, supporting text

- Optional add-ons: Badge, icon, in-line label, or more text elements

- Avoid long lines of text to preserve readability

3. Trailing slots can contain:

- Action elements or text: Icon, icon button, or trailing text

- Selection controls: Checkbox, radio button, or switch

[image: Slot diagram showing slot placement in the middle of the list.]

The content slot must be the largest section, placed in the middle of the list item

#### Selection lists

For selection lists, use only one selection interaction per list item.

[image: A selected list item with a checkmark in the leading slot.]

Use only one selection interaction per list item

[image: A selected list item with both a checkmark in the leading slot and a bookmark in the trailing slot.]

Don't use multiple selection interactions in one item

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 10 list element color roles in light mode and dark mode.]

List color roles used for light and dark themes:

- Surface

- On surface variant

- On surface

- On surface variant

- On surface variant

- On surface variant

- Outline variant

- Primary container

- On primary container

- On surface variant

## States

States are visual representations used to communicate the status of a component or an interactive element. Learn more about interaction states More on list focus

### Default list items

[image: 6 default list states in light and dark mode.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

- Dragged

### Selected list items

[image: 6 selected list states in light and dark mode.]

- Enabled

- Disabled

- Hovered

- Focused

- Pressed

- Dragged

## Measurements

[image: Size and padding measurements for list items.]

List item alignment, padding, and size measurements. The icon button height is dynamic, and automatically adjusts to fill the list item height.

### Shape morphing

When a list item is selected, the corner shape changes to highlight the active item:

- Unselected corner radius: 4dp inner, 16dp outer

- Selected corner radius: 16dp

[image: A 3-item list. The middle item is unselected, with a 4dp corner radius.]

Unselected list items have a 4dp inner corner radius, and 16dp outer corner radius

[image: A 3-item list. The middle item is selected, with a 16dp corner radius.]

Selected list items have a 16dp corner radius all around

## List (baseline)

The baseline list variant is available and continues to work in existing products. However, the expressive list variant is recommended for new designs.

### Tokens & specs

Baseline list tokens are in the common token set. Note: This set also includes several expressive tokens.

### Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 9 baseline list element color roles in light and dark mode.]

List color roles used for light and dark themes:

- Surface

- On surface

- On surface variant

- On surface variant

- On surface variant

- Outline variant

- Primary container

- On primary container

- On surface variant

### States

States are visual representations used to communicate the status of a component or interactive element.

[image: 6 baseline list states in light and dark mode.]

1. Enabled

2. Disabled

3. Hovered

4. Focused

5. Pressed

6. Dragged

### Layout

#### One-line lists

[image: Alignment, padding, and size specifications for baseline list items with 1 line of text.]

Baseline one-line list alignment, padding, and size measurements

[image: Measurements for a 3-item list with 1 line each.]

Baseline list item measurements and padding

#### Two-line lists

[image: Alignment, padding, and size specifications for baseline list items with 2 lines of text.]

Baseline two-line list alignment, padding, and size measurements

[image: Measurements for a 3-item list with 2 lines each.]

Baseline list item measurements and padding

#### Three-line lists

[image: Alignment, padding, and size specifications for baseline list items with 3 lines of text.]

Baseline three-line list alignment, padding, and size measurements

[image: Measurements for a 3-item list with 3 lines each.]

Baseline list item measurements and padding

| Attribute | Value |

|---|---|

| Label alignment | Center |

| Label alignment when height is 88dp or taller | Top |

| Label left padding | 16dp |

| Leading element alignment (vertical) | Center |

| Leading element alignment (vertical) when height is 88dp or taller | Top |

| Leading element left padding | 16dp |

| Leading icon alignment (vertical) | Top |

| Leading icon top padding | 8dp |

| Leading icon top padding when height is 88dp or taller | 12dp |

| Trailing element alignment (vertical) | Center |

| Trailing element alignment (vertical) when height is 88dp or taller | Top |

| Trailing element left padding | 16dp |

| Trailing element right padding | 24dp |

| Padding above/below divider | 0dp |

| Targets | 48dp |

| Divider full-width | 100% |

| Divider inset left padding | 16dp |

| Divider inset right padding | 24dp |

### Configurations

#### Leading avatar

[image: 1, 2, and 3-line list items with and without a leading avatar and trailing checkbox, in dark mode.]

- With leading avatar

- With leading avatar and trailing checkbox

#### Leading image or thumbnail

[image: 1, 2, and 3-line list items with and without a leading image and trailing checkbox, in dark mode.]

- With leading image

- With leading image and trailing checkbox

#### Leading video

[image: 1, 2, and 3-line list items with and without a leading video and trailing checkbox, in dark mode.]

- With leading video

- With leading video and trailing checkbox

#### Leading icon

[image: 1, 2, and 3-line list items with and without a leading icon and trailing checkbox, in dark mode.]

- With leading icon

- With leading icon and trailing checkbox

#### Text-only

[image: 1, 2, and 3-line text only list items with and without a trailing checkbox, in dark mode.]

- With text only

- With text and trailing checkbox

#### Leading checkbox

[image: 1, 2, and 3-line list items with and without a leading checkbox and trailing text, in dark mode.]

- With leading checkbox

- With leading checkbox and trailing text

#### Leading radio button

[image: 1, 2, and 3-line list items with and without a leading radio button and trailing text, in dark mode.]

- With leading radio button

- With leading radio button and trailing text

#### Trailing switch

[image: 1, 2, and 3-line list items with and without a leading icon and trailing switch, in dark mode.]

- With trailing switch

- With leading icon and trailing switch
