---
author: Bosco Ho
date: 2024-06-14
title: Unicode + Swift - How to Transform Mandarin Pinyin Diacritic Tone Marks into IPA (Numeric) Form
description: Use-case involving speech synthesis on Apple platforms.
image: /
---

# Unicode + Swift: How to Transform Mandarin Pinyin Diacritic Tone Marks into IPA (Numeric) Form

> 💡 This is a brief note on how to convert Mandarin Pinyin diacritic tone marks into its numeric form.  While the concepts are applicable to programming languages that provide proper Unicode support, the code examples are written in Swift and geared towards a specific use-case on Apple platforms.

### Why

Unicode’s “Unihan” working group has a treasure trove of data on CJKV (Chinese/Japanese/Korean/Vietnamese) logographs, more commonly known as Han characters in the English-speaking world, Chinese characters, Hanja (Korean) or Kanji (Japanese).  The Unihan working group’s CJKV database includes Mandarin pronunciations for many CJKV logographs written in Pinyin, encoding tone marks as diacritics.

Using Apple’s `AVSpeechSynthesizer`, one would hope to be able to reproduce the pronunciations as represented in Pinyin. And indeed, Apple provides various Mandarin speech synthesizers.  

Unfortunately, Apple’s speech synthesizer appears to have trouble reproducing some Pinyin pronunciations when the tone marks are encoded as Combining Diacritical Marks. The same speech synthesizers correctly reproduce speech when the same Pinyin pronunciations are written using numeric tone marks in International Phonetic Alphabet (IPA) form.

This means we need a way to convert these diacritic tone marks into its IPA (numeric) form.


### Background on Pinyin

In China, Singapore and Taiwan, pronunciations for Mandarin can be written using a standard called **Pinyin**, which literally means “spelled sounds”.

Since Mandarin is a tonal language, Pinyin includes four tone marks (and, in some cases, an additional fifth neutral tone mark):

|  Tone   |       Diacritic       | Numeral  | Example  |       |
|:-------:|:---------------------:|:--------:|:--------:|:-----:|
|  First  |         ⟨◌̄⟩          |    1     |    mā    |  ma1  |
| Second  |         ⟨◌́⟩          |    2     |    má    |  ma2  |
|  Third  |         ⟨◌̌⟩          |    3     |    mǎ    |  ma3  |
| Fourth  |         ⟨◌̀⟩          |    4     |    mà    |  ma4  |
|         |                       |    5     |    ma    |  ma5  |
|         | before syllable ⟨·◌⟩  |    0     |   ·ma    |  ma0  |

