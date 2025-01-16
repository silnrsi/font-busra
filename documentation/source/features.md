---
title: Busra - Font Features
fontversion: 9.000
---

Busra is an OpenType-enabled font family that supports the Khmer script. It includes a number of optional features that provide alternative rendering that might be preferable for use in some contexts. The sections below list the details of these features. Whether these features are available to users will depend on both the application and the rendering technology being used. Some applications let the user control certain features such as Character Variants to turn on the rendering of variant characters. However, at this point, most applications do not make use of those features.

See [Using Font Features](https://software.sil.org/fonts/features/). That page provides a comprehensive list of applications that make full use of the OpenType font technology.

This page uses web fonts (WOFF) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Busra as a web font see *Busra-webfont-example.html* in the font package web folder. 

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## User-selected feature list

### Stylistic alternates

#### Variant forms

<span class='affects'>Affects: U+17B1, U+17B3, U+17CC, U+17D0</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x17B1; &#x17B3; &#x1780;&#x17CC; &#x1780;&#x17D0;</span>| `ss01=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss01" 1'>&#x17B1; &#x17B3; &#x1780;&#x17CC; &#x1780;&#x17D0;</span>| `ss01=1`

#### Hooked coengs

<span class='affects'>Affects: U+17D2</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1780;&#x17D2;&#x1783; &#x1780;&#x17D2;&#x1788; &#x1780;&#x17D2;&#x1788;&#x17C5;</span>| `ss02=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss02" 1'>&#x1780;&#x17D2;&#x1783; &#x1780;&#x17D2;&#x1788; &#x1780;&#x17D2;&#x1788;&#x17C5;</span>| `ss02=1`

#### Alternate ka

<span class='affects'>Affects: U+1780</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1780; &#x1780;&#x17B6; &#x1780;&#x17C5;</span>| `ss03=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss03" 1'>&#x1780; &#x1780;&#x17B6; &#x1780;&#x17C5;</span>| `ss03=1`

#### Alternate muusikatoan placement after -aa and -oo

<span class='affects'>Affects: U+17C9</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1780;&#x17C9;&#x17B6; &#x1780;&#x17C9;&#x17C4; &#x1782;&#x17C9;&#x17B6; &#x1782;&#x17D2;&#x1783;&#x17C9;&#x17C4;</span>| `ss07=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss07" 1'>&#x1780;&#x17C9;&#x17B6; &#x1780;&#x17C9;&#x17C4; &#x1782;&#x17C9;&#x17B6; &#x1782;&#x17D2;&#x1783;&#x17C9;&#x17C4;</span>| `ss07=1`

#### Alternate coeng-Nho 

This feature is provided to accommodate historical texts.

<span class='affects'>Affects: U+17D2 U+1789</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1780;&#x17D2;&#x1789;</span>| `ss08=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss08" 1'>&#x1780;&#x17D2;&#x1789;</span>| `ss08=1`

#### Lower vowels following below coengs

<span class='affects'>Affects: U+17BB, U+17BC, U+17BD, U+17D2</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1789;&#x17BB; &#x17AB;&#x17D2; &#x179f;&#x17d2;&#x17a0;&#x17ca;&#x17b8;</span>| `ss09=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss09" 1'>&#x1789;&#x17BB; &#x17AB;&#x17D2; &#x179f;&#x17d2;&#x17a0;&#x17ca;&#x17b8;</span>| `ss09=1`

#### Alternate samyok sannya and nikahit before -i

This feature supports the Tampuan language.

<span class='affects'>Affects: U+17C6, U+17D0</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1780;&#x17D0;&#x17C7; &#x1780;&#x17CA;&#x17B6;&#x17C6;</span>| `ss18=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss18" 1'>&#x1780;&#x17D0;&#x17C7; &#x1780;&#x17CA;&#x17B6;&#x17C6;</span>| `ss18=1`

#### Hyphen after ka

This feature turns U+1780 into a hyphen for demonstration purposes.

<span class='affects'>Affects: U+1780</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1780;&#x17B6; &#x1780;&#x17C5;</span>| `ss05=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss05" 1'>&#x1780;&#x17B6; &#x1780;&#x17C5;</span>| `ss05=1`

#### Space after ka

This feature turns U+1780 into a space for demonstration purposes.

<span class='affects'>Affects: U+1780</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1780;&#x17B6; &#x1780;&#x17C5;</span>| `ss06=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss06" 1'>&#x1780;&#x17B6; &#x1780;&#x17C5;</span>| `ss06=1`

#### muusikatoan downshift

<span class='affects'>Affects: U+17C9</span>

Feature        | Sample | Feature setting
:------------- | :--------------- | :------------- 
Standard | <span class='busra-R normal'        >&#x1789;&#x17C9;&#x17B6; &#x1784;&#x17C9;&#x17B6; &#x1798;&#x17C9;&#x17B6;</span>| `ss19=0`
Alternate | <span class='busra-R normal' style='font-feature-settings: "ss19" 1'>&#x1789;&#x17C9;&#x17B6; &#x1784;&#x17C9;&#x17B6; &#x1798;&#x17C9;&#x17B6;</span>| `ss19=1`

<!-- PRODUCT SITE ONLY
[font id='busra' face='Busra-Regular' size='150%']
-->
