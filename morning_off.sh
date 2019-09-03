#!/bin/bash

if [ "$(/home/jessebishop/git/home_automation/sun_calculator.py 5)" == "True" ]
then
    /usr/local/bin/sunwait sun up 43.921510N 70.084008W; /home/jessebishop/git/home_automation/light_controller.py 3 0 0; /home/jessebishop/git/home_automation/light_controller.py 6 0 0
fi
