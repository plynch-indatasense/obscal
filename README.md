# obscal
** Please add **

__TO DO__
- Add error checking and mitigation to scripts.
- Allow Obsidian vault to be a parameter to install.
- Allow a tomorrow option to build out working page for next day.



These scripts will install and setup replication of daily events to Obsidian.  It uses a application called iCalBuddy to pull events and then formats the output for Obsidian (obscal.py)

A template for Obsidian is included.

Pre Reqs

- You must have Apple Calander configured for Amazon email and calendars.
- You Obsidian vault should be in ~/Documents/Obsidian/aws
- Ensure there is a directory in there called  /Documents/Obsidian/aws/dailyNotes/

Clone the repository

Run the install.sh

Test script by running ~/obscal/dailyrun.sh

The generated template also includes tasks and notes.


For other example of using iCalBuddy check here.  https://hasseg.org/icalBuddy/examples.html

# The MIT License
### Copyright (c) Phil Lynch 
### icalBuddy Copyright (c) Ali Rantakari

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

