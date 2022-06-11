#!/usr/bin/env python3

from apa102_pi.driver import apa102
from gpiozero import LED
import time

class execute():
    def __init__(self, colour_scheme):
        self.colour_scheme = colour_scheme
            
    def ready(self):
        l = LED(5)
        l.on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        strip.clear_strip()
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFF0000)   
        strip.show()
        time.sleep(2) 
        strip.clear_strip()
        strip.cleanup()
        
    def wakeword(self):
        l = LED(5)
        l.on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFF0000)   
        strip.show()
        time.sleep(2) 
        strip.clear_strip()
        strip.cleanup()   

    def mute(self):
        l = LED(5)
        l.on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFF0000)   
        strip.show()

    def unmute(self):
        strip.clear_strip()
        strip.cleanup()
        l = LED(5)
        l.on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFF0000)   
        strip.show()


   
        
