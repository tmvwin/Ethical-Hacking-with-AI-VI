# FIFTH modula of voice assistent with automated AI wifi Pentesting with python
import os
# automated wifi network card address fetching added to be soon
print("searching for wifi Network address.......")
"""if mac address found == yes:
    #fetch MAC address & Store in List
    pass
else:
    print("No Wifi Network Address Found:")"""
print("Changing MAC adress procedure Activated")

cmd1 = ' ifconfig wlan0 down '
cmd2 = ' ifconfig wlan0 hw ether 00:11:22:33:44:55 '
cmd3 = ' ifconfig wlan0 up '
cmd4 = ' airmon-ng check kill '
cmd5 = ' ifconfig wlan0 down '
cmd6 = ' iwconfig wlan0 mode monitor '
cmd7 = ' ifconfig wlan0 up'

print(" currently Disabling Wifi Network Adopter......")
os.system(cmd1)
print("sucessfully wifi network adopter Disabled")
print("MAC address changing Procedure started........")
#Mac Address Change Conditional code  added soon...
os.system(cmd2)
print("MAC address sucessfully Changed")
print("currently Enabling wifi network Adopter........ ")
os.system(cmd3)
print("Successfully Wifi Network Adopter enabled")
print("currently activating airmon-ng network kill process..........")
os.system(cmd4)
print("sucessfully killed networking process")
print(" currently Disabling Wifi Network Adopter......")
os.system(cmd5)
print("sucessfully wifi network adopter Disabled")
print("currently started process of changing network to monitor mode............")
os.system(cmd6)
print("sucessfully monitor mode enable on wifi adopter")
print("currently Enabling wifi network Adopter........ ")
os.system(cmd7)
print("Successfully Wifi Network Adopter enabled")
print("Searching for signal.......")
