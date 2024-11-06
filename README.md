# plex-dvr-converter
This file converts a Plex DVR recorded TS file to an MP4 container file.  In my experience, it reduces file size 50-70%

## Usage
To use the script copy it to whatever directory you want to run the folllowing command

`python video-transcode.py /path/to/ts/files`

The script will find all the `.ts` files in that directory (NO SUBFOLDERS), then, using the `ffmpy` module in python, run `ffmpeg` on all the files to convert them to `mp4` files.  It will put the transcoded file in the same directory as the original file.  The script does NOT remove the original file.  If you want to delete the original file, you can add the `--deleteOriginal` parameter to the command and if the transcoded file is between 0.25 and 1.2 times the size of the original it will delete the original.

## Updates

### Python 3 Compatibility Update
- Updated the `video-transcoder-py3.py` script to be compatible with Python 3.
- Fixed syntax issues, primarily by modifying `print` statements to use parentheses.
- This update ensures compatibility with modern Python versions while maintaining the existing functionality.

