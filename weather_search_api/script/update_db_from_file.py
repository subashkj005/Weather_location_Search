import json


def parse_json_file():
    with open('./weather_data.txt') as f:
        json_data = json.load(f)
    
    return json_data