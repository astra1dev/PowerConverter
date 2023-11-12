#!/usr/bin/python

# -------------------- IMPORTS -------------------- #
from files.converters import *
from colorama import Fore, Style  # , Back
import sys
import argparse


# -------------------- BANNERS -------------------- #
banner_console = Fore.GREEN + r"""                                                         
 _____                        _____                          _             
|  __ \                      / ____|                        | |            
| |__) |____      _____ _ __| |     ___  _ ____   _____ _ __| |_ ___ _ __  
|  ___/ _ \ \ /\ / / _ \ '__| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__| 
| |  | (_) \ V  V /  __/ |  | |___| (_) | | | \ V /  __/ |  | ||  __/ |    
|_|   \___/ \_/\_/ \___|_|   \_____\___/|_| |_|\_/ \___|_|   \__\___|_|    

V.1.6.2                                 created by kk, github.com/kk-dev7
""" + Style.RESET_ALL

banner_converters = """
Supported File Types:

Image:      .png     .jpg     .ico     .webp
Video:      .mp4     .avi     .mov     .flv
Audio:      .mp3     .wav   
YouTube:    yt-mp3      yt-mp4      yt-thumb
"""

banner_usage = Fore.BLUE + "\nInput Format: [FileType1]-[FileType2]  ---> example: flv-mp4\n" + Style.RESET_ALL

# -------------------- VARIABLES -------------------- #
user_continue = "y"


converters = {
    # Image
    "png-jpg": png2jpg, "png-ico": png2ico, "png-webp": png2webp,
    "jpg-png": jpg2png, "jpg-ico": jpg2ico, "jpg-webp": jpg2webp,
    "ico-png": ico2png, "ico-jpg": ico2jpg, "ico-webp": ico2webp,
    "webp-png": webp2png, "webp-ico": webp2ico, "webp-jpg": webp2jpg,

    # Video
    "mp4-mov": mp42mov, "mp4-avi": mp42avi, "mp4-flv": mp42flv,
    "mov-mp4": mov2mp4, "mov-avi": mov2avi, "mov-flv": mov2flv,
    "avi-mp4": avi2mp4, "avi-mov": avi2mov, "avi-flv": avi2flv,
    "flv-mp4": flv2mp4, "flv-mov": flv2mov, "flv-avi": flv2avi,

    # Audio
    "wav-mp3": wav2mp3, "mp3-wav": mp32wav,
}

yt_converters = {
    "yt-mp3": yt2mp3, "yt-mp4": yt2mp4, "yt-thumb": ytthumb,
}


# -------------------- FUNCTIONS -------------------- #
def convert(c):
    if c in converters:
        f = input("\n[-] Please provide the path of the file you want to convert: ")
        converters[c](f)
    elif c in yt_converters:
        youtube(yt_converters[c])
    else:
        print(Fore.RED + "[ERROR] That's not a valid converter!" + Style.RESET_ALL)


def advanced_convert(c, f):  # c = converter, f = file
    if c in converters:
        converters[c](f)
    elif c in yt_converters:
        youtube(yt_converters[c])
    else:
        print(Fore.RED + "[ERROR] That's not a valid converter!" + Style.RESET_ALL)


def youtube(c):
    c(input("\n[-] Please provide a YouTube-Video Link you want to download: "))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# DEFAULT / USER-FRIENDLY MODE
if not len(sys.argv) > 1:
    while user_continue == "y":  # While the user wants to continue converting...
        print(banner_console + banner_converters + banner_usage)
        print("[-] Please enter a converter you want to use:")
        convert(input(">").lower())
        print("\n[-] Do you want to continue converting? (y/n)")
        user_continue = input(">")
        clear_screen()


# ADVANCED MODE
else:
    print(banner_console)
    # argumentList = sys.argv[1:]

    parser = argparse.ArgumentParser(description=None)

    parser.add_argument("-f", "--file", help="Choose a file to convert", required=True)
    parser.add_argument("-c", "--converter", help="Choose a conversion method", required=True)
    # parser.add_argument("-l", "--list", help="Choose a list of files to convert")    maybe I'll add that later :D

    args = parser.parse_args()
    advanced_convert(args.converter, args.file)
