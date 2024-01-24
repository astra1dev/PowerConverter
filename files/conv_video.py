import os
import subprocess
from tqdm import tqdm
from files.error_handler import error_handler
from files.config_handler import path_to_ffmpeg

"""
All converter methods take a list of files to convert as an argument.
Then they loop through every file in the list, convert it and save it under the same file name as the original file.
"""


if path_to_ffmpeg() is None:
    PATH_TO_FFMPEG = "ffmpeg"
else:
    PATH_TO_FFMPEG = path_to_ffmpeg()


@error_handler
def to_mp4(files):
    for file in tqdm(files, desc="Converting to MP4", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".mp4"
        out_file = os.path.join(out_file)
        # call ffmpeg to convert the file, and suppress any output so the user isn't overwhelmed with text
        subprocess.call([PATH_TO_FFMPEG, '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@error_handler
def to_mov(files):
    for file in tqdm(files, desc="Converting to MOV", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".mov"
        out_file = os.path.join(out_file)
        subprocess.call([PATH_TO_FFMPEG, '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@error_handler
def to_avi(files):
    for file in tqdm(files, desc="Converting to AVI", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".avi"
        out_file = os.path.join(out_file)
        subprocess.call([PATH_TO_FFMPEG, '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@error_handler
def to_flv(files):
    for file in tqdm(files, desc="Converting to FLV", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".flv"
        out_file = os.path.join(out_file)
        subprocess.call([PATH_TO_FFMPEG, '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
