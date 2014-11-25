#!/usr/bin/python

import argparse, ConfigParser, os, sys

# Get the db config from our config file
config = ConfigParser.RawConfigParser()
config.read('/home/jessebishop/.pyconfig')
pi_ip = config.get('zwave', 'PI_IP')
pi_port = config.get('zwave', 'PI_PORT')

# Temp argument
device = sys.argv[1]
instance = sys.argv[2]
level = sys.argv[3]


url = "http://{0}:{1}/ZWaveAPI/Run/devices[{2}].instances[{3}].SwitchMultilevel.Set({4})".format(pi_ip, pi_port, device, instance, level)

os.system('curl -globoff -X PUT "{0}"'.format(url))
