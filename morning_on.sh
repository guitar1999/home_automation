#!/bin/bash

if [ "$(/home/jessebishop/scripts/home_automation/sun_calculator.py)" == "True" ]
then 
    /home/jessebishop/scripts/home_automation/light_controller.py 2 0 99    
fi
