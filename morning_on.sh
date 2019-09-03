#!/bin/bash

if [ "$(/home/jessebishop/git/home_automation/sun_calculator.py 5)" == "True" ]
then
    /home/jessebishop/git/home_automation/light_controller.py 3 0 90
    /home/jessebishop/git/home_automation/light_controller.py 6 0 90
fi
