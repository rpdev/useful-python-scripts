#!/usr/bin/python3

import argparse
import os
import shlex
from subprocess import Popen
from sys import stderr
from time import strftime


def main(folder, output_folder, convert):
    def __execute_cmd__(cmd):
        p = Popen(shlex.split(cmd))
        if p.wait() != 0:
            print('Error when executing ' + cmd, file=stderr)
        return p.returncode == 0

    if not os.path.isdir(folder):
        print("'%s' is not a folder or does not exist!" % folder, file=stderr)
        return 1

    avi_files = []
    for root, _, files in os.walk(folder):
        avi_files += [os.path.join(root, f) for f in files if f.lower().endswith('.avi')]

    filename = 'video-%s' % strftime('%Y-%m-%d_%H%M')
    cmd = 'avimerge -o video-%s.avi -i \"%s\"' % (os.path.join(output_folder, filename), ', '.join(avi_files))
    if not __execute_cmd__(cmd):
        return 1

    if convert:
        if not __execute_cmd__('ffmpeg -i {0}.avi {0}.mkv'.format(os.path.join(output_folder, filename))):
            return 1
        if not __execute_cmd__('touch -r {0}.avi {0}.mkv'.format(filename)):
            return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge and convert AVI files')
    parser.add_argument('-c', '--convert', action='store_true', help='Convert avi files to mkv')
    parser.add_argument('folder', metavar='FOLDER', help='Path to root folder of avi files')
    parser.add_argument('-o', '--output-folder', type=str,
                        default=os.path.expanduser('~'),
                        help='Output folder for merged and converted videos')

    args = parser.parse_args()
    main(args.folder, args.output_folder, args.convert)
