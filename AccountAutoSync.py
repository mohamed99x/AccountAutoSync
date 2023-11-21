import pymysql
import subprocess
import schedule
import time
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
from threading import Thread


# Function to add users to Windows
def add_windows_users():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='pythonapp')
        cursor = conn.cursor()

        cursor.execute("SELECT username, password FROM users")
        for row in cursor.fetchall():
            username, password = row
            command = f'net user /add "{username}" "{password}"'
            subprocess.run(command, shell=True)

        print("Users have been added successfully.")
    except pymysql.MySQLError as e:
        print(f"Failed to connect to the database: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Function to change the 'Administrator' user's password
def change_admin_password():
    try:
        conn = pymysql.connect(host='', user='', password='', db='')
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE username = 'pc'")
        result = cursor.fetchone()
        if result:
            pc_password = result[0]
            command = f'net user Administrator {pc_password}'
            subprocess.run(command, shell=True)

            print("Administrator user's password has been changed.")
        else:
            print("User 'pc' was not found.")
    except pymysql.MySQLError as e:
        print(f"Failed to connect to the database: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Scheduling periodic functions
schedule.every(5).minutes.do(add_windows_users)
schedule.every(6).minutes.do(change_admin_password)

# Continuous running function for scheduling
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Other functions for the icon
def exit_action(icon, item):
    icon.stop()

# Create an image for the icon
image = Image.new('RGB', (44, 64), color=(215, 25, 25))
draw = ImageDraw.Draw(image)
draw.text((10, 10), 'Test', fill=(0, 0, 0))

# Setting up the icon and context menu
icon = icon('test_icon', image, menu=menu(
    item('Synchronize new users', add_windows_users),
    item('Synchronize Administrator user password', change_admin_password),
    item('Exit', exit_action)
))

# Starting the icon and scheduling in parallel threads
if __name__ == '__main__':
    Thread(target=icon.run).start()
    Thread(target=run_schedule).start()