[https://en.wikipedia.org/wiki/Pinyin#Numbers](https://en.wikipedia.org/wiki/Pinyin#Numbers)

Pinyin can be written in the following two forms:

1. Phonetic reading, followed by its tone mark in numeric form (if any).  For example, window or `chuang1`, where 1 indicates the first tone. This is the **International Phonetic Alphabet** format.
2. Phonetic reading combined with a diacritic mark above the appropriate letter.  For example window or `chuāng`.

Generally, the latter form is used in both digital and handwritten text, while the IPA form was useful before the advent of computerized input.


### Prior Art

A quick web search returns various answers on how to convert numeric Pinyin tone marks into its diacritic forms.  But there appears to be a lack of discussion on how to convert diacritic tone marks into numeric form.  That’s what we need, so we’ll look at how to achieve that below.


### Technical Discussion

In most cases, a Pinyin letter with tone mark consists of a “base” character and a single **Combining Diacritic Mark**. The major exception is when an umlaut is added to `ü` in order to distinguish it from `u`, in this case the base character is combined with two diacritic marks. There are also some rare letters that follow the same logic.

Using the Pinyin example from earlier, window `chuāng`, the letter `ā` is in fact a Unicode compositional character consisting of both `a` (`U+0061`) and the macron combining diacritic mark (`U+0304`).  When combined, the compositional character is represented by the Unicode codepoint `U+0101`

For our purposes, all we want is to retrieve the macron character from the compositional character. To do this, we need to properly “decompose” the compositional character. Fortunately, Swift’s `String` type supports character decomposition via the APIs `String.decomposedStringWithCanonicalMapping` and `String.decomposedStringWithCompatibilityMapping`.

**What are “canonical” and “compatibility” mappings?**

According to Unicode, canonical mapping or 

> equivalence is a **fundamental equivalency** between characters or sequences of characters which represent the same abstract character, and which when correctly displayed should always have the same visual appearance and behavior.
> 
> – **Unicode, UAX #15, emphasis added**

Or in visual terms,

![Screenshot 2024-06-13 at 5.07.29PM.png](/blog/Screenshot_2024-06-13_at_5_07_29_PM.png)

Whereas, compatibility mapping or 

> *equivalence is a **weaker type of equivalence** between characters or sequences of characters which represent the same abstract character (or sequence of abstract characters), but which may have distinct visual appearances or behaviors.*
> 
> 
> – **Unicode, UAX #15, emphasis added**
> 

Some salient examples of this include,

![Screenshot 2024-06-13 at 5.12.20PM.png](/blog/Screenshot_2024-06-13_at_5_12_20_PM.png)

![Screenshot 2024-06-13 at 5.12.48PM.png](/blog/Screenshot_2024-06-13_at_5_12_48_PM.png)

For our purposes, the logical choice is to use canonical mapping to decompose a Pinyin letter to retrieve its tone mark.  In Swift, compatibility mapping behaves the same as canonical mapping when it comes to the diacritic marks used to represent Pinyin tone marks, but your mileage may vary in other programming languages.

>💡 Unicode character composition is a complex topic. For a full discussion on Unicode canonical and compatibility forms, see [https://www.unicode.org/reports/tr15/#Norm_Forms]().


### Code Snippets (Swift)

>💡 Note: We assume that we are only dealing with individual Pinyin readings (i.e. a single CJKV logograph for each Pinyin reading, space or comma-delimited). The logic is more complex when dealing with Pinyin prose (e.g. whole sentences or paragraphs), where the word boundaries are not immediately clear.

How to decompose a Pinyin tone mark from the base letter.

```swift
let decomposedString = "chuāng".decomposedStringWithCanonicalMapping
let scalarView = decomposedString.unicodeScalars
/// ["c", "h", "u", "a", "\u{0304}", "n", "g"]
for codepoint in scalarView {
	/// Note: the combining diacritic mark comes 
	/// after the letter with which it is combined.
	/// In this case, "a" + "\u{0304}".
	print(codepoint)
}
```

Once you are able to retrieve the diacritic mark’s codepoint, the process is really as simple as matching that codepoint to a Pinyin tone mark (e.g. in a lookup table).

```swift
/// Lookup table
/// "Combining Diacritic Marks"
let diacriticCodepointToNumericValueMapping = [
		"U+0304": 1,  // First tone
		"U+0301": 2,  // Second tone
		"U+030C": 3,  // Third tone
		"U+0300": 4   // Fourth tone
		"\u{00B7}": 5 // Placed before syllable, not commonly used in Pinyin.
]
```

And finally, the process is as simple as concatenating the base Pinyin reading with the tone mark’s numeric value.

```swift
/// Simply append the numeric value to the Pinyin without the diacritic mark(s).
/// One possible approach is to use a helper function
/// that strips all tone marks from a Pinyin string.
/// We want to keep any umlauts.
let pinyinDiacritic = "chuāng"
let toneMarkCodepoint = "U+0304"
let toneMarkNumeric = 1
let pinyinIPA = "chuang\(toneMarkNumeric)"
```

I’ve implemented **PinyinParse** so that we can make the process as easy as just writing one line of code:

```swift
/// Assumes $0.pinyinReading is written in diacritic form.
Pinyin(diacriticForm: $0.pinyinReading).ipaForm
```

For a full implementation, see here [https://github.com/boscojwho/PinyinParse](https://github.com/boscojwho/PinyinParse).  Feel free to contribute or use as-is!