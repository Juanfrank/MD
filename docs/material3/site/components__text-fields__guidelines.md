<!-- source: https://m3.material.io/components/text-fields/guidelines -->
# Text fields – Material Design 3

# Text fields

[image: A side by side view of a filled and a outlined text field.]

Filled and outlined text fields

## Usage

Use a text field when someone needs to enter text into a UI, such as filling in contact or payment information.

[image: Mobile UI of contact form with several text fields. ]

Contact form using outlined text fields

There are two variants of text fields:

- Filled text fields

- Outlined text fields

Both variants of text fields use a container to provide a visual cue for interaction and provide the same functionality.

[image: Side by side view of a populated and unpopulated filled text field. ]

Filled text field

[image: Side by side view of a populated and unpopulated outlined text field. ]

Outlined text field

### Outlined text fields

Outlined text fields have less visual emphasis than filled text fields. When they appear in places like forms (where many text fields are placed together), their reduced emphasis helps simplify the layout.

[image: App screen with 1 focused and 1 unfocused outlined text field.]

Login screen with outlined text fields

## Choosing text fields

### Choosing text fields

Both variants of text field provide the same functionality. The variant of text field used can depend on style alone.

Choose the variant that:

- Works best with an app’s visual style

- Best accommodates the UI's goals

- Is most distinct from other components (like buttons) and surrounding content

[image: Mobile UI of a contact form with several filled text fields. ]

Mobile form using filled text fields

[image: Mobile UI of a contact form with several outlined text fields. ]

The same mobile form using outlined text fields

### Using both text field variants on the same screen

If both variants of text field are used in a UI, they should be used consistently within different sections, and not intermixed within the same region.

For example, use outlined text fields in one section and filled text fields in another.

[image: Mobile UI of a contact form with several filled text fields, and an open dialog on top using an outlined text field. ]

When using both variants of text fields in a UI, separate them by region

[image: Mobile UI of a contact form with a mix of outlined and filled text fields.]

When using both variants of text fields, don't use both next to each other or within the same form

## Anatomy

### Filled text field

[image: Diagram of filled text field indicating the 10 parts of its anatomy.]

- Container

- Leading icon (optional)

- Label text in empty field

- Label text in populated field

- Trailing icon (optional)

- Focused active Indicator

- Caret

- Input text

- Supporting text (optional)

- Enabled active Indicator

### Outlined text field

[image: Diagram of an outlined text field indicating the 9 parts of its anatomy.]

- Enabled container outline

- Label text in empty field

- Leading icon (optional)

- Label text in populated field

- Trailing icon (optional)

- Focused container outline

- Caret

- Input text

- Supporting text (optional)

### Containers

Containers improve the discoverability of text fields by creating contrast between the text field and surrounding content.

Fill and stroke A text field container has a fill and a stroke either around the entire container, or just the bottom edge. The color and thickness of a stroke can change to indicate when the text field is active.

Rounded corners The container of an outlined text field has rounded corners, while the container of a filled text field has rounded top corners and square bottom corners.

[image: Side by side view of the containers of a filled and outlined text field.]

Text field containers

### Label text

Label text tells people what information is requested. Every text field should have a label.

Label text should be aligned with the input text, and always visible. It can be placed in the middle of a text field, or rest near the top of the container.

Label text shouldn't be truncated or take up multiple lines. Keep it short, clear, and fully visible.

[image: Text field with very long label text, too long to display fully display inside the text field container.]

[image: Text field with very long label text split into 2 lines. ]

Label text shouldn’t take up multiple lines

### Adjacent label

A text field doesn't require a label if the field's purpose is indicated by a separate, adjacent label.

Adjacent labels should be aligned to the leading edge of the text field container.

[image: Mobile UI of a contact form with label texts placed outside and on top of the text fields. ]

Text fields with adjacent labels

### Required text indicator

To show a field is required, display an asterisk (*) next to the label text, and explain that asterisks indicate required fields in one of two ways:

- Supporting text

- A single note at the beginning of the form

Additional best practices include:

- Indicate all required fields

- If required text has a particular color, use the same color for the asterisk

[image: Mobile UI of a contact form showing supporting text below the text field, indicating an input is required. ]

Asterisk with required supporting text

### Input text

Input text is text a person has entered into a text field.

Text fields can display input text in the following ways:

- Single line text fields display only one line of text

- Multi-line text fields grow to accommodate multiple lines of text

- Text areas are fixed-height fields

[image: Text field with populated input text. ]

Input text in a filled text field

In single-line fields, as the cursor reaches the right field edge, text longer than the input line automatically scrolls left. Single-line fields are not suitable for collecting long responses; use a multi-line text field or text area instead.

