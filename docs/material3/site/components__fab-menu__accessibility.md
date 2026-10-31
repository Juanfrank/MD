<!-- source: https://m3.material.io/components/fab-menu/accessibility -->
# FAB menu - Material Design 3

# FAB menu

## Use cases

People should be able to do the following using assistive technology:

- Navigate and interact with the FAB menu

- Ensure focus is correct when navigating through the menu

## Interaction & style

FAB menu elements meet the minimum target size of 48dp.

[image: FAB menu measurement annotations. All elements are larger than the minimum target size.]

FAB menus have 48x48dp minimum width and sufficient spacing by default

When the FAB menu can scroll, make sure the items scroll behind the close button.

The close button should always be easy to access and unobstructed.

[image: FAB menu items are scrolling behind the close button.]

Allow the menu items to scroll behind the close button

[image: FAB menu items are scrolling in front of the close button.]

Don’t obstruct the close button in short screens like horizontal orientation

## Initial focus

When the FAB is selected, the FAB menu opens, and initial focus remains on the close button, which takes the place of the original FAB.

Then the focus moves from the top menu item to the bottom.

[image: 4 FAB menus with the focus order labelled. Focus moves from the close button at the bottom to the topmost menu item next.]

Focus lands on the close button. People can then navigate through all the items.

- Close button

- First menu item

- Second menu item

- Third menu item

## Keyboard navigation

| Keys | Actions |

|---|---|

| Tab | Navigate to the next interactive element |

| Space or Enter | Activate the focused button or item |

## Labeling elements

### Android

On Android, a FAB menu’s close button should include a state to tell screen readers what action will occur when it's toggled. The close button should be labeled:

- Label: Toggle menu

- Role: Button

- State: Expanded or collapsed

[image: Accessibility labels for the close button on an Android device.]

On Android, the close button accessibility labels should include a toggle menu label, button role, and an expanded or collapsed state

FAB menu items should be labeled:

- Label: Match the item’s UI text, such as Reply all

- Role: Button

[image: Accessibility labels for a FAB menu item on an Android device.]

Label FAB menu items to match their UI text, like Reply all, and use the button role

### Web

On web, a FAB menu is a combination of a FAB and a menu component. The FAB opens the menu. Follow the accessibility guidelines for FABs and menus.

The FAB's accessibility label should describe the menu that the FAB will open.
