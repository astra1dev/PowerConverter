# console.py
# this is the console version of PowerConverter

from files.console_converters import *
from colorama import Fore, Style #, Back
# from time import sleep

console_banner = Fore.GREEN + r"""                                                         
 _____                        _____                          _             
|  __ \                      / ____|                        | |            
| |__) |____      _____ _ __| |     ___  _ ____   _____ _ __| |_ ___ _ __  
|  ___/ _ \ \ /\ / / _ \ '__| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__| 
| |  | (_) \ V  V /  __/ |  | |___| (_) | | | \ V /  __/ |  | ||  __/ |    
|_|   \___/ \_/\_/ \___|_|   \_____\___/|_| |_|\_/ \___|_|   \__\___|_|    
""" + Style.RESET_ALL

creator_banner = Fore.RED + "\nV.1.5.0                                 created by kk, github.com/kk-dev7\n" + Style.RESET_ALL

converters = """
Supported File Types:

Image:      .png     .jpg     .ico     .webp
Video:      .mp4     .avi     .mov     .flv
Audio:      .mp3     .wav   
YouTube:    yt-mp3      yt-mp4      yt-thumb
"""

usage = Fore.BLUE + "\nInput Format: [FileType1]-[FileType2]  ---> example: flv-mp4\n" + Style.RESET_ALL

cont = "y"
INPUT_CONVERTER = ""

print(console_banner + creator_banner + converters + usage)


while cont == "y":
    print("Please enter a converter you want to use:")
    INPUT_Converter = input(">").lower()
    if INPUT_Converter == "png-jpg":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        png2jpg(INPUT_File)

    elif INPUT_Converter == "png-ico":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        png2ico(INPUT_File)

    elif INPUT_Converter == "png-webp":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        png2webp(INPUT_File)

    elif INPUT_Converter == "jpg-png":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        jpg2png(INPUT_File)

    elif INPUT_Converter == "jpg-ico":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        jpg2ico(INPUT_File)

    elif INPUT_Converter == "jpg-webp":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        jpg2webp(INPUT_File)

    elif INPUT_Converter == "ico-png":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        ico2png(INPUT_File)

    elif INPUT_Converter == "ico-jpg":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        ico2jpg(INPUT_File)

    elif INPUT_Converter == "ico-webp":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        ico2webp(INPUT_File)

    elif INPUT_Converter == "webp-png":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        webp2png(INPUT_File)

    elif INPUT_Converter == "webp-ico":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        webp2ico(INPUT_File)

    elif INPUT_Converter == "webp-jpg":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        webp2jpg(INPUT_File)

# Video

    elif INPUT_Converter == "mp4-mov":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        mp42mov(INPUT_File)

    elif INPUT_Converter == "mp4-avi":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        mp42avi(INPUT_File)

    elif INPUT_Converter == "mp4-flv":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        mp42flv(INPUT_File)

    elif INPUT_Converter == "mov-mp4":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        mov2mp4(INPUT_File)

    elif INPUT_Converter == "mov-avi":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        mov2avi(INPUT_File)

    elif INPUT_Converter == "mov-flv":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        mov2flv(INPUT_File)

    elif INPUT_Converter == "avi-mp4":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        avi2mp4(INPUT_File)

    elif INPUT_Converter == "avi-mov":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        avi2mov(INPUT_File)

    elif INPUT_Converter == "avi-flv":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        avi2flv(INPUT_File)

    elif INPUT_Converter == "flv-mp4":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        flv2mp4(INPUT_File)

    elif INPUT_Converter == "flv-mov":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        flv2mov(INPUT_File)

    elif INPUT_Converter == "flv-avi":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        flv2avi(INPUT_File)


# Audio

    elif INPUT_Converter == "wav-mp3":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        wav2mp3(INPUT_File)

    elif INPUT_Converter == "mp3-wav":
        INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
        mp32wav(INPUT_File)

# YouTube Downloader

    elif INPUT_Converter == "yt-mp3":
        INPUT_Link = input("Please provide a YouTube-Video Link you want to download: ")
        yt2mp3(INPUT_Link)

    elif INPUT_Converter == "yt-mp4":
        INPUT_Link = input("Please provide a YouTube-Video Link you want to download: ")
        yt2mp4(INPUT_Link)

    elif INPUT_Converter == "yt-thumb":
        INPUT_Link = input("Please provide a YouTube-Video Link you want to get the thumbnail from: ")
        ytthumb(INPUT_Link)

    else:
        print(Fore.RED + "[ERROR] That's not a valid converter!" + Style.RESET_ALL)

    print("\nDo you want to continue converting? (y/n)")
    cont = input(">")
