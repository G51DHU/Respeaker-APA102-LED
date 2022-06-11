#!/usr/bin/env python3

from apa102_pi.driver import apa102
from gpiozero import LED
import time

class execute():
    def __init__(self, colour_scheme):
        self.colour_scheme = colour_scheme

    def leds_on()
        l = LED(5)
        l.on()

    def ready(self):
        leds_on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        strip.clear_strip()
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFF0000)   
        strip.show()
        time.sleep(2) 
        strip.clear_strip()
        strip.cleanup()
        
    def wakeword(self):
        leds_on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        strip.clear_strip()
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0x00CAFF)   
        strip.show()
        time.sleep(3) 
        strip.clear_strip()
        strip.cleanup()   

    def mute(self):
        leds_on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        strip.clear_strip()
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFF0000)   
        strip.show()

    def unmute(self):
        leds_on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        strip.clear_strip()
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFF0000)   
        strip.show()


    def failed_wifi(self):
        leds_on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        strip.clear_strip()
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0x800080)   
        strip.show()
        time.sleep(4) 
        strip.clear_strip()
        strip.cleanup()   

    def volume_change(self):
        leds_on()
        strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        for led_num in range(12):
            strip.set_pixel_rgb(led_num, 0xFFFFFF)   
        strip.show()
        time.sleep(1.5) 
        strip.clear_strip()
        strip.cleanup()       
