#!/usr/bin/env python


#* part of the mate-battery-status project
#* mate-battery-status - an applet/indicator with battery information
#* Copyright (c) 2010-2012 Ivan Zorin <ivan.a.zorin@gmail.com>
#* and Kristian Picon <kristianpicon@gmail.com>
#* see README for more information


"""applet/indicator with battery status for the MATE panel""";


from distutils.core import setup;
from distutils.command.install_data import install_data;


class InstallData(install_data):
	def run(self):
		install_data.run(self);


setup(
	name = "mate-battery-status",
	version = "0.1.2",
	maintainer = "Kristian Picon",
	maintainer_email = "kristianpicon@gmail.com",
	description = "battery status",
	license = "GNU GPL v3",
	scripts = [],
	url = "https://github.com/mate-desktop/mate-applets",
	package_dir = {},
	packages = [],
	data_files=[('/usr/lib/battery-status', ['battery-status']),
		('/usr/lib/matecomponent/servers', ['Battery_Applet.server']),
		('/usr/share/mateconf/schemas', ['battery-status.schemas']),
	],
	cmdclass={'install_data': InstallData}
)
