# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
from cmath import sin
import this
import sys
import time
import math
import datetime
#import dateutil
import greet

def wait (seconds):
    time.sleep(seconds)
    print('we waited,', seconds, 'seconds')

seconds = 3
wait(seconds)

def my_sin(sinus):
    return (math.sin(sinus))

sinus = 1.05
my_sin (sinus)

def iso_now():
    output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    print(output_date)
    return(output_date)

def platform():
    print (sys.platform)
    return (sys.platform)

platform()

def supergreeting_wrapper(argu):
    print (greet.supergreeting(argu))
    return(greet.supergreeting(argu))

argu = 'bob'
supergreeting_wrapper(argu)
