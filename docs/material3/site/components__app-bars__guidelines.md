<!-- source: https://m3.material.io/components/app-bars/guidelines -->
# Top app bar – Material Design 3

# App bars

[image: 4 app bars with headlines and action icons.]

App bars show information about the page, key actions, and navigation actions like Back or Menu

## Usage

Use an app bar to provide content and actions related to the current page, such as page navigation actions, headlines, images, and 1–2 essential actions.

The information and actions in the app bar should be contextual and specific to a page, but can also include global product controls, such as search or notifications.

[image: App bar with navigation icon buttons and a 2-line title.]

App bars provide content and actions related to the current page

App bars should only have one action, two if necessary.

The primary action should alter or exit the entire page, like Send, Save, or Edit.

If the product has many actions, place those in a toolbar. Avoid placing an overflow menu in the app bar when possible.

[image: App bar with content below.]

App bars can display one high visibility action to boost its prominence

To boost visibility of a primary action, change the style of the icon button to filled or tonal, and consider using a wide icon button.

Avoid using multiple filled or tonal buttons.

[image: App bar with 1 filled button.]

Use a filled or tonal button for important actions

[image: App bar with 2 filled buttons, side by side.]

Don’t put multiple filled or tonal buttons in the app bar

The four variants of app bars are:

- Search app bar Use on home pages when search is key to the product.

- Small Use in dense layouts or when a page is scrolled.

- Medium flexible Use to display a larger headline. It can collapse into a small app bar on scroll.

- Large flexible Use to emphasize the headline of the page.

[image: The 4 app bar variants.]

- Search app bar

- Small

- Medium flexible

- Large flexible

### Baseline app bars

There are two baseline app bars that are no longer recommended:

- Medium Replace with medium flexible.

- Large Replace with large flexible.

[image: 2 baseline app bars.]

- Medium

- Large

## Search app bar

Use a search app bar to provide an emphasized entry-point to open the search view.

[image: A search bar within an app bar.]

Search app bars have a search field instead of heading text

Search bars should always include the word Search. They can use various capitalization styles depending on the product.

- Search

- Searching a specific area Example: Search inbox

- Search [Product] Example: Search Photos

[image: 3 examples of search text in an app bar.]

Use proper capitalization depending on what’s being searched

### Buttons in search app bar

In addition to a trailing avatar, search app bars can have up to two trailing icons on mobile.

Trailing icons can be placed inside or outside the search bar.

[image: 2 icons placed in the search bar.]

Put the most used actions on the left and least used on the right

The leading element of a search app bar can be used for a product’s logo to brand the app’s overall experience. This logo can be purely cosmetic, or can trigger an action like returning to the home screen or refreshing it.

Avoid using a logo to open an expanded navigation rail.

[image: A search app bar with a logo, search bar, and avatar.]

The leading element can be a product logo

Don’t use more than two trailing icon buttons with an avatar. If more actions are needed, place them in a toolbar instead.

[image: 3 icons placed in a search app bar.]

Don’t use three icons and an avatar in a search app bar

### Large screens

The search app bar dynamically adapts to available width. There should be up to four trailing icons on larger screens.

[image: 4 actions placed in a search app bar on a large screen.]

Increased horizontal space on larger screens allows for up to four trailing icons.

### Alternate color options

By default, search containers in app bars use the surface container color to distinguish it from the app background. If the background is darker, use a lighter container color on the search bar, like surface bright.

When choosing alternate colors, make sure the search text and container have at least 3:1 contrast for readability.

[image: App bar with a light search container color.]

Search app bars can use different colors, like surface bright, for improved contrast with surrounding elements

## Anatomy

[image:  Diagram of app bar layout.]

- Container

- Headline

- Trailing icons

- Subtitle

- Leading button

### Container

The app bar container holds all information and actions at the top of a screen, including navigation icons, headlines, and buttons.

Avoid changing the position or shape of the container.

[image: App bar with square corners.]

Use straight corners for app bars

[image: App bar with curved corners.]

Don’t use curved shapes. This implies that the container can expand upon interaction.

Always use the default height of the app bar, and make it span the full width of the window.

[image: App bar at default height.]

Default heights were chosen to ensure readability of on-screen elements

[image: App bar with reduced height.]

Don't make an app bar shorter than its default height

