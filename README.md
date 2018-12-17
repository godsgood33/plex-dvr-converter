# plex-dvr-converter
This file converts a Plex DVR recorded TS file to an MP4 container file.  In my experience, it reduces file size 50-70%

## Usage
To use the script copy it to whatever directory you want to run the folllowing command

`python video-transcode.py /path/to/ts/files`

The script will find all the `.ts` files in that directory (NO SUBFOLDERS), then, using the `ffmpy` module in python, run `ffmpeg` on all the files to convert them to `mp4` files.  It will put the transcoded file in the same directory as the original file.  The script does NOT remove the original file.  It leaves it to you to validate that the conversion looks ok, then you can delete the original if you like.

## Tested
I've test this on Python 2.7.5 as that is what I have on my server.  Feel free to post any bugs AND SOLUTIONS if there are problems with other versions.
