import pywhatkit
from datetime import *

today = datetime.now()

shour = today.strftime("%H")
mob_no = input('Enter Mobile Number of Receiver : ')
msg = input('Enter Message you want to Send :')
hour = int(input('Enter Hour :'))
minute = int(input('Enter Minute :'))

pywhatkit.sendwhatmsg(mob_no , msg , hour , minute)