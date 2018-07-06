import time
from datetime import datetime as dt

# Path to the hosts file in Windows
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Holding values to be entered in the hosts file. Include 'www' included url too
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com"]

# Blocking websites from 8 am to 4 pm

while (True):
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
		print("Working hours")
		time.sleep(5)