### Adding logos

Image logos can be used in app bars to bolster brand identity or visual appeal.

The image should be high quality and pertinent, and shouldn’t disrupt the app bar's functionality.

[image: A logo added to an app bar.]

Image logos can replace all text in small app bars, and appear above the text in other app bars

### Leading button

The leading button should be used for navigating the product.

It typically is one of the following:

- A menu icon, which opens a modal expanded navigation rail

- A back arrow, which returns to the previous screen

[image: Leading navigation icon aligned on left of app bar]

- Leading Back button

### Headline

The headline can describe:

- The current page

- The current section

- The product

Headline text should be brief enough to easily fit in the app bar.

In medium flexible and large flexible app bars, the headline can wrap to a second line.

Don’t truncate the headline text.

[image: App bar headline text set in 2 lines.]

If headline text is long, use a medium flexible or large flexible app bar and wrap the headline to two lines maximum

[image: Small app bar headline text wrapped on 2 lines.]

Don’t wrap text in a small app bar

Headlines can be aligned to the leading edge or centered.

The headline’s typography size and style change depending on the app bar variant.

[image: Search, small, medium and large flexible app bars with headline styles.]

Headline typography style for each app bar

- Search: Body large

- Small: Title large

- Medium flexible: Headline medium

- Large flexible: Display small

### Subtitle

Subtitles can add additional context to a page.

These can be leading-aligned or center-aligned with the headline text.

[image: Small to large flexible app bars with headline and subtitle styles.]

Subtitle typography style for each app bar:

- Small: Label medium

- Medium flexible: Label large

- Large flexible: Title medium

### Trailing icon buttons

Up to two icon buttons can be placed after the headline, aligned to the trailing edge of the app bar. Place most-used actions closest to the leading edge.

Avoid using these buttons to open a menu with more actions. If more actions are needed, place them in a toolbar instead.

If changing the icon button color style to filled or tonal, only use one icon button.

[image: 2 icons placed to right of headline, from most to least used.]

Put the most used actions on the left and least used on the right

Use filled icons when possible for the best visibility. Outlined icons can also be used, particularly for unselected toggle buttons.

[image: App bar with 2 filled icons, “save” and “download.”]

Use filled icons for clear, visible actions

[image: App bar with 2 outlined icons, “save” and “download.”]

Outlined icons can be used as needed, or when using toggle buttons

## Adaptive design

Adaptive design allows an interface to respond or change based on context, such as the user, device, and usage. More on adaptive design

### Resizing

The width of the app bar container responds to the view or device width.

It should always span 100% of the window width.

The app bar’s container responds to always fill the window width

Resizing may cause actions at the trailing edge of the app bar to collapse into an overflow menu at smaller breakpoints.

These actions become visible again at larger sizes.

Actions at the trailing edge collapse into an overflow menu

The search container of the search app bar should fill 100% of the space between leading and trailing app bar elements until it reaches 312dp. Then, it should only grow further to fill 50% of that space.

The search field adapts to the amount of space between other elements in the app bar

### Presentation

The app bar automatically supports right-to-left (RTL) languages by aligning the layout of elements to the leading and trailing edges of the container.

This means that in RTL languages, the layout of the app bar is mirrored.

[image: App bar in RTL with Hebrew text.]

The app bar’s layout is mirrored for right-to-left (RTL) languages

## Behavior

### Scrolling

App bars should initially be the same color as the background, then fill with a contrasting color on scroll to provide visual separation from the background.

The app bar can remain on a page at all times, or can hide and reappear when scrolling.

Upon scrolling, an app bar container fills with contrasting color to create a visual separation

To focus more on body content, consider setting the app bar container to be transparent on scroll. This allows the buttons to float above the content.

Make sure icon buttons have a container fill.

Consider using narrow-width icon buttons for actions, like Back, to reduce the amount of space they take up.

Upon scrolling, an app bar container remains transparent and actions inside become filled icon buttons

Selecting the search bar should open the search view component.

When selected, a search app bar opens a search view

When scrolled, medium flexible and large flexible app bars can transform into small app bars. They should remain small until the page is scrolled back to the top. Don’t transform app bars into a search app bar.

The app bar can hide when scrolling up and reveal when scrolling down

Medium and large flexible app bars can use the compress effect to transform into small app bars when scrolled
