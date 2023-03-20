---
title: "Matrix OS User Manual"
author: [203 Electronics]
date: "\\date"
footer-left: "\\leftmark"
footer-center: ""
footer-right: "Page \\thepage"
header-left: "\\thetitle"
header-center: ""   
header-right: "OS Version WIP"
toc: true
toc-own-page: true
header-includes: |
    \usepackage{sectsty}
    \sectionfont{\clearpage}
...
# Intro

Matrix is a multipurpose grid controller, designed to be community centric, highly customizable, and fully open sourced. 

Matrix OS is the soul of Matrix, enabling Matrix to be multi purpose and have enhanced standalone capabilities. All software features are shipped as Matrix OS applications and be completely independent of each other. 

# Matrix Overview

# Matrix OS Basic
After connecting Matrix to power, a boot animation will start playing. 
If Matrix OS can not connect to the host (eg, connected to a power bank)

After the boot animation, the application launcher will be the first thing that the OS shows.

## Application Launcher
Application Launcher is the main menu of the OS. It allows user to select an application to use.

In this menu, you also have access to the system setting. 

## OS Setting
The OS setting controls things that are system wide. Like brightness, rotation, velocity sensitivity and more.


In most of Matrix OS UI. You can hold down any light up buttons to see what their name or meaning. Holding down any unlit keys will show the current menu name.

Some lit keys will have more advanced control panel if held down (eg, brightness control). In that case, you can hold down the unlit keys in the advance control to see the meaning for the button.

# Matrix OS Applications
Matrix OS features are available as separate applications. How the device behaves will complete differ depends on the active application.

## Performance APP
This application is used as a canvas for visual performance or drum pad. It can be used to perform visual performance with Amethyst Player, Ableton Live, or Unipad. 

It sends standard Midi signal with aftertouch so it should be compatible with any DAW that accepts midi if it is used as drum pad purpose.

## Note APP


## Lighting APP

# Matrix OS Update

Matrix can enter OS update mode in two ways:
1. Use the red button on the bottom left of the setting menu.
2. Hold down the function key while plug in Matrix.

Matrix will show up as a USB mass storage drive in your host device. Simply copy the UF2 file of your desired OS into this drive. Matrix will complete the firmware update and will reboot upon finish.

# Special Booting Mode
Matrix has a few special booting mode. Holding the indicated keys down during booting will enter them instead of the regular OS routine.

## Hardware Test & Configuration
This is a testing mode and configuration menu for Matrix.

## Low Brightness
This will reset Matrix’s brightness setting to lowest, allowing hosts with low power delivery capabilities to operate Matrix.

## Factory Reset
This key combination will reset Matrix OS’s user configuration

# Credit
203Null