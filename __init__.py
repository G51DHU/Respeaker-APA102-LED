
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
        
    def led_config(self):
        return self.settings.get("led_config") 


class onMessageBusEvent(MycroftSkill):
    def initialize(self):
        self.led_config = checkSettingsMeta().led_config()
        #self.add_event('mycroft.skills.initialized', update.settingsmeta_and_profile_paths())
        leds = led.execute(self.led_config)
        if checkSettingsMeta().is_led_enabled() == True:
            self.add_event('mycroft.ready', leds.execute()) #,"ready"
            self.add_event('recognizer_loop:wakeword', leds.execute()) #self.led_config,"wakeword"

                        

def create_skill():
    return onMessageBusEvent()


