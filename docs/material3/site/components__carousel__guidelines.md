<!-- source: https://m3.material.io/components/carousel/guidelines -->
# Carousel – Material Design 3

# Carousel

[image: Carousel items adapting dynamically to device size by shrinking and reducing in number.]

Carousel items adapt dynamically based on breakpoint

## Usage

Carousels display a scrollable list of items. Carousel items emphasize visuals, but can also contain brief text that adapts to the item size.

There are four carousel layouts:

- Multi-browse

- Uncontained

- Hero

- Full-screen

All of these layouts can be centered, though center-aligned hero is the most common centered carousel.

Carousels can scroll in two ways:

- Default: Standard scrolling. Recommended for uncontained layouts.

- Snap-scrolling: Scrolled items snap to the carousel's layout. Recommended for multi-browse, hero, and full-screen layouts

[image: Contained carousel with a large, medium, and small item. Text is hidden on the small item.]

A carousel can contain different sized items

Choose the best carousel layout for your product. Some layouts are more visual-focused, while others are more customizable.

| Layout | Best used for |

|---|---|

| Multi-browse | Browsing many visual items at once (like photos), dynamic designs |

| Uncontained | Highly-customized or text-heavy carousels, stacked imaged and text, traditional carousel behavior |

| Hero | Spotlighting very large visual items (like a movie or featured app) |

| Center-aligned hero | Centered, large visual items |

| Full-screen | Vertically-scrolling video or image feeds, immersive experiences |

Carousel items must be fully visible on-screen (except for the uncontained layout). When scrolled, items automatically change size and snap into place to maintain the same layout.

[image: Multi-browse carousel with all images and text easily legible.]

Set the large carousel item size to ensure the images and text are easy to read and recognize

[image: Multi-browse carousel with a very thin small item, making the image unrecognizable.]

Avoid setting carousel items so small that the image isn't recognizable

### Accessibility requirements on scrolling pages

