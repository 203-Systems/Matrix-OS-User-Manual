---
title: "Matrix OS 用户手册"
author: [203 Electronics]
date: "\\date"
footer-left: "\\leftmark"
footer-center: ""
footer-right: "\\thepage"
header-left: "\\thetitle"
header-center: ""   
header-right: "OS 版本 WIP"
toc: true
toc-own-page: true
toc-title: "目录"
header-includes: |
    \usepackage{sectsty}
    \sectionfont{\clearpage}
...

# 简介
Matrix是一款多用途的矩阵控制器，旨在以社区为中心，高度可定制，并完全开源。

Matrix OS是Matrix的灵魂，使Matrix具备多用途和强大的独立能力。所有软件功能都作为Matrix OS应用程序进行发布并且彼此完全独立。

# Matrix概述
# Matrix OS基础知识
连接Matrix电源后，将开始播放启动动画。
如果Matrix OS无法连接到主机（例如，连接到移动电源），默认的等待动画会循环播放。此时可以按下中间的功能键进入OS。

启动动画后，应用程序启动器将是操作系统显示的第一件事。

## 应用程序启动器
应用程序启动器是操作系统的主菜单。它允许用户选择要使用的应用程序。

在此菜单中，您还可以访问系统设置。

## Matrix OS设置
操作系统设置控制系统范围内的事物。例如，亮度、旋转、压力感应等。

在Matrix OS的大多数UI中，您可以按住任何亮起的按钮以查看它们的名称或含义。按住任何未点亮的键将显示当前菜单名称。

某些亮灯按键如果按住会有更高级别的控制面板（例如亮度控制）。在这种情况下，您可以按住高级控制面板中未点亮的按键以查看按钮的含义。

# Matrix OS应用程序
Matrix OS功能作为独立应用程序提供。设备的行为将完全取决于活动应用程序。

## 演奏APP
该应用程序用作灯光表演或普通Midi鼓垫。它可用于使用Amethyst Player、Ableton Live或Unipad进行灯光表演。

它发送标准的Midi信号和触后效果，因此如果它被用作鼓垫的话，它可任何接受midi的DAW兼容。

## 音符/音阶APP

## 灯光APP

# Matrix OS更新
Matrix可以以两种方式进入OS更新模式：

- 在设置菜单的左下角使用红色按钮。
- 插入Matrix时按住中心功能键。
Matrix将显示为您的设备中的U盘。只需将新OS的UF2文件复制到此U盘中。Matrix将完成固件更新，并在完成后重新启动。

# 特殊启动模式
Matrix具有几种特殊的启动模式。在启动过程中按下指示的键将进入它们，而不是常规的操作系统例程。

## 测试和配置界面
这是Matrix的测试模式和配置菜单。

## 低亮度设置
这个模式会将Matrix的亮度设置降至最低，允许使用电力输出能力较低的设计使用Matrix。

## 工厂重置
这个按键组合将重置Matrix OS的用户配置
