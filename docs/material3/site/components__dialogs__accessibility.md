<!-- source: https://m3.material.io/components/dialogs/accessibility -->
# Dialogs – Material Design 3

# Dialogs

## Use cases

People should be able to use assistive technology to:

- Open and close a dialog

- Provide and submit other inputs if the dialog is interactive, such as a text field or selectable list

- Scroll the dialog to access all of its contents if that content extends beyond the container of the dialog

## Interaction & style

### Use sparingly

Dialogs are purposefully interruptive. This means they appear in front of app content and disrupt the flow of content for people who may, for example, be using a screen reader to navigate the page.

As such, dialogs should be used sparingly and only to provide critical information. Less critical information should be presented in a non-blocking way within the flow of app content.

[image: An inline tooltip doesn’t block a photo app’s content on a mobile screen.
A modal dialog blocks the content of a photo app on a mobile screen.]

[image: A modal dialog blocks the content of a photo app on a mobile screen.
A modal dialog blocks the content of a photo app on a mobile screen.]

### 200% text size

Avoid excessive text wrapping or truncation by choosing concise strings.

On Android, headlines should be kept concise enough to fit within four lines after the text size is increased to 200%. If a headline exceeds this limit and gets truncated, provide an alternative way to access the full content in a single tap.

[image: A dialog with 200% text wraps multiple times in the header and description. It covers most of the mobile screen.]

Avoid excessive text wrapping or truncation by choosing concise strings

### Elements within dialogs

Because dialogs can contain various elements within them, refer to the relevant accessibility guidelines for each element. Some common examples include:

- Text fields

- Typography

- Buttons

[image: 3 elements of a full-screen dialog.]

Full-screen dialogs can contain various elements such as (1) text fields, (2) typography, and (3) buttons, which each may have their own accessibility guidelines

## Initial focus

When a dialog appears, focus should automatically land on the first interactive element within the dialog.

[image: A modal dialog titled “Permanently delete?” whose second interactive element is focused by selecting the Tab key.]

[image: A modal dialog titled “Permanently delete?” whose previous interactive element is focused on by selecting both the Shift and Tab keys.]

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab | Focus lands on the next interactive element contained in the dialog, or the first element if focus is currently on the last element |

| Shift + Tab | Focus lands on the previous interactive element contained in the dialog, or the last element if focus is currently on the first element |

| Space or Enter | Triggers or commits the action of the focused element |

| Escape | Closes the dialog |

## Labeling elements

The accessibility label for a dialog is typically the same as the dialog’s title or headline.

On web, basic dialogs should have the alert dialog role.

[image: An alert dialog with a title “Set up traffic updates?”  Its label is “Set up traffic updates?” and its role as “Alert Dialog.”]

Basic dialogs are known as alert dialogs on web

Components contained within the dialog, such as buttons, should be labeled according to the guidelines specific to those components.

For common examples, see:

- Buttons

- Text fields

[image: A full-screen dialog titled “New event” containing a “Save” button and a text field, both with their own accessibility labels.]

Elements within a dialog should be labeled according to their guidelines
