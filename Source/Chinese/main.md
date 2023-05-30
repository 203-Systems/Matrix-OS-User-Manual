---
title: "Matrix OS 用户手册"
subtitle: "OS 版本 2.4.1"
author: [203 Electronics]
date: "\\date"
footer-left: "\\leftmark"
footer-center: ""
footer-right: "\\thepage"
header-left: "\\thetitle"
header-center: ""   
header-right: "OS 版本 2.4.1"
toc: true
toc-own-page: true
toc-title: "目录"
colorlinks: true
titlepage: true
titlepage-rule-height: 0
titlepage-background: "backgrounds/background.pdf"
titlepage-text-color: "FFFFFF"
header-includes: |
    \usepackage{sectsty}
    \sectionfont{\clearpage}
...

# 简介
Matrix是一款多用途的矩阵控制器，旨在以社区为中心，高度可定制，并完全开源。

Matrix OS是Matrix的灵魂，使Matrix具备多用途和强大的独立能力。

注：此文档中的所有坐标都是以左上角为基准点 (0,0)

# Matrix OS基础知识
连接Matrix电源后，将开始播放启动动画。
如果Matrix OS无法连接到主机（例如，连接到移动电源），默认的等待动画会循环播放。此时可以按下中间的功能键进入OS。

启动动画后，应用程序启动器将是操作系统显示的第一件事。

Matrix OS 的各项功能是作为独立的应用程序提供的，彼此之间完全独立。设备的功能和行为将根据当前的应用程序而完全不同。

## 应用程序启动器
应用程序启动器是操作系统的主菜单。它允许用户选择要使用的应用程序。

在此菜单中，你还可以访问系统设置。


\pagebreak
![](Image/app-launcher.svg)

