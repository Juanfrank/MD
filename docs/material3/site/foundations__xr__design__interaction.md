<!-- source: https://m3.material.io/foundations/xr/design/interaction -->
# Design – Material Design 3

# Design for immersive XR

XR interactions should be flexible, comfortable, and intuitive. People expect to interact with digital objects just like they do with physical ones.

A person should be able to switch between hands, eyes, voice, or controllers depending on their posture and preference

## Natural interactions

Natural interactions like gestures allow people to navigate, select, and move content using their hands. Gestures should be:

- Easy to learn

- Follow familiar patterns, such as press, pinch, and swipe on mobile

- Comfortable to use repeatedly

Support one-handed interactions for essential actions. Don’t require large, repetitive arm movements, as they can cause fatigue.

More on Android XR gestures

A person can select items by pinching with the index finger and thumb

### System navigation

People should be able to open a navigation menu anywhere, anytime.

On Android XR, the system-level navigation menu includes:

- Go back: Operates the same as the back gesture on Android phones

- Launcher: Goes to the home screen

- Recents: People can open, close, and switch apps

A navigation menu should always be available using a simple gesture, so people don’t get lost

## Multimodal inputs

XR apps should support flexible, multimodal inputs, such as hand and eye tracking, voice, keyboard and mouse, and controllers.

More on Android XR multimodal inputs

### Hand & eye tracking

Tracking allows people to interact with the virtual world without a controller.

Hand tracking

- Direct: People can touch, grab, or push virtual objects in arm's reach

- Ray-based: A ray, like a laser pointer, extends from the hand to target distant items, then a pinch selects it

Eye tracking

- Enables gaze and dwell interactions

- Looking at an object triggers a hover state

Distant elements can be moved using hand and eye tracking

### Voice, keyboard, mouse, & controller inputs

XR apps should also support voice and physical inputs including:

- Voice for hands-free text entry on virtual keyboards

- Voice commands for common actions like Open Settings or Go back

- Mouse & keyboard inputs for precision and text-heavy workflows

- Six degrees of freedom (6DoF) controllers for gaming or complex 3D manipulation

## Motion

In XR, motion sickness can happen when visual cues disconnect from the inner ear's sense of balance.

To keep people comfortable:

- Use standard easing and long duration motion tokens

- Maintain a stable horizon line

- Limit continuous motion. To switch locations, use teleportation or instant jump instead.

- Use tunnel vision or vignetting to reduce the field of view while in motion

Limit use of continuous motion. If required, keep the horizon line stable.

## Feedback

Since virtual objects lack physical resistance, use visual, audio, and sensory feedback to confirm interactions.

### Visual cues

Use hover icons, focus indicators, ripples, text labels, and elevation changes to show an object’s interaction state.

To indicate an item is targeted, use spatial elevation or a highlight state.

Use visual clues to show when a spatial element is hovered, focused, or selected

### Spatial audio

Sound emitters can be positioned in 3D space and provide audio confirmation of an action. For example, add a click sound when a button is pressed.

Spatial audio can help signify where a person should look or that an action was taken

### Haptics

For controllers, allow people to turn vibration on or off to simulate the feel of touching or grabbing an object.
