## [sx-sf][xfce-sx]

- [x] configure **laptop-mode-tools** ([#4](https://github.com/philmmanjaro/project-sx/issues/4))
- [x] as alternative we may configure **tlp** via **tlpui** and provide a sane default file for **tlp**
- [ ] fine-tune **xfce4-power-manager** settings
- [x] use **powertop** to detect parts wasting battery life and tweak it
- [ ] preconfigure hibernation
- [x] only add drivers for our specific models (consider **mhwd** just for kernel config)
- [x] test suspend/resume in several situations
- [x] enable kernel.sysrq
- [x] decide which kernel we should use (currently **linux413**)
- [x] check why hibernate and sleep is broken with **v4.12+** series
- [x] check why cpu scaling is broken with **v4.13** series
- [ ] work on modified **sx-kernels**, if they improve battery life
- [x] adopt to **XFCE-GTK3**
- [x] check if we can optimize fan control even further
- [x] test/introduce CAL OEM modes
- [x] optimize CAL OEM modes
- [x] try to make all special keys work (touchpad, flightmode, screenshot)
- [ ] add nag-screen to inform if not running on a **sx-sf** hardware
- [ ] color calibration ?
- [ ] font tuning
- [x] include pulse-equalizer with default/alternative preset(s)
- [x] 50% of volume is enough. Setup it properly
- [x] include custom wallpapers (landscapes and abstract)
- [ ] use [hdparm](https://wiki.archlinux.org/index.php/hdparm) to automatically spin down normal HDDs when not needed
- [ ] update user guide for SX usage
- [ ] write a basic guide for **SX-SF** and explain its hardware and basic functions
- [ ] start benchmarking MJR-SX Edition against other common OSs

## [sx-hc][xfce-sx]
- [ ] figure out on how to use prime best to switch gfx cards
- [ ] adopt most of the configuration based on **sx-sf**
