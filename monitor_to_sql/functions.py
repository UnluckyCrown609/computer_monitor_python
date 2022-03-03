import pandas as pd
import wmi
import time


def sensor_scan():
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
    sensors = w.Sensor()
    temps = []
    for sensor in sensors:
        if sensor.SensorType == u'Temperature' and not 'GPU' in sensor.Name:
            temps += [float(sensor.Value)]
        elif sensor.SensorType == u'Temperature' and 'GPU' in sensor.Name:
            temps += [float(sensor.Value)]
    time.sleep(1)
    temps = pd.DataFrame(data=temps)
    return temps


def name_scan():
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
    sensors = w.Sensor()
    names = []
    for sensor in sensors:
        if sensor.SensorType == u'Temperature' and not 'GPU' in sensor.Name:
            names += [sensor.Name]
        elif sensor.SensorType == u'Temperature' and 'GPU' in sensor.Name:
            names += [sensor.Name]
    time.sleep(1)
    names = pd.DataFrame(data=names)
    return names
