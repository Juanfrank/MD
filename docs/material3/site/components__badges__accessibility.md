<!-- source: https://m3.material.io/components/badges/accessibility -->
# Badge – Material Design 3

# Badges

## Use cases

People should be able to use assistive technology to:

- Understand the dynamic information conveyed in badges, such as counts or labels

- Address badge announcements by selecting corresponding navigation destinations

## Interaction & style

Badges are most commonly used within other components, such as navigation bar, navigation rail, app bars, and tabs. When a badge is used to indicate an unread notification, the badge gets hidden once it's selected.

## Visual indicators

Badges use a color intended to stand out against labels, icons, and navigation elements. Use the default color mapping to avoid color conflict issues.

[image: Diagram of large and small badges showing that they need to pass 3 to 1 contrast.]

Badges must use default color with at least 3:1 contrast

[image: Diagram of large and small badges not passing 3 to 1 contrast.]

Avoid using custom color roles for the badge container and label text. If custom roles are necessary, make sure they have contrast of at least 3:1.

## Labeling elements

The accessibility label for a badge item will be read after its navigation destination. Any numerical badges will have their number read, while non-counting badges will simply announce New notification.

[image: Navigation bar highlighting numerical badge.]

Numerical badges will have their number read

[image: Navigation bar highlighting non-counting badge.]

Non-counting badges will simply announce New notification
