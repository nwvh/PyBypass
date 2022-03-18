# Imports
import colorama
import requests
import os
import webbrowser
from pypresence import Presence
import time 

from sys import platform
from colorama import Fore, Back, Style

### Discord RPC Status, set  enabled to False to disable it
RPC = Presence(954518931756945479) #My own app id, if you want to use yours, create an application on Discord Developer Portal
RPC.connect()


##########################
enabled = True # Set it to "False" to disable it (With capital F)
##########################


if enabled == True:
  start_time = time.time()
  #You can also edit your text here
  RPC.update(state='github.com/WooxHimself', details=('Bypassing Linkvertise...'), large_image='logo', large_text='By Woox', start=start_time)
elif enabled == False:
  pass

### Color Variables
### You can edit this and set your own colors:
"""
Blue - Fore.BLUE
Red - Fore.RED
White - Fore.WHITE
Green - Fore.GREEN
Cyan - Fore.CYAN
Yellow - Fore.YELLOW
Magenta - Fore.MAGENTA
Black - Fore.BLACK

"""
b = Fore.BLUE
g = Fore.GREEN
w = Fore.WHITE
r = Fore.RED

# Because Windows and Linux has different command to clear terminal screen, we have a OS detection
if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "win32":
    os.system('cls')

#Banner
banner = Fore.RED + """

        ██████╗ ██╗   ██╗██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
        ██╔══██╗╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
        ██████╔╝ ╚████╔╝ ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
        ██╔═══╝   ╚██╔╝  ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
        ██║        ██║   ██████╔╝   ██║   ██║     ██║  ██║███████║███████║
        ╚═╝        ╚═╝   ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

"""

# Prints status of Discord RPC in Main Menu
if enabled == True:
  enabledstatus = f"{g}ON"
elif enabled == False:
  enabledstatus = f"{r}OFF"
else:
  enabledstatus = f"{r}ERROR"


#Main Menu
mainmenu = f"""

                                MAIN MENU
                                {w}RPC STATUS: {enabledstatus}
{g}                  ╔════════════════════════════════════╗
                  ║                                    ║
                  ║    [1] Start Bypasser              ║
                  ║    [2] Visit my GitHub             ║
                  ║    [3] EXIT                        ║
                  ║                                    ║
                  ║                                    ║
                  ╚════════════════════════════════════╝
"""
# Prints Banner & Main Menu
print(banner)
print(mainmenu)
print("")
# Gets user's choice
choice = input(f"                           {w}[{g}???{w}] Choice: ")

#If users enters choice 2, open github link
if choice == '2':
  print("Opening link in your default browser...")
  webbrowser.open("https://github.com/WooxHimself", new=2)
  print("Done!")

#But if he enters choice 3, the program will end itself
elif choice == '3':
  print("See ya!")
  exit()

#If choice is 1, run the main function
elif choice == '1':
  if platform == "linux" or platform == "linux2":
      os.system('clear')
  elif platform == "win32":
      os.system('cls')

  #Bypasser function to send request
  def bypasser(url):
    pl = {
      "url": url,
    }

    rq = requests.post("https://api.bypass.vip/", data=pl)
    return rq.json()

  print(banner)

  #Get the URL
  url = input(f"{w}[{g}???{w}] Enter LinkVertise URL: ")
  print(f"{w}[{b}INFO{w}] Bypassing...")

  result = bypasser(url)

  # All possible responses
  success = result['success']
  query = result['query']
  #destination = result['destination']
  timetaken = result['time_ms']

  # If the success response equals True, then print the following:
  if success == 'true' or 'True':
      try:
          destination = result['destination']
          print("""

  ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗███████╗██████╗ ██╗
  ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██║
  ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗█████╗  ██║  ██║██║
  ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║██╔══╝  ██║  ██║╚═╝
  ██████╔╝   ██║   ██║     ██║  ██║███████║███████║███████╗██████╔╝██╗
  ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═════╝ ╚═╝


          """)
          print(f"Destination URL: {destination}")
          print(f"Base URL: {query}")
          print(f"Time Taken:  {timetaken}ms")
          print("")
          print("Thank you for using PyBypass!")

      # When theres an error, there is no DESTINATION Key in the json so it throws an error    
      except KeyError:
          response = result['response']
          print(Fore.RED + """

  ███████╗██████╗ ██████╗  ██████╗ ██████╗ ██╗
  ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║
  █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝██║
  ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗╚═╝
  ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║██╗
  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝

          """)

          print(f"Link: {query}")
          print(f"Time Taken: {timetaken}ms")
          print(f"Error: {response}")

#Thats it!