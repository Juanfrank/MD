<!-- source: https://m3.material.io/components/app-bars/specs -->
# Top app bar – Material Design 3

# App bars

## Variants

[image: 4 variants of app bars.]

- Search app bar

- Small

- Medium flexible

- Large flexible

### Baseline variants

The baseline M3 medium and large app bars are no longer recommended in M3 Expressive, and should be replaced with medium flexible and large flexible app bars, which are similar visually, but have multi-line support, a shorter height, and can contain a wide variety of elements, like images. Jump to baseline app bar specs

[image: 2 baseline app bar variants, medium and large.]

Baseline variants

- Medium

- Large

| Variant | M3 | M3 Expressive |

|---|---|---|

| Search app bar | -- | Available |

| Small | Available | Available |

| Center-aligned | Available | Merged into small. Use centered-text configuration. |

| Medium (baseline) | Available | Not recommended. Use medium flexible |

| Medium flexible | -- | Available |

| Large (baseline) | Available | Not recommended. Use large flexible |

| Large flexible | -- | Available |

## Configurations

### Text alignment

[image: 4 variants of app bars with different left and center aligned text headlines.]

Text labels, including supporting text, can be aligned to the leading edge or centered

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Text alignment | Leading edge (default) | Available | Available |

| Centered | -- | Available |

## Tokens & specs

Select a token set to view in the table's menu. App bar token sets are organized into a common token set, and size-specific tokens. Learn about design tokens

### Search component tokens & specs

The default search component tokens are used in the search app bar.

## Anatomy

[image: 5 elements of the component.]

- Container

- Leading button

- Trailing elements

- Headline

- Subtitle

App bars can be customized to include:

- An image or logo

- A subtitle

- A filled icon button

Avoid customizing the size of the heading and subtitle, or adding too many actions.

[image: 3 app bars: 1 with a newspaper logo, 1 with a subtitle, and 1 with a filled icon button.]

The app bar can have different layouts depending on which elements are shown

### Search

The search app bar can include trailing actions inside and outside the search bar. When the search bar is selected, it should open the search view component.

[image: 5 elements of the search app bar.]

- Container

- Leading icon button

- Hinted search text

- Trailing icon or avatar

- Search container

[image: 3 layouts of icons in the search app bar.]

- A leading element and a trailing element outside search

- A leading element, a trailing element inside search, and a trailing element outside search

- A leading element and two trailing elements outside search

### Image

An image can be placed in the app bar. In small app bars, this can replace the label text.

[image: Graphic replacing text headline content.]

Images can be added to app bars and can replace label text on small app bars

### Filled trailing icon button

The app bar's trailing icon buttons can be replaced with a single, primary, or tonal filled icon button in default or wide sizes.

[image: App bars configured with filled trailing icons.]

The trailing icons can be configured to be a single filled icon button

### Subtitle

[image: App bars configured with subtitles below their headlines.]

The medium flexible and large flexible app bars hug the text contents, so they are taller when a subtitle is visible

- Small

- Small with subtitle

- Medium flexible

- Medium flexible with subtitle

- Large flexible

- Large flexible with subtitle

## Color

Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. Learn more about design tokens

All app bars share the same color roles. On scroll, the container changes color to surface container.

[image: 4 color roles of the leading edge app bar in light and dark scheme.]

App bar color roles used for light and dark themes:

- Surface

- On surface

- On surface variant

- On surface

- On surface variant

- Surface container (on scroll)

[image: 4 color roles of the center-aligned app bar in light and dark scheme.]

Search app bar color roles used for light and dark themes:

- Surface

- On surface variant

- On surface variant

- On surface variant

- Surface container

- Surface container

- Surface container highest

### Scroll states

[image: Color roles for app bars when flat and on scroll.]

The app bar changes color when flat or on scroll. The search bar can also change color on scroll.

- Flat

- On scroll

## Measurements

### Search app bar

[image: Search app bar size and padding measurements.]

Search app bar padding and size measurements

### Small app bar

[image: Small app bar size and padding measurements.]

Small app bar padding and size measurements

### Medium flexible app bar

[image: Medium flexible app bar padding and size measurements.]

Medium flexible app bar padding and size measurements

### Large flexible app bar

[image: Large flexible app bar padding and size measurements]

Large flexible app bar padding and size measurements

## Baseline app bars

The medium and large app bars are no longer recommended in M3 Expressive. Use the medium flexible and large flexible app bars in their place.

[image: 4 elements of medium and large app bars.]

Medium and large app bars have the same elements:

- Container

- Leading button

- Trailing icons

- Headline

### Tokens & specs

Select a token set to view in the table's menu. Baseline app bar token sets are organized into medium, large, and older baseline token sets. Learn about design tokens

### Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. Learn more about design tokens

[image: 4 color roles of the medium top app bar in light and dark scheme.]

Medium top app bar color roles used for light and dark schemes:

- Surface

- On surface

- On surface

- On surface variant

### Measurements

#### Medium app bar

[image: Diagram of medium app bar padding and size measurements.]

Medium app bar padding and size measurements

#### Large app bar

[image: Diagram of large app bar padding and size measurements.]

Large app bar padding and size measurements
