from PIL import Image
import os
import subprocess
from pydub import AudioSegment
from pytube import YouTube, exceptions
import requests
from colorama import Fore, Style #, Back
from time import sleep


# Error Handlers

def FNFError():
    print(Fore.RED + "[ERROR] The File was not found! Make sure you put in the path correctly." + Style.RESET_ALL)
    sleep(5)

def ConvError():
    print(Fore.RED + "[ERROR] The file could not be converted!" + Style.RESET_ALL)
    sleep(5)

def Success():
    print(Fore.GREEN + "[SUCCESS] File successfully converted!" + Style.RESET_ALL)
    sleep(5)

# Image Converters

def png2jpg(file):
    try:
        image = Image.open(file)
        rgb_image = image.convert('RGB')
        jpg_file = file[:-4] + ".jpg"
        rgb_image.save(jpg_file)
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def jpg2png(file):
    try:
        image = Image.open(file)
        png_file = file[:-4] + ".png"
        image.save(png_file, format="PNG")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()

def png2ico(file):
    try:
        image = Image.open(file)
        ico_file = file[:-4] + ".ico"
        image.save(ico_file, format="ICO")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        print(Fore.RED + "[ERROR] The file could not be converted!" + Style.RESET_ALL)


def ico2png(file):
    try:
        image = Image.open(file)
        png_file = file[:-4] + ".png"
        image.save(png_file, format="PNG")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def jpg2ico(file):
    try:
        image = Image.open(file)
        ico_file = file[:-4] + ".png"
        image.save(ico_file, format="ICO")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def ico2jpg(file):
    try:
        image = Image.open(file)
        rgb_image = image.convert('RGB')
        jpg_file = file[:-4] + ".jpg"
        rgb_image.save(jpg_file, format="JPG")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def png2webp(file):
    try:
        image = Image.open(file)
        webp_file = file[:-4] + ".webp"
        image.save(webp_file, format="WEBP")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def webp2png(file):
    try:
        image = Image.open(file)
        png_file = file[:-5] + ".png"
        image.save(png_file, format="PNG")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def jpg2webp(file):
    try:
        image = Image.open(file)
        webp_file = file[:-4] + ".webp"
        image.save(webp_file, format="WEBP")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def webp2jpg(file):
    try:
        image = Image.open(file)
        rgb_image = image.convert('RGB')
        jpg_file = file[:-4] + ".jpg"
        rgb_image.save(jpg_file, format="JPG")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def ico2webp(file):
    try:
        image = Image.open(file)
        webp_file = file[:-4] + ".webp"
        image.save(webp_file, format="WEBP")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def webp2ico(file):
    try:
        image = Image.open(file)
        ico_file = file[:-5] + ".png"
        image.save(ico_file, format="ICO")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()

# Video Converters

