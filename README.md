

# <img src='https://user-images.githubusercontent.com/53785846/111136788-00251f00-8576-11eb-83c9-62c6e5933e7c.png' card_color='#22a7f0' width='70' height='70' style='vertical-align:bottom'/> **Respeaker APA102 LED**

<span style="color:red">Cant find my Raspberry Pi<br/>  R.I.P project </span>

## **About:**

This is a Mycroft skill, to enable LED lights, on Respeaker devices using the APA102 LED's.

## **Disclaimer:**

This skill currently does not work.

Button on respeaker hardware is not supported.

## **Supported Respeaker devices:**
* ReSpeaker USB 6+1 Mic Array
* May work with other devices, but not tested. 


## **Examples:**
* "Enable Mycroft LED"
* "Disable Mycroft LED"
* "Change inactive LED colour to Blue"
* "Set LED brightness to 50"

## **Instructions:**
#### Adding Custom LED profile
In order to create a custom LED profile, 
* Add your python file to the "led_profiles/custom" following the templates within the "led_profiles/default".
### Enabling custom profile from the website.
* Disable default LED profiles.
* Select the newly added profile from the skill settings page on mycroft.
### Enabling custom profile from "settingsmeta.json"
* Go to the mycroft skills folder
* Open this skill's folder.
* Open settingsmeta.jon
* Make sure the value of "default_or_custom" under the LED section, is set too "custom".
* If your skill isn't already listed within the "options" of "led_custom_config" then add it.
* Change "value" to the name of your python file, without the ".py" extension.

## **Credits:**
* tinue         |   https://github.com/tinue/apa102-pi
* J1nx          |   https://github.com/j1nx/respeaker-4mic-hat-skill
* Respeaker     |   https://github.com/respeaker/pixel_ring
* domcross      |   https://github.com/domcross/respeaker-io-skill

## **Category:**

Configuration

## **Tags:**

#configuration #led #colour #respeaker #apa102

