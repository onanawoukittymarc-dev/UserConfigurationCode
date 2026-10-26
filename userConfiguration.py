def add_setting(settings_dict, setting_tuple):
    key, value = setting_tuple
    # Convert key and value to lowercase
    key = str(key).lower()
    value = str(value).lower()
    
    # Check if the key already exists
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, setting_tuple):
    key, value = setting_tuple
    # Convert key and value to lowercase
    key = str(key).lower()
    value = str(value).lower()
    
    # Check if the key exists before updating
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings_dict, key):
    # Convert key to lowercase
    key = str(key).lower()
    
    # Check if the key exists before deleting
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings_dict):
    # Check if the dictionary is empty
    if not settings_dict:
        return "No settings available."
    
    # Build the display string starting with the header
    result = "Current User Settings:\n"
    
    for key, value in settings_dict.items():
        # Capitalize the key for display purposes as required
        capitalized_key = key.capitalize()
        result += f"{capitalized_key}: {value}\n"
        
    return result


# 13. Create a dictionary named test_settings to store user configuration preferences
test_settings = {}
# Add some initial settings using our add_setting function
print(add_setting(test_settings, ('Theme', 'Dark')))
print(add_setting(test_settings, ('Notifications', 'Enabled')))
print(add_setting(test_settings, ('Volume', 'High')))

# View the current settings
print("\n" + view_settings(test_settings))