#!/usr/bin/python3
"""
Simple script for fetching information from a DS18B20 Temperature Sensor, verifying if the data is correct by CRC
and store the temperature if it's valid. The storage is done to a supplied csv file. The values stored in the csv file
is date, temperature and temperature error range.
"""
import csv
import locale
import os
import sys
from datetime import datetime, timezone
import re


def read():
    folder = [d for d in os.listdir('/sys/bus/w1/devices/') if d.startswith('28-')]
    with open(file='/sys/bus/w1/devices/{}/w1_slave'.format(folder[0]), mode='r') as f:
        crc_line, temp_line = f.readlines()
        search = re.search(r'crc=[0-9a-f]+\s+(?P<valid>.*)$', crc_line)
        if search:
            if search.group('valid') == 'YES':
                search = re.search(r't=(?P<temp>-?\d+).*$', temp_line)
                if search:
                    return int(search.group('temp'))
        return None


def store(csv_filename, temp: float, error: float):
    locale.setlocale(locale.LC_ALL, '')
    iso = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%dT%H:%M:%S,%f%z')
    with open(csv_filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([iso, '{0:n}'.format(temp), '±{0:n}'.format(error)])


def get_temp_error(temp):
    # https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf
    if -10 < temp < 85:
        return 0.5
    elif -30 < temp < 100:
        return 1.0
    elif -55 < temp < 125:
        return 2.0
    else:
        return float('NaN')


def main(csv_file):
    temp = read()
    if temp:
        temperature = temp / 1000
        store(csv_file, temperature, get_temp_error(temperature))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('{} <path-to-csv-file>'.format(sys.argv[0]))
