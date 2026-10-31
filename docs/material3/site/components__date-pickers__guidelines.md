<!-- source: https://m3.material.io/components/date-pickers/guidelines -->
# Date pickers – Material Design 3

# Date pickers

[image: A date picker opens in a form UI.]

Docked date picker on desktop

## Usage

Date pickers let people select a date or range of dates. They should be suitable for the context in which they appear. Date pickers can be embedded into:

- Dialogs on compact breakpoints like mobile

- Text field drop-downs on medium and expanded breakpoints like tablet and desktop

[image: 2 date picker variations: a dialog on mobile and a dropdown within a text field on desktop.]

- Date picker dialog on mobile

- Date picker text field dropdown on desktop

There are three variants of date pickers:

- Docked date picker

- Modal date picker

- Modal date input

[image: A docked date picker component.]

[image: A modal date picker component.]

[image: A modal date input component.]

## Anatomy

### Docked date picker

[image: 7 elements of a docked date picker.]

- Text field

- Menu button

- Icon button

- Label text

- Menu

- Text buttons

- Container

[image: 3 elements of a docked date picker.]

1. Text field 2. Menu button 3. Menu

### Modal date picker

[image: 12 elements of a modal date picker.]

- Headline

- Supporting text

- Container

- Icon button

- Previous/next month buttons

- Day of week labels

- Today’s date

- Unselected date

- Text buttons

- Selected date

- Menu button

- Divider

[image: 9 elements of a modal date picker.]

- Headline

- Supporting text

- Container

- Icon button

- Unselected year

- Selected year

- Text buttons

- Divider

- Menu button

### Modal date input

[image: 7 elements of a modal date input.]

1. Headline 2. Supporting text 3. Container 4. Icon button 5. Date input 6. Text buttons 7. Divider

### Full-screen date picker

[image: 14 elements of a full-screen date picker.]

1. Headline 2. Supporting text 3. Icon button 4. Container 5. Text button 6. Icon button 7. Divider 8. Day of week labels 9. Today’s date 10. Selected date range 11. Unselected date 12. Text buttons 13. Selected date range start date 14. Month label

## Docked date picker

### Usage

Docked date pickers allow the selection of a specific date and year. The docked date picker displays a date input field by default, and a dropdown calendar appears when the user taps on the input field. Either form of date entry can be interacted with. Docked date pickers are ideal for navigating dates in both the near future or past and the distant future or past, as they provide multiple ways to select dates.

[image: Docked date picker on a desktop screen.]

Docked date picker on desktop

### Behavior

Dates can be added by using a keyboard or by navigating the calendar UI; both options are immediately available when the docked date picker is accessed.

[image: Docked date picker with a text field and the UI picker showing the selected date. ]

Docked date pickers adjust size dynamically

The year selection menu replaces the calendar view

### Month selection

Month selection can be navigated with the corresponding back and next arrows or by tapping the dropdown menu.

[image: Docked date picker with a list of months May through September. August is selected.]

Docked date picker month selection

### Year selection

Year selection can be navigated with the corresponding back and next arrows or by tapping the dropdown menu.

[image: Docked date picker with a list of years 2025 to 2029. 2025 is selected.]

## Modal date picker

### Behavior

Modal date pickers navigate across dates in several ways:

- To navigate across months, swipe horizontally

- To navigate across years, scroll vertically

- To access the year picker, tap the year

Don’t use a modal date picker to prompt for dates in the distant past or future, such as a date of birth. In these cases, use a modal input picker or a docked date picker instead.

To navigate across months, swipe horizontally

To navigate across years, tap the year picker and scroll vertically

### Date range selection

Date range selection provides a start and end date. Common use cases include:

- Booking a flight

- Reserving a hotel

Modal date pickers navigate across date ranges in several ways:

- To select a range of dates, tap the start and end dates on the calendar

- To navigate across months, scroll vertically

Modal date range picker

Modal date range picker with vertical scroll

## Modal date input

### Usage

Modal date inputs allow the manual entry of dates using the numbers on a keyboard. People can input a date or a range of dates in a dialog.

[image: A modal date input component.]

Modal date with manual input

[image: A modal date input component showing a day in 1979, which would be difficult to choose using UI.]

For dates that don’t require a calendar view, the modal date input can be the default view

[image: A modal date input with hint text for entering the date.]

Alternatively, a text field with appropriate hint text can prompt for dates, such as in a form

### Behavior

You can swap between the modal date picker and modal date input using the edit or calendar icon.

Switching from a modal date picker to a mobile date input for selecting ranges

Switching from a modal date picker to a modal date input for selecting a single date

### Compact breakpoint

On compact breakpoints, such as mobile, a full-screen modal date picker is recommended to increase readability and touch target size. It can cover the entire screen.

[image: A full-screen view of modal date picker on a mobile device.]

A full-screen modal date picker on mobile

### Medium and expanded breakpoints

The docked date picker works best for medium and expanded breakpoints. It displays a date input field by default, and a dropdown calendar appears when a person taps on the input field. A person can interact with either form of date entry. Docked date pickers are ideal for navigating dates in both the near future or past, and in the distant future or past, as they provide multiple ways to select dates.

[image: A docked date picker displaying a full calendar view on a large screen device.]

A docked date picker with a full calendar view is best used on larger devices

### Selection

Selection is indicated through color, drawing visual attention. In date ranges, start and end dates are selected, while dates in-between appear connected with a subtle highlight.

Differences between selected the selected date range (August 17–23) and today's date (August 5) are shown through color and fill

### Appearing and disappearing

Like other kinds of dialogs, modal date pickers use an enter and exit transition pattern to appear on the screen. To exit a date picker, the input can either be confirmed (OK) or dismissed (Cancel). Interacting outside of the dialog will also dismiss the time picker. Unless one of these actions is taken, a time picker will continue to retain focus. Mobile full-screen pickers also have an additional close affordance (x) icon button and Save confirmation. Docked date pickers appear just below the input field.

Modal date pickers can be dismissed through interacting with content outside the dialog, or with the action buttons in the lower right

Interacting with the input for a docked date picker makes the calendar view appear below

### Responsive layout

The sizing of the docked and modal date picker components don’t scale responsively to different breakpoints.

[image: Docked date picker enlarged on a large screen responsively.]

Don’t scale the date picker responsively to a larger size
