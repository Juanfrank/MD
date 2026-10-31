<!-- source: https://m3.material.io/foundations/xr/design/accessibility -->
# Design – Material Design 3

# Design for immersive XR

## Use cases

XR presents unique physical constraints. Designing accessible XR products means accounting for different bodies, postures, and sensory abilities.

People should be able to do the following with assistive technology:

- Navigate and interact with spatial content using their preferred input method

- Understand the spatial environment and select interactive elements

- Customize the experience to fit their physical posture and comfort

More on Android XR accessibility

## System-level accessibility

Android XR adapts familiar Android assistive technologies for spatial environments.

To ensure an inclusive experience, design XR apps to work with system-level features like Google's TalkBack screen reader, voice to text, live captions, dwell control, magnification, and color inversion and correction.

Android XR app quality guidelines

## Text accessibility & color contrast

Make sure text and UI are legible in different lighting conditions and environments. For example, in passthrough, the background might be a bright window or a dark room.

- Use a minimum 14dp body font size

- Ensure high contrast between text and background

- Use standard background color roles like surface container, rather than custom colors, so they dim automatically

- Support light and dark themes

Use color roles to dim backgrounds automatically

## Physical accessibility

To support different mobility levels, provide flexible input methods and positions:

- Actions should be achievable with one hand, voice, or eye control

- Don’t require two-handed gestures

- Design for seated, standing, and reclined positions

- Allow people to recenter and pull UI closer to them

Offer adjustable input methods and viewing positions

## Target size

Use large target sizes to make XR interactions precise and accessible. Interactive elements should have:

- 56x56dp or larger target

- 48x48dp or larger visual affordance

- 4dp offset

Don’t overlap targets of different elements.

Targets and icons should scale with their parent container or label text.

[image: A gear icon with a 56dp target size and 4dp offset.]

Use 56dp or larger target sizes for interactive elements
