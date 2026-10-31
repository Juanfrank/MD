<!-- source: https://m3.material.io/components/progress-indicators/accessibility -->
# Progress indicators – Material Design 3

# Progress indicators

## Use cases

People should be able to do the following using the assistive technology:

- Navigate to the progress indicator

- Understand what progress the indicator is communicating

## Interaction & style

The active indicator, which displays progress, provides visual contrast of at least 3:1 against most background colors.

[image: Dark line of progress indicator stands out against the lighter colored track.]

The progress indicator and stop indicator provide visual contrast of at least 3:1 against most background colors

When integrated into another component, such as a button, make sure that the active indicator provides visual contrast of at least 3:1 against the other component.

For the active indicator, use the same color as the label text or icon. The track should be removed.

[image: Circular indicator on button passes 3 to 1 contrast test.]

Ensure the indicator’s color provides at least 3:1 contrast against the surface it's on

[image: Circular indicator on button fails 3 to 1 contrast test.]

Avoid using a color below 3:1 contrast

For linear progress indicators, the stop indicator is required if the track has a contrast below 3:1 with its container or the surface behind the container.

Essentially, the end of the track must be easy to identify.

[image: Bright container holding the progress bar is on a dark surface, passing the 3:1 color contrast.]

Only remove the stop indicator when the linear progress indicator has at least a 3:1 color contrast with surrounding containers and surfaces

[image: Bright container holding progress indicator is on a bright surface, failing the 3:1 color contrast.]

Avoid removing the stop indicator if any adjacent containers or surfaces are below the 3:1 color contrast

## Labeling elements

Since the progress indicator is a visual cue, it needs an accessibility label to describe the kind and amount of progress made.

Use the progress bar accessibility role, and write an accessibility label that describes the purpose of the progress indicator. The label should include the process, such as "loading,” and the affected content, such as a page, article, or episode. For example: "Loading news article" or "Refreshing page."

[image: Determinate linear progress indicator has an accessibility label of “loading news article” and role of “progressbar”.]

Progress indicator labels should explain which items are loading

[image: Indeterminate linear progress indicator has an accessibility label of “loading my episodes” and role of “progressbar.”]

A label on an intedeterminate progress indicator on a screen which is loading a set of podcast episodes
