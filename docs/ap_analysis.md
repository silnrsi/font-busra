# Attachment Point Analysis

This document describes each of the attachment points giving its old and new
name.

| AP Name | Old Name | Description                                          |
| ------- | -------- | ---------------------------------------------------- |
| \_B6    | \_17B6   | Attach to 17B6 and 17C5.rightpart                    |
| B6      | 17B6     | Base of 17B6: uni17B6, uni17C5                       |
| B61     | 17B6\_1  | [Unused] First ligature component base for uni16C6.ms.narrowhigh |
| B62     | 17B6\_2  | [Unused] Second ligature component base for uni16C6.ms.narrowhigh |
| \_D0    | \_17D0   | Attaching to 17D0: uni17D0, uni17D0.ms.high, uni17D0.ms.high2 |
| D0      | 17D0     | 17D0 base: uni17B6, uni17C5, uni17C5.rightpart       |
| \_A0    | \_above\_marks0 | Attaches diacritic (incl. vowel) to diacritic |
| A0      | above\_marks0 | Base for attaching diacritic to diacritic |
| \_A1    | \_above\_marks1 | Attaches diacritic (incl. vowel) to diacritic, second level |
| A1      | above\_marks1 | Base for attaching diacritic to diacritic |
| \_A2    | \_above\_marks\_1 | Attaches diacritic (incl. vowel) to diacritic, second level at first level |
| A2      | above\_marks\_1 | Base for attaching diacritic to diacritic |
| \_B1    | \_below  | lower diacritic to attach below something another diacritic |
| B1      | below    | lower diacritics to attach to |
| \_B2    | \_below2 | attaches to lower diacritics |
| B2      | below2   | lower diacritics including coengs |
| \_C6C   | \_c6n    | narrow nikahit attaching AP |
| C6C1    | c6n\_1   | nikahit base on first ligature component for centred positions |
| C6C2    | c6n\_2   | nikahit base on second ligature component for centred positions |
| \_D2    | \_coengx | coengs attaching to coengs |
| D2      | coengx   | coengs coengs attach to |
| def     | default  | default spacing attachment - not sure why it's needed |
| def1    | default\_1 | default attachment to first ligature component |
| def2    | default\_2 | default attachment to second ligature component |
| \_H     | \_high2  | diacritics for high attachment |
| H       | high2    | Bases that take extra high diacritics |
| \_C6    | \_lig\_C6 | nikahits |
| C61     | lig\_C6\_1 | AP for nikahit on first ligature component |
| C62     | lig\_C6\_2 | AP for nikahit on second ligature component |
| C63     | lig\_C6\_3 | AP for nikahit on third ligature component |
| \_L     | \_lig\_L | lower diacritics including coengs |
| L       | lig\_L   | [unused] to attach lower diacritics to |
| L1      | lig\_L\_1 | First ligature component attaching lower diacritics |
| L2      | lig\_L\_2 | Second ligature component attaching lower diacritics |
| L3      | lig\_L\_3 | Third ligature component attaching lower diacritics |
| \_U     | \_lig\_U | Upper diacritics to attach |
| U       | lig\_U   | [Unused] to attach upper diacritics to |
| U1      | lig\_U\_1 | First ligature component attaching upper diacritics |
| U2      | lig\_U\_2 | Second ligature component attaching upper diacritics |
| U3      | lig\_U\_3 | Third ligature component attaching upper diacritics |
| \_UR    | \_lig\_U\_right | Consonant shifters |
| UR1     | lig\_U\_right\_1 | First ligature component for attaching consonant shifters |
| UR2     | lig\_U\_right\_2 | Second ligature component for attaching consonant shifters |
| UR3     | lig\_U\_right\_3 | Third ligature component for attaching consonant shifters |
| \_NA    | \_na\_above | true diacritics to attach |
| NA1     | na\_above\_1 | First ligature component attaching diacritics |
| NA2     | na\_above\_2 | Second ligature component attaching diacritics |
| \_NBB   | \_na\_BB  | u-vowel for attachment (as consonant shifter) |
| NBB1    | na\_BB\_1 | attach u-vowel to first component |
| NBB2    | na\_BB\_2 | attach u-vowel to second component |
| \_NC    | \_na\_cent | Centre attaching diacritics (e.g. coengs) |
| NC1     | na\_cent\_1 | Attach centre to first component |
| NC2     | na\_cent\_2 | Attach centre to second component |
| \_N     | \_Na\_middle | centre attaching diacritics under na |
| N       | Na\_middle | Non ligatures receiving centre diacritics |
| \_NG    | \_ng\_coeng | below diacritics incl. coengs for ng |
| NG      | ng\_coeng | 81, 8C, 91, A7, A8, AA, B1, B3 receive lower diacritics |
| \_PA    | \_Pabove | upper combining diacritics 0300 range |
| PA      | Pabove | upper combining diacritics 0300 range to stack onto |
| \_PB    | \_Ph\_below | lower stacking combining diacritics 0300 range |
| PB      | Ph\_below | Lots of latin to stack lower combining underneath |
| PHB     | Phbelow | lower stacking combining diacritics 0300 range |

That's a lot of attachment points. But thankfully not too many per glyph. Many
are overlapping and so may need minor offsets to allow them to be edited.


