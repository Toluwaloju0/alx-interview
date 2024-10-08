#!/usr/bin/python3
"""A module to create a lock box function"""


def canUnlockAll(boxes):
    """A function to check if all the boxes can be unlocked
    Args:
        boxes(list of list): containint=g the keys for the box
    return: True if all boxes cn be unlocked else False
    """

    checker = set([0])
    newList = []

    if boxes is None or not isinstance(boxes, (list)):
        return False
    # Iterate over the boxes, checking if the key is in the set.
    for box in range(len(boxes)):
        if box in checker:
            for key in boxes[box]:
                checker.add(key)
                if key < box:
                    for P_key in boxes[key]:
                        checker.add(P_key)
        else:
            newList.append(box)

    final = []
    # Using newList check for missing keys
    for key in newList:
        if key not in checker:
            final.append(key)

    if len(final) > 0:
        return False
    return True
