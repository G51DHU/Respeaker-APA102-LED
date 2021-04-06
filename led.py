#!/usr/bin/env python3


from apa102_pi.driver import apa102
from gpiozero import LED
import time
import commentjson

def getInfoThenExecute(event, led_config):
    pass


class execute():
    def __init__(self, led_dict):
        self.led_dict = led_dict
        self.duration = led_dict[:-1]
        self.strip = apa102.APA102(num_led=12, mosi=10, sclk=11, order='rbg')
        if len(self.led_dict[0][0].upper()) == 2:
            self.brightness_global = True
            self.strip.set_global_brightness(self.led_dict[0][1])
            self.led_dict = self.led_dict[1:]
        else:
            self.brightness_global = False
            
    def execute_with_local_brightness(self):
        for LED in self.led_dict:
            self.strip.set_pixel_rgb(LED[0], f"0x{LED[1]}", LED[2])   
        self.strip.show()
        time.sleep(self.duration)
            
    def execute_with_global_brightness(self):
        for LED in self.led_dict:
            self.strip.set_pixel_rgb(LED[0], f"0x{LED[1]}")   
        self.strip.show()
        time.sleep(self.duration) 
        
    def shutdown(self):
        self.strip.clear_strip()
        self.strip.cleanup()      
        
