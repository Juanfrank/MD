<!-- source: https://m3.material.io/components/search/specs -->
# Search – Material Design 3

# Search

## Variants

When a person executes a search, results appear in a list below the search bar

| Variant | M3 | M3 Expressive |

|---|---|---|

| Search | Available | Available |

## Configurations

### Style

Search comes in two styles:

- Contained: Has an expressive look and feel. It uses a filled container to separate a search bar from a list of suggestions or results

- Divided ( baseline): Doesn’t have the latest visual style, motion, or flexibility

[image: An email inbox search bar in a contained style.]

The contained style has a persistent, filled container, expressive motion, and rounded shape

[image: An email inbox search bar in a divided style.]

The divided (baseline) style uses a divider to separate the search bar from suggestions and results

### Layout

Search suggestions and results appear in customizable lists, with two layout options: full-screen and docked. More on search layouts

[image: Full-screen search results with a search bar in the contained style.]

[image: Full-screen search results with a search bar in the contained style.]

Full-screen layout in the contained style

[image: Docked search results with a search bar in the contained style.]

[image: Docked search results with a search bar in the contained style.]

Docked layout in the contained style

[image: Full-screen search results with a search bar in the divided style.]

[image: Full-screen search results with a search bar in the divided style.]

Full-screen layout in the divided style

[image: Docked search results with a search bar in the divided style.]

[image: Docked search results with a search bar in the divided style.]

Docked layout in the divided style

| Category | Configuration | M3 | M3 Expressive |

|---|---|---|---|

| Style | Contained | -- | Available |

|  | Divided | Available | Not recommended. Use contained. |

| Layout | Docked, full-screen | Available | Available |

## Tokens & specs

Use the table's menu to select a token set. The search bar set only contains tokens for the unfocused search bar. The search view set contains all other tokens when interacting with search, including all styles and layouts. Learn more about design tokens

## Anatomy

Search includes a search bar and a container for suggestions and results. The container is empty by default. Use the list component to add content. In the divided (baseline) style, a divider separates the search bar and results.

[image: 6 elements of search.]

- Search bar container

- Leading icon

- Supporting text

- Trailing icon and avatar (optional)

- Input text

- Container for search suggestions or results

### Examples

- With avatar

- With one trailing icon button

- With two trailing icon buttons

- With trailing icon button and avatar

[image: 4 search bars with different trailing elements.]

## Color

Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.

### Full-screen layout

[image: 6 full-screen search color roles in light and dark themes.]

Full-screen search color roles used in light and dark themes:

- Surface container low

- On surface variant

- On surface variant

- Surface container high

- On surface variant

- On surface

### Docked layout

[image: 6 docked search color roles in light and dark themes.]

Docked search color roles used in light and dark themes:

- Surface container high

- On surface variant

- On surface variant

- Surface container high

- On surface variant

- On surface

## States

States are visual representations used to communicate the status of a component or an interactive element. In focused search, individual elements maintain their own interaction states. Learn more about interaction states

### Search bar

[image: 4 search bar states in light and dark mode.]

- Enabled

- Hovered

- Focused

- Pressed (ripple)

### Search suggestions & results

Search includes a container for suggestions and results. The container is empty by default. Use the list component to add content.

[image: 4 search result states in light and dark mode.]

- Enabled

- Hovered

- Focused

- Pressed (ripple)

## Measurements

### Search bar

[image: Search bar with leading and trailing icon size and padding measurements.]

Unfocused search bar with leading and trailing icon measurements

[image: Search bar with trailing avatar size and padding measurements.]

Unfocused search bar with avatar measurements

In M3 Expressive, the search bar expands when focused. The margins change from 24dp to 12dp.

[image: Unfocused search bar margins of 24dp.]

Unfocused search bar margin measurements

[image: Focused search bar margins of 12dp.]

Focused search bar margin measurements

| Element | Attribute | Value |

|---|---|---|

| Container | Width | Min: 360dp, max: 720dp |

| Height | 56dp |

| Label alignment | Start-aligned |

| Leading padding | Unfocused: 24dp, focused: 12dp |

| Trailing padding | Unfocused: 24dp, focused: 12dp |

| Leading icon and label padding (from tap target) | 4dp |

| Label and trailing icon padding (from tap target) | 4dp |

| Avatar | Size | 30dp |

### Focused search

#### Contained style

[image: Full-screen layout size and padding measurements in contained style.]

Full-screen search padding and size measurements for contained style

[image: Docked layout size and padding measurements in contained style.]

Docked search padding and size measurements for contained style

| Element | Attribute | Value |

|---|---|---|

| Full-screen container | Width | Full width |

| Height | Full height |

| Docked container | Width | Min: 360dp, max: 720dp |

| Height | Min: 240dp, max: 2/3 of screen height |

| Search bar container | Height | 56dp |

| Label alignment | Start-aligned |

| Leading padding | 16dp |

| Trailing padding | 16dp |

| Leading icon and label padding (from tap target) | 4dp |

| Leading icon and label padding (from tap target) | 4dp |

#### Divided style

[image: Full-screen layout size and padding measurements in divided style.]

Full-screen search padding and size measurements for divided style

[image: Docked layout size and padding measurements in divided style.]

Docked search padding and size measurements for divided style
