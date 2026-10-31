<!-- source: https://m3.material.io/components/button-groups/accessibility -->
# Button groups

# Button groups

## Use cases

People should be able to do the following with assistive technology:

- Navigate to and interact with each button in the group

- Identify when buttons are selected

## Interaction & style

Each button in a group should have a minimum 48x48dp target. Extra small and small button groups have larger inner padding to ensure accessible targets. Avoid reducing the padding in these sizes.

[image: Extra small and small button groups with 48x48dp target areas annotated over top. The area is larger than the buttons.]

- Extra small button group

- Small button group

### Initial focus

The button group container is not a focusable element. Initial focus should land on the first button in the group and then move to each button.

[image: Focus order lands on the first button, then the next buttons.]

Initial focus should land on the first button, not on the container

Use Tab to navigate to a button group, the arrow keys to navigate between each item in the group, and Space or Enter to select a focused button.

[image: Button group with annotations for navigation with Tab and selecting with Space or Enter.]

- Tab: Initial focus lands on the first button

- Arrow keys: Navigate between items

- Space or Enter: Selects a focused item

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab | Navigate between buttons |

| Arrow keys | Navigate inside the component |

| Space or Enter | Activate a focused button |

## Labeling elements

The button group container doesn't need to be labeled. Label each button according to the button and icon button accessibility guidance.

[image: In a messaging products, an email icon is labelled “email” with the role “button”.]

Label each button within the button group
