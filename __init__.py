
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
        led_scheme_execute = led.execute(self.colour_scheme)
        if checkSettingsMeta().is_led_enabled() == True:
            self.add_event('mycroft.ready', led_scheme_execute.ready)
            self.add_event('recognizer_loop:wakeword', led_scheme_execute.wakeword)
            self.add_event('mycroft.mic.mute', led_scheme_execute.mute) 
            self.add_event('mycroft.mic.unmute', led_scheme_execute.unmute) 
            self.add_event('mycroft.volume.increase', led_scheme_execute.volume_change) 
            self.add_event('mycroft.volume.decrease', led_scheme_execute.volume_change) 

                        

def create_skill():
    return onMessageBusEvent()


