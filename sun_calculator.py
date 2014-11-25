#!/usr/bin/python

import argparse, ConfigParser, datetime, ephem

# Get the db config from our config file
config = ConfigParser.RawConfigParser()
config.read('/home/jessebishop/.pyconfig')
mylat = config.get('location', 'LAT')
mylon = config.get('location', 'LON')

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
print sunrise.time() > datetime.time(6,0,0)
