import os, sys

SCREEN_HEIGHT=500
SCREEN_WIDTH=800
FPS=60
GAME_SPEED=3

def img(rel_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path).replace("/","\\")