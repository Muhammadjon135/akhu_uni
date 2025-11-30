def parse_config(config_string, required_settings):
    if config_string[-1] != ">":
        return "Error: Incomplete configuration."
    config_string = config_string[:-1]
    config_string = config_string.split("--")
     
    elements = []
    keys = []
    final_result = []
    missing_elements = []

    for item in config_string:
        item = item.split("::")
        elements.append(item[0])
        keys.append(item[1])
    for i in range(len(required_settings)):
        if required_settings[i] not in elements:
            missing_elements.append(required_settings[i])
        else:
            finder = elements.index(required_settings[i])
            final_result.append(keys[finder])
    if len(missing_elements) > 0:
        return f"Error: Missing settings: {missing_elements}"
    else:
        return final_result
            


# Test Case 1: Valid config
conf1 = "SSID::GuestNet--PASS::Secret123--IP::DHCP>"
req1 = ["SSID", "PASS", "IP"]
print(parse_config(conf1, req1))

# Test Case 2: Valid config but missing a setting
conf2 = "SSID::HomeWifi--CHANNEL::6>"
req2 = ["SSID", "PASS"]
print(parse_config(conf2, req2))

# Test Case 3: Invalid format (missing end bracket)
conf3 = "SSID::Office--PASS::Admin"
req3 = ["SSID"]
print(parse_config(conf3, req3))

# Test Case 4: Different order
conf4 = "TIMEOUT::30--PORT::8080--HOST::Localhost>"
req4 = ["HOST", "PORT", "TIMEOUT"]
print(parse_config(conf4, req4))

'''
Expected Output:
1) ['GuestNet', 'Secret123', 'DHCP']
2) Error: Missing settings: ['PASS']
3) Error: Incomplete configuration.
4) ['Localhost', '8080', '30']
'''
