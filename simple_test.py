from send_reading_test import SendReading
from atm90e32_u import ATM90e32


# ***** CALIBRATION SETTINGS *****/
linefreq = 4485  # 4485 for 60 Hz (North America)
# 389 for 50 hz (rest of the world)
pgagain = 21  # 21 for 100A (2x), 42 for >100A (4x)

ugain = 42080  # 42080 - 9v AC transformer.
# 32428 - 12v AC Transformer

igainA = 25498  # 38695 - SCT-016 120A/40mA
igainC = 25498  # 25498 - SCT-013-000 100A/50mA
# 46539 - Magnalab 100A w/ built in burden resistor

energy_sensor = ATM90e32(linefreq, pgagain, ugain, igainA, 0, igainC)
sys0 = energy_sensor.sys_status0
print('Sys status:  S0:{:#04x}   S1:{:#04x}'.format(
    sys0, energy_sensor.sys_status1))
print('meter status E0: {:#04x} S1:{:#04x}'.format(
    energy_sensor.meter_status0, energy_sensor.meter_status1))
print('Last SPI read: {:#04x}'.format(energy_sensor.lastSpiData))
if (sys0 == 0xFFFF or sys0 == 0):
    print('ERROR: not receiving data from the energy meter')
    exit(0)
v1 = energy_sensor.line_voltageA
v2 = energy_sensor.line_voltageC
i1 = energy_sensor.line_currentA
i2 = energy_sensor.line_currentC
power = energy_sensor.active_power



s = SendReading('bambi','0090')
s.send_reading(v1,v2,i1,i2,power)

