---
title: "Matrix OS User Manual"
subtitle: "OS Version 2.4.1"
author: [203 Electronics]
date: "\\date"
footer-left: "\\rightmark"
footer-center: ""
footer-right: "Page \\thepage"
header-left: "\\thetitle"
header-center: ""   
header-right: "OS Version 2.4.1"
toc: true
toc-own-page: true
colorlinks: true
titlepage: true
titlepage-rule-height: 0
titlepage-background: "backgrounds/background.pdf"
titlepage-text-color: "FFFFFF"
header-includes: |
    \usepackage{sectsty}
    \sectionfont{\clearpage}
...
# Intro

Matrix is a multipurpose grid controller, designed to be community centric, highly customizable, and fully open sourced. 

Matrix OS is the soul of Matrix, enabling Matrix to be multi purpose and have enhanced standalone capabilities. All software features are shipped as Matrix OS applications and be completely independent of each other. 

Note: All Coordination in this document is based as the top left as (0,0)

# Matrix OS Basic
After connecting Matrix to power, a boot animation will start playing. 
If Matrix OS can not connect to the host (eg, connected to a power bank), a standby animation will be playing in loop. You can click the center function key to enter the OS.

After the boot animation, the application launcher will be the first thing that the OS shows.

Matrix OS features are available as separate applications. How the device behaves will complete differ depends on the active application.

# Application Launcher
Application Launcher is the main menu of the OS. It allows user to select an application to use.

Top section of the app launcher are applications available. The bottom section are the control bars hosting application class / page selection and system setting.

\pagebreak
![](Image/app-launcher.svg)

