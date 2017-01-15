#!/usr/bin/python3

import argparse
import os
import shlex
from subprocess import Popen
from sys import stderr, argv

def main(folder):
    def _execute_cmd(cmd):
        p = Popen(shlex.split(cmd))
        if p.wait() != 0:
            print('Error when executing ' + cmd, file=stderr)
        return p.returncode == 0
    
    for root, _, files in os.walk(folder):
        for f in files:
            file_path = os.path.join(root, f)
            if not os.path.isfile(file_path):
                return 1

            if not (f.lower().endswith('.jpg') or f.lower().endswith('.mkv')):
                mkv_name = os.path.splitext(f)[0] + '.mkv'
                mkv_file_path = os.path.join(root, mkv_name)
                
    
                if not _execute_cmd('ffmpeg -i "%s" "%s"' % (file_path, mkv_file_path)):
                    return 1
                if not _execute_cmd('touch -r "%s" "%s"' % (file_path, mkv_file_path)):
                    return 1
                os.remove(file_path)

if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
