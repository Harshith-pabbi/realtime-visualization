import json
import os

def load_theme_config(theme_name):
    """
    Loads theme settings from the config/themes.json file.
    """
    # Navigate to the config folder relative to this file
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'themes.json')
    
    try:
        with open(config_path, 'r') as f:
            themes = json.load(f)
            return themes.get(theme_name, themes['dark_emerald'])
    except FileNotFoundError:
        print("Warning: themes.json not found. Using default fallbacks.")
        return {
            "bg_color": "#ffffff", "ax_color": "#ffffff", 
            "grid_color": "#cccccc", "line_color": "#000000", "text_color": "#000000"
        }