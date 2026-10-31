<!-- source: https://m3.material.io/blog/jetpack-compose-beta -->
# Jetpack Compose: Now in Beta - Material Design

# Jetpack Compose: Now in Beta

Posted by

Today marks the first beta release of Jetpack Compose, Android’s modern, declarative toolkit designed to simplify and accelerate UI development. With Jetpack Compose, you can quickly bring your apps to life with less code, powerful tools, intuitive Kotlin APIs, and built-in support for Material Design, dark theme, animations, and more.

## Compose Material

Jetpack Compose offers an implementation of Material Design and provides all the components you need to create beautiful apps, following the guidance described at material.io.

## Material Theming

Jetpack Compose implements Material Theming and supports dark theme by default. You can customize color, typography, and shape theming values to fit your product's brand, and get access to convenient functions for working with system dark theme (like isSystemInDarkTheme, lightColors, and darkColors).

When creating new screens in Compose, you should ensure that you apply your custom MaterialTheme before any UI-emitting Material composables. The Material components (Button, Checkbox, BottomNavigation, etc.) depend on a MaterialTheme being in place and their behavior is undefined without it.

Check out the Theming in Compose guide for more information, and try the Jetpack Compose Theming codelab.

## Material Components

Jetpack Compose offers implementations of Material Components. See the table below for composables available in the beta release, or check out the full list in the API reference.

| App bars: bottom | BottomAppBar |

|---|---|

| App bars: top | TopAppBar |

| Backdrop | Backdrop |

| Banners | Not available yet |

| Bottom navigation | BottomNavigation |

| Buttons | Button OutlinedButton TextButton |

| Buttons: floating action button | FloatingActionButton ExtendedFloatingActionButton |

| Cards | Card |

| Checkboxes | Checkbox TriStateCheckbox |

| Chips | Not available yet |

| Data tables | Not available yet |

| Date pickers | Not available yet |

| Dialogs | AlertDialog |

| Dividers | Divider |

| Image lists | Not available yet |

| Lists | ListItem |

| Menus | DropdownMenu DropdownMenuItem |

| Navigation drawer | ModalDrawerLayout BottomDrawerLayout |

| Navigation rail | Not available yet |

| Progress indicators | CircularProgressIndicator LinearProgressIndicator |

| Radio buttons | RadioButton |

| Sheets: bottom | BottomSheetScaffold ModalBottomSheetLayout |

| Sheets: side | Not available yet |

| Sliders | Slider |

| Snackbars | Snackbar Scaffold |

| Switches | Switch |

| Tabs | Tab TabRow ScrollableTabRow |

| Text fields | TextField OutlinedTextField |

| Time pickers | Not available yet |

| Tooltips | Not available yet |

These components can be combined—using layouts and composables like Scaffold—as the building blocks for beautiful UIs.

Check out the Layouts in Compose guide for more information.

## Dark theme

Material composables that make use of a Surface (like Card, TopAppBar, etc.) automatically include dark theme properties like desaturated colors for accessibility, elevation overlays, and limited color accents. You can also incorporate these in custom scenarios.

## Material Icons

Jetpack Compose also provides a convenient means of using icons listed in the Material Icons tool, including all icon styles—filled, outlined, rounded, two-tone, and sharp. With this artifact, you can use icons directly, without the need to download SVGs and convert them to VectorDrawables in Android Studio.

## Interoperability

Jetpack Compose is designed to work with Android Views. If you're building a new app, the best option might be to implement your entire UI with Compose. But if you're modifying an existing app, you might not want to migrate your app straight away. Instead, you can combine Compose with your existing UI design and adopt it at your own pace.

If you’re using Material Components for Android in your app—in particular Material Theming—the MDC-Android Compose Theme Adapter library allows you to easily re-use the color, typography and shape definitions from your existing XML themes, from within your composables, so you don’t need to declare them again and have a single source of truth.

If you’re using AppCompat, you can access similar functionality by using the AppCompatTheme composable from the AppCompat Compose Theme Adapter library.

Check out the Compose interoperability guide for more information.

## Resources

With Jetpack Compose reaching beta, it’s a great time to start learning all about it and get ready to adopt it in your apps. Check out the resources below to get started.

- Develop knowledge and skills at your own pace with the Jetpack Compose Pathway, through sequential learning experiences that include articles, codelabs, quizzes, and videos.

- Visit the Jetpack Compose Samples GitHub repository, where you’ll find a variety of up-to-date samples including Material Studies like Owl, Crane, and Rally.

- Get setup using the Android Studio with Jetpack Compose guide.

- View the Converting an existing app screen to Jetpack Compose video on the Material Design YouTube channel.

- Join the Compose community on StackOverflow and the Kotlin Slack group.

- Report an issue and track bugs on the bug tracker.