In multi-line fields, overflow text causes the text field to expand, shifting screen elements downward and text wraps onto a new line. These fields initially appear as single-line fields, which is useful for compact layouts that need to accommodate large amounts of text.

Text areas are taller than text fields and wrap overflow text onto a new line. They are a fixed height and scroll vertically when the cursor reaches the bottom of the field. The large initial size indicates that longer responses are possible and encouraged. These should be used instead of multi-line fields on the web. Ensure the height of a text area fits within mobile screen sizes.

### Prefix text

Text fields can contain prefix text such as currency symbol.

[image: Text field with a currency prefix before the input text. ]

A text field with a currency symbol text prefix

### Suffix text

Text fields can contain suffix text such as unit of measurement or email domain.

[image: Text field with a suffix after the input text indicating a maximum input of 100. ]

A text field with a grading scale as suffix

[image: Text field with a suffix after the input text indicating an email address. ]

A text field with an email domain suffix

### Supporting text & character counter

Supporting text conveys additional information about the input field, such as how it will be used. It should ideally be one line, though may wrap to multiple lines if required. It can be either persistently visible or visible only on focus.

If there is a character or word limit, include a character or word counter. They display the ratio of characters used and the total character limit.

[image: A side by side view of a text field with supporting text aligned with the trailing side, and a character counter aligned with the trailing side. ]

- Supporting text

- Character counter

### Error text

For text fields that validate their content such as passwords, replace supporting text with error text. Swapping supporting text with error text prevents new lines of text from bumping content and changing the layout.

- If only one error is possible, error text should describe how to avoid the error

- If multiple errors are possible, error text should describe how to avoid the most likely error

Swap supporting text with error text

Don't add error text in addition to supporting text, as their appearance will shift content

[image: Mobile UI of a sign up form with an invalid text field entry. The error message wraps to 2 lines. ]

Long errors can wrap to multiple lines if there isn't enough space to clearly describe the error. In this case, ensure padding between text fields is sufficient to prevent multi-lined errors from bumping layout content.

### Error icon

It’s strongly recommended to show an error icon when the text field is in the error state.

This highlights the error for people with visual impairments, and provides an additional sensory indicator.

[image: 2 text fields with error messages. The active text field has a thicker border. Both text fields have a trailing error icon.]

The error icon is an important second visual indicator that a text field has an error

### Icons & images

Icons in text fields are optional. Text field icons can:

- Describe valid input methods such as a microphone icon

- Provide affordances to access additional functionality such as clearing the content of a field

- Express an error

Leading and trailing icons change their position based on LTR or RTL contexts.

Images that are 24dp in height can be placed inside of text fields. This image height allows for optimal top and bottom padding within the field and is consistent with icon size recommendations.

- Icon signifier Icon signifiers can describe the type of input a text field requires, and be touch targets for nested components. For example, a calendar icon may be tapped to reveal a date picker.

- Valid or error icon Iconography can indicate both valid and invalid inputs, making error states clear for colorblind users.

- Clear icon Clear icons let a person clear an entire input field. They appear only when input text is present.

- Voice input icon A microphone icon signifies that people can input characters using voice.

- Dropdown icon A dropdown arrow indicates that a text field has a nested selection component.

- Image An image can help contextualize the required input text such as a credit card number.

[image: Side by side view of text fields with different icons and images as trailing elements within the container. ]

- Icon signifier

- Valid or error icon

- Clear icon

- Voice input icon

- Dropdown icon

- Image

### Read-only fields

Read-only text fields display pre-filled text that people cannot edit.

A read-only text field is styled the same as a regular text field and is clearly labeled as read-only.

[image: Read only filled text field. ]

A filled read-only text field

[image: Read only outlined text field. ]

An outlined read-only text field

## Adaptive design

As layouts adapt to larger screens and different breakpoints, apply flexible container dimensions to text fields. Set minimum and maximum values for margins, padding, and container dimensions as layouts scale so that typography adjusts for better reading experiences.

[image: UI for creating a new album in a side by side view on mobile and tablet. ]

For compact breakpoints, text fields can span the full width of the display. For medium and expanded breakpoints, text fields should be bound by flexible margins or other containers.

As text fields expand in fluid layouts, avoid maintaining fixed margins and typography properties. This can lead to extra long text fields.

For example, text fields should not span the full width of a large screen.

[image: Tablet UI with text fields spanning the complete width of the screen. ]

Don’t use fixed text field margins on large devices. Text fields shouldn’t span the full width of a large screen.

### Density

Dense text fields enable people to scan and take action on large amounts of information.

[image: Tablet UI with desne text field as part of event creation form. ]

A form with dense text fields

#### Avoid applying density by default

Don't apply density to text fields by default. This lowers their targets below the recommended 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.

To ensure this density setting can be easily reverted when it's active, keep all the targets to change it at a minimum of 48x48 CSS pixels each.
