<!-- source: https://m3.material.io/components/segmented-buttons/guidelines -->
# Segmented button – Material Design 3

# Segmented buttons

[image: Two types of segmented buttons.]

- Single-select

- Multi-select

## Usage

Segmented buttons help people select options, switch views, or sort elements.

[image: A segmented button for switching between restaurants and bar options. ]

A segmented button can help switch between viewing restaurant and bar options

There are 2 variants of segmented buttons:

- Single-select

- Multi-select

[image: Side by side view of single and multi-select segmented buttons]

- Single-select segmented button can only have 1 segment selected

- Multi-select segmented button can have multiple segments selected

## Anatomy

[image: Diagram of segmented button indicating 5 parts of its anatomy]

- Segment

- Container

- Icon (optional)

- Label text (optional)

- Selected icon

### Segments

Segmented buttons can have 2-5 segments. Each segment is clearly divided and contains label text, an icon, or both.

[image: Side by side view of segmented buttons each with additional segment starting from 2 to 5]

There can be anywhere from 2 to 5 segments in single-select and multi-select segmented buttons

[image: Mobile UI of data usage screen with segmented button]

Segmented buttons are best used for selecting between 2 and 5 choices

[image: Incorrect use of segmented button with 6 segments]

Don’t use more than five segments in a single segmented button. Choices should be scoped. If you have more than five choices, consider using another component, such as chips.

### Container

Like common buttons, segmented buttons have fully rounded corners by default.

[image: Close up detail of segmented button with fully rounded corners]

Segmented buttons have fully rounded corners

### Icons

Icons may be used as labels by themselves or alongside text.

If an icon is used without label text, it must clearly communicate the option it represents.

[image: Side by side view of segmented buttons with different configurations of icons and label text]

Segmented buttons can include icons

### Label text

Labels should be short and succinct. If a label is too long to fit within its segment, consider using an icon alone.

[image: Mobile UI of music app showing a segmented button with options for music, albums, podcasts]

Use labels that are as clear and short as possible

[image: Segmented button with options for day, week, month]

Keep labels short and consistent in length

[image: Segmented button with 4 segments. 3 are next to each other. The 4th is wrapped on a new line.]

Don’t allow segments to wrap onto a new line

[image: Segmented button with text labels reading day, week, month]

Use consistent label types

[image: Segmented button with icons only labels for walking, transit, driving]

Icons can be used in place of labels, but they must clearly communicate their meaning

[image: Segmented button with 2 icon only options indicating favorite and bookmark and 3rd option with text label reading recent]

Avoid mixing icon-only labels with text labels. Choose one label type and use that type for all segments.

## Single-select

Use a single-select segmented button to select one option from a set, switch between views, or sort elements from up to five options.

For example, use a single-select segmented button to choose one of a set of sizes, such as this beverage size selector.

[image: Mobile UI for ecommerce app with segmented button with 3 beverage size options]

A single select segmented button for choosing beverage size

## Multi-select

Use a multi-select segmented button to select or sort from two to five options. Unlike single-select, selection is not required and a user may concurrently select anywhere from all to none of the options.

For example, multi-select segmented buttons can be used to filter by price range when searching for a restaurant.

[image: Mobile UI for ecommerce app with multi-select segmented button with 4 price range options ]

A multi-select segmented button for filtering restaurant search options

## Placement

Segmented buttons should have adequate margins from the edge of the viewport or frame.

On larger screens, set a maximum padding for all button segments so the set doesn't fill the screen.

[image: Mobile UI with 2-segment segmented button and 4-segment segmented button each with same margins to the viewport edge.]

Allow adequate space for margins. The button container shouldn’t reach the edge of the viewport.

[image: Game store UI with a segmented button the proper width]

Set a maximum padding within the segments to ensure usability on larger screens

[image: Game store UI with a segmented button improperly spanning the entire width of the screen]

Don’t allow segmented buttons to span the full width of larger screens or panes. This can leave too much padding on either side of the segment label, making the button less usable.

Segmented buttons can be placed on other components, such as bottom sheets or full-screen dialogs.

[image: Mobile UI with segmented button in bottom sheet]

A segmented button can be placed on a bottom sheet

## Behavior

When using both icons and label text in segmented buttons, the icon label is replaced by the checkmark icon when the segment is selected.

Icons become checkmarks when selected in buttons that also use label text
