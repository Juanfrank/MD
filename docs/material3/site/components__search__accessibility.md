<!-- source: https://m3.material.io/components/search/accessibility -->
# Search – Material Design 3

# Search

## Use cases

People should be able to use assistive technology to:

- Navigate to and focus on a search bar

- View the hinted search text or persistent label

- Input text and complete a search

- Interact with a list of search suggestions and results

- Clear the input text

## Interaction & style

### Autosuggest

When search suggestions and results appear, the screen reader must announce the change. This lets people know list items are available for selection.

[image: Hinted search text and autocomplete results on a mobile screen.]

Autocomplete results should be announced by the screen reader

## Initial focus

Initial focus lands on the first interactive element. This is often a leading icon button or text field. A leading icon button usually activates search directly or opens a navigation component.

[image: Search bar with a focused leading icon. ]

Initial focus can land on a leading icon

[image: Search bar with no leading icon. The text field is focused.]

If there’s no leading icon, focus lands on the text field

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab or Shift + Tab | Navigate between interactive elements |

| Space or Enter | Activate the search text field for input |

| Arrows | Navigate between search result items |

## Labeling elements

The hinted search text should be used as the accessibility label describing the search bar. The role for the input field should be:

- Android: Text field

- iOS: Search field

[image: Search bar with “Label: Search messages” and “Role: Text field”.]

The accessibility label should match the hinted search text

Leading and trailing icon buttons should be labeled according to their accessibility guidance.

[image: A search bar with accessibility labels for its leading icon button and trailing avatar.]

Use icon labels for icon buttons

Search suggestions and results use the list component. Screen readers automatically announce the results as a list. For accessibility labels, follow the list accessibility guidelines.

[image: A search bar on mobile, showing search results in a list.]

Search suggestions and results are created using lists