On vertically-scrolling pages, carousels require an accessible way to view all the items without horizontally scrolling. (This requirement doesn't apply to full-screen carousels.)

Material recommends adding a Show all button below the carousel, which opens a dedicated vertically-scrolling page of all carousel items.

If the carousel has a header, you can use an arrow icon button instead.

View the accessibility tab for more details and alternate solutions.

Make sure users can scroll vertically through all carousel items

### Multi-browse

The multi-browse layout is best for browsing many items at once, like photos or event feeds. Snap-scrolling is recommended to ensure items are recognizable and consistently sized.

On larger screens, more large and medium items are visible in this layout.

Avoid using this layout if the carousel items need lots of text or have complicated imagery.

A multi-browse layout has different sized items within the carousel

At compact breakpoints, only show up to three carousel items if they have text.

If you need to show more than three items, make sure the images and content are easy to understand and recognize.

[image: Carousel on a phone. 2 large, 1 medium, and 1 small item are fully visible but thin. The items don't have text.]

At compact breakpoints, only show more than three items if the items are easy to understand and recognize

### Uncontained

The uncontained layout is most similar to a traditional carousel, where items are a single size and flow past the edge of the screen.

Both default scrolling and snap-scrolling work well with this layout.

Since items don't change size, this layout can be customized to show more text or other UI above or below each item without the text being masked or cropped.

Carousel items are all the same size in an uncontained layout

### Uncontained multi-aspect ratio

The uncontained multi-aspect ratio carousel has the same layout as the uncontained carousel but contains items of various sizes.

Item widths can range anywhere between 9:16 for min width size to 16:9 for max width.

Only use this carousel layout if the items have various widths.

Carousel items are of various sizes in an uncontained multi-aspect ratio layout

### Hero

The hero layout is best for spotlighting content that needs more attention, like movie, shows, or other media thumbnails. It highlights one large image to focus on, while providing a sneak peek of what’s next.

On larger screens, more large items are visible.

Use snap-scrolling so users can easily cycle through items one at a time.

A hero carousel at a compact breakpoint should show one large item and one small item

### Center-aligned hero

When the hero layout is center-aligned, it adds an additional previewed item on the leading edge, making the large carousel item centered.

A centered hero carousel has two small carousel items, with a large item centered

### Full-screen

The full-screen layout is best used for immersive experiences like video articles, featured headlines, or items that are visually rich. It can contain text and other UI elements on top of the image.

This layout works best with content that is taller than it is wide, and scrolls vertically. It only works in portrait orientation in compact and medium breakpoints. Don't use this layout in landscape orientation.

Use snap-scrolling for full-screen layouts. Don't use default scrolling.

Full-screen carousels fill the entire content area of the screen

## Anatomy

[image: 4 elements of a carousel.]

Multi-browse carousel (left) and hero carousel (right):

- Container

- Large carousel item

- Medium carousel item

- Small carousel item

### Container

The carousel container holds all carousel items. The number of carousel items visible in the container can change based on the carousel layout and breakpoint.

[image: An empty rectangle representing a carousel container.]

The carousel container is a rectangle. It can be used in many ways and stretched to any size.

### Carousel items

Carousel items hold content. A carousel item has no fixed width; it changes width depending on the breakpoint or its position in the carousel's layout. There are three dynamic widths an item can be: large, medium, and small.

[image: 3 sizes of carousel items.]

- Large carousel item

- Medium carousel item

- Small carousel item

Large items have a max width that can be adjusted. This changes how all other large, medium, and small carousel items fit on screen. Large items must remain big enough to be easy to understand and recognize.

Medium items adjust width dynamically to the carousel size and available space.

Small items have a width range of 40–56dp.

[image: 2 sizes of carousel items for hero layouts.]

- Large item

- Small item

When the large item's max width is narrow enough, more items can be shown on screen at once. At compact breakpoints, this is only recommended for carousels with simple imagery.

[image: 3 sizes of carousel items for multi-browse layouts. 2 large items are visible.]

- Large item

- Medium item

- Small item

### Item text (optional)

Carousel items are primarily visual. Item text is optional and should be brief.

If your carousel items require a lot of text, consider using the uncontained layout, which can show more information, or use a series of cards instead.

[image: Contained carousel items with 5 lines of content: a title, a description, and a label.]

Avoid exceeding two lines of text in carousel items at compact breakpoints unless the background is simple, like a single color

Content within a carousel item can adapt dynamically based on the container and breakpoint.

Text should always be understandable at each size. Consider adapting the text to use brief labels on smaller carousel items.

[image: A carousel item at 3 different sizes to show  how text changes at each size.]

- Large carousel item with the full title and label text

- Medium carousel item hiding the title text

- Small carousel item abbreviating the label text

## Adaptive design

As the carousel container size increases, so do the number of carousel items visible at a time.

At compact breakpoints, carousels can comfortably show up to three carousel items at once.

At larger breakpoints, more carousel items are added and scale in size.

Full-screen carousels only ever show one item at once.

[image: 8 carousel items visible at once on a tablet in landscape orientation.]

Carousels can show more items at once on larger screens

## Behavior

### Scrolling

Carousel items have a parallax effect when they're scrolled.

The default scrolling behavior doesn't snap items to a layout grid. They can stop anywhere in the container. Only use this for the uncontained layout.

The snap-scrolling behavior aligns carousel items to the layout grid after they're scrolled. Items snap to the grid when released. Use this for multi-browse, hero, and full-screen layouts.

Carousel items with snap-scrolling maintain the same layout when released

In full-screen layouts, make sure the carousel items snap to the edges of the carousel container. Avoid letting them scroll freely or stop halfway.

Full-screen layouts must use snap-scrolling.

[image: Full-screen carousel with items stopping halfway off screen once scrolled.]

Avoid scrolling freely on full-screen carousels