def mov2mp4(file):
    try:
        mp4_file = file[:-4] + ".mp4"
        mp4_file = os.path.join(mp4_file)
        subprocess.call(['ffmpeg', '-i', file, mp4_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def mp42mov(file):
    try:
        mov_file = file[:-4] + ".mov"
        mov_file = os.path.join(mov_file)
        subprocess.call(['ffmpeg', '-i', file, mov_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def mov2avi(file):
    try:
        avi_file = file[:-4] + ".avi"
        avi_file = os.path.join(avi_file)
        subprocess.call(['ffmpeg', '-i', file, avi_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()

def avi2mov(file):
    try:
        mov_file = file[:-4] + ".avi"
        mov_file = os.path.join(mov_file)
        subprocess.call(['ffmpeg', '-i', file, mov_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def mp42avi(file):
    try:
        avi_file = file[:-4] + ".avi"
        avi_file = os.path.join(avi_file)
        subprocess.call(['ffmpeg', '-i', file, avi_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def avi2mp4(file):
    try:
        mp4_file = file[:-4] + ".mp4"
        mp4_file = os.path.join(mp4_file)
        subprocess.call(['ffmpeg', '-i', file, mp4_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def mov2flv(file):
    try:
        flv_file = file[:-4] + ".avi"
        flv_file = os.path.join(flv_file)
        subprocess.call(['ffmpeg', '-i', file, flv_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def flv2mov(file):
    try:
        mov_file = file[:-4] + ".avi"
        mov_file = os.path.join(mov_file)
        subprocess.call(['ffmpeg', '-i', file, mov_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def mp42flv(file):
    try:
        flv_file = file[:-4] + ".avi"
        flv_file = os.path.join(flv_file)
        subprocess.call(['ffmpeg', '-i', file, flv_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def flv2mp4(file):
    try:
        mp4_file = file[:-4] + ".mp4"
        mp4_file = os.path.join(mp4_file)
        subprocess.call(['ffmpeg', '-i', file, mp4_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def avi2flv(file):
    try:
        flv_file = file[:-4] + ".avi"
        flv_file = os.path.join(flv_file)
        subprocess.call(['ffmpeg', '-i', file, flv_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def flv2avi(file):
    try:
        avi_file = file[:-4] + ".avi"
        avi_file = os.path.join(avi_file)
        subprocess.call(['ffmpeg', '-i', file, avi_file])
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()

# Audio Converters

def wav2mp3(file):
    try:
        sound = AudioSegment.from_wav(file)
        file = file[:-4] + ".mp3"
        sound.export(file, format="mp3")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()


def mp32wav(file):
    try:
        sound = AudioSegment.from_mp3(file)
        file = file[:-4] + ".wav"
        sound.export(file, format="wav")
        Success()
    except FileNotFoundError:
        FNFError()
    except OSError:
        ConvError()

# YouTube Downloaders

def yt2mp3(link):
    try:
        video = YouTube(link).streams.filter(only_audio=True).first()
        out_file = video.download()
        new_file = out_file[:-4] + ".mp3"
        subprocess.call(['ffmpeg', '-i', out_file, new_file])
        os.remove(out_file)
        print(Fore.GREEN + "[SUCCESS] Audio successfully downloaded!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.RegexMatchError:
        print(Fore.RED + "[ERROR] The video URL you entered is not valid!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.LiveStreamError:
        print(Fore.RED + "[ERROR] You entered a livestream link, not a video link!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.VideoPrivate:
        print(Fore.RED + "[ERROR] The video you entered is private!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.VideoRegionBlocked:
        print(Fore.RED + "[ERROR] The video you entered is blocked in your region!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.AgeRestrictedError:
        print(Fore.RED + "[ERROR] The video you entered is age restricted!" + Style.RESET_ALL)
        sleep(5)


def yt2mp4(link):
    try:
        video = YouTube(link).streams.filter(file_extension="mp4").first()
        video.download()
        print(Fore.GREEN + "[SUCCESS] Video successfully downloaded!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.RegexMatchError:
        print(Fore.RED + "[ERROR] The video URL you entered is not valid!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.LiveStreamError:
        print(Fore.RED + "[ERROR] You entered a livestream link, not a video link!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.VideoPrivate:
        print(Fore.RED + "[ERROR] The video you entered is private!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.VideoRegionBlocked:
        print(Fore.RED + "[ERROR] The video you entered is blocked in your region!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.AgeRestrictedError:
        print(Fore.RED + "[ERROR] The video you entered is age restricted!" + Style.RESET_ALL)
        sleep(5)

def ytthumb(link):
    try:
        thumb = YouTube(link).thumbnail_url
        r = requests.get(thumb).content
        with open('thumbnail.png', 'wb') as f:
            f.write(r)
        print(Fore.GREEN + "[SUCCESS] File successfully converted!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.RegexMatchError:
        print(Fore.RED + "[ERROR] The video URL you entered is not valid!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.LiveStreamError:
        print(Fore.RED + "[ERROR] You entered a livestream link, not a video link!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.VideoPrivate:
        print(Fore.RED + "[ERROR] The video you entered is private!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.VideoRegionBlocked:
        print(Fore.RED + "[ERROR] The video you entered is blocked in your region!" + Style.RESET_ALL)
        sleep(5)
    except exceptions.AgeRestrictedError:
        print(Fore.RED + "[ERROR] The video you entered is age restricted!" + Style.RESET_ALL)
        sleep(5)
