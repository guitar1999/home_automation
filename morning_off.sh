#!/bin/bash

if [ "$(/home/jessebishop/scripts/home_automation/sun_calculator.py)" == "True" ]
then 
    /usr/local/bin/sunwait sun up 41.569604N 70.57333W; /home/jessebishop/scripts/home_automation/light_controller.py 2 0 0    
fi
