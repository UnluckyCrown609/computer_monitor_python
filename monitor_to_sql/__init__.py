import subprocess
import pandas as pd
from functions import sensor_scan
from functions import name_scan

command_open = r'..\OpenHardwareMonitor\OpenHardwareMonitor.exe'
command_close = r'taskkill /F /IM "OpenHardwareMonitor.exe" /T'

subprocess.Popen(command_open)
x = 1
str_repeats = input("Number of repeats: ")
no_repeats = int(str_repeats)
dataframe_1 = name_scan()
dataframe_2 = sensor_scan()
zipped = pd.concat([dataframe_1, dataframe_2], ignore_index=True, sort=True, axis=1)
while x < no_repeats:
    x += 1
    zipped = pd.concat([zipped, sensor_scan()], ignore_index=True, sort=True, axis=1)
print(f'Temperatures:\n{zipped}')

subprocess.Popen(command_close)

