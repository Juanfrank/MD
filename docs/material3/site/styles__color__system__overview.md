<!-- source: https://m3.material.io/styles/color/system/overview -->
# Color - Material Design 3 - Create personal color schemes

# Color system

The Material color system includes:

- Built-in set of accessible color relationships

- 26+ color roles mapped to Material Components

- Built-in dark theme colors

- Static baseline color scheme with default colors assigned to each color role

- Dynamic color features including user-generated and content-based color

Learn how the system works

Learn about the value and function of Material 3’s dynamic color system and how it differs from past color systems

View transcript

[image: Primary, on primary, primary container, and on primary container roles shown in baseline light theme color scheme.]

The baseline color scheme doesn't dynamically change

[image: Diagram showing an input color resulting in a simplified illustration of four roles of a color scheme. Shown in green and yellow in light theme.]

A dynamic color scheme changes the UI's colors based on different inputs, like a wallpaper

[image: Diagram showing an orange input color generating a static orange color scheme for an auto heating UI element.]

Specific colors, such as semantic colors, can be set to not dynamically change

Products with dynamic color can automatically generate and assign colors to each element in the UI.

This provides:

- Personalized UI

- Accessible contrast

- User-controlled contrast

- Automatic dark theme

The UI colors change dynamically

## Resources

| Type | Link | Status |

|---|---|---|

| Design | Design Kit (Figma) | Available |

| Implementation | Android Views (MDC-Android) | Available |

| Jetpack Compose | Available |

| Flutter | Available |

| Tools | Material Theme Builder | Available |

## What's new

May 2025

### Three levels of contrast

Color roles support three levels of contrast so people can select the one that best suits their vision needs. Contrasts also are tokenized.

[image: Email app in standard contrast.]

Standard contrast

[image: Email app in medium contrast.]

Medium contrast

[image: Email app in high contrast.]

High contrast

August 2024

### More colorful text and icons

The following color roles are updated in light theme to be more colorful while still having accessible color contrast:

- On primary container

- On secondary container

- On tertiary container

- On error container

Affected components:

- Badges

- Buttons Buttons Extended FAB FAB Icon buttons Segmented buttons

- Chips

- Lists

- Menus

- Navigation bar

- Navigation drawer

- Navigation rail

- Switches

- Toolbars

[image: Comparison of the color before and after the update, with FAB and button examples.]

Colors used for text and icons now appear more colorful

Oct 2023

### Reorganized guidelines

Same color system, explained in a new way. Updated sections include:

- How the system works

- Advanced customizations

- Color resources

[image: Diagram illustrating guidelines being reorganized]

The guidelines have been reorganized and updated

Feb 2023

### Tone-based surface colors

Tone-based surface color roles have replaced the previous approach of surfaces at +1 to +5 elevation. The new color roles are not tied to elevation and offer more flexibility and support for color features, such as user-controlled contrast.

[image: Simplified tablet UI showcasing the application of surface roles, shown in light theme]

New tone-based surface colors offer more flexibility and support

Technical changes were made to align the color system with Android SysUI:

- Updated the default light theme surface from tone 99 to tone 98

- Updated the chroma for the neutral palette, increasing it from 4 to 6

- Slightly darkened surface roles in dark theme

[image: Before and after swatch of the default light theme surface, showcasing the difference in chroma and tone]

Changes in tone and chroma in the default light theme surface

Feb 2023

### Additional accent colors

Additional accent colors in the scheme provide more flexibility and choice for color application. In particular, a new set of fixed colors for the primary, secondary, and tertiary accent groups provide colors which stay the same across light and dark themes.

[image: Fab and star icon show in fixed and fixed dim roles, in both light and dark theme]

Additional accent colors provide more choice for color application
