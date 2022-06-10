#!/usr/bin/env python3

from apa102_pi.driver import apa102
from gpiozero import LED
import time

class execute():
    def __init__(self, colour_scheme):
        self.colour_scheme = colour_scheme
        self.strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
            
    def execute(self):
        LED(5).on()
        for led in range(12):
            self.strip.set_pixel_rgb(led, f"0xFF0000")   
        self.strip.show()
        time.sleep(2) 
        self.strip.clear_strip()
        self.strip.cleanup()      
        
