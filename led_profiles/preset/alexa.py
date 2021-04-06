#!/usr/bin/env python3
# The Alexa Echo device light colour scheme:
# https://www.amazon.com/gp/help/customer/display.html?nodeId=GKLDRFT7FP4FZE56

from apa102_pi.driver import apa102
from gpiozero import LED
import time

#led = LED(5)
#led.on()

# Initialize the library and the strip
#strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')

# Increase the brightness to 100% (from the default of 12.5%)
#strip.set_global_brightness(31)
 
#-------------------------------#

class setttings():
    def startingUp():
        #Google calls this "boot up"
        pass
    
    def connectingToWifi():
        pass
    
    def beingFactoryReset():
        pass
    
    
    class readyFor():
        def setup():
            pass
        
        def verification():
            pass
    
    
class volume():
    def current():
        pass
    
    def muted():
        pass
    
    class change():
        def up():
            pass
        
        def down():
            pass
        
        



#--------------------------

class micoff():
    pass

#--------------------------

class update():
    def downloading():
        pass
    
    def installing():
        pass
    
    def takingTooLong():
        pass
    
#--------------------------

class ringing():
    def call():
        pass
    
    def alarm():
        pass
    
    def timer():
        pass

#--------------------------

class other():
    def listening():
        pass
    
    def processing():
        pass
    
    def responding():
        pass
    
    def do_not_disturb():
        pass
    
    def notification():
        pass

#--------------------------



