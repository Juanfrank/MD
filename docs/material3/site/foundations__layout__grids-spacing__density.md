<!-- source: https://m3.material.io/foundations/layout/grids-spacing/density -->
# Grids & spacing – Material Design 3

# Grids & spacing

- Information density is the consideration of the amount of information visible on the screen

- The default target size should be at least 48x48 CSS pixels

- People can change density as long as the density controls are accessible

- Apply density thoughtfully; not every layout needs it

- Layout and component scaling (component adaptation or component density) can allow people to scan, view, or compare more information at once

Information density can change based on context and preference

Consider whether components should scale

Information density

- Information density can be achieved through layout and design decisions without using component scaling

- Some people may not benefit from increased density

Component scaling

- Components can adapt and change dimensions to help people scan, view, or compare different amounts of information

- Don't apply component scaling by default if it would result in a target below 48x48 CSS pixels

Information density and component scaling can be used together to provide more information and additional user control

## Information density

Information density refers to the amount of content (such as text, images, or videos) in a given space.

A layout’s spacing dimensions, including margins, spacers, and padding, can change to increase or decrease its information density. High density layouts are useful when people need to scan, view, or compare a lot of information, such as in a data table. Increasing the layout density of lists, tables, and long forms makes more content available on-screen.

Consider density settings in the context of a device. Although a person may prefer a denser layout for desktop, they may not for mobile. Density shouldn’t automatically change across breakpoints or orientation unless a person changes it.

[image: 2 layouts: 1 with low density and 1 with high density.]

Consider using higher density information design when people need to scan lots of information

[image: News website on desktop displaying a high information density. ]

Consider the amount and priority of information on-screen. Higher density can be useful for data-rich products where people expect to scan lots of information quickly. Examples: News, financial portals, dashboards

[image: News website on desktop displaying a low information density.]

Lower density can be better for sites prioritizing aesthetics, a focused message, less information, or easier navigation

## Component scaling

The component density scale controls the internal spacing of individual components.

The density scale is numbered, starting at 0 for a component’s default density. The scale moves to negative numbers (-1, -2, -3) as space decreases, creating higher density.

Higher density is typically applied by decreasing the top and bottom padding or overall height by 4dp.

[image: 3 buttons with densities  of 0, -1, -2.]

Apply component density based on the needs and layout of a design

Center the grouped element within the component container.

Text size shouldn’t change as the container size scales.

[image: Text field showing 20dp between label and input]

The measurement between the label and input is 20dp

[image: Parent container showing label above input.]

The label and input are centered within their parent container

[image: Dropdown menu with high density items and selectable space height of 38dp.]

Don’t increase density in UIs that involve focused tasks, such as selecting from a menu. It reduces usability by limiting selectable space.

[image: Single-line snackbar with high density.]

Don't increase the density in components that alert a person of changes, such as snackbars or dialogs

### Avoid applying component scaling by default

People should be able to opt in to dense layouts and components.

To ensure density settings can be easily reverted, settings interactions must use default target sizes (48x48 CSS pixels).

Don't scale layouts below 48x48dp by default.

People can opt in to dense layouts in settings

## Targets

Dense components can be less accessible because interactive elements are smaller, so use caution when increasing information density.

[image: Selectable target of only 40dp.]

Use caution when applying component scaling where selectable targets will be reduced to less than 48x48dp. Only apply density where it provides a better experience.

Use caution when applying density to interaction targets. Accessible targets should retain a minimum of 48x48dp, even if the visual element, such as an icon, is smaller.

[image: Settings button icon is 24x24dp, but has interaction target of 48x48dp.]

The target should remain 48x48dp, even if the icon is smaller

[image: Button with height of 36dp and interaction target of 48dp.]

The interaction target of a common button can be larger, as long as it meets the 48x48dp minimum size

## Pixel density

Pixel density is the number of pixels per inch. High-density screens have more pixels per inch than low-density ones. Elements with the same pixel dimensions appear larger on low-density screens and smaller on high-density screens.

To calculate pixel density:

Pixel density = Screen width (or height) in pixels / Screen width (or height) in inches

[image: Magnified UI element  showing a high number of pixels in the focus area.]

High-density elements have more pixels per inch

[image: Magnified UI element  showing a low number of pixels in the focus area.]

Low-density elements have fewer pixels per inch

### Density-independent pixels

Density-independent pixels, written as dp, are flexible units that scale to have uniform dimensions on any screen. They provide a flexible way to accommodate a design across devices. The Material design system uses density-independent pixels to display elements consistently on screens with different densities.

A dp is equal to one physical pixel on a screen with a density of 160.

To calculate dp: dp = (width in pixels * 160) / screen density

[image: Screen with grid representing a low number of pixels.]

Low-density screen displayed with density independence

[image: Screen with grid representing a high number of pixels.]

High-density screen displayed with density independence

| Screen physical width | Screen density | Screen width in pixels | Screen width in dps |

|---|---|---|---|

| 1.5 in | 120 | 180 px | 240dp |

| 1.5 in | 160 | 240 px |

| 1.5 in | 240 | 360 px |
