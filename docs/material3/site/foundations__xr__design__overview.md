<!-- source: https://m3.material.io/foundations/xr/design/overview -->
# Design – Material Design 3

# Design for immersive XR

- Use depth and expanded space to create believable environments

- Map interactions, like gaze and gestures, to real-world expectations

- Group UI elements on floating spatial panels

- Design for comfort to minimize motion sickness and physical strain

- Provide feedback through spatial audio, haptics, and visual cues

In home space, an XR app can run side by side with other apps, with the real world in the background. In full space, the XR app takes center stage with immersive, spatial capabilities.

## Resources & availability

| Type | Resource | Status |

|---|---|---|

| Design | M3 Design Kit (Figma) | Available |

|  | Android XR immersive design guidelines | Available |

|  | Design for AI glasses | Available |

| Implementation | Build for Android XR | Available |

|  | Jetpack XR SDK | Available |

|  | Material Design for XR API reference | Available |

## Principles

### Use familiar patterns

Material components like buttons and menus help people navigate spatial apps with confidence.

[image: A button opens to show a 3D Material menu.]

In XR, a Material menu uses elevation to appear in 3D

### Prioritize comfort

Place content in the center of a person’s field of view, and design for different body positions, such as seated, standing, and reclined.

[image: A person sitting in a chair in an immersive XR environment, with lines marking their field of view.]

Positioning content in a person’s field of view keeps the UI visible and minimizes the need for excessive head or body movement

### Embrace depth

Use elevation and 3D models to add volume, create a sense of realism, and spatial understanding.

[image: A person stands in front of an XR app with 3 curved panels and a 3D shark.]

3D models can be viewed from all angles and moved with natural interactions

### Design for accessibility

Design apps to work with system-level assistive technologies like screen readers, voice commands, and text resizing. Provide large target sizes, support multimodal inputs, and ensure text is legible against any background.

[image: 1 XR settings icon button with labeled target size and offset. 1 microphone icon button with a visible cursor.]

In XR, icon buttons should have a 56dp target size and 4dp offset

## Material XR components

The following Material components are adapted for XR:

- App bars

- Dialogs

- Navigation bar

- Navigation rail

- Toolbars

A toolbar’s behavior and placement changes from a 2D to a 3D experience

## XR terms

- 3D models: Digital objects rendered with depth and volume

- Field of view: The area a person can see without turning their head

- Full space: Android XR’s immersive mode that supports spatial components

- Home space: Compatible with mobile and large screen apps, but doesn’t support spatial components

- Orbiters: Floating elements that control the content within spatial panels, full space only

- Passthrough: A blended reality where an XR device displays multiple large apps and the user’s physical environment

- Spatial elevation: Displays a component above an app on the Z-axis

- Spatial environments: The 360° 3D virtual worlds people see in an immersive app

- Spatial panels: A container for UI elements, interactive components, and immersive content, full space only
