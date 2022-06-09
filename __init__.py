
from mycroft import MycroftSkill
from .modules import led, update

class checkSettingsMeta(MycroftSkill):
    """ 
        Get settings from "settingsmeta.json"
    """
    def is_led_enabled(self):
        if self.settings.get("is_led_enabled", "") == "yes":
            return True
        return False
        
    def led_config(self):
        self.settings.get("led_default_config", "") 


class onMessageBusEvent(MycroftSkill):
    def initialize(self):
        self.led_config = checkSettingsMeta.led_config
        #self.add_event('mycroft.skills.initialized', update.settingsmeta_and_profile_paths())
    
        if checkSettingsMeta.is_led_enabled() == True:
            self.add_event('mycroft.ready', led.execute(self.led_config,"ready"))
            self.add_event('recognizer_loop:wakeword', led.execute(self.led_config,"wakeword"))

                        
                    

