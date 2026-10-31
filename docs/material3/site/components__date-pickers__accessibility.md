<!-- source: https://m3.material.io/components/date-pickers/accessibility -->
# Date pickers – Material Design 3

# Date pickers

## Use cases

People should be able to:

- Enter dates manually by inputting text, without using the picker

- Use multiple input methods, making it accessible to those using assistive technology

On the docked date picker, the text field can be used for input. On the modal date picker, the date input option should be available using the edit icon.

## Interaction & style

The edit icon indicates the ability to switch to the modal date input. Interactive targets for all elements meet Material's 48x48dp minimum touch target requirement. Increasing density would negatively impact accessibility by limiting tappable/clickable targets.

[image: Date picker with the edit icon focused.]

The edit icon indicates the ability to switch to the modal date input

[image: Touch target used to select September 17 to 23 on a date picker.]

Touch targets are 48x48dp

## Date entry methods

The date entry component offers two ways to enter a date:

- Direct text entry into a text field

- Through the date picker

The calendar icon is the exclusive entry point for the date picker. This improves efficiency for a screen reader and other keyboard users, as it makes interaction with the date picker optional and reduces the amount of key presses required to input a date. Each input is a separate tab stop, which improves discoverability of the control.

[image: Text input field next to a date picker icon provides a choice of how to enter the date.]

Entering a date either through direct text entry or the date picker

## Accessible date input

Automatically format the date after the user hits “Enter“ or navigates out of the text field. Don't automatically format the date by adding slashes or other special characters while the user is typing (also known as input masks). This can cause confusion for people using screen readers because it changes what they typed.

To reduce errors, accept a range of formats including dashes, spaces, slashes, dots, and 0 to the left of a single digit month/day. This is especially helpful for assistive technology users who might be more prone to errors when interacting with complex inputs.

[image: Numeric entry 08172323 automatically formatted to 08/17/2023.]

The text field's logic can adapt to the user's actual input format, applying the correct formatting after the user has completed their text entry

## Optional Clear button

If it's not needed for your use case, remove the Clear button from the screen to reduce the number of tab stops for keyboard users.

[image: Optional clear button on lower left corner of a date picker.]

Remove non-critical actions to reduce the number of tab stops for keyboard users

## Affordance for keyboard shortcuts

Ensure keyboard shortcuts are readily available for keyboard and screen reader users by providing the shortcut key in the tooltip. It should be included in the hint description to be read out by the screen reader. As shown here, the previous year button is interactive and can therefore be focused via the keyboard. Upon focus, the tooltip explains the behavior of the button and shows the shortcut key.

[image: Shift + Page up is the keyboard shortcut to go to the previous year on a date picker.]

Keyboard tooltip example for date picker

## Truncated labels & tooltips

Truncating labels isn't ideal, but tooltips allow the full text to be shown on hover or keyboard focus. Days of the week are not interactive and are therefore not focusable via keyboard, yet the tooltip is available on hover. The date picker relies on the conventionality of these abbreviations for some assistive technology users.

[image: A pointer hover over the “T” day on a date picker produces the tooltip “Tuesday.”]

Days of the week are not navigable via keyboard, so the tooltip is shown only on pointer hover

## Color contrast between dates

Dates should have contrast of at least 4.5:1 between the link text colors and the background.

[image: A date picker’s label text passes the color contrast minimum of 4.5:1.]

Dates pass the 4.5:1 contrast minimum

## Keyboard navigation

| Keys | Actions |

|---|---|

| Enter/return | Enter/return |

| Enter/return | Closes the calendar and saves the selected date |

| Page up/down | Move to the same date on next/previous month |

| Home/End | Move to the first day of the month |

| Shift + Page up/down | Moves to the same date in the next/previous year |

| Shift + M | Moves to the month list dropdown |

| Shift + Y | Moves to the year list dropdown |

## Labeling elements

The text field's accessibility label should clearly state the purpose of the input (for example, event date or reservation date) and should match the placeholder text when the field is empty. The helper text (below the text field) should specify the date format (for example, MM/DD/YYYY or YYYY/MM/DD) and act as a description for the text field. The default helper text is "MM/DD/YYYY," but this can be customized.

[image: Text field accessibility labels.]

The accessibility label clearly states the kind of input as an event date

| Element | A11y label | Role |

|---|---|---|

| Previous / next month and year | “{label}” | Button |

| Month and year dropdowns | “{label}” | Button |

| Days of the week | Column header |  |

| Month grid | Grid |  |

## Screen reader verbalizations

To support screen reader users, labels are used to enumerate the complete date. This allows screen reader users to hear the full context of "Monday, August 17” instead of just part of the date.

[image: Current date label providing day, month, and year for screen reader accessibility.]

Screen readers will state the full day, month, date, and year instead of just the number 17
