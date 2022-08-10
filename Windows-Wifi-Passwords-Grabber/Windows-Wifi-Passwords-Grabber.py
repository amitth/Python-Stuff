import subprocess

# netsh wlan show profiles is the command to show wifi lists
# check_output subprocess module is used to capture the output
# splitting at "\n"
profiles = subprocess.check_output(("netsh", "wlan", "show", "profiles")).decode("utf-8").split("\n")

# Checking the word "All User Profile" in profiles list 
# If True; Splitting at ":" 
# Keeping only wifi names removing other unneccessary space and \r from the list
wifi_names = [name.split(":")[1][1:-1] for name in profiles if "All User Profile" in name]

# Formatting output
print("\n")
print("-" * 34)
print("{:25}{}".format("Wifi-Name (SSID)", "Passwords"))
print("-" * 34)

# Grabbing individual ssid (wifi) password from the above created list wifi_names
for ssid in wifi_names:
    info = subprocess.check_output(("netsh", "wlan", "show", "profile", ssid, "key=clear")).decode("utf-8").split("\n")
    password = [word.split(":")[1][1:-1] for word in info if "Key Content" in word]
    
    # Changing list to normal string
    password="".join(password)
    
    # Printing out passwords
    print("{:25}{}".format(ssid, password))




