#!/bin/sh
icalBuddy -eep notes,attendees eventsToday > ~/.calout/icalout.txt
python3 ~/obscal/obscal.py
