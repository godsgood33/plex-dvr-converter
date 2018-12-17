#!/usr/bin/python

import argparse
import sys
import os
import glob
import ffmpy

def create_arg_parser():
    """"Creates and returns the ArgumentParser object."""

    parser = argparse.ArgumentParser(description='This script allows you to find all .ts files in the inputDirectory and convert them to mp4 files using ffmpeg')
    parser.add_argument('inputDirectory',
                    help='Path to the input directory.')
    parser.add_argument('--deleteOriginal', default=False, action="store_true",
                    help='Decide if you want to delete the original file')
    return parser

def list_files(dir):
    return glob.glob(dir + "/*.ts")

def transcode_file(inputFile):
    outputFile = inputFile[:-2] + "mp4"
    ff = ffmpy.FFmpeg(
        inputs={inputFile: None},
        outputs={outputFile: '-c:v libx264 -strict -2'},
    )
    print ff.cmd
    ff.run()

def check_file(inputFile, deleteOriginal):
    if deleteOriginal == False:
        return
    outputFile = inputFile[:-2] + "mp4"
    ofs = os.path.getsize(inputFile)
    tfs = os.path.getsize(outputFile)
    size_min = ofs * 0.25
    size_max = ofs * 1.2

    if (tfs < size_min) or (tfs > size_max):
        print "Transcoded file not within reasonable size limits"
        print "Transcoded file size: " + tfs + " bytes"
        print "Limits:\nMin: " + size_min + "\nMax: " + size_max
        print "Original file size: " + ofs + " bytes"
        os._exit(1)
    elif tfs >= size_min and tfs <= size_max:
        print "Transcoded file within reasonable size limits"
        if deleteOriginal:
            os.remove(inputFile)

if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.inputDirectory):
       files = list_files(parsed_args.inputDirectory)
       files.sort()
       for f in files:
           transcode_file(f)
           check_file(f, parsed_args.deleteOriginal)
