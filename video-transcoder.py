#!/usr/bin/python

import argparse
import sys
import os
import glob
import ffmpy

def create_arg_parser():
    """"Creates and returns the ArgumentParser object."""

    parser = argparse.ArgumentParser(description='Description of your app.')
    parser.add_argument('inputDirectory',
                    help='Path to the input directory.')
    parser.add_argument('--outputDirectory',
                    help='Path to the output that contains the resumes.')
    return parser

def list_files(dir):
    return glob.glob(dir + "/*.ts")

def transcode_file(file):
    ff = ffmpy.FFmpeg(
        inputs={file: None},
        outputs={file + ".mp4": '-c:v libx264 -strict -2'},
    )
    print ff.cmd
    ff.run()

def check_file(file):
    ofs = os.path.getsize(file)
    tfs = os.path.getsize(file + ".mp4")
    size_min = ofs * 0.8
    size_max = ofs * 1.2

    if tfs < size_min || tfs > size_max:
        print "Transcoded file not within reasonable size limits"
        exit
    else if tfs >= size_min && tfs <= size_max:
        print "Transcoded file within reasonable size limits"
        #os.remove(file)
        exit

if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.inputDirectory):
       files = list_files(parsed_args.inputDirectory)
       for f in files:
           transcode_file(f)
           check_file(f)
