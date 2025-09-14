# midi-controller

I wrote this because I wanted to use plugins from Polychrome/Neural DSP without having to fire up a DAW.
I want the tones from these plugins but still want to switch between patches easily like a FX unit/pedal,
**without having to buy a MIDI switcher.**
This holds up well when the songs need not so frequent tone changes,
and there is a second of respite between sections to quickly press a number key on the keyboard with my hand.
This is mostly what I play, so it fits me. :-)


Tested on M1 Macbook Pro (2022) with Sequoia 15.6.1.

# Setup

Run this to install all dependencies.

```bash
sh install.sh
```

Go to `Audio MIDI Setup -> Window -> Show MIDI Studio`.
Double-click on `IAC driver`, check `Device is online`, click on `Bus 1`.
(If not available, add a port called `Bus 1`).

If you have multiple MIDI channels, this program is going to pick one.
Change the code to choose a particular channel of your liking.

Go to System settings and enable input monitoring for your terminal.


# Running

```bash
source .venv/bin/activate

python3 __main__.py
```

# Controls

Currently, keys 0-9 fire Program change commands,
and `j` and `h` are used to go up and down banks, respectively.

The program change command fired is `bank * 10 + (key - 1)`
where `key` is the number pressed between 0-9.
Due to the common keyboard layout where a 0 is placed after 9, 0 is considered as 10.

So, in bank 0, pressing 1 gives you PC#0, 2 gives you PC#1, ..., 0 gives you PC#9.

# Connecting to a MIDI Sink

Usually plugins/softwares that accept MIDI have the MIDI channel they are feeding from as an audio I/O parameter.
Change it to use IAC Driver Bus 1 (or whatever you configured in MIDI studio).