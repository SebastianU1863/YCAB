YCAB Internship Projects - Sebastian U | July 1st - August 22nd

This repository contains all of the programming projects I worked on during my summer internship at the YCAB foundation. Each project is organized into a folder containing the script(s). Only the budget-compiler project has an exectuable file.
Feel free to reach out again if you would like clarification or exectuables for any of the projects.

1. Log Organizers
There are three Log Organizers: Application, Error, and Webserver. All Log Organizers output csv files. Pak Erwin provided samples and example structures.

_1. The Application Log Organizer organizes Pak Erwin's application log example from the "Struktur Log untuk Application & DB" file.
_2. The Error Log Organizer organizes errors like the ones found in the "single-laravel" file. This uses RegEx to match patterns.
_3. The Webserver Log Organizer organizes the webserver logs which include various user data like the device name or ip address.

None of these scripts are executables, they are simply bits of logic Pak Erwin requested from me so that his team could incorporate them into the dashboard project.

2. Dashboard Validation
This Dashboard Validation project was requested from Pak Johannes and Pak Jeremy.
This was a part of the data compiling step in YCAB's dashboard project to shift from spreadsheets towards an application.
By calculating these values, my program was validating the accuracy of Semesta Akademi's numbers as they created the dashboard application.
If you are developing the dashboard application, this script may be useful in providing the logic for calculations behind the UI.

3. Budget Compiler
This Budget Compiler project was requested from the finance team to help calculate remaining budget amounts when budget reports are entered into the database.
I have turned my program into an executable. If you are using this program here are the steps:
_1. Download the "budget-compiler" folder
_2. Look at the templates provided, Budget Template and Payment Template are the respective templates for how your budget and payment spreadsheets/csv files should be formatted
     - If your spreadsheets/csv files do not match the templates provided, the program will not work as it matches specific column titles provided by the finance team
_3. Run the executable (.exe file) found in the dist folder. If you have downloaded the build and have everything, the code will show a popup with instructions.
     - You can select multiple budget and payment files by dragging your cursor to batch-select them.
