

from mycroft import MycroftSkill
import importlib


class onMessageBusEvent(MycroftSkill):
    def initialize(self): 
        self.add_event('mycroft:ready', activateLedOnEvent("ready"))
        self.add_event('recognizer_loop:wakeword', activateLedOnEvent("wakeword"))
        self.add_event('mycroft:ready', activateLedOnEvent())
        self.add_event('mycroft:ready', activateLedOnEvent())



class activateLedOnEvent():
    pass


                
class settingsMeta(MycroftSkill):
    def isLedEnabled(self):
        if self.settings.get("is_led_enabled", "") == "yes":
            return True
        return False

    def customOrDefault(self):
        return self.settings.get("led_default_config", "") 
    
    def led_custom_config(self):
        return self.settings.get("led_custom_config", "") 

    def led_default_config(self):
        return self.settings.get("led_default_config", "") 



class findProfileImport():
    def preset(self):
        return importlib.import_module(".led_profiles.default." + settingsMeta.led_default_config )

    def custom(self):
        return importlib.import_module(".led_profiles.custom." + settingsMeta.led_custom_config )

