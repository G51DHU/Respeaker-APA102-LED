#!/usr/bin/env python3

import commentjson, glob, os
    
class profilePaths():
    def __init__(self):
        self.globbed_profiles = {}
        self.globbed_profiles["file_paths"] = {}
        self.globbed_profiles["file_paths"]["presets"] = {}
        self.globbed_profiles["file_paths"]["custom"] = {}
        self.file_contents = {}
        
    def glob_to_find_profiles(self):
        for file in glob.glob(f"led_profiles/**/*.py", recursive=True):
            self.globbed_profiles [ "file_paths" ][ self.preset_or_custom(file) ][ os.path.basename(file) [ :-2 ]] = f"{file}"
        print(self.globbed_profiles)
        
    def get_from_file(self):
        with open("led_profile_paths.json","r") as file_contents:
            try:
                self.file_contents = commentjson.load(file_contents)
            except:
                pass
        
    def compare_maybe_update(self):
        if self.globbed_profiles != self.file_contents:
            self.write_to_file()
                
    def write_to_file(self):
        with open("led_profile_paths.json","w") as f:
            commentjson.dump(self.globbed_profiles, f, indent=4)

    def preset_or_custom(self, file):
        if file[:19] == "led_profiles/preset":
            return "presets"
        elif file[:19] == "led_profiles/custom":
            return "custom"
    
    
    
class settingsMeta():
    def __init__(self):
        self.settingsMeta_options = {}

    def get_config_options(self):
        with open("settingsmeta.json", "r") as file_contents:
            self.settingsMeta_options = commentjson.load(file_contents)["skillMetadata"]["sections"][2]["fields"][0]["options"]
            self.settingsMeta_options = self.seperate_options()

    def seperate_options(self):
        self.settingsMeta_options = self.settingsMeta_options[:-1]
        self.settingsMeta_options = self.settingsMeta_options.replace(";", "|")
        self.settingsMeta_options = self.settingsMeta_options.split("|")
        return self.settingsMeta_options
    
    def put_in_globbed_profiles(self, globbed_profiles):
        self.globbed_preset_profiles = list( globbed_profiles["file_paths"]["presets"].keys() )
        self.globbed_custom_profiles = list( globbed_profiles["file_paths"]["custom"].keys() )
        self.globbed_all_profiles =  list( self.globbed_preset_profiles + self.globbed_custom_profiles )
        self.settingsMeta_profiles_to_add = []
        self.settingsMeta_profiles_to_remove = []
        
    def compare_to_globbed_profiles(self):
        for globbed_profile in self.globbed_all_profiles:
            if globbed_profile not in (self.settingsMeta_options):
                self.settingsMeta_profiles_to_add.append( globbed_profile )
                
        for option in self.settingsMeta_options:
            if option not in self.globbed_all_profiles:
                self.settingsMeta_profiles_to_remove.append( option )

    def edit_options_if_needed(self):
        if len(self.settingsMeta_profiles_to_remove) != 0:
            self.remove_profiles_from_options()
            
        if len(self.settingsMeta_profiles_to_add) != 0:
            self.add_profiles_to_options()
            
        if ( len(self.settingsMeta_profiles_to_remove) != 0 ) or ( len(self.settingsMeta_profiles_to_add) != 0 ):
            self.sort_option_format()
            self.write_option_changes_to_file()
            
    def remove_profiles_from_options(self):
        for profile in self.settingsMeta_profiles_to_remove:
            self.settingsMeta_options.remove( profile )
        
    def add_profiles_to_options(self):
        self.settingsMeta_options = ( self.settingsMeta_options + self.settingsMeta_profiles_to_add )

    def sort_option_format(self):
        self.settingsMeta_options_capitalize = self.settingsMeta_options.copy()
        for x in range(len(self.settingsMeta_options_capitalize)):
            self.settingsMeta_options_capitalize[x] = self.settingsMeta_options_capitalize[x].capitalize()
            self.settingsMeta_options_capitalize[x] = self.settingsMeta_options_capitalize[x].replace("_", " ")
            self.settingsMeta_options.insert(x+x, f";{self.settingsMeta_options_capitalize[x]}|")
        self.settingsMeta_options = ", ".join(self.settingsMeta_options)
        self.settingsMeta_options = self.settingsMeta_options.replace(", ", "")
        self.settingsMeta_options = self.settingsMeta_options[1:]
    
    def write_option_changes_to_file(self):
        with open("settingsmeta.json", "r") as f:
            self.file_contents = commentjson.load(f)
            self.file_contents["skillMetadata"]["sections"][2]["fields"][0]["options"] = self.settingsMeta_options

        with open("settingsmeta.json", "w") as f:
            commentjson.dump( self.file_contents ,f, indent=4 )
    
    
def settingsmeta_and_profile_paths():
    paths = profilePaths()
    paths.glob_to_find_profiles()
    paths.get_from_file()
    paths.compare_maybe_update()

    settings = settingsMeta()
    settings.get_config_options()
    settings.put_in_globbed_profiles(paths.globbed_profiles)
    settings.compare_to_globbed_profiles()
    settings.edit_options_if_needed()

settingsmeta_and_profile_paths()