
Busra is based on an earlier font that is part of a larger package of Khmer script fonts called Mondulkiri. Earlier forms of Busra were called “Khmer Mondulkiri book” and “Khmer Busra”. Significant changes exist between the earlier versions and this Busra release:

## Change history

### 7 February 2025 (SIL WSTech Team) Busra version 9.000
- The font family is now called "Busra" so it and the old "Khmer Busra" can be installed at the same time.
- There are six weights: ExtraLight, Light, Regular, Medium, SemiBold, and Bold. This also replaces the older Khmer Mondulkiri family.
- Oblique (italic) styles are not included but will be provided in a later release.
- Glyph outlines have been revised and improved.
- OpenType support has been rewritten, supporting latest best practice in Khmer text encoding; see [UTN #61: Khmer Encoding Structure]( https://www.unicode.org/notes/tn61).
- Support for Graphite and AAT rendering has been removed.
- Latin glyphs have been replaced with ones specifically designed to work well with the Khmer glyphs. 
- Default line spacing has updated to best practice. This could affect older Windows apps.
- Three font formats are provided: OpenType (.ttf) for desktop use and WOFF/WOFF2 for the web.

### 8 September 2014 (Diethelm Kanjahn) Mondulkiri Font Family version 7.100
- Mondulkiri changes:
   - The hinting has been improved, the difference between regular and bold is visible on screen in much smaller font sizes than before. 
   - A few bugs were addressed: the disappearing of glyphs on Mac in certain strings that do not occur in correctly typed text, a positioning problem in some Tampuan words on Mac, one syllable in Bunong text on Windows/Linux. 
   - Minor changes in diacritic placement, mostly on Mac. Coeng Kho and coeng Ttha were modified. 
   - Glyphs were added - mostly in the phonetic symbols section. The shaping tables for Mac were streamlined and are now the same as for the Busra font.
- Busra changes:
   - The fonts now have AAT tables so that they work on Mac OS X 
   - many glyphs were added, the glyph range is the same as in Mondulkiri 7.100
   - many glyph shapes and diacritic placements were improved slightly
   - the ligatures of some consonants with the 'sra-a', 'sra-oo' and 'sra-ou' have changed and are now the same as in Mondulkiri.
   - hinting has been improved
   - most other changes from Mondulkiri 5.300 to 5.513 are now also in Busra 7.100
   - The descender value was changed which may affect line spacing.

### 31 October 2012 (Diethelm Kanjahn) Mondulkiri Font Family version 5.300
- Split Khmer Mondulkiri fonts from older fonts release
- Support for Apple's AAT rendering system (tested in OS X 10.6.8) as well as Microsoft OpenType tables.
- Support for typographical features to be used under OS X with software that does support them (like Pages or TextEdit, but apparently not MS Word or LibreOffice). 
- Support for 'Stylistic Sets' that provide similar options in OpenType as the 'typographical features' in OS X. These Stylistic Sets work in Adobe software (tested with CS5 and 5.5 on PC), but not in MS Word. MS Word 2010 does support Stylistic Sets, but apparently only for Latin scripts. 
- Support for Khmer Unicode in Adobe CS5 and CS5.5. Two of the Stylistic Sets address the remaining problems. Please refer to the documentation on stylistic sets.
- Many Latin script characters have been added. The bold fonts now have also bold Latin characters.
- Some of the vowel-a ligatures have been changed (e.g. Cho-AA).
- Many characters have been slightly modified. Most significantly the 'hooks' or 'hair' of some coengs have been removed (e.g. coeng-Kho, coeng-Ha, coeng-Qa).
- The positioning of many characters was modified.
- Many other smaller modifications of glyphs and rules.
- To prevent register shifters from being rendered as subscript zero-width-non-joiner has now to be inserted before the register shifter in accordance with The Unicode Standard. Also zero-width-joiner has to be in this position now to force the alternative rendering.
- Increased the descender by a small amount so that second level elements are no longer cut off.
- For users of the Tampuan language: coeng-vo after coeng-ro and shifting of samyuk before reahmuk are now enabled by default. The Tampuan option now only covers the width of space and the permission to use samyuk after reahmuk.
- The support for the use of vowels and coengs with independent vowels in OS X is limited. If there is a real need for improvement please contact the font designer.
- Changed position of quotes (U+2018-9, 201C-D) and mirrored U+201C. 

### 9 November 2010 (Diethelm Kanjahn) Mondulkiri Font Family version 5.300
- First version released under the SIL Open Font License
- First version released on https://scripts.sil.org
- Added fonts: Ratanakiri, all italic typefaces
- Renamed fonts: Busra and Oureang
- Major OpenType code revisions
- Corrections of outlines to comply with TTF conventions
- Many small edits of the outlines
- Outlines are now TrueType outlines
- Improved hinting
- Added characters
- Size of Khmer base characters now equivalent to Roman capital letters.

### 16 September 2005 (Diethelm Kanjahn) Mondulkiri Font Family version 1.1
- OpenType and Graphite test fonts

### 12 April 2003 (Diethelm Kanjahn) Mondulkiri Font Family version 0.9
- first public release as legacy fonts