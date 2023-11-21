# AccountAutoSync
"AccountAutoSync" is a background tool designed to synchronize user accounts between a local database and the Windows operating system, with the ability to control and monitor through an icon in the notification area.
# Developed by
Developed by [Mohamed Ismail](https://www.instagram.com/mohamedismail_100/)


## Overview
This tool is designed to run as a background service, periodically adding new users from a local database to the Windows operating system and changing the `Administrator` account's password based on the database entries. It also provides a system tray icon for manual control.

## Prerequisites
- Python 3.x
- PyMySQL
- pystray
- Pillow (PIL fork)
- Schedule

Ensure that you have the required libraries installed. You can install these using pip:

pip install pymysql pystray pillow schedule
Setup
First, set up your MySQL database with the required
users
table. The application expects a
username
and
password
column.

CREATE TABLE `users` (
  `username` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`username`)
);
Then, fill in the database access credentials in the script (
host
,
user
,
password
,
db
) to allow the tool to connect to your database.

Running the Tool
To run the tool, use the following command:

python path/to/script.py
Once started, the tool will:

Add new users from the database to the Windows OS every 5 minutes.
Change the
Administrator
password every 6 minutes according to the
Administrator
user entry in the database.
Display a system tray icon for manual operation.
Functions
add_windows_users
This function adds users to Windows from the local database.

change_admin_password
This function updates the Administrator's password using the details from the
Administrator
user in the local database.

Scheduling
The tool is configured to run its synchronization tasks periodically. The schedule is defined within the script and can be adjusted as needed.

System Tray Icon
The system tray icon provides quick access to manually trigger user synchronization and password updates. It also allows the program to be exited safely.

Note
This tool requires administrative privileges to run correctly since it interacts with Windows user accounts.

