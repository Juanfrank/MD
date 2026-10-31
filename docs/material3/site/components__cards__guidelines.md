<!-- source: https://m3.material.io/components/cards/guidelines -->
# Cards – Material Design 3

# Cards

[image: 3 variants of cards: elevated, filled, and outlined.]

## Usage

Use a card to display content and actions on a single topic.

Cards should be easy to scan for relevant and actionable information.

Elements like text and images should be placed on cards in a way that clearly indicates hierarchy.

[image: Example card containing an image, title, text, and button.]

Cards can display content and actions on a single topic

Cards can serve as entry points into deeper levels of detail or navigation, such as a music album or details on an upcoming vacation.

[image: Example world tour card.]

Card text and image show a clear hierarchy

[image: Card displaying connected details about a world tour.]

Use cards to display related information on a single subject

Cards can be displayed together in a grid, vertical list, or carousel.

[image: 4 cards together in a grid layout.]

Cards can be shown together

[image: 5 albums in a vertical list of cards.  ]

Don't force content into cards when spacing, headlines, or dividers would create a simpler visual hierarchy

There are three card variants:

- Elevated

- Filled

- Outlined

Each provides the same legibility and functionality, so the variant you use depends on style alone.

[image: 3 variants of cards.]

- Elevated card

- Filled card

- Outlined card

[image: Example elevated card.]

Elevated cards have a drop shadow, providing more separation from the background than filled cards, but less than outlined cards

[image: Example filled card.]

Filled cards provide subtle separation from the background. This has less emphasis than elevated or outlined cards.

[image: Example outlined card.]

Outlined cards have a visual boundary around the container. This can provide greater emphasis than the other variants.

## Anatomy

The card container is the only required element in a card. Card layouts can vary to support the kinds of content they contain. Below is a common configuration of elements.

[image: Diagram labeling the 6 parts of card anatomy.]

- Container

- Image

- Button

- Supporting text

- Subhead

- Headline

### Container

Card containers hold all card elements. Their size is determined by the space those elements occupy. Card elevation is expressed by the container.

The card container is the only required element of a card. All other elements are optional.

[image: 3 card containers with various elements: 1 with all elements except a button. 1 with a container, headline, supporting text, button. 1 with a container, headline, supporting text, 2 buttons.]

Card size is determined by the elements it contains

### Content blocks

Card contents are grouped into blocks. Content can have different levels of visual emphasis depending on importance.

Card layouts vary to support the kinds of content they contain.

[image: Diagram of card content blocks.]

Cards can contain a headline, subhead, supporting text, media, and actions

### Dividers

Dividers can separate regions in cards or indicate areas of a card that can expand.

[image: A divider running the entire width of the card.]

1. Use full-width dividers for content that can be expanded

[image: An inset divider indented from the edge of card.]

1. Use inset dividers, which don’t run the full width of a card, to separate related content

### Media

Thumbnail Cards can include thumbnails for an avatar or logo.

Image Cards can include photos, illustrations, and other graphics, such as weather icons.

Video Cards can include video.

[image: A mobile chat app with: 5 cards with images, 1 card with a thumbnail avatar, and 1 card with a video. ]

Cards can contain thumbnails, images, and video

### Text

Headline Headline text often communicates the subject of the card, such as the name of a photo album or article.

Subhead Subheads are smaller text elements, such as an article byline or a tagged location.

Supporting text Supporting text includes body content, such as an article summary or a restaurant description.

[image: card container with several elementsA tablet email app with an email summary card with multiple text elements.]

Headline, subhead, and supporting text in a card

#### Layering text, icons, and images

It isn’t recommended to place text or icons on images. If it’s necessary, ensure the background image provides sufficient contrast for the text to meet accessibility standards.

Add a translucent scrim or bounding shape beneath the text or icon to help ensure proper contrast.

[image: Layered text contrasts with the background image.]

Ensure that text on images meets accessible contrast standards

[image: Icon within a bounding shape, placed on an image.]

When placing text or icons on images, consider using a bounding shape to ensure proper contrast

### Actions

#### Primary action area

Cards can be one large touch target triggering an expanded detail screen.

[image: The action area of a card contains rich media and supporting text.]

Cards can include a primary action area that expands into a full-screen view

Buttons Cards can include buttons for actions such as Learn more or Add to cart.

Icon buttons Cards can include icon buttons for actions such as Save, Heart, or Leave a 4-star review.

Selection controls Cards can also include chips, sliders, checkboxes, and other selection controls.

Linked text There can be a link in the supporting text on a card.

[image: Supplemental text and actions at the top and bottom of the card.]

Cards can include multiple action areas containing buttons, links, and other controls

[image: Album card with an option to give a star rating.]

Cards can contain icon buttons like stars to rate content

[image: Card to purchase tickets with choice chips for 3 event times.]

Cards can contain choice chips in the action area

[image: Card with slider to control a song’s volume.]

Cards can contain a slider control in the action area

Overflow menu Overflow menus contain related actions. They are typically placed in the upper-right or lower-right corner of a card.

