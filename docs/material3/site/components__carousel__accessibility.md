<!-- source: https://m3.material.io/components/carousel/accessibility -->
# Carousel – Material Design 3

# Carousel

## Use cases

Users should be able to do the following with assistive technology:

- Navigate to the carousel container

- Navigate between different carousel items

- Activate a carousel item

- Skip over the carousel items

## Requirements on scrolling pages

On vertically-scrolling pages, carousels require an accessible way to view all the items without horizontally scrolling. (This requirement doesn't apply to full-screen carousels.)

Material recommends adding a Show all button below the carousel, which opens a dedicated vertically-scrolling page of all carousel items.

Carousels without headers should use a Show all button to view all carousel items

[image: Measurements of a "show all" button added below a carousel.]

The Show all button should have a padding of 4dp

If the carousel has a header, you can use an arrow icon button instead. Place the arrow icon directly next to the header or in the same row.

Make sure the header is also displayed on the page of all carousel items.

Carousels with headers should use an arrow to view all carousel items

[image: Measurements of an arrow icon button added next to a carousel header.]

Headers should align with the leading edge, and the arrow icon should have a size of 48dp

Avoid customizing the accessibility solution when possible. However, if your product needs an alternative solution, consider adding a Show all button in nearby navigation, or add alternative control buttons close to the carousel.

Avoid adding UI elements, like arrows or other icons, within or beside the carousel.

[image: Arrow icons on the left and right of the carousel, reducing container width.]

Avoid adding buttons into the carousel container or beside it. Place any buttons above or below the carousel.

[image: Arrow icons floating on top of the carousel edge, concealing items.]

Don't cover the carousel with buttons or other UI

## Interaction & style

### Touch

Tapping on a carousel item changes the shape slightly, and creates a touch ripple for interaction feedback.

Touch: Tap

### Cursor

The hover state provides a visual cue that the carousel item is interactive.

When the carousel item is clicked (in both active and inactive states), a ripple appears for interaction feedback.

Cursor: Hover, click

### Initial focus

When navigating to a carousel using assistive technology, use Tab to place initial focus on the first carousel item. Then, use Tab or the arrow keys to navigate the carousel items.

Use the up and down arrow keys to leave the carousel and focus on the next element on the page, like the Show all button.

[image: Diagram of how to navigate a carousel using assistive technology.]

Set initial focus on the first carousel item, and use arrows to navigate items

[image: Diagram of how not to navigate a carousel using assistive technology.]

Avoid focusing on the carousel container

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab or Arrows | Moves to the previous or next carousel item |

| Space or Enter | Activates the focused carousel item |

## Labeling elements

The carousel container has the container role.

[image: Accessibility labels of a carousel.]

The carousel container is labelled appropriately and has the container role

Each carousel may have a different number of items, so the label reads out the total amount of items and the current item in focus.

[image: Accessibility labels of a carousel item.]

The carousel item label indicates the current item in focus and the total number of items

## Reduced motion

When reduced motion settings are turned on, the parallax effect should be removed and carousel items should no longer expand as they come into view. All items are the same size.

Make sure carousels with reduced motion reach the edges of the window to avoid clipping visuals.

- Default carousel for multi-scroll

- Carousel with reduced motion settings turned on

For hero carousels with reduced motion, the small carousel item is only partially shown on screen.

- Default carousel for single-scroll

- Carousel with reduced motion settings turned on
