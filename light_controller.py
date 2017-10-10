#!/usr/bin/python

import argparse, ConfigParser, os, sys

# Get the db config from our config file
config = ConfigParser.RawConfigParser()
config.read('/home/jessebishop/.pyconfig')
pi_ip = config.get('zwave', 'PI_IP')
pi_port = config.get('zwave', 'PI_PORT')
z_user = config.get('zwave', 'Z_USER')
z_passwd = config.get('zwave', 'Z_PASSWD')

# Temp argument
device = sys.argv[1]
instance = sys.argv[2]
level = sys.argv[3]

login_url = "http://{0}:{1}/ZAutomation/api/v1/login".format(pi_ip, pi_port)
url = "http://{0}:{1}/ZWaveAPI/Run/devices[{2}].instances[{3}].SwitchMultilevel.Set({4})".format(pi_ip, pi_port, device, instance, level)

os.system('''wget --save-cookies /tmp/cookies.txt --keep-session-cookies --post-data 'login={0}&password={1}' --delete-after {2}'''.format(z_user, z_passwd, login_url))
os.system('''wget --load-cookies /tmp/cookies.txt "{0}"'''.format(url))
