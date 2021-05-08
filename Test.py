import os, time
from os import system, name
from pathlib import Path


if os.name == 'nt':
    downloads_path = str(Path.home() / "Downloads")
else:
    downloads_path = str(os.path.join(Path.home(), "Downloads"))

if os.name == 'nt':
    documents_path = str(Path.home() / "Documents")
else:
    documents_path = str(os.path.join(Path.home(), "Documents"))

if os.name == 'nt':
    desktop = str(Path.home() / "Desktop")
else:
    desktop = str(os.path.join(Path.home(), "Desktop"))

if os.name == 'nt':
    Music = str(Path.home() / "Music")
else:
    Music = str(os.path.join(Path.home(), "Music"))

if os.name == 'nt':
    Movies = str(Path.home() / "Movies")
else:
    Movies = str(os.path.join(Path.home(), "Movies"))

if os.name == 'nt':
    Photos = str(Path.home() / "Photos")
else:
    Photos = str(os.path.join(Path.home(), "Pictures"))

f = open('Bruh.txt', 'w')
for _ in range(100):
    f.write('﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽'+
    '﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽'+
    '﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽'+
    '﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽\n')