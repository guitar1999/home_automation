#!/usr/bin/python

import argparse, ConfigParser, datetime, ephem, sys

# Get the db config from our config file
config = ConfigParser.RawConfigParser()
config.read('/home/jessebishop/.pyconfig')
mylat = config.get('location', 'LAT')
mylon = config.get('location', 'LON')

# Temp Args
start_hour = int(sys.argv[1])

sun = ephem.Sun()
home = ephem.Observer()
home.lat = mylat
home.lon = mylon
sun.compute(home)

sunset = ephem.localtime(home.next_setting(sun))
#print sunset.ctime()
sunrise = ephem.localtime(home.next_rising(sun))
#print sunrise.ctime()

# See if the sunrise is after 6 AM
print sunrise.time() > datetime.time(start_hour,0,0)
