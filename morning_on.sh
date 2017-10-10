#!/bin/bash

if [ "$(/home/jessebishop/scripts/home_automation/sun_calculator.py 5)" == "True" ]
then
    /home/jessebishop/scripts/home_automation/light_controller.py 3 0 90
    /home/jessebishop/scripts/home_automation/light_controller.py 4 0 90
fi
