#!/bin/sh
icalBuddy -eep notes,attendees eventsToday > ~/.calout/icalout.txt
python3 ~/Code/obscal/obscal.py
