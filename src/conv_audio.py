from pydub import AudioSegment
import os
from tqdm import tqdm
from src.error_handler import error_handler

"""
All converter methods take a list of files to convert as an argument.
Then they loop through every file in the list, convert it and save it under the same file name as the original file.
"""


@error_handler
def wav_to_mp3(files):
    for file in tqdm(files, desc="Converting to MP3", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".mp3"
        out_file = os.path.join(out_file)
        sound = AudioSegment.from_wav(file)
        sound.export(out_file, format="mp3")


@error_handler
def mp3_to_wav(files):
    for file in tqdm(files, desc="Converting to WAV", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".wav"
        out_file = os.path.join(out_file)
        sound = AudioSegment.from_mp3(file)
        sound.export(out_file, format="wav")
