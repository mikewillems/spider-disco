---
date: 2019-08-13T09:26:34-07:00
menu: "main"
title: Quick Reference
weight: 20
---

<br>
<br>
<br>
The [Jumping Spider Disco Floor](https://github.com/mikewillems/spider-disco) is a system that creates a temperature differential between spiders during experiments observing their mating habits. 
    

# Features
- **Position Tracking** - Automatically record movements of spiders and other small subjects.
- **Temperature Monitoring** - Record relative temperatures of test subjects.
- **Selective Heating** - Heat one spider up by a specified differential.
- **Thermal and Visible Video Recording** - Review spider movements for context.
- **Adjustable Detection Parameters** - Tune the instrument for use with other subjects and in different conditions.
- **Hardware and Software Lockouts** - Prevent unauthorized or unwitting operation.
- **System Freeze Protection** - Any freeze will turn off the laser.

# Specifications
- **Target Size Range**: 2-4mm abdomen diameter<br>
    Detects dark areas, 20-90 visible camera pixels by default and can be changed in the *config.json* file. This translates to spider abdomens 2mm - 4mm in diameter.

- **Object Tracking Speed**: 0.5-1m/s<br>
    Visual tracking is processed at roughly 200fps, and objects can be tracked with high fidelity at 0.5m/s and up to 1m/s at the fixed target distance of 55cm.

- **Power Output**: 250mW<br>
    Peak optical power output is roughly 200 mW within a 1 cm<sup>2</sup> center spot. For comparison, midday sun has an optical power of ~100mW per cm<sup>2</sup>.

- **Thermal Resolution**: 50mK<br>
    The instrument's specs are limited by those of the FLIR Boson core. Thermal sensitivity (minimum detectable temperature difference) is very fine at ~50mK.

- **Thermal Accuracy**: ~20%<br>
    The FLIR sensor output has only somewhat linear correlation to temperature and undergoes significant drift over time. If properly calibrated using a hot plate, a given trial can have a finer thermal accuracy. Please reference the [User Manual](/user-manual).

- **Video Resolution**: 400 x 300<br>
    This instrument uses a Basler ACE visible light camera for target tracking. Thermal camera resolution is 320 x 256. 

- **Arena Size / Field of View**: 10cm / 16&deg;<br>
    The instrument is made to house circular mating arenas up to 20cm in diameter, but the current thermal camera lens limits FoV to roughly 10cm / 16&deg;. Replacement thermal core lenses can be obtained from FLIR, and the visible camera uses a standard C-Mount lens.

- **Instrument Dimensions**: 65cm x 22cm x 22cm<br>
    While the laser unit is removable for secure transport, while the frame should be left assembled for best results.

# Preparing for Testing

#### **What's in the "Box"**
The Spider Disco system includes the following components:

1. Laser System
    1. Laser unit & enclosure
    1. Mounting bolt
    1. Keys for arming laser system (x2)
    1. Keys for enabling remote use (x2)
    1. Protective case
1. Test Enclosure (pre-assembled)
    1. Mechanical Rig
    1. Visible Camera & Mount
    1. Thermal Camera & Mount
    1. Light Source
1. Laser System PSU
1. Instrument Control PC
1. Cables
    1. PC power cable for PSU
    2. Laser unit power cable
    3. USB 3.0 cable for Basler camera
    4. USB 3.0 cable for FLIR camera
    5. micro USB 2.0 cable for light
    6. CAT5 Ethernet cable
    7. Laptop charging cable / PSU
1. Safety Equipment
    1. Broad spectrum IR-blocking glasses (x2)
 


#### **System Assembly**
To assemble your Spider Disco, first check for the presence of all components listed above. After verifying that all are present, proceed through the following steps:

1. Attach the laser unit via the steel mounting disc on its underside and the 1/4" hand screw in the black bar on top of of the laser unit. Tighten screw firmly, ensuring that the body of the laser unit extends inward toward the center of the mechanical rig with its screen pointing away from the cameras.

1. Use the PC power cable to plug in the Laser System PSU to wall power.

1. Attach the Laser System PSU to the Laser System using its 15' power cable. Both sides use the same aircraft screw connectors, and the cable is reversible. Twist the screw connectors to secure them, preventing accidental disconnection and unnecessary stress on the cable internals.

1. Attach the light to one of the USB ports on the Laser Unit using a micro USB cable.

1. Place the Instrument Control PC in sight of the arena, connecting it to wall power if necessary.

1. Connect the Instrument Control PC and the Laser Unit using an Ethernet cable.

1. Attach both external cameras to the Instrument Control PC using the included USB 3.0 cables.

1. Place the arena to be used on the base of the mechanical rig.

#### **Pre-trial Considerations** 
- **Access**
Conduct trials only in closed rooms where you can prevent entry of unwitting or unauthorized bystanders.

- **Lighting**
Visual tracking works best in indoor areas with consistent lighting.

- **Surface**
The system should be operated only on non-reflective background surfaces.

- **Tools**
Any tools used to adjust the spiders should be non-reflective.

- **Calibration**
If fine absolute temperature calibration is desired, a controllable hot plate should be available that can be put at the edge of the thermal camera's field of view.

#### **Turning on the System**
1. Turn on the Laser System PSU using the switch on its AC jack. 
1. Turn on the Laser Unit using the black rocker switch on its side.
1. Turn on the Instrument Control PC by opening its lid and pressing the power button at the top right of its keyboard.<br><br>

#### **Starting the Program**
1. On the Instrument Control PC, open a terminal (this can be done by pressing `Ctrl`, `Alt`, and `T` simultaneously).
2. Navigate within the terminal to the install directory using `CD`.
3. From the install directory, type `python run.py`.

# Experimental Workflow
After powering on the system, it is designed to walk you through the process of using it. The steps are as follows.

#### **1. Trial Setup**
After selecting `New Trial`, the Trial Setup step allows you to choose or set parameters for your trial:

- duration
- desired temperature differential
- max laser power

#### **2. Calibration**
The calibration step is not currently used and will be removed subsequently in the posted app.

#### **3. Safety Checks**
If the laser is set to off for the trial, no safety checks are necessary. Otherwise, the system will prompt you to ensure that:

- all users understand the risk
- all users are wearing eye protection
- proper area access control is in place
- the instrument is sitting on a non-reflective surface
- any tools used are non-reflective

#### **4. Specimen Loading**
Once safety checks are complete, the user must load the specimens into the arena.

Specimens are conceptually distinguished as heated vs. unheated targets, and the user must select the appropriate detected object as each target. This is done by clicking the heading at the right then clicking the detected object (the spider). The user can then press the `Swap Targets` command if necessary to ensure that the proper target is selected for heating. 

#### **5. Running the Trial**
During the trial, the system will update the positions of both spiders, as well as the temperature differential. In the event that a spider is temporarily not tracked (for example if they hop on the side of the arena or if they move while the trial is paused), then it will no longer be selected as a target once tracking resumes to recognize it. In this case, the information under that heading will be replaced with dashes `--`, and the user can simply tap the heading then tap a target on the screen to select it. This workflow requires a bit more user involvement but ensures that the wrong target is not heated by accident. The user continues to be able to use the `Swap Targets` command if necessary.

#### **6. Transferring Data**
All video, temperature, and position tracking data is saved to a single directory for each trial, named according to the trial's start date and time. The data can be transferred (or processed on the Instrument Control PC) from the trial folder, which is specified on the app home screen.
<br><br>

# Additional Safety Information
#### **Laser Classification**
At a total laser power of ~500mW and a transmitted optical power of ~250mW, this instrument's laser has a [3B classification](https://www.lasersafetyfacts.com/3B/). It is harmful to eye exposure and, since it is divergent and not focused, poses no burn risk to skin without additional optical system elements. The largest potential danger, therefore, arises from incidental focusing by additional reflective objects entering the laser's path.

#### **Eye Protection**
The included eye protection was selected for its broad spectrum of protection, which includes ultraviolet wavelengths below 390nm and infrared above 800nm. At the system wavelength of 810nm, optical power reduction was measured at 99.0%, bringing optical power well within safe limits. Nevertheless, better eye protection is readily available for these wavelengths from Honeywell which blocks more of the infrared radiation while allowing less obstructed eyesight, and we recommend contacting Honeywell for additional information. 

#### **Rig Modifications**
As the mechanical rig is made of 6061 Aluminum, it is recommended to cover its posts with a non-reflective material, for example a black vinyl sticker (provided). Additionally, there are mounting options for adding hardware to the rig, and the safety shields may be replaced or augmented as desired with larger ones that provide better coverage. Their primary design consideration is preventing users from accidentally moving their heads into the path of the laser at a close distance (where the beam has not diverged as much yet and intensity is higher).

#### **Disclaimer**
1. **Misuse**
Any use of this system outside of the designed procedure laid out in this document is at the user's sole risk and responsibility. Every effort has been made to integrate the necessary safety practices into the system and enforce their use by design. Within the designed parameters and using the required eye protection, this system poses an acceptable safety risk to users. Any use beyond these conditions must be carefully evaluated for its impact on safety.

2. **Failsafe Design**
This system is designed such that a failure of most subsystems results in the laser being turned off. This has the implication that many things can render the laser inoperable. If the laser is not operating, the use or status of any software submodule could be the source of the problem, so please refer to the [User Manual](/user-manual#troubleshooting) for troubleshooting procedures.
{{< admonition title="Caution" >}}
The exception to this design parameter is the galvo subsystem (the laser steering system), which has the ability to fail "silently" without shutting down the laser. While the galvo subsystem is designed to point the beam directly downward into the center of the arena in the event of a failure, this is the one situation to look out for from a safety perspective. If heating is being used and all signals indicate that the laser is on, but the target isn't heating up after 30-60 seconds, please use another thermal camera (such as the FLIR E-60) or a cell phone camera to ensure that the infrared beam is being directed into the arena.
{{< /admonition >}}
3. **Not Regulated**
This instrument is not approved or regulated by CE, ROHS, UL, or any other regulating body.

# Support
In the event of a system malfunction, please feel free to email Michael Willems for assistance. He will return your email at his earliest convenience.