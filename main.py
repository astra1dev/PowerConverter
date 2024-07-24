#!/usr/bin/python
import colorama

# -------------------- IMPORTS -------------------- #
from src.conv_image import *
from src.conv_video import *
from src.conv_audio import *
from colorama import Fore, Style  # , Back
import sys
import argparse
import pathlib

# -------------------- BANNERS -------------------- #
banner_console = Fore.GREEN + r"""                                                         
 _____                        _____                          _             
|  __ \                      / ____|                        | |            
| |__) |____      _____ _ __| |     ___  _ ____   _____ _ __| |_ ___ _ __  
|  ___/ _ \ \ /\ / / _ \ '__| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__| 
| |  | (_) \ V  V /  __/ |  | |___| (_) | | | \ V /  __/ |  | ||  __/ |    
|_|   \___/ \_/\_/ \___|_|   \_____\___/|_| |_|\_/ \___|_|   \__\___|_|    

v1.6.5                           created by Astral, github.com/astra1dev
""" + Style.RESET_ALL

banner_converters = """
Supported File Types:

Image:       PNG     JPG     ICO     WEBP 
             DDS     TGA     TIFF    XBM
Video:       MP4     AVI     MOV     FLV
Audio:       MP3     WAV 
"""

banner_usage = Fore.BLUE + "\nInput Format: to-[DesiredFormat]  ---> example: to-mp4\n" + Style.RESET_ALL

# -------------------- VARIABLES -------------------- #

converters = {
    # Image
    "to-jpg": to_jpg, "to-ico": to_ico, "to-webp": to_webp, "to-png": to_png,
    "to-dds": to_dds, "to-tga": to_tga, "to-tiff": to_tiff, "to-xbm": to_xbm,

    # Video
    "to-mov": to_mov, "to-mp4": to_mp4, "to-avi": to_avi, "to-flv": to_flv,

    # Audio
    "wav-mp3": wav_to_mp3, "mp3-wav": mp3_to_wav,
}


# -------------------- FUNCTIONS -------------------- #
def convert(c):
    if c in converters:
        f = input("\n[-] Please provide the path of the file you want to convert: ")
        f = [f.strip() for f in f.split(';')]
        converters[c](f)
    else:
        print(Fore.RED + "[ERROR] Please provide a valid converter!" + Style.RESET_ALL)


def advanced_convert(c, f):  # c = converter, f = files
    if not f:
        print(Fore.RED + "[ERROR] Please provide either a single file or a list of files." + Style.RESET_ALL)
        return

    # if the user provided a single file, make a list out of it
    if not isinstance(f, list):
        f = [f]

    # check the given converter and if valid, convert the file
    if c in converters:
        converters[c](f)
    else:
        print(Fore.RED + "[ERROR] Please provide a valid converter!" + Style.RESET_ALL)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    user_continue = "y"
    # DEFAULT / USER-FRIENDLY MODE
    if not len(sys.argv) > 1:
        while user_continue.lower() == "y":  # While the user wants to continue converting...
            print(banner_console + banner_converters + banner_usage)
            print("[-] Please enter a converter you want to use:")
            convert(input(">"))
            print("\n[-] Do you want to continue converting? (y/n)")
            user_continue = input(">")
            clear_screen()

    # ADVANCED MODE
    else:
        print(banner_console)
        # argumentList = sys.argv[1:]

        parser = argparse.ArgumentParser(description=None)

        parser.add_argument("-f", "--file", help="path of file(s) to convert",
                            dest="file_list", type=pathlib.Path, nargs="+")
        # nargs="+" allows for input of one or more files
        parser.add_argument("-c", "--converter", help="conversion method")

        args = parser.parse_args()

        if args.file_list:
            # if files are given, pass them to convert function
            advanced_convert(args.converter, args.file_list)
        else:
            print(Fore.RED + "[ERROR] Please specify file(s) to convert!" + Style.RESET_ALL)


if __name__ == "__main__":
    colorama.init()
    colorama.just_fix_windows_console()
    try:
        main()
    except KeyboardInterrupt:
        # If user uses "Ctrl + C", exit.
        sys.exit(0)
