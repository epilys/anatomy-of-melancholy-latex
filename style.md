---
title: Style for AoM edition
date: May 5, 2021
documentclass: article
author:
 - epilys
mainfont: "CMUSerif-Roman"
mathfont: "CMUSerif-Roman"
sansfont: "CMUSansSerif"
monofont: DejaVuSansMono
header-includes: |
  \usepackage[x11names,dvipsnames]{xcolor}
  \usepackage{tikz}
...

# Structure

Chapters, sections but not subsections *must* start in a fresh, recto page. Accompanying illustrations can be placed on the facing verso.

# Ampersands

There should be no ampersands in the main text and notes. Convert all instances of `&c.` to `etc.`.

# Dashes

Use single dash `-` for inter-word dashes.

Use en `--` for number ranges.

Use em `---` for parenthetical dashes.

# Abbreviations

All abbreviations in english, latin, greek should be expanded in every case. Explicit is better than ambiguity.

- *ap.* - *apud*, quoted in.
- *fr.* - fragment
- *h.l.* - *hic locus*, this passage.
- *h.v.* - *haec verba*, these words.
- *init.* - *initio*, at the beginning.
- *schol.* - *scholium*, ancient commentary.
- *str.* - strophe.
- *s.v.* - *sub voce*, under the heading.
- *temp.* - *tempore*, in the time of.
- *var. lect* - *varia lectio*, variant reading.

The only exceptions are *i.e.*, *e.g.*, *etc.*. Such an abbreviation at the end of a sentence should lack the final full stop to prevent its repetition.

# Roman numerals

Roman numerals are to be displayed in Junicode using the roman numeral sylistic set `6`. They are to always be lowercase, unless referring to years or titles, for example Richard III.

# Arabic numerals and dates

Use a `\thinspace` to separate hundreds unless the number is a year.

Always spell out `\emph{anno}` before a year and not with a capital 'A'.

# Units

Add a marginal note for explanations of archaic units.

# Symbols

Symbols (for example astrological) *must* be annotated with marginal notes or footprints. Every symbol, even if only used once, must be defined in the preamble as a command. If a `TeX` symbol looks out of place for a 17th century book, find an appropriate replacement or design one in inkscape/FontForge.

# Marginal notes, footprints, etc

- Notes are printed in miniscule `scriptsize` in Junicode.
- Notes must always begin capitalised and end with a full stop.
- Editor notes must have superscript arabic numerals as text indicators and end with `\theeditor{}`.
- Author notes must have superscript lowercase latin letter symbols as text indicatiors. When running out of letters, add an 'a' on the left side of the indicator and start from 'a' again. For example after 'z' comes 'aa', then 'ab', 'ac', and so on.

## Footnotes Inside Quotations, Verses

`csquotes`  will automatically reset the nesting level within any footnote included in a quotation. It will also reset the language. The language of the footnote text including the hyphenation patterns will match the language of the text surrounding the quotation. This applies to parboxes, minipages, and floats as well.

# Quotations / Verses

Quotations must use single quotes and double quotes for nested quotations:

   ‘he described the scheme as “totally unworkable”’.

Inline latin quotations should be in roman font and written with the `\foreignquote{latin}{〈text〉}` command.

Inline latin should be in emphasis `\emph{text}` and followed by an inline translation.

Latin quotations should be in roman font in the `\foreignblockquote{latin}{text}` command.

```tex
\begin{foreigndisplaycquote}{latin}[〈prenote〉][〈postnote〉]
Lorem ipsum.
\end{foreigndisplaycquote}
```

English verse should be in roman font in `verse` environment:

```tex
\begin{verse}
Woe is me.
\end{verse}
```

With the exception of Chaucer, which needs Blackletter.

```tex
{\gothfont
\begin{verse}
I followed aye mine inclination,\\*
By virtue of my constellation.
\end{verse}
}
```

Latin verse should be in roman font in `verse` and `latin` environments:

```tex
\begin{latin}
\begin{verse}
Lorem ipsum.
\end{verse}
\end{latin}
```

Margin notes should directly precede quotations/verses but footnotes should directly follow.

# Translations

They are of two kinds:

- Inline translations. They are set in a maroon red color, inside brackets, and in italics. The brackets have the same text formatting. They must not include ending punctuation: if any, must be placed after the inline translation. Translations not by the author must be indicated with an editor's footnote.
- Translations of verse or displayed quotations. They are to be separated by a horizontal rule of 60% the textwidth centered on its own line. The original text is first and the translation follows. If translation not by author, it must be indicated with an editor's footnote.

Other Latin text, for example book titles and chapters, should be set in roman font (but still surrounded by `\textlatin{}`) with all abbreviations expanded.

# Biblical references

Names of the books of the Bible should be roman, not italic and not abbreviated.

If chapter numbers are arabic, a point or colon must be used between chapter
and verse number: Genesis 8.7 or 8:7.

Roman lower-case chapter numbers *must* be followed by a full stop (viii. 7); but
the abbreviations v. and vv. (verse, verses) should be spelt out to avoid
confusion with chapter numbers. See that references are consistently
spaced or closed up.

A series of verses within one chapter is separated by commas
(2 Corinthians 8.7, 10, 13). A series of references in different chapters is
best separated by semicolons, to avoid confusion in mixed references
such as 6:4, 5; 8:9.

A long passage within one chapter has an unspaced en rule between
the verse numbers (6.4–12).

# Names

Names of authors, holy figures, etc. must be set in roman font, unless if in the original text it is in all capitals i.e. "GOD" or "CHRIST". Then it should be set in small capitals with `\textsc{}`.

If space is enough, include one to two sentences about a notable personality in the margin.

# Cross references

*All* cross references must use the `hyperref` package and be usable in the pdf.

Retain original author wording for sections and chapters.

# Classical text references

Those should be annotated with a `\{greek,latin}classicalref` macro in order to make them easily searchable if they are to include hyperlinks to online text.