### Available Applications:
- \textcolor[rgb]{1,0,0}{$\blacksquare$} (0,0) - [Performance APP](#performance-app)
- \textcolor[rgb]{0,1,1}{$\blacksquare$} (1,0) - [Note/Scale APP](#note-app)
- \textcolor[rgb]{1,0,1}{$\blacksquare$} (2,0) - [Lighting APP](#lighting-app)


### Control Bar
- \textcolor[rgb]{0,1,1}{$\blacksquare$} (0,7) - System Applications
- \textcolor[rgb]{0,0,0}{$\square$} (7,7) - [System Setting}](#system-setting)

\pagebreak
# System Setting
The System setting controls things that are system wide. Like brightness, rotation, device specific features, and more.

In most of Matrix OS UI. You can hold down any light up buttons to see what their name or meaning. Holding down any unlit keys will show the current menu name.

Some lit keys will have more advanced control panel if held down (eg, brightness control). In that case, you can hold down the unlit keys in the advance control to see the meaning for the button.

![](Image/system-setting.svg)

### System Control
- \textcolor[rgb]{0,0,0}{$\square$} Center - Brightness Control, tap to cycle though all brightness level, hold to enter brightness control panel.
- \textcolor[rgb]{0,1,0}{$\blacksquare$} Around the Center - Rotation Control, tap to rotate to specific direction. Up direction serves no purpose.
- \textcolor[rgb]{1,0,0}{$\blacksquare$} (0,7) - [Firmware Update Mode, tap to enter firmware update mode](#matrix-os-update).
- \textcolor[rgb]{0,1,1}{$\blacksquare$} (7,7) - Device ID, Tap to enter device ID. This is useful if you have mulitple Matrix and want to identify them.

### System Info
- \textcolor[rgb]{0,1,0.19}{$\blacksquare$} (1,7) - Matrix OS Version
- \textcolor[rgb]{0,1,0.19}{$\blacksquare$} (2,7) - Device Info
- \textcolor[rgb]{0,1,0.19}{$\blacksquare$} (3,7) - Device Serial Number

### Matrix Specific
- \textcolor[rgb]{0,0.51,0.99}{$\blacksquare$} (0,0) - Bluetooth Midi toggle
- \textcolor[rgb]{0.48,0.34,0.98}{$\blacksquare$} (0,2) - Touchbar toggle, useful if touchbar is causing unintended actions.

# Matrix OS Applications
All user features on Matrix OS are provided as separate applications. In this documentation only stock applications are covered. Some applications might have their own manual.

\pagebreak
## Performance APP
This application is used as a canvas for visual performance or drum pad. It can be used to perform visual performance with Amethyst Player, Ableton Live, or Unipad. 

It sends standard Midi signal with aftertouch so it should be compatible with any DAW that accepts midi if it is used as drum pad purpose.

When you first enter the application, you will see a blank canvas. You can click or hold on the function key to enter the action menu.

To exit performance app, enter action menu and hold down the function key. You will be brought back to the application launcher.

### Action Menu
![](Image/performance-action.svg)

- \textcolor[rgb]{0,0,0}{$\square$} Center - Brightness Control, tap to cycle though all brightness level, hold to enter brightness control panel.
- \textcolor[rgb]{0,1,0}{$\blacksquare$} Above the Center - Clear Canvas. Reset the canvas to blank, clearing all on lights. 
- \textcolor[rgb]{0,1,0}{$\blacksquare$} Around the Center (Except Up) - Rotation Control, tap to rotate to specific direction. 
- \textcolor[rgb]{0.67,1,0}{$\blacksquare$} (0,0) - Flicker Reduction. Normally this should be off, in some application this can help with flickering lightshows (mainly Ableton Live)
- \textcolor[rgb]{1,1,0}{$\blacksquare$} (7,0) - Compatibility mode, mostly used to maintain compatibility with some visual performance software that is not fully compatible with Matrix yet. This will likely be removed in the future version of Matrix OS.
- \textcolor[rgb]{0,0,0}{$\square$} (6,0) - Velocity Sensitivity, lit as velocity sensitivity is on.
- \textcolor[rgb]{0.67,1,0}{$\blacksquare$} (0,5) - Hold Mode, When hold mode is on, action menu is only accessible via holding down the function key. This is useful if you want to avoid accidental action menu pop up.
- \textcolor[rgb]{0,0,0}{$\square$} (7,5) - [System Setting](#system-setting)
- \textcolor[rgb]{1,0,1}{$\blacksquare$} or \textcolor[rgb]{1,0.33,0}{$\blacksquare$} On the Bottom - Additional Midi Keys. Color differs based on current (compatibility) mode.

\pagebreak
## Note APP
Note APP is used for as a midi note interface. It can be used to play midi notes with different layout, scale, and modes.

After configuration, click the function key to enter the notepad, click again to return to the configuration menu.

To exit note app, enter action menu and hold down the function key in the config menu. You will be brought back to the application launcher.

\pagebreak
### Config Menu
![](Image/note-config.svg)

System Config:

- \textcolor[rgb]{0,0,0}{$\square$} Center - Brightness Control, tap to cycle though all brightness level, hold to enter brightness control panel

- \textcolor[rgb]{0,1,0}{$\blacksquare$} Around the Center - Rotation Control, tap to rotate to specific direction. Up direction serves no purpose

- \textcolor[rgb]{0,0,0}{$\square$} (7,7) - [System Setting](#system-setting)

App Config:

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (Depends on config color) (0,3) - Layout Config 1

- \textcolor[rgb]{0,1,1}{$\blacksquare$} (Depends on config color) (0,4) - Layout Config 2

- \textcolor[rgb]{0,0,0}{$\square$} (0,1) - Split Mode, spilt the layout in half, left and right will be config 1 and config 2

Layout Config:

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (Depends on config color) Left Bar - Octive Selector

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (Depends on config color) (7,0) - Color Selector, change the color combination of the layout.

- \textcolor[rgb]{0,1,1}{$\blacksquare$} (6,7) - Velocity Sensitivity, lit as velocity sensitivity is on.

- \textcolor[rgb]{1,0,0.56}{$\blacksquare$} (7,2) - [Scale Selector](#scale-selector)

- \textcolor[rgb]{1,0.31,0}{$\blacksquare$} (7,3) - Enforce Scale. When on, only notes in the selected scale will be shown, when off, all notes will be shown but notes that are not in the selected scale will be dimmed. (Chromatic mode when off, scale mode when on)

- \textcolor[rgb]{1,1,0}{$\blacksquare$} (7,4) - Overlap Selector. Selects how much each row above overlaps with the row below it. This is useful if you want to play chords with one hand. (There is also an aligh root toggle inside this menu. When on the next row above after the 
entire scale is completed will realign with root note)

- \textcolor[rgb]{0.37,1,0}{$\blacksquare$} (7,5) - Channel Selector, selects the midi channel that the note app will send midi notes to.

\pagebreak
### Scale Selector
![](Image/note-scale.svg)

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (Depends on config color) Top - Scale Visualizer and Root Note Selector, tap any note to select as root note.
- \textcolor[rgb]{1,0,1}{$\blacksquare$} (Depends on config color) Bottom - Scale Selector, see the following table for scale selection. 

\pagebreak
#### Scale Table
|Index | Scale                     | C | C# | D | Eb | E | F | F# | G | Ab | A | Bb | B |
|------|---------------------------|---|----|---|----|---|---|----|---|----|---|----|---|
| 1    | Natural Minor             | X |    | X |    |   | X |    | X |    | X |    |   |
| 2    | Major                     | X |    | X |    | X |   | X  |   | X  |   | X  |   |
| 3    | Dorian                    | X |    | X |    |   | X |    | X |    | X |    |   |
| 4    | Phrygian                  | X | X  |   | X  |   | X |    | X |    | X |    | X |
| 5    | Mixolydian                | X |    | X |    | X |   | X  |   | X  |   | X  |   |
| 6    | Melodic Minor Ascending   | X |    | X |    |   | X |    | X |    | X |    | X |
| 7    | Harmonic Minor            | X |    | X |    |   | X |    | X |    |   | X  |   |
| 8    | Bebop Dorian              | X |    |   | X  | X | X |    | X |    | X |    |   |
| 9    | Blues                     | X |    |   | X  |   | X | X  |   |    | X |    | X |
| 10   | Minor Pentatonic          | X |    |   | X  |   | X |    |   |    | X |    | X |
| 11   | Hungarian Minor           | X |    | X |    |   |   | X  | X |    | X |    | X |
| 12   | Ukranian Dorian           | X |    | X |    |   |   | X  | X |    | X | X  |   |
| 13   | Marva                     | X | X  |   | X  |   | X |    | X |    | X |    | X |
| 14   | Todi                      | X | X  |   | X  |   |   | X  | X |    | X |    | X |
| 15   | Whole Tone                | X |    | X |    | X |   | X  |   | X  |   |    |   |
| 16   | Chromatic                 | X | X  | X | X  | X | X | X  | X | X  | X | X  | X |
| 17   | Lydian                    | X |    | X |    | X |   | X  | X |    | X |    |   |
| 18   | Locrian                   | X | X  |   | X  |   | X | X  |   | X  |   |    | X |
| 19   | Major Pentatonic          | X |    | X |    | X |   |    | X |    | X |    |   |
| 20   | Phyrigian Dominate        | X | X  |   |    | X |   | X  | X |    | X |    | X |
| 21   | Half-Whole Diminished     | X | X  |   | X  | X |   | X  |   | X  |   | X  | X |
| 22   | Mixolydian BeBop          | X |    | X |    | X | X |    | X |    | X | X  | X |
| 23   | Super Locrian             | X | X  |   | X  | X |   | X  |   | X  |   |    |   |
| 24   | Hirajoshi                 | X |    | X |    |   |   |    | X |    | X |    |   |
| 25   | In Sen                    | X | X  |   |    |   | X |    | X |    |   | X  |   |
| 26   | Yo Scale                  | X |    | X |    | X |   | X  |   | X  |   |    |   |
| 27   | Iwato                     | X | X  |   |    |   | X |    |   |    |   | X  |   |
| 28   | Whole Half                | X |    | X |    | X | X |    | X |    | X |    | X |
| 29   | BeBop Minor               | X |    | X |    | X | X |    | X |    | X |    | X |
| 30   | Major Blues               | X |    | X |    |   |   | X  |   | X  |   |    | X |
| 31   | Kumoi                     | X |    | X |    |   |   | X  |   | X  |   |    |   |
| 32   | BeBop Major               | X |    | X |    | X | X |    | X | X  |   | X  |   |

\pagebreak
## Lighting APP
Lighting APP is very simple app that is used to allow Matrix to be used for lighting purpose.

It is very easy to operate, just click on the function key allows you to change the color. First selector selects the hue and the second selector selects the brightness & saturation.

Holding down the function key will exit this app and bring you back to the application launcher.

# Matrix OS Update

Matrix can enter OS update mode in two ways:

1. Use the red button on the bottom left of the setting menu.
2. Hold down the function key while plug in Matrix.

You will also need a new firmware file to update your Matrix. You can find them in the release section of the [Matrix OS Github](https://github.com/203Electronics/MatrixOS/releases)

Matrix will show up as a USB mass storage drive in your host device. Simply copy the UF2 file of your desired OS into this drive. Matrix will complete the firmware update and will reboot upon finish.

![](Image/firmware-upload.svg)

Note: If the arrow is red then that means USB communication is not established. Try replugging Matrix or try a different USB port.

# Special Booting Mode
Matrix has a few special booting mode. Holding the indicated keys down during booting will enter them instead of the regular OS booting routine.

Note that those keys are not affected by your OS's rotation setting. All key combination are based on the physical key location (USB port on the top).

\pagebreak
## Low Brightness
This will reset Matrix’s brightness setting to lowest, allowing hosts with low power delivery capabilities to operate Matrix.

![](Image/special-booting-low-brightness.svg)

\pagebreak
## Factory Reset
This key combination will reset Matrix OS’s user configuration.

![](Image/special-booting-factory-reset.svg)

\pagebreak
## Hardware Test & Configuration
This is a testing mode and configuration menu for Matrix.

![](Image/special-booting-factory-menu.svg)

# Feedback & Support
If you have any feedback or suggestion for Matrix OS, you can let us know by creating an issue or discussion post on our [Github](https://github.com/203Electronics/MatrixOS). Alternatively, you can also contact us via email at null@203.io.

If there are any feedback or suggestion for this manual. You can also let us know by creating an issue or even contribute it yourself by creating a pull request on our [Github](https://github.com/203Electronics/Matrix-OS-User-Manual).

If you need any support on your Matrix specificlly, sent us an email at null@203.io and we will try our best to help you out.

We also have a discord server for all 203's projects and more. You can join us at [203 Lab](https://discord.gg/Aw99cAgmDA).

# Credit
- Null - 203 Electronics