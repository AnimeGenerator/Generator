import json
import os

def load_config(config_path="config.json"):
    """Load configuration from JSON file"""
    default_config = {
        "api_key": "",
        "default_style": "shonen",
        "output_dir": "outputs"
    }
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return default_config
