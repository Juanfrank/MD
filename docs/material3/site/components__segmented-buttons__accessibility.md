<!-- source: https://m3.material.io/components/segmented-buttons/accessibility -->
# Segmented button – Material Design 3

# Segmented buttons

## Use cases

Users should be able to:

- Navigate to and activate segmented buttons with assistive tech

- Understand what each segment selection will do

### Interaction & style

For keyboard navigation, Tab navigates to the button, and arrow keys navigate between the individual segments.

For single-select segments, Space or Enter will select or unselect the focused segment.

For multi-select segments, Space or Enter will:

- Select an unselected segment

- Select all of the segments

- Unselect a selected segment

[image: Tab moves the focus through segments of a segmented button.  Space or enter selects and unselects segments.]

Use Tab to navigate through segments, and Space or Enter to select and unselect

### Color contrast

Segmented buttons are clusters of similar components, so the outline should have at least a 3:1 contrast ratio with the background or surface. This helps distinguish each button.

Both a checkmark icon and a color change are used to distinguish selection. Make sure color isn’t the only way to show selection.

[image: The outline of segmented buttons on the surface passes the minimum contrast of 3:1.]

Use an outline with a surface contrast of at least 3:1

[image: The outline of segmented buttons on the surface fails the minimum contrast of 3:1.]

The segmented button shouldn't have a contrast outline less than 3:1

### Initial focus

Focus will start in the first segment. Depending on the direction of the language, it is either the most left or the most right segment.

For single select and multi-select, the first segment will be focused regardless of selection state.

[image: Segmented button focus starts on the left for left-to-right languages and on the right for right-to-left languages.]

Focus begins on the left for left-to-right languages and on the right for right-to-left languages

### Keyboard navigation

| Keys | Actions |

|---|---|

| Tab | Navigate between buttons |

| Arrow keys | Navigate inside the component |

| Space or Enter | Activate a focused button |

### Labeling elements

The accessibility label for a segmented button comes from the visible label text on such as Relevance and Distance. If the segmented button displays icons without label text, the accessibility label describes the action that the button is expressing, such as Inexpensive for one currency symbol.

[image: The the text and accessibility role for the left-most section of a segmented button following “sort by” is  is “relevance.”]

The label for segmented button matches the text label

Single-select segmented buttons behave like radio buttons: only one option can be selected at a time. The label is Radiogroup.

Multi-select buttons behave like checkboxes: more than one option can be selected. The label is Checkbox.

[image: Selected price range segmented buttons range from $ to $$$$. The accessibility label of the $ button is “inexpensive.”]

The role for the multi-select segmented button is Checkbox
