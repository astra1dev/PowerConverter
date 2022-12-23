from PIL import Image
import os
import subprocess
from pydub import AudioSegment
from pytube import YouTube


def png2jpg(file):
    try:
        image = Image.open(file)
        rgb_image = image.convert('RGB')
        jpg_file = file[:-4] + ".jpg"
        rgb_image.save(jpg_file, format="JPG")
        print("File converted: " + file)
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def jpg2png(file):
    try:
        image = Image.open(file)
        png_file = file[:-4] + ".png"
        image.save(png_file, format="PNG")
        print("File converted: " + file)
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def png2ico(file):
    try:
        image = Image.open(file)
        ico_file = file[:-4] + ".ico"
        image.save(ico_file, format="ICO")
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def ico2png(file):
    try:
        image = Image.open(file)
        png_file = file[:-4] + ".png"
        image.save(png_file, format="PNG")
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def png2webp(file):
    try:
        image = Image.open(file)
        webp_file = file[:-4] + ".webp"
        image.save(webp_file, format="WEBP")
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def webp2png(file):
    try:
        image = Image.open(file)
        png_file = file[:-5] + ".png"
        image.save(png_file, format="PNG")
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def mov2mp4(file):
    try:
        mp4_file = file[:-4] + ".mp4"
        mp4_file = os.path.join(mp4_file)
        subprocess.call(['ffmpeg', '-i', file, mp4_file])
        print("File converted: " + file)
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def mp42mov(file):
    try:
        mov_file = file[:-4] + ".mov"
        mov_file = os.path.join(mov_file)
        subprocess.call(['ffmpeg', '-i', file, mov_file])
        print("File converted: " + file)
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def wav2mp3(file):
    try:
        sound = AudioSegment.from_wav(file)
        file = file[:-4] + ".mp3"
        sound.export(file, format="mp3")
        print("File converted: " + file)
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def mp32wav(file):
    try:
        sound = AudioSegment.from_mp3(file)
        file = file[:-4] + ".wav"
        sound.export(file, format="wav")
        print("File converted: " + file)
    except FileNotFoundError:
        print("The File was not found! Make sure you put in the path correctly.")
    except OSError:
        print("The file could not be converted!")


def yt2mp3(link):
    video = YouTube(link).streams.filter(only_audio=True).first()
    out_file = video.download()
    new_file = out_file[:-4] + ".mp3"
    subprocess.call(['ffmpeg', '-i', out_file, new_file])
    os.remove(out_file)


def yt2mp4(link):
    video = YouTube(link).streams.filter(file_extension="mp4").first()
    video.download()
