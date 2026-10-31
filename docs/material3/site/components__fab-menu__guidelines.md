<!-- source: https://m3.material.io/components/fab-menu/guidelines -->
# FAB menu - Material Design 3

# FAB menu

[image: On a page of music albums, a FAB menu shows options to make a new playlist, collection, or station.]

Use the FAB menu to show multiple related actions in a prominent, expressive style

## Usage

A FAB menu opens from a FAB to show multiple related actions. It should always appear in the same place as the FAB that opened it.

This makes actions immediately accessible, and keeps the UI clean by concealing actions when they’re not needed.

Don’t open a FAB menu from an extended FAB or any other component.

[image: 1 mobile screen with a FAB, 1 with a FAB menu. Both are right aligned.]

The FAB menu should always open from a FAB

The FAB menu should be aligned to the trailing edge of the window.

In right-to-left (RTL) languages, this means the FAB and FAB menu should be aligned to the left edge, and the layout of elements should be mirrored.

[image: 1 mobile screen with a FAB, 1 with a FAB menu. Both are left aligned and mirrored for a right-to-left language.]

In RTL languages, the FAB menu should be left-aligned with the icon and text placement mirrored

FAB menus can contain 2–6 items. These should be closely related under a single action, like Share.

Avoid grouping unrelated actions in the same FAB menu.

[image: A FAB menu with 5 options on a photo gallery UI.]

FAB menus can have 2-6 items

[image: A FAB menu with 1 option on a photo gallery UI.]

Don’t use a FAB menu with one item

When a FAB is paired with other components, like the floating toolbar or navigation rail, don’t use the FAB menu. This prevents cognitive overload and interface clutter.

[image: A toolbar with a FAB directly next to it.]

FABs can be placed next to toolbars and other components

[image: A toolbar with a FAB menu next to it.]

Don't use a FAB menu with a toolbar or navigation rail

### Color sets

FAB menus have three color sets: primary, secondary, and tertiary. Use the color set that best matches the FAB color style.

Use the primary FAB menu color set with the primary or primary container FAB color styles.

[image: A FAB menu using the primary color set. ]

A primary FAB is paired with a primary FAB menu

Use the secondary FAB menu color set with the secondary or secondary container FAB color styles.

[image: A FAB menu using the secondary color set.]

A secondary FAB is paired with a secondary FAB menu

Use the tertiary FAB menu color set with the tertiary or tertiary container FAB color styles.

[image: A FAB menu using the tertiary color set.]

A tertiary FAB is paired with a tertiary FAB menu

## Anatomy

[image: 2 elements of a FAB menu.]

- Close button

- List item

FAB menu items should always have label text. The icons shouldn’t be removed since they make each item easy to identify.

[image: A FAB menu with 3 options for selecting Food, People, or Nature. There are no icons next to the text.]

Only remove the icon if necessary. The icon provides a differentiation between items.

[image: A FAB menu with 3 options for selecting Food, People, or Nature. The options are only icons, no text.]

Don’t remove the label

The list item should always hug its contents and look consistent. Avoid truncating text or setting fixed widths. All FAB menu elements should be rounded.

[image: A FAB menu used out of the box with no configurations.]

Keep the padding between the container and icon, icon and text, and text and container consistent

[image: FAB menu items are equal width despite having different lengths of text.]

Don’t expand container sizes

[image: FAB menu items are square instead of round.]

Don’t change FAB menu shapes

## Adaptive layout

The FAB menu can open from any sized FAB. Use with a FAB size suitable for the window size class. For example, larger FABs are recommended for larger windows.

The FAB menu works in any window size. Pair it with the FAB suitable for that window size.

The FAB menu should remain anchored to the same corner or edge regardless of window size.

In large and extra large windows, the FAB and FAB menu margins should increase from 16dp to 24dp.

[image: A FAB menu with 24dp margins from the edge of the window.]

On desktop, use larger FABs and margins

On web, the FAB menu uses a menu component for an experience that's consistent with other desktop apps.

[image: A FAB menu using menu component on web and traditional FAB menu on compact screen.]

The same FAB menu options on both large window (left) and an Android compact window (right)

## Behavior

### Appearing

The FAB should transform into the close button of the FAB menu. The menu items should appear using the enter and exit transition.

Originate the transition from one of the FAB's trailing corners, preferably the top-aligned corner.

Animate FAB menus from the top-aligned corner of FABs

To ensure accessibility for keyboard users on the web, avoid positioning the FAB menu to completely obscure the focus indicator of an actionable element. Partially covering the desired element is fine, as long as the focus indicator is visible.

[image: FAB menu doesn’t obscure actionable element and its focus indicator.]

Ensure the actionable element and its focus indicator are visible behind the FAB menu

[image: FAB menu obscures both an actionable element and its focus indicator.]

Don’t block an actionable element and its focus indicator completely with the FAB menu

### Scrolling

When window height is limited, like when viewing phones in horizontal orientation, FAB menu items can scroll.

The items should scroll behind the close button.

FAB menus can scroll if the window height is too short to contain all the options

### Expanding

Any FAB menu item can expand and adapt to any shape using a container transform transition pattern. This includes a surface that is part of the app structure, or a surface that spans the entire screen.

FAB menu items can transition into any kind of shape when selected
