# console.py

# -------------------- IMPORTS -------------------- #
from files.console_converters import *
from colorama import Fore, Style #, Back
# from time import sleep
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
""" + Style.RESET_ALL
banner_version = Fore.RED + "\nV.1.5.0                                 created by kk, github.com/kk-dev7" + Style.RESET_ALL
banner_converters = """
Supported File Types:

Image:      .png     .jpg     .ico     .webp
Video:      .mp4     .avi     .mov     .flv
Audio:      .mp3     .wav   
YouTube:    yt-mp3      yt-mp4      yt-thumb
"""
banner_usage = Fore.BLUE + "\nInput Format: [FileType1]-[FileType2]  ---> example: flv-mp4" + Style.RESET_ALL

# -------------------- VARIABLES -------------------- #
ask_file = "Please provide the path of the file you want to convert: "
cont = "y"
converters = ["png-jpg", "png-ico", "png-webp",
              "jpg-png", "jpg-ico", "jpg-webp",
              "ico-png", "ico-jpg", "ico-webp",
              "webp-png", "webp-ico", "webp-jpg",

              "mp4-mov", "mp4-avi", "mp4-flv",
              "mov-mp4", "mov-avi", "mov-flv",
              "avi-mp4", "avi-mov", "avi-flv",
              "flv-mp4", "flv-mov", "flv-avi",

              "yt-mp4", "yt-mp3", "yt-thumb"
              ]

# -------------------- FUNCTIONS -------------------- #
def convert(i): # "i" is the selected converter, "f" will be the file (standard mode)
        # image
        if i == "png-jpg":
            f = input(ask_file)
            png2jpg(f)
        elif i == "png-ico":
            f = input(ask_file)
            png2ico(f)
        elif i == "png-webp":
            f = input(ask_file)
            png2webp(f)
        elif i == "jpg-png":
            f = input(ask_file)
            jpg2png(f)
        elif i == "jpg-ico":
            f = input(ask_file)
            jpg2ico(f)
        elif i == "jpg-webp":
            f = input(ask_file)
            jpg2webp(f)
        elif i == "ico-png":
            f = input(ask_file)
            ico2png(f)
        elif i == "ico-jpg":
            f = input(ask_file)
            ico2jpg(f)
        elif i == "ico-webp":
            f = input(ask_file)
            ico2webp(f)
        elif i == "webp-png":
            f = input(ask_file)
            webp2png(f)
        elif i == "webp-ico":
            f = input(ask_file)
            webp2ico(f)
        elif i == "webp-jpg":
            f = input(ask_file)
            webp2jpg(f)
        # video
        elif i == "mp4-mov":
            f = input(ask_file)
            mp42mov(f)
        elif i == "mp4-avi":
            f = input(ask_file)
            mp42avi(f)
        elif i == "mp4-flv":
            f = input(ask_file)
            mp42flv(f)
        elif i == "mov-mp4":
            f = input(ask_file)
            mov2mp4(f)
        elif i == "mov-avi":
            f = input(ask_file)
            mov2avi(f)
        elif i == "mov-flv":
            f = input(ask_file)
            mov2flv(f)
        elif i == "avi-mp4":
            f = input(ask_file)
            avi2mp4(f)
        elif i == "avi-mov":
            f = input(ask_file)
            avi2mov(f)
        elif i == "avi-flv":
            f = input(ask_file)
            avi2flv(f)
        elif i == "flv-mp4":
            f = input(ask_file)
            flv2mp4(f)
        elif i == "flv-mov":
            f = input(ask_file)
            flv2mov(f)
        elif i == "flv-avi":
            f = input(ask_file)
            flv2avi(f)
        # audio
        elif i == "wav-mp3":
            f = input(ask_file)
            wav2mp3(f)
        elif i == "mp3-wav":
            f = input(ask_file)
            mp32wav(f)
        # YouTube Downloader
        elif i == "yt-mp3":
            l = input("Please provide a YouTube-Video Link you want to download: ")
            yt2mp3(l)
        elif i == "yt-mp4":
            l = input("Please provide a YouTube-Video Link you want to download: ")
            yt2mp4(l)
        elif i == "yt-thumb":
            l = input("Please provide a YouTube-Video Link you want to get the thumbnail from: ")
            ytthumb(l)

        else: # If the converter is not valid
            print(Fore.RED + "[ERROR] That's not a valid converter!" + Style.RESET_ALL)


def a_convert(i, f): # "i" is the selected converter, "f" is the file (advanced mode)
    if i == "png-jpg":
        png2jpg(f)
    elif i == "png-ico":
        png2ico(f)
    elif i == "png-webp":
        png2webp(f)
    elif i == "jpg-png":
        jpg2png(f)
    elif i == "jpg-ico":
        jpg2ico(f)
    elif i == "jpg-webp":
        jpg2webp(f)
    elif i == "ico-png":
        ico2png(f)
    elif i == "ico-jpg":
        ico2jpg(f)
    elif i == "ico-webp":
        ico2webp(f)
    elif i == "webp-png":
        webp2png(f)
    elif i == "webp-ico":
        webp2ico(f)
    elif i == "webp-jpg":
        webp2jpg(f)
    # video
    elif i == "mp4-mov":
        mp42mov(f)
    elif i == "mp4-avi":
        mp42avi(f)
    elif i == "mp4-flv":
        mp42flv(f)
    elif i == "mov-mp4":
        mov2mp4(f)
    elif i == "mov-avi":
        mov2avi(f)
    elif i == "mov-flv":
        mov2flv(f)
    elif i == "avi-mp4":
        avi2mp4(f)
    elif i == "avi-mov":
        avi2mov(f)
    elif i == "avi-flv":
        avi2flv(f)
    elif i == "flv-mp4":
        flv2mp4(f)
    elif i == "flv-mov":
        flv2mov(f)
    elif i == "flv-avi":
        flv2avi(f)
    # audio
    elif i == "wav-mp3":
        wav2mp3(f)
    elif i == "mp3-wav":
        mp32wav(f)
    # YouTube Downloader
    elif i == "yt-mp3":
        yt2mp3(f)
    elif i == "yt-mp4":
        yt2mp4(f)
    elif i == "yt-thumb":
        ytthumb(f)

    else:  # If the converter is not valid
        print(Fore.RED + "[ERROR] That's not a valid converter!" + Style.RESET_ALL)

# If there are no arguments, enter default / user-friendly mode
if not len(sys.argv) > 1:
    print(banner_console + banner_version + banner_converters + banner_usage)
    while cont == "y": # While the user wants to continue converting...
        print("Please enter a converter you want to use:")
        input_converter = input(">").lower()
        convert(input_converter)
        print("\nDo you want to continue converting? (y/n)")
        cont = input(">")

# If there are arguments, enter pro /advanced mode
else:
    print(banner_console + banner_version)
    argumentList = sys.argv[1:]

    parser = argparse.ArgumentParser(description=None)          # Set up argparse to parse arguments

    parser.add_argument("-f", "--file", help="Choose a file to convert", required=True)
    # Add required file argument

    # parser.add_argument("-l", "--list", help="Choose a list of files to convert")    maybe I'll add that later :D

    parser.add_argument("-c", "--converter", help="Choose a conversion method", required=True)
    # Add required converter argument
    args = parser.parse_args()
    a_convert(args.converter, args.file)  # convert the file