### 应用程序
- \textcolor[rgb]{1,0,0}{$\blacksquare$} (0,0) - [演奏 APP](#演奏APP)
- \textcolor[rgb]{0,1,1}{$\blacksquare$} (1,0) - [音符/音阶 APP](#音符/音阶app)
- \textcolor[rgb]{1,0,1}{$\blacksquare$} (2,0) - [灯光 APP](#灯光-app)


### 控制栏
- \textcolor[rgb]{0,1,1}{$\blacksquare$} (0,7) - 系统应用
- \textcolor[rgb]{0,0,0}{$\square$} (7,7) - [系统设置](#matrix-os设置)

\pagebreak

## Matrix OS设置
操作系统设置控制系统范围内的事物。例如，亮度、旋转、压力感应等。

在Matrix OS的大多数UI中，你可以按住任何亮起的按钮以查看它们的名称或含义。按住任何未点亮的键将显示当前菜单名称。

某些亮灯按键如果按住会有更高级别的控制面板（例如亮度控制）。在这种情况下，你可以按住高级控制面板中未点亮的按键以查看按钮的含义。

![](Image/system-setting.svg)

### 系统控制
- \textcolor[rgb]{0,0,0}{$\square$} 中心 - 亮度控制，轻触循环所有亮度级别，长按进入亮度控制面板。
- \textcolor[rgb]{0,1,0}{$\blacksquare$} 围绕中心 - 旋转控制，轻触旋转到特定方向。上方向的按钮没有作用。
- \textcolor[rgb]{1,0,0}{$\blacksquare$} (0,7) - [固件更新模式，轻触进入固件更新模式](#matrix-os更新)。
- \textcolor[rgb]{0,1,1}{$\blacksquare$} (7,7) - 设备ID，轻触进入设备ID。如果你有多个Matrix并且并想要识别它们，则此功能非常有用。

### 系统信息
- \textcolor[rgb]{0,1,0.19}{$\blacksquare$} (1,7) - Matrix OS 版本
- \textcolor[rgb]{0,1,0.19}{$\blacksquare$} (2,7) - 设备信息
- \textcolor[rgb]{0,1,0.19}{$\blacksquare$} (3,7) - 设备序列号

### Matrix 设备相关
- \textcolor[rgb]{0,0.51,0.99}{$\blacksquare$} (0,0) - 蓝牙MIDI开关
- \textcolor[rgb]{0.48,0.34,0.98}{$\blacksquare$} (0,2) - 触摸条开关，如果触摸条导致意外操作，则可以通过此开关关掉。

# Matrix OS应用程序
Matrix OS上的所有用户功能都作为单独的应用程序提供。本文档仅涵盖自带应用程序。一些应用可能有自己的用户手册。

## 演奏APP
该应用程序用作灯光表演或普通Midi鼓垫。它可用于使用Amethyst Player、Ableton Live或Unipad进行灯光表演。

该应用发送标准的Midi信号和触后效果，因此如果当作鼓垫的话，则可与任何接受midi的DAW兼容。

当你进入应用时，设备只会显示空白的页面。你可以单击或按住功能键进入操作菜单。

要退出演奏APP，请进入操作菜单并按住功能键。应用就会退出，OS返回应用程序启动器。

### 操作菜单
![](Image/performance-action.svg)

- \textcolor[rgb]{0,0,0}{$\square$} 中心 - 亮度控制，轻触循环所有亮度级别，长按进入亮度控制面板。
- \textcolor[rgb]{0,1,0}{$\blacksquare$} 中心上方 - 清空画布。将画布重置为空白，清除所有点亮的灯光。
- \textcolor[rgb]{0,1,0}{$\blacksquare$} 中心周围（除了上方） - 旋转控制，轻触旋转到特定方向。
- \textcolor[rgb]{0.67,1,0}{$\blacksquare$} (0,0) - 闪灯优化模式。通常应该关闭此功能，在某些应用中，它可以帮助减少闪烁的灯光效果（主要是在Ableton Live中）。
- \textcolor[rgb]{1,1,0}{$\blacksquare$} (7,0) - 兼容模式，主要用于保持与某些目前与Matrix不完全兼容的软件的兼容性。在未来的Matrix OS版本中，可能会将此功能删除。
- \textcolor[rgb]{0,0,0}{$\square$} (6,0) - 压力感应，当点亮时表示压力感应已开启。
- \textcolor[rgb]{0.67,1,0}{$\blacksquare$} (0,5) - 锁定模式，当锁定模式开启时，只能通过按住功能键来访问操作菜单。如果你想要避免意外弹出操作菜单，则此功能非常有用。
- \textcolor[rgb]{0,0,0}{$\square$} (7,5) - [系统设置](#matrix-os设置)
- \textcolor[rgb]{1,0,1}{$\blacksquare$} 或 \textcolor[rgb]{1,0.33,0}{$\blacksquare$} 底部 - 额外的Midi按键。颜色根据当前（兼容）模式而异。

\pagebreak
## 音符/音阶APP
音符/音阶APP用作MIDI音符演奏界面。此软件可用于以不同的布局、音阶和模式来让用户演奏。

配置后，单击功能键进入演奏界面，再次单击返回配置菜单。

要退出此程序，请进入配置菜单，在配置菜单中按住功能键。应用就会退出，OS返回应用程序启动器。

### 配置菜单
![](Image/note-config.svg)

系统配置：

- \textcolor[rgb]{0,0,0}{$\square$} 中心 - 亮度控制，轻触循环所有亮度级别，长按进入亮度控制面板。

- \textcolor[rgb]{0,1,0}{$\blacksquare$} 中心周围 - 旋转控制，轻触旋转到特定方向。向上方向没有作用。

- \textcolor[rgb]{0,0,0}{$\square$} (7,7) - [系统设置](#matrix-os设置)

应用配置：

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (取决于配置颜色) (0,3) - 布局配置1

- \textcolor[rgb]{0,1,1}{$\blacksquare$} (取决于配置颜色) (0,4) - 布局配置2

- \textcolor[rgb]{0,0,0}{$\square$} (0,1) - 分屏模式，将布局分成左右两部分，左边和右边将分别是配置1和配置2

布局配置：

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (取决于配置颜色) 左侧边条 - 音高选择器

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (取决于配置颜色) (7,0) - 颜色选择器，更改当前配置的颜色组合。

- \textcolor[rgb]{0,1,1}{$\blacksquare$} (6,7) - 压力感应，当点亮时表示压力感应已开启。

- \textcolor[rgb]{1,0,0.56}{$\blacksquare$} (7,2) - [音阶选择器](#音阶表格)

- \textcolor[rgb]{1,0.31,0}{$\blacksquare$} (7,3) - 强制音阶。开启时，仅显示所选音阶中的音符；关闭时，将显示所有音符，但不在所选音阶中的音符将变暗。（关闭时为半音音阶模式，开启时为音阶模式）

- \textcolor[rgb]{1,1,0}{$\blacksquare$} (7,4) - 重叠选择器。选择每一行上方与下方重叠的程度。如果你想用一只手弹奏和弦，则此功能非常有用。（此菜单中还有一个对齐根开关。当打开时，在完成整个音阶后，下一行将重新对齐根音符）

- \textcolor[rgb]{0.37,1,0}{$\blacksquare$} (7,5) - 通道选择器，选择音符应发送到的MIDI通道。

### 音阶选择器
![](Image/note-scale.svg)

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (取决于配置颜色) 顶部 - 音阶可视化器和根音符选择器，轻触任何音符以选择为根音符。

- \textcolor[rgb]{1,0,1}{$\blacksquare$} (取决于配置颜色) 底部 - 音阶选择器，以下表格显示了可供选择的音阶。

\pagebreak
#### 音阶表格

| 编号 | 音阶                       | C | C# | D | Eb | E | F | F# | G | Ab | A | Bb | B |
|------|----------------------------|---|----|---|----|---|---|----|---|----|---|----|---|
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
## 灯光 APP
灯光 APP 是一个非常简单的应用程序，用于让 Matrix 用于布光照明等目的。

此应用非常易于操作，只需单击功能键即可更改颜色。第一个页面选择色调，第二个页面选择亮度和饱和度。

要退出此程序，在纯色照明的时候按住功能键。应用就会退出，OS返回应用程序启动器。

# Matrix OS更新
Matrix 可以通过两种方式进入 OS 更新模式：

1. 使用设置菜单左下角的红色按钮。
2. 在插入 Matrix 时长按功能键。

你还需要一个新的固件文件来更新你的 Matrix。你可以在 [Matrix OS Github](https://github.com/203Electronics/MatrixOS/releases) 的发布部分中找到它们。

Matrix将显示为USB大容量存储器驱动器在你的主机设备中。只需将所需OS的UF2文件复制到此驱动器中。Matrix将完成固件更新，并在完成后重新启动。

![](Image/firmware-upload.svg)

注意：如果箭头为红色，则表示未建立 USB 通信。尝试重新插入 Matrix 或尝试使用不同的 USB 接口。

# 特殊启动模式
Matrix 有几种特殊启动模式。在启动过程中按住指示的键将进入这些特殊模式而不是常规的 OS 启动程序。

请注意，这些键不受 OS 的旋转设置的影响。所有组合键都基于物理键的位置（顶部的 USB 接口）。

\pagebreak
## 低亮度
这个组合键将重置 Matrix 的亮度设置为最低，允许具有低功率供电能力的主机操作 Matrix。

![](Image/special-booting-low-brightness.svg)

\pagebreak
## 恢复出厂设置
这个组合键将重置 Matrix OS 的用户配置。

![](Image/special-booting-factory-reset.svg)

<!-- \pagebreak
## 硬件测试和配置
这是一个用于 Matrix 的测试模式和配置菜单。

![](Image/special-booting-factory-menu.svg) -->


# 反馈和支持
如果你对Matrix OS有任何反馈或建议，你可以在我们的Github上创建一个问题或讨论帖子来让我们知道。或者，你也可以通过电子邮件联系我们，邮箱地址为null@203.io。

如果对于本手册有任何反馈或建议，你也可以通过在我们的Github上手册的仓库创建一个问题，或者提交Pull Request的方式来为其做出贡献。

如果你需要有关Matrix的任何支持，请发送电子邮件至null@203.io，我们将尽最大努力帮助你。

你也可以加入我们的QQ群来与我们联系或者与其他玩家交流，群号为：868894656。

# 本文贡献
- Null - 203 Electronics