---
layout:     post
title:      MIDI Program Change Footswitch with Arduino
date:       2020-05-13 17:20:00
summary:    A little 2 footswitch pedal that can send MIDI program change messages using an Arduino
categories: blog
tags:       arduino midi electronics diy
published:  false
---

Well, it's been a while. I won't go into details, but I decided to expand my blog to include all my passions, namely music, coding, data and electronics. Soon (hopefully) you'll be seeing more diverse stuff here.

Let's start with a small Arduino project that I built out of necessity, which triggered my whole renewed interest in DIY electronics.

One of my guitar pedals, Eventide ModFactor, had some wonky footswitches. They didn't work half the time and it started to drove me crazy. As it's quite an old pedal, Eventide asked for 100 euros for repair, excluding shipping to and back from US! I tried going the DIY repair route, but it had proprietary switches that had be ordered from a distributor in the UK, which cost almost as much as the repair. Next option was to use an external momentary switch to change presets, but that went out the window quickly as I figured out that external aux switches cannot change presets, only banks, which would still require me to use the glitchy footswitches.

While thinking what to do, I saw the MIDI I/O on the side of the pedal. A quick look at the user manual confirmed that I can indeed change presets (or anything really) using standard MIDI program change commands. The only issue was, I didn't have anything to send such MIDI commands. Some sleepless nights researching the topic led me to the conclusion that I needed to do that with arduino, which would not only work, but be cheap and easy to build as well.

So let's start.

Parts I used:

- Arduino Nano, or a clone
- 2 momentary footswitches
- An RGB Led (I used a prebuilt one with built in SMD resistors)
  - If using bare RGB led, 3 resistors (Anything from 330Ω to 10KΩ works, depending the on the brightness you want)
- Led Bezel
- DC input jack
- 5 pin DIN MIDI jack
- Hammond 1590A enclosure
- Some cables

Equipment needed

- Soldering station
- Drill & metal drill bits (step drill bits works great)
- Hot glue or 2-part adhesive to fix everything
- Patience
