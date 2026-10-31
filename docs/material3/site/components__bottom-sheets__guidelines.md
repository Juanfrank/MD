<!-- source: https://m3.material.io/components/bottom-sheets/guidelines -->
# Bottom sheets – Material Design 3

# Bottom sheets

[image: Two variants of bottom sheets.]

- Standard bottom sheets

- Modal bottom sheets

## Usage

Bottom sheets display supplementary content and actions on a mobile screen.

[image: Photo sharing bottom sheet with contact list, app icons, and action buttons.]

Bottom sheet containing contacts and applications

Bottom sheets are a versatile component that can contain a wide variety of information and layouts, including menu items (in list or grid layouts), actions, and supplemental content.

[image: Bottom sheet displaying 3 menu options.]

Bottom sheet with menu items in a list

## Anatomy

A container is the only required element of a bottom sheet. Bottom sheet layouts can vary widely to support the kinds of content they contain.

[image: 3 elements of a bottom sheet.]

- Container

- Drag handle (optional)

- Scrim (modal only)

### Container

Bottom sheet containers hold all bottom sheet elements. Their size is determined by the space those elements occupy.

The container is the only required element of a bottom sheet. All other elements are optional.

[image: Empty bottom sheet container.]

Bottom sheets are flexible containers that adapt to their content and available space

### List items (optional)

Lists are a continuous group of text or images. List items can include label text, icons, and text buttons, among other elements.

[image: A bottom sheet displaying a list of actions for a song.]

Bottom sheet containing a list with icons

### Dividers (optional)

Dividers can be used to separate related content in bottom sheets.

[image: Bottom sheet with image action buttons and contact list separated by an inset divider.
]

Bottom sheet with a divider separating kinds of actions

### Media (optional)

Thumbnail Bottom sheets can include thumbnails for an avatar or logo.

Image Bottom sheets can include photos, illustrations, and other graphics, such as weather icons.

Video Bottom sheets can include video.

[image: A bottom sheet displaying various media formats, including thumbnails, images, and video.]

Bottom sheets can contain thumbnails, images, and video

## Standard bottom sheets

Standard bottom sheets co-exist with the screen’s main UI region and allow for simultaneously viewing and interacting with both regions, especially when the main UI region is frequently scrolled or panned.

Use a standard bottom sheet to display content that complements the screen’s primary content, such as an audio player in a music app.

[image: Bottom sheet with music player controls visible while browsing albums.]

The music player in this standard bottom sheet allows people to control their music while browsing albums

At full-screen height, standard bottom sheets contain a collapse icon in an app bar to return to their initial position.

Standard bottom sheets can contain supplementary content that continues below the screen, such as location information over a map.

A bottom sheet can have preset positions from full-screen height to preview

## Modal bottom sheets

Like dialogs, modal bottom sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken.

[image: A modal sheet with filter options to categorize files in the app. ]

A modal bottom sheet must be interacted with or dismissed. Its blocking behavior makes it suitable for a menu, such as in this files app, to help people focus on their available choices.

Use a modal bottom sheet as an alternative to inline menus or simple dialogs on mobile, especially when offering a long list of action items, or when items require longer descriptions and icons.

Modal bottom sheets are used in mobile apps only.

[image: A modal bottom sheet displayed as an alternative to a traditional menu, presenting a list of actions.]

Modal bottom sheets can be used instead of menus to present additional actions

### Visibility

To provide access to its top actions, the initial vertical position of modal bottom sheets is capped at 50% of the screen height.

Modal bottom sheets whose contents exceed 50% of the screen height can then be pulled across the full screen and scrolled internally to access their remaining items.

[image: A modal bottom sheet covering half of the screen, so both images and actions are accessible.]

The initial vertical position of modal bottom sheets can't exceed 50% of the screen height

Modal bottom sheets appear when triggered by a user action, such as tapping a button or an overflow icon. They can be dismissed by:

- Tapping a menu item or action within the bottom sheet

- Tapping the scrim

- Swiping the sheet down

- Using a close affordance within the bottom sheet’s app bar, if available

Display a close affordance in a full-screen modal bottom sheet.

[image: A modal bottom sheet disappearing by tapping the scrim.]

Tapping the scrim dismisses a modal bottom sheet

[image: A modal bottom sheet disappearing by swiping the sheet down.]

A modal bottom sheet can be dismissed by swiping the sheet down

## Responsive layout

### Compact breakpoint

In compact breakpoints, like mobile devices, bottom sheets extend across the width of a screen and are elevated above the primary content.

[image: A bottom sheet extended to the width of a mobile screen.]

Bottom sheets should extend to the width of the screen on mobile

### Medium and expanded breakpoints

For larger screens with medium and expanded breakpoints, bottom sheets have a default max-width to prevent undesired layouts and awkward spacing. However, this can be overridden if needed. For more complex tasks and flows, consider using a non-transient surface such as a floating sheet.

[image: A bottom sheet extended to its max-width on a large screen device, not spanning the full screen.]

Bottom sheets on larger screens like tablet have a max width that can be overridden

On larger expanded breakpoints, like desktop, a bottom sheet can be swapped for a side sheet that shows similar content.

[image: A side sheet on desktop.]

Side sheets can contain the same content as bottom sheets and may be more suitable for desktop

## Behavior

Bottom sheets can offer an expansion option where the sheet is fully raised and toggled between a collapsed and expanded state. This provides a more predictable footprint of the sheet, and can be set by the system or toggled by the user.

[image: Bottom sheet fully raised, showing photo actions, sharing options, and albums to add the photo to.]

A bottom sheet for sharing can appear fully raised if needed

[image: Collapsed bottom sheet, showing focused set of options.]

Alternately, a bottom sheet for sharing can appear collapsed for a more focused set of actions

### Custom positioning

The drag handle can be dragged or selected to change the bottom sheet height. Sheets should be able to cycle through preset heights and close completely without dragging. Selecting the drag handle should toggle through preset heights or close the sheet, while selecting the scrim should always close the bottom sheet. If the bottom sheet has multiple preset heights but can’t use a drag handle, Material requires the inclusion of a single-pointer alternative to change height.

[image: Bottom sheet with a visible drag handle that can be used to adjust its height.]

Interacting with the drag handle can quickly move a bottom sheet through preset heights

[image: Bottom sheet resized using the visible drag handle.]

A bottom sheet can automatically resize to another height after interacting with the drag handle

### Scrolling

Bottom sheets can be horizontally scrolled, independent of the rest of the screen’s content.

[image: Bottom sheet that can be scrolled horizontally.]

Bottom sheets should be scrollable when their content exceeds the initial viewable height

### Back

On Android, a gesture called predictive back allows a user to swipe left or right on the bottom sheet.

- Bottom sheet detaches from the left and right edges of the screen to signal it will close

- Previous screen is revealed in a preview

A list of compatible components is available in the gestures article.

Preview of the result of the gesture, release to commit, fling to commit, and cancel
