from PIL import Image
import os
import subprocess
from pydub import AudioSegment
from colorama import Fore, Style  # , Back
from tqdm import tqdm


# -------------------- Error Handler -------------------- #

# @error_handler is the shorthand way of saying: some_function = handle_errors(some_function)
# when some_function is called, it is actually calling the "wrapper" function returned by error_handler
# the wrapper allows you to modify or extend the behavior of the original function, without modifying its code
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print(Fore.GREEN + "[SUCCESS] File(s) successfully converted!" + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR] File(s) not found! Make sure you put in the path correctly." +
                  Style.RESET_ALL)
        except FileExistsError:
            print(Fore.RED + "[INFO] The file is already in the desired format!" + Style.RESET_ALL)
        except OSError:
            print(Fore.RED + "[ERROR] The file(s) could not be converted!" + Style.RESET_ALL)

    return wrapper


"""
All converter methods take a list of files to convert as an argument.
Then they loop through every file in the list, convert it and save it under the same file name as the original file.
"""


# -------------------- Image Conversion -------------------- #

# JPG does not support transparency. RGBA means Red, Green, Blue, Alpha. Alpha = Transparency
# So we need to discard the Alpha channel with Image.convert which converts RGBA to RGB, so we can save as JPG.
@error_handler
def anything_to_jpg(files):
    for file in tqdm(files, desc="Converting to JPG", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".jpg"
        out_file = os.path.join(out_file)
        # if the user didn't already give a jpg file
        with Image.open(file) as im:
            # if the image given has a transparent background, discard it
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
                im.save(out_file, format="JPEG")


@error_handler
def anything_to_png(files):
    for file in tqdm(files, desc="Converting to PNG", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".png"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="PNG")


@error_handler
def anything_to_ico(files):
    for file in tqdm(files, desc="Converting to ICO", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".ico"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="ICO")


@error_handler
def anything_to_webp(files):
    for file in tqdm(files, desc="Converting to WEBP", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".webp"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="WEBP")


# -------------------- Video Conversion (FFmpeg required) -------------------- #
@error_handler
def anything_to_mp4(files):
    for file in tqdm(files, desc="Converting to MP4", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".mp4"
        out_file = os.path.join(out_file)
        # call ffmpeg to convert the file, and suppress any output so the user isn't overwhelmed with text
        subprocess.call(['ffmpeg', '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@error_handler
def anything_to_mov(files):
    for file in tqdm(files, desc="Converting to MOV", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".mov"
        out_file = os.path.join(out_file)
        subprocess.call(['ffmpeg', '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@error_handler
def anything_to_avi(files):
    for file in tqdm(files, desc="Converting to AVI", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".avi"
        out_file = os.path.join(out_file)
        subprocess.call(['ffmpeg', '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@error_handler
def anything_to_flv(files):
    for file in tqdm(files, desc="Converting to FLV", unit="file", colour="#00ff00"):
        out_file, ext = os.path.splitext(file)
        out_file += ".flv"
        out_file = os.path.join(out_file)
        subprocess.call(['ffmpeg', '-i', file, out_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# -------------------- Audio Conversion -------------------- #
@error_handler
def wav_to_mp3(files):
    for file in tqdm(files, desc="Converting to MP3", unit="file", colour="#00ff00"):
        sound = AudioSegment.from_wav(file)
        file = file[:-4] + ".mp3"
        sound.export(file, format="mp3")


@error_handler
def mp3_to_wav(files):
    for file in tqdm(files, desc="Converting to WAV", unit="file", colour="#00ff00"):
        sound = AudioSegment.from_mp3(file)
        file = file[:-4] + ".wav"
        sound.export(file, format="wav")
