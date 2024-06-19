---
author: Bosco Ho
date: 2024-06-19
title: Text Variant Preference View Modifier in SwiftUI
description: Simplify code for displaying text variants of formatted text in SwiftUI.
image: /
---

# Text Variant Preference in SwiftUI

#wwdc2024 #swiftui

> 💡 TL;DR: Use the `.textVariant(.sizeDependent)` view modifier to automatically format and fit text inside `Text` view’s size.

I stumbled upon this cute new SwiftUI view modifier called `.textVariant(...)` while looking for a way to scale font size to fit inside any `Text` view (I’m not sure which WWDC 2024 session this new API was discussed in). This new `Text` view modifier makes rendering text that can be formatted in various variants easier (think short or long dates, for example), without needing to use conditional views or `ViewThatFits`.

___

### Use Case

Imagine a `Text` view that displays the date on which some record was updated.  We can achieve this in a few ways in SwiftUI:

```swift
Text(Date.distantPast, style: .date)
Text(Date.distantPast, format: .dateTime)
/// e.g. DateFormatter where dateStyle = .full
Text(Date.distantPast, formatter: Self.dateFormatter)
```

This code resolves to the following views:

![Screenshot 2024-06-18 at 6.55.32 PM.png](/blog/Screenshot_2024-06-18_at_6.55.32_PM.png)

However, this could be an issue if the `Text` view’s width is forced to shrink to accommodate other content, and is constrained to a line limit of 1. 

![Screenshot 2024-06-18 at 6.59.23 PM.png](/blog/Screenshot_2024-06-18_at_6.59.23_PM.png)

Previously, we would have to have to either use `ViewThatFits` or use conditional views to ensure that our date text never displays as truncated text.

```swift
ViewThatFits {
	Text(Date.distantPast, formatter: Self.fullDateFormatter)
	Text(Date.distantPast, formatter: Self.longDateFormatter)
	Text(Date.distantPast, formatter: Self.mediumDateFormatter)
	Text(Date.distantPast, formatter: Self.shortDateFormatter)
}
.lineLimit(1)
```

Now, new in iOS 18 (and all other platforms), we can achieve this with a simple call to `.textVariant(.sizeDependent)`.

```swift
Text(Date.distantPast, format: .dateTime)
	.textVariant(.sizeDependent)
	.lineLimit(1)
```

In fact, the text variant view modifier appears to generate even shorter text variants than what `DateFormatter` offers, as seen in this screenshot here (the last two variants aren’t available via `DateFormatter` out of the box).

![Screenshot 2024-06-19 at 1.08.27 AM.png](/blog/Screenshot_2024-06-19_at_1.08.27_AM.png)

While this means we can write less code to avoid truncating formatted text, it’s worth noting that this new text variant modifier differs from `ViewThatFits` ”both in usage and behavior” ([see discussion here](https://developer.apple.com/documentation/swiftui/textvariantpreference/sizedependent#Difference-to-doccomappleSwiftUIdocumentationSwiftUIViewThatFits) in Apple’s documentation). 

What’s great is this new API works on all Apple devices, including visionOS and macOS, and works with other formatted text, including the new `.stopwatch(...)` format style in iOS 18 ([see here)](https://developer.apple.com/documentation/swiftui/systemformatstyle/stopwatch).

___

### References
See here for a full working example: https://gist.github.com/boscojwho/a21ede6943a435ea600fd51cab2f24fb

[https://developer.apple.com/documentation/swiftui/text/textvariant(_:)](https://developer.apple.com/documentation/swiftui/text/textvariant(_:))

[https://developer.apple.com/documentation/swiftui/textvariantpreference](https://developer.apple.com/documentation/swiftui/textvariantpreference)