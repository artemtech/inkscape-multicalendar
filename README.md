# Inkscape Multicalendar

This project is extended version of svgcalendar from Aurelio A. Heckert (2008). Upstream version
already included in inkscape release as main extension (see changelog).

The aim of this fork is to add new features, such as Hijri Calendar, Local Calendar (Javanese), update UI and more.
Hijri calendar is based on Kuwaiti Algorithm.

![preview](https://user-images.githubusercontent.com/22854966/204311092-56fca04f-12e2-4822-b8ad-afde5130806d.png)


## Requirements

- inkscape 1.0
- python >= 3.6

## How to Install
just copy the `multicalendar_libs, multicalendar.inx, and multicalendar.py` into inkscape user extensions folder
(usually located in `$HOME/.config/inkscape/extensions`)

Cannot find your inkscape user's extensions folder?, 
check `Edit > Preferences > System > User Extensions`

This extension also available in Gipmpscape PPA, to activate Gimpscape PPA please follow steps below:

```bash
curl -s --compressed "https://gimpscape.github.io/gimpscape-ppa/tools/KEY.gpg" | sudo apt-key add -

sudo curl -s --compressed -o /etc/apt/sources.list.d/gimpscape-ppa.list "https://gimpscape.github.io/gimpscape-ppa/tools/gimpscape-ppa.list"

sudo apt update && sudo apt install multicalendar
```

## How to Use
Open this menu: `Extensions > Render > Multicalendar`

## Features
- [x] Hijri Calendar 
...

## Changelog
See [Changelog](CHANGELOG.md)

## Donation
You can donate to support this project by visiting https://devlovers.netlify.app
