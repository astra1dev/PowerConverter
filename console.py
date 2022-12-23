# console.py
# this is the console version of PowerConverter

from files.console_converters import *

console_banner = r"""                                                         
  _____                        _____                          _             
 |  __ \                      / ____|                        | |            
 | |__) |____      _____ _ __| |     ___  _ ____   _____ _ __| |_ ___ _ __  
 |  ___/ _ \ \ /\ / / _ \ '__| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__| 
 | |  | (_) \ V  V /  __/ |  | |___| (_) | | | \ V /  __/ |  | ||  __/ |    
 |_|   \___/ \_/\_/ \___|_|   \_____\___/|_| |_|\_/ \___|_|   \__\___|_|    
"""

print(console_banner + "\n\nWelcome to PowerConverter!")
INPUT_Converter = input("Available converters: png2jpg, jpg2png, png2ico, ico2png, png2webp, webp2png, mov2mp4, mp42mov,"
                        " wav2mp3, mp32wav, yt2mp3, yt2mp4\n"
                        "\nPlease enter the converting method you want:").lower()

if INPUT_Converter == "png2jpg":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    png2jpg(INPUT_File)

elif INPUT_Converter == "jpg2png":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    jpg2png(INPUT_File)

elif INPUT_Converter == "png2ico":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    png2ico(INPUT_File)

elif INPUT_Converter == "ico2png":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    ico2png(INPUT_File)

elif INPUT_Converter == "png2webp":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    png2webp(INPUT_File)

elif INPUT_Converter == "webp2png":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    webp2png(INPUT_File)

elif INPUT_Converter == "mov2mp4":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mov2mp4(INPUT_File)

elif INPUT_Converter == "mp42mov":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mp42mov(INPUT_File)

elif INPUT_Converter == "wav2mp3":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    wav2mp3(INPUT_File)

elif INPUT_Converter == "mp32wav":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mp32wav(INPUT_File)

elif INPUT_Converter == "yt2mp3":
    INPUT_Link = input("Please provide a YouTube-Video Link you want to download: ")
    yt2mp3(INPUT_Link)

elif INPUT_Converter == "yt2mp4":
    INPUT_Link = input("Please provide a YouTube-Video Link you want to download: ")
    yt2mp4(INPUT_Link)
