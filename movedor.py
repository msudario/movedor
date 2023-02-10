#!/usr/bin/env python3

import os
import shutil
import argparse

parser = argparse.ArgumentParser(
    description='move files with a specific extension to a folder')
parser.add_argument('-f', '--format', metavar='', type=str, required=True,
                    help='The extension of the files to move, i.e: ".gbk"')
parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='The path to the directory where the files are located, i.e "/path/to/input/folder"')
parser.add_argument('-o', '--outdir', metavar='', type=str, required=True,
                    help='The path to the directory where the files should be moved to, i.e "/path/to/output/folder"')

args = parser.parse_args()

for root, dirs, files in os.walk(args.input):
    for file in files:
        if file.endswith(args.format):
            destination_folder = os.path.join(
                args.outdir, args.format + '_files')
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)
            shutil.copy(source_file, destination_file)
