from PIL import Image
import os
import subprocess
from pydub import AudioSegment
from pytube import YouTube, exceptions
import requests
from colorama import Fore, Style  # , Back
# from time import sleep
import json


# ---------- SOME EXPLANATION ---------- #
# @error_handler is the shorthand way of saying: some_function = handle_errors(some_function)
# when some_function is called, it is actually calling the "wrapper" function returned by error_handler
# the wrapper function allows you to modify or extend the behavior of the original function, without directly
# modifying its code

def get_youtube_directory():
    with (open("config.json", "r") as config):
        yt_dir = json.load(config).get("youtube_download_directory", False)  # default to true if key not found
        if yt_dir is False:
            return None
        return yt_dir


# Error Handler
def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print(Fore.GREEN + "[SUCCESS] File successfully converted!" + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + "[ERROR] The File was not found! Make sure you put in the path correctly." +
                  Style.RESET_ALL)
        except OSError:
            print(Fore.RED + "[ERROR] The file could not be converted!" + Style.RESET_ALL)

    return wrapper


def youtube_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            print(Fore.GREEN + "[SUCCESS] Video successfully downloaded!" + Style.RESET_ALL)
        except exceptions.RegexMatchError:
            print(Fore.RED + "[ERROR] The video URL you entered is not valid!" + Style.RESET_ALL)
        except exceptions.LiveStreamError:
            print(Fore.RED + "[ERROR] You entered a livestream link, not a video link!" + Style.RESET_ALL)
        except exceptions.VideoPrivate:
            print(Fore.RED + "[ERROR] The video you entered is private!" + Style.RESET_ALL)
        except exceptions.VideoRegionBlocked:
            print(Fore.RED + "[ERROR] The video you entered is blocked in your region!" + Style.RESET_ALL)
        except exceptions.AgeRestrictedError:
            print(Fore.RED + "[ERROR] The video you entered is age restricted!" + Style.RESET_ALL)

    return wrapper


# All the converters take a list of files to convert as an argument.
# Then they loop through every file in the list, convert it and save it under the same file name as the original file.

# Image Converters


