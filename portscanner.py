import pyfiglet 
import sys 
import socket 
from datetime import datetime
import keyboard
import validators
import ipaddress


# There are a few public IPs that can be used for testing purposes such as
#
# 45.33.32.156 which belongs to http://scanme.nmap.org/
# 176.28.50.165 for http://testphp.vulnweb.com/
   
ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print(ascii_banner) 


if len(sys.argv) != 2:
    print("Invalid number of arguments. You must add a url or IP address")
    print("Press ENTER to try again or any other key to exit")
    while True:
        event = keyboard.read_event()  # Captures all key events
        if event.event_type == "down":
            key = event.name
            print(event.name)
            if key == "enter":
                print("ENTER PRESSED!")
            break
        else:
            print("You entered an invalid choice. Exiting programme")
            sys.exit()
    input()  # captures any residual 'enter' presses
    target = input("Enter a url or IP address: ")

else:
    target = sys.argv[1]

while True:
    if validators.url(target) :
        print(f"You entered {target}")
        break
    try:
        ipaddress.ip_address(target)
        target = socket.gethostbyname(target)
        break
    except ValueError:
        print("You entered an invalid IP address. Exiting...")
        sys.exit()

print("-" * 50)

print("""The default port scan range is 1 to 100. If you wish to set the range, press 1 OR
      press ENTER to continue with default range""")
while True:
    event = keyboard.read_event()
    if event.event_type == "down":
        key = event.name
        if key == "1":
            input()
            start = int(input("start: "))
            end = int(input("end: "))
            break
        elif key == "enter":
            start = 1
            end = 100
            break
        else:
            print("You entered an invalid choice. Exiting...")
            sys.exit()


print(f"Scanning Target: {target} on ports {start} - {end}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(start, end):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\n Server not responding !!!!")
    sys.exit()