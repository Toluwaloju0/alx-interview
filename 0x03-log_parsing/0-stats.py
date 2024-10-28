#!/usr/bin/python3
"""A module to print from stdin"""

import re
import sys
import signal
from typing import Dict


def print_file(file_size: int, status_code: Dict):
    """A function to print status codes and file size"""

    print(f'File size: {file_size}')
    for key, value in status_code.items():
        if value > 0:
            print(f"{key}: {value}")


# Get all variables ready
status_code = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
file_size = 0
count = 0
i_format = re.compile(r'^(\S+) - \[(.*?)\] "(GET \/projects\/\d+ HTTP\/1\.1)" (\d{3}) (\d+)$')


def handler(signum, frame):
    """Handle SIGINT signal (CTRL + C) and print statistics."""
    print_file(file_size, status_code)
    sys.exit(0)  # Exit gracefully after printing


signal.signal(signal.SIGINT, handler)

# iterate over the stdin file descriptor
for line in sys.stdin:
    if line.rstrip() == '':
        break
    if i_format.match(line):
        count += 1
        line = line.split()
        if line[-2] in status_code.keys():
            status_code[line[-2]] += 1
            file_size += int(line[-1])
    if count == 10:
        print_file(file_size, status_code)
        count = 0
print_file(file_size, status_code)
exit()
