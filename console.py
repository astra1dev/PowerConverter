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

converters = """
------------------------------------------------
IMAGE:
png2jpg     jpg2png     ico2png     webp2png
png2ico     jpg2ico     ico2jpg     webp2ico
png2webp    jpg2webp    ico2webp    webp2jpg
------------------------------------------------
VIDEO: (ffmpeg required)
mp42mov     mov2mp4     avi2mp4     flv2mp4
mp42avi     mov2avi     avi2mov     flv2mov
mp42flv     mov2flv     avi2flv     flv2avi
------------------------------------------------
AUDIO: (ffmpeg required)
mp32wav     wav2mp3
------------------------------------------------
YOUTUBE DOWNLOADER: (ffmpeg required)
yt2mp3      yt2mp4
------------------------------------------------
"""

print(console_banner + converters)
print("\nPlease enter a converter you want to use:")
INPUT_Converter = input(">").lower()


# Image

if INPUT_Converter == "png2jpg":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    png2jpg(INPUT_File)

elif INPUT_Converter == "png2ico":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    png2ico(INPUT_File)

elif INPUT_Converter == "png2webp":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    png2webp(INPUT_File)

elif INPUT_Converter == "jpg2png":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    jpg2png(INPUT_File)

elif INPUT_Converter == "jpg2ico":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    jpg2ico(INPUT_File)

elif INPUT_Converter == "jpg2webp":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    jpg2webp(INPUT_File)

elif INPUT_Converter == "ico2png":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    ico2png(INPUT_File)

elif INPUT_Converter == "ico2jpg":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    ico2jpg(INPUT_File)

elif INPUT_Converter == "ico2webp":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    ico2webp(INPUT_File)

elif INPUT_Converter == "webp2png":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    webp2png(INPUT_File)

elif INPUT_Converter == "webp2ico":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    webp2ico(INPUT_File)

elif INPUT_Converter == "webp2jpg":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    webp2jpg(INPUT_File)

# Video

elif INPUT_Converter == "mp42mov":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mp42mov(INPUT_File)

elif INPUT_Converter == "mp42avi":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mp42avi(INPUT_File)

elif INPUT_Converter == "mp42flv":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mp42flv(INPUT_File)

elif INPUT_Converter == "mov2mp4":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mov2mp4(INPUT_File)

elif INPUT_Converter == "mov2avi":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mov2avi(INPUT_File)

elif INPUT_Converter == "mov2flv":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mov2flv(INPUT_File)

elif INPUT_Converter == "avi2mp4":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    avi2mp4(INPUT_File)

elif INPUT_Converter == "avi2mov":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    avi2mov(INPUT_File)

elif INPUT_Converter == "avi2flv":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    avi2flv(INPUT_File)

elif INPUT_Converter == "flv2mp4":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    flv2mp4(INPUT_File)

elif INPUT_Converter == "flv2mov":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    flv2mov(INPUT_File)

elif INPUT_Converter == "flv2avi":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    flv2avi(INPUT_File)



# Audio

elif INPUT_Converter == "wav2mp3":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    wav2mp3(INPUT_File)

elif INPUT_Converter == "mp32wav":
    INPUT_File = input("Please provide the absolute path of the file you want to convert: ")
    mp32wav(INPUT_File)

# YouTube Downloader

elif INPUT_Converter == "yt2mp3":
    INPUT_Link = input("Please provide a YouTube-Video Link you want to download: ")
    yt2mp3(INPUT_Link)

elif INPUT_Converter == "yt2mp4":
    INPUT_Link = input("Please provide a YouTube-Video Link you want to download: ")
    yt2mp4(INPUT_Link)
