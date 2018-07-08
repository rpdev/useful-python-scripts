#!/usr/bin/python3
import os

import sys


def main(source, target):
    i = 0
    for root, _, files in os.walk(source):
        for f in files:
            ff = os.path.join(root, f)
            os.symlink(ff, os.path.join(target, new_name(f, target)))

def new_name(filename, target):
    num = 1
    name = filename
    ext = os.path.splitext(filename)
    while os.path.exists(os.path.join(target, name)):
        name = ext[0] + '_' + str(num) + ext[1]
        num += 1
    return name


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])