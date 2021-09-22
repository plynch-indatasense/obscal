#!/bin/sh
icalBuddy -eep notes,attendees eventsToday > ~/.calout/icalout.txt
python ~/Code/obscal/obscal.py
