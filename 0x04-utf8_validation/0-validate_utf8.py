#!/usr/bin/python3
"""A module to validate utf-8 content"""

import sys


def validUTF8(data):
    """A function to validate utf-8 contents"""
    # iterate each number and shift the bits to the last 2
    for char in data:
        num = char >> 6
        if num > 3:
            return False

    return True
