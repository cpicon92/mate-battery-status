mate-battery-status
===================

Battery Applet/Indicator for MATE Power Management
------------------------------------------------
MATE Battery Status is a project for MATE that shows information about the
laptop battery state. It has some additional features, so the usual 
mate-power-manager icon can be removed from notification/indicator area.
Battery Status doesn't rely on mate-power-manager directly, but counts
on its presence in the system for useful integration with it. 

Rationale
------------
mate-power-manager's icon has got a user interface shortcoming (if its
purpose - to show battery information) - for see exactly battery percentage or
battery lifetime, user should hover mouse to icon, wait couple seconds, and
only then user could see required information (tooltip - the bad way for
getting information in such cases). Such behavior pretty annoying, so
Battery Status' applet hasn't got such behavior and allow to user see
percentage/lifetime/charge time of battery right in panel next to icon.
Also, using mate-power-manager's icon, user can't direct place, where exactly
battery information should be showing.

/!\ Problems, which has been described above, can be solved
by using battstat-applet (Battery Charge Monitor applet), but it has some
historical architectural disadventages (such as relies on ACPI and HAL) and
user interface problems (such as using non-consistent icons) itself, and by
these reasons this applet has been declared as obsolete, has been deprecated
and removed from set of standard gnome-applets package in such key GNOME Desktop
GNU/Linux distributions as Fedora and Ubuntu.

Another impovement - warning message about critical battery charge.
mate-power-manager supports notifications (via notification-daemon/notify-osd),
and this is very useful. But when user is deep in thoughts about his current
work/task/action/etc, his locus of attention 
may just couldn't see notification-like warning about critical low (which very
important if user hasn't get access for power) - it should be message on top of
all windows.

Device information dialog (which has been totaly deprecated in last versions)
from mate-power-manager's icon has been replaced by battery
status dialog in Battery Status. In "Device Information" dialog all battery
information puts in one non-human-readable heap and this dialog doesn't meet
MATE HIG requirements partially, but in "Battery Status" dialog battery
information divided by two easy-readable areas - one for battery capacity,
and another for battery charge.

Installation
------------------
Battery Status can be installed from package, or from sources.
For better experience you should re-login after installation.
Command for installation from sources:
`python setup.py install`

Basic Usage
---------------
After adding the applet to the panel, by default it shows the icon only.
From main menu user (by default) can get access to:

 - Battery Status dialog
 - Power Statistics (provided by mate-power-manager)
 - Show setting
 - Text Size setting
 - CPU frequency scaling (provided by cpufreq-applet)
 - Power Management preferences (provided by mate-power-manager)
From context menu (by clicking right mouse button at applet) user can get
access to:

 - Bug Reporting (apport/launchpad integration)
 - MATE Power Management help
 - About information dialog
 - generic applet-related options (such as Remove, Move, Lock To Panel)
 
Additional settings
----------------------
Battery Applet uses MateConf for settings. All keys can be found in
`/apps/battery_status`. Description for each key you
can find using `mateconf-editor`.

Technical Details
-------------------------
Battery Status written in Python using:
 - PyGTK - python bindings to GTK library
 - python-appindicator - python bindings to AppIndicator library
 - MateComponent - for integration application in MATE panel as applet
 - MateConf - for keep and manage applet settings
 - UPower/DeviceKit-power - for getting power information
 - D-Bus - for getting power information from DeviceKit-power and update it on changes
