<!-- source: https://m3.material.io/components/tooltips/guidelines -->
# Tooltips – Material Design 3

# Tooltips

[image: A plain tooltip labeling a button, and a rich tooltip announcing new settings available.]

Plain and rich tooltips serve different purposes

## Usage

A tooltip provides additional context for a UI element.

Plain tooltips Plain tooltips briefly describe a UI element. They're best used for labelling UI elements with no text, like icon-only buttons and fields.

Rich tooltips Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks.

Rich tooltips are best used for longer text like definitions or explanations.

[image: 2 variants of tooltips.]

- Plain tooltip

- Rich tooltip

[image: Plain tooltip labeling an icon-only button in Google Meet as "Present now".]

Use plain tooltips to label icon-only buttons

[image: Button with an icon and label text saying "Edit". It has a plain tooltip on hover that also says "Edit".]

Plain tooltips aren't needed when the UI element already has label text

[image: Rich tooltip describing a new button for adding people. It has a subhead, description, and a button to learn more.]

Use rich tooltips to provide extra information and actions about a UI element or new feature

[image: Rich tooltip explaining that an action is destructive and permanently deletes files.]

Don't hide critical information within tooltips as it’s easy to miss. Use an interruptive dialog instead.

## Anatomy

### Plain tooltip

[image: 2 elements of a plain tooltip.]

- Container

- Supporting text

### Supporting text

[image: Plain tooltip for an icon-only button shaped like a gear. The tooltip text is "Settings".]

Briefly describe a UI element

[image: Plain tooltip for the account switcher. The supporting text includes the user's name and email address on new lines.]

Avoid wrapping text to multiple lines or including many pieces of information

### Rich tooltip

[image: 4 elements of a rich tooltip.]

- Subhead (optional)

- Container

- Supporting text

- Text button (optional)

### Subhead (optional)

Keep subheads brief, ideally to one line. They should summarize or describe the message of the rich tooltip.

Subheads are important to include when the rich tooltip appears automatically, like when the page loads.

[image: Rich tooltip with a brief subhead, supporting text, and a text button.]

Summarize the message in a few words

[image: Rich tooltip with a subhead wrapping to multiple lines.]

Avoid wrapping to more than one line

### Text buttons (optional)

Rich tooltips can have up to two text buttons. These should be brief and relevant to the message in the supporting text.

Keep buttons short so they can be side by side. Avoid stacking them when possible.

[image: Rich tooltip with 2 buttons stacked on each other.]

Avoid stacking buttons

## Placement

### Plain tooltips

By default, plain tooltips are positioned directly above the parent element.

- If there's a visual boundary, like a button, the distance is 4dp

- If there's no visual boundary, like with text baselines, the distance is 8dp

If the element is in an app bar, the plain tooltip appears below the element at the same distance.

[image: Plain tooltip appearing 4dp below a button with a clear visual boundary.]

Plain tooltip with a 4dp distance between the target and tooltip

### Rich tooltips

By default, rich tooltips are positioned to the bottom right of the parent element. They adjust position to avoid going off screen. Tooltips shouldn't cover the parent element.

Dynamic positioning The position of the tooltip adjusts in increments of 8dp to avoid going off-screen.

Desktop placement On desktop, tooltips may appear centered below the parent element and remain visible while moving within the target region.

[image: A rich tooltip in 4 different corners. It   changes position to remain fully on screen.]

Four different rich tooltip locations based on dynamic positioning

## Behavior

To show a tooltip, hover on the parent element on desktop, or tap and hold the element on mobile. Persistent rich tooltips only appear when clicked or tapped.

### Transient by default

Both plain and rich tooltips disappear 1.5 seconds after navigating away from the target region.

Triggering a new tooltip immediately closes any other open tooltip.

Tooltips disappear after a 1.5 second delay when no other element is hovered

[image: 2 buttons both showing plain tooltips at once.]

Only display one tooltip at a time

### Persistent rich tooltips

Persistent rich tooltips appear when either:

- The parent element is clicked

- The page loads and a new feature is being explained

Persistent rich tooltips remain active even when leaving the target region. They only disappear once a person interacts with another UI element. Hovering doesn't trigger the tooltip.

When appearing on page load, the tooltip can introduce and explain new features on various parent elements.

Avoid using persistent rich tooltips on icon buttons.

[image: Persistent rich tooltip about a new sharing feature in the Photos app. The button says  "Learn more.”]

Don’t use a persistent rich tooltip on icon buttons
