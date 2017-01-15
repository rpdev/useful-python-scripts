#!/usr/bin/python3

import argparse
import os

def main(folder, file_types = ['.avi', '.mkv', '.mp4']):
    videos = {}

    for root, _, files in os.walk(folder):
        for f in files:
            name, ext = os.path.splitext(f)
            if ext.lower() in file_types:
                k = os.path.join(root, name)
                if k not in videos:
                    videos[k] = []
                videos[k] += [os.path.join(root, f)]

    for k, v in videos.items():
        if len(v) > 1:
            print(k, v)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Detects duplicated movie files')
    parser.add_argument('folder', metavar='FOLDER', help='Path to root folder')

    args = parser.parse_args()
    main(args.folder)