@error_handler
def png2jpg(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            rgb_image = image.convert('RGB')
            jpg_file = file[:-4] + ".jpg"
            rgb_image.save(jpg_file)


@error_handler
def jpg2png(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            png_file = file[:-4] + ".png"
            image.save(png_file, format="PNG")


@error_handler
def png2ico(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            ico_file = file[:-4] + ".ico"
            image.save(ico_file, format="ICO")


@error_handler
def ico2png(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            png_file = file[:-4] + ".png"
            image.save(png_file, format="PNG")


@error_handler
def jpg2ico(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            ico_file = file[:-4] + ".ico"
            image.save(ico_file, format="ICO")


@error_handler
def ico2jpg(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            rgb_image = image.convert('RGB')
            jpg_file = file[:-4] + ".jpg"
            rgb_image.save(jpg_file, format="JPG")


@error_handler
def png2webp(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            webp_file = file[:-4] + ".webp"
            image.save(webp_file, format="WEBP")


@error_handler
def webp2png(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            png_file = file[:-5] + ".png"
            image.save(png_file, format="PNG")


@error_handler
def jpg2webp(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            webp_file = file[:-4] + ".webp"
            image.save(webp_file, format="WEBP")


@error_handler
def webp2jpg(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            rgb_image = image.convert('RGB')
            jpg_file = file[:-4] + ".jpg"
            rgb_image.save(jpg_file, format="JPG")


@error_handler
def ico2webp(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            webp_file = file[:-4] + ".webp"
            image.save(webp_file, format="WEBP")


@error_handler
def webp2ico(files):
    for file in files:
        with open(file, "rb") as f:
            image = Image.open(f)
            ico_file = file[:-5] + ".ico"
            image.save(ico_file, format="ICO")


# Video Converters
# FFmpeg is required for those!


@error_handler
def mov2mp4(files):
    for file in files:
        mp4_file = file[:-4] + ".mp4"
        mp4_file = os.path.join(mp4_file)
        subprocess.call(['ffmpeg', '-i', file, mp4_file])


@error_handler
def mp42mov(files):
    for file in files:
        mov_file = file[:-4] + ".mov"
        mov_file = os.path.join(mov_file)
        subprocess.call(['ffmpeg', '-i', file, mov_file])


@error_handler
def mov2avi(files):
    for file in files:
        avi_file = file[:-4] + ".avi"
        avi_file = os.path.join(avi_file)
        subprocess.call(['ffmpeg', '-i', file, avi_file])


@error_handler
def avi2mov(files):
    for file in files:
        mov_file = file[:-4] + ".avi"
        mov_file = os.path.join(mov_file)
        subprocess.call(['ffmpeg', '-i', file, mov_file])


@error_handler
def mp42avi(files):
    for file in files:
        avi_file = file[:-4] + ".avi"
        avi_file = os.path.join(avi_file)
        subprocess.call(['ffmpeg', '-i', file, avi_file])


@error_handler
def avi2mp4(files):
    for file in files:
        mp4_file = file[:-4] + ".mp4"
        mp4_file = os.path.join(mp4_file)
        subprocess.call(['ffmpeg', '-i', file, mp4_file])


@error_handler
def mov2flv(files):
    for file in files:
        flv_file = file[:-4] + ".avi"
        flv_file = os.path.join(flv_file)
        subprocess.call(['ffmpeg', '-i', file, flv_file])


@error_handler
def flv2mov(files):
    for file in files:
        mov_file = file[:-4] + ".avi"
        mov_file = os.path.join(mov_file)
        subprocess.call(['ffmpeg', '-i', file, mov_file])


@error_handler
def mp42flv(files):
    for file in files:
        flv_file = file[:-4] + ".avi"
        flv_file = os.path.join(flv_file)
        subprocess.call(['ffmpeg', '-i', file, flv_file])


@error_handler
def flv2mp4(files):
    for file in files:
        mp4_file = file[:-4] + ".mp4"
        mp4_file = os.path.join(mp4_file)
        subprocess.call(['ffmpeg', '-i', file, mp4_file])


@error_handler
def avi2flv(files):
    for file in files:
        flv_file = file[:-4] + ".avi"
        flv_file = os.path.join(flv_file)
        subprocess.call(['ffmpeg', '-i', file, flv_file])


@error_handler
def flv2avi(files):
    for file in files:
        avi_file = file[:-4] + ".avi"
        avi_file = os.path.join(avi_file)
        subprocess.call(['ffmpeg', '-i', file, avi_file])

# Audio Converters


@error_handler
def wav2mp3(files):
    for file in files:
        sound = AudioSegment.from_wav(file)
        file = file[:-4] + ".mp3"
        sound.export(file, format="mp3")


@error_handler
def mp32wav(files):
    for file in files:
        sound = AudioSegment.from_mp3(file)
        file = file[:-4] + ".wav"
        sound.export(file, format="wav")

# YouTube Downloaders
# FFmpeg is required to convert downloaded file to MP3 if wanted


@youtube_error_handler
def yt2mp3(links):
    for link in links:
        # Download file as mp4, then convert it to mp3 using FFmpeg, then remove the mp4 file
        video_file = YouTube(link).streams.filter(only_audio=True).first().download(output_path=get_youtube_directory())
        mp3_file = video_file[:-4] + ".mp3"
        subprocess.call(['ffmpeg', '-i', video_file, mp3_file], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        os.remove(video_file)


@youtube_error_handler
def yt2mp4(links):
    for link in links:
        YouTube(link).streams.filter(file_extension="mp4").get_highest_resolution().download(
            output_path=get_youtube_directory())


@youtube_error_handler
def ytthumb(links):
    for link in links:
        # Get the Thumbnail URL and download it
        r = requests.get(YouTube(link).thumbnail_url).content
        with open('thumbnail.png', 'wb') as f:
            f.write(r)