[image: 2 cards: 1 with an overflow menu in the upper-right corner, the other with it in the lower right.]

Overflow menus are usually located in the upper-right or lower-right corner of a card

## Cards in a collection

Multiple cards can be grouped together into collections displayed in a grid, list, or carousel.

By default, cards in a collection are coplanar. They share the same resting elevation unless they're picked up or dragged.

[image: 9 cards in a grid layout.]

Multiple cards can be grouped into collections with a shared resting elevation

#### Filtering and sorting

Card collections can be filtered in a variety of ways, including by date or alphabetical order. If a collection can be filtered, the filter must apply to each card in the collection.

Filter or sorting options should be placed outside of the card collection.

[image: A sort-by-date option placed above a card collection.]

Card collections can be filtered in a variety of ways, including by date: 1. A sort-by-date option is placed outside of the card collection

Organize card collections so that they'e easy to use. Their layout affects how they are perceived.

[image: A template for an 8-card collection layout.]

Place cards in a collection in a straightforward, easy-to-use manner

### Grid

Cards can be displayed together in a grid.

Cards displayed in a grid

The default grid can be customized in code to show cards in staggered or mosaic grids.

[image: 5 menu item cards in a mosaic grid.]

Custom mosaic grid

[image: 4 menu item cards in a staggered grid.]

Custom staggered grid

### Vertical list

Cards can be displayed together in a vertical list.

Cards can be shown in a vertical list

### Carousel

Cards can be displayed together in a horizontal row or carousel.

Cards displayed together in a horizontal row or carousel

## Adaptive design

As cards scale to adapt to different breakpoints, their position and alignment can also change.

Cards and their elements can align left, right, or center as the layout scales.

[image: 2 cards on a mobile screen row expand to 4 cards on a tablet screen row. ]

Card position and alignment changes as the screen size changes

### Ergonomics

Adjust the layout of cards to meet the ergonomic needs of large screens. For example, a horizontally-oriented card in a compact breakpoint may become a larger, vertically-oriented card in an expanded breakpoint, with more space for images and text on the larger screen.

[image: Card sizes change from mobile to tablet, with larger images in the tablet layout.]

Adjust the card layout so content remains the main focus on large screens

### Visual presentation

To adjust the presentation of content-focused components, begin with spacing.

Allow components like lists, cards, and images to optimize space while filling the region of a screen that suits a device breakpoint’s ergonomic needs.

[image: 2 cards with optimized space: 1 narrow rectangle, 1 wide square.]

Spacing adjusts for components such as cards, lists, and images

[image: 2 examples of the same card: 1 vertical with an image at the top, 1 horizontal with an image on the left.]

Example of the same card with two different orientations and element positioning

### Column-based layouts

In mobile layouts, components such as lists or cards are stretched to fit the full width of the screen without compromising visual quality or user experience. When designing for large screens with an expanded breakpoint, use multiple columns to display content.

Avoid extending UI elements across the screen when possible. On larger screens, rearrange groups of related cards into horizontal rows or carousels, to allow for better content organization.

[image: 3 related cards in a carousel.]

When designing for large screens, use multiple columns to display content

### Small screens

On smaller screens with the compact breakpoint, consider swapping cards for lists, which can display images and text in a more compact form.

Make sure that controls, actions, and other component-specific elements are maintained.

Certain devices or user contexts require different components to meet platform expectations

## Behavior

### Expanding

Cards can use a container transform transition pattern to reveal additional content. Reserve this pattern for hero moments that are meant to be expressive.

A card expands to fill the full screen using a parent-child transition

Expand a card to reveal information

Don’t scroll within a card to reveal information

### Navigation

Cards can use a forward and backward transition pattern to navigate between screens at consecutive levels of hierarchy. This pattern has a simpler motion style compared to container transform, which makes it suitable for common navigation transitions.

Cards can use a forward and backward transition pattern to navigate between screens

### Gestures

#### Swipe

A swipe gesture can be performed on a single card at a time, anywhere on that card.

It can be used to:

- Dismiss a card

- Change the state of a card, such as flagging or archiving it

A card should only have one swipe action assigned to it

Cards shouldn’t contain content that can be swiped, such as an image carousel or pagination. Also, swipe gestures shouldn’t cause portions of cards to detach upon swiping.

#### Pick up & move

The pick-up-and-move gesture allows users to move and reorder cards in a collection.

When moving a card, increase its elevation

Don’t let cards bump other elements out of the way. When a card is picked up, it appears in front of all elements, except app bars and navigation.

#### Scrolling

Card content that’s taller than the maximum card height is truncated and doesn’t scroll, but can be displayed by expanding the height of a card. A card can expand beyond the maximum height of the screen, in which case the card scrolls within the screen.

On a mobile device, cards can't internally scroll, as it could cause two scroll bars to be displayed

#### Scrolling on desktop

On a desktop device, card content can expand and scroll within a card.

On a desktop, content can expand and scroll within a card
