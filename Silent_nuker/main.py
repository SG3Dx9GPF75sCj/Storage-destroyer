import os, time, random, webbrowser
from os import system, name
from pathlib import Path

if os.name == 'nt':
    downloads_path = str(Path.home() / "Downloads")
else:
    downloads_path = str(os.path.join(Path.home(), "Public"))