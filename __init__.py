
from mycroft import MycroftSkill
from .modules import led

class checkSettingsMeta(MycroftSkill):
    """ 
        Get settings from "settingsmeta.json"
    """
    def is_led_enabled(self):
        if self.settings.get("is_led_enabled") == "yes":
            return True
        return False
        
    def colour_scheme(self):
        return self.settings.get("colour_scheme") 


class onMessageBusEvent(MycroftSkill):
    def initialize(self):
        self.colour_scheme = checkSettingsMeta().colour_scheme()
        leds = led.execute(self.colour_scheme)
        if checkSettingsMeta().is_led_enabled() == True:
            self.add_event('mycroft.ready', leds.execute()) #,"ready"
            self.add_event('recognizer_loop:wakeword', leds.execute()) #self.colour_scheme,"wakeword"

                        

def create_skill():
    return onMessageBusEvent()


