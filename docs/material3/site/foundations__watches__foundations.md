<!-- source: https://m3.material.io/foundations/watches/foundations -->
# Watches – Material Design 3

# Design for watches

## Resources

| Type | Resource |

|---|---|

| Design | Get Started with M3 Expressive |

| UI Design for Wear OS |

| Figma Design Kits for Wear OS |

| Implementation | Android Developers: Wear OS |

| Jetpack Compose for Wear OS |

## Anatomy

### The watch face

Watch faces display the time, as well as other information and can provide access to other functions through apps and tiles. They can also include complications, self-contained details that can show contextual info like heart rate or progress. Ongoing activities on the watch face show in-progress actions, like a stopwatch countdown or a workout timer.

[image: A watch face with hands showing analog time readout, and complications showing the date in a calendar, heart rate, water consumption, and weather.]

Complications are details on the watch face that can be customized for style or function

[image: A watch face with an entry point for an ongoing exercise activity.]

1. Ongoing activities, like timers, media players, or workouts, can be accessed from the watch face

### Physical buttons

Wearable devices can have a variety input surfaces, which include physical buttons and controls.

[image: 3 watch faces with indications showing the locations of a rotating side button, system button, and multifuction button.]

- Rotating side buttons: Used for volume control, or to scroll through options or lists

- System buttons: Dedicated to OS functions like powering on and off, and cannot be customized

- Multifunction buttons: Used by apps for custom actions like starting and stopping a stopwatch

## Design principles

- Tailor layouts for different screen sizes with adaptive design

- Design for short interactions to conserve battery

- Focus on one or two tasks at a time rather than a full app experience

- Test designs in situations that involve movement to make sure the design is usable at a glance

[image: Calendar screen with date, time of dentist appointment, and more button.]

At-a-glance views allow people to quickly see calendar events

[image: 3 columns with times, dates, and appointment names cut off.]

Don't create complex and detailed apps such as a calendar grid

### Always relevant

Watches are always with people. Consider how to update app content based on context, such as time, place, and activity.

[image: A map search for a garden’s location on a watch and on a phone.]

Navigation on a watch complements the experience on a phone

### Works offline

Design for slow connections and offline use, such as exercising and commuting.

[image: 2 watches: 1 with offline music downloads list. 1 with a dialog about no internet connection with dismiss and accept buttons.]

The network state can be communicated through:

- An offline icon

- A dialog

## Interaction patterns

### Cross-device experiences

Watches are often dependent on connected phones for functionality or complex interactions. In some cases, a watch and a phone are used together to accomplish different parts of the same task.

Consider how experiences can be consistent and complement the strengths of each device.

More on multidevice development for Android

[image: A contact entry shown on a phone and a watch, with options to call or message.]

Consider which actions are appropriate for each device

### Always on displays

Watches can have always on displays, which allow ambient content to be shown when the watch isn’t in use.

This are especially helpful for ongoing experiences like a timer or a workout that should remain in view. Because they remain on the screen for long time periods, consider limiting the number of pixels that are illuminated.

More on always-on apps and system ambient mode in Wear OS

[image: A watch face showing progress through a task and the current time.]

Limit the number of illuminated pixels for a display that's always on
