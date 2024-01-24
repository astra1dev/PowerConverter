from PIL import Image
import os
from tqdm import tqdm
from files.error_handler import error_handler

"""
All converter methods take a list of files to convert as an argument.
Then they loop through every file in the list, convert it and save it under the same file name as the original file.
"""


# JPG does not support transparency. RGBA means Red, Green, Blue, Alpha. Alpha = Transparency
# So we need to discard the Alpha channel with Image.convert which converts RGBA to RGB, so we can save as JPG.
@error_handler
def to_jpg(files):
    for file in tqdm(files, desc="Converting to JPG", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".jpg"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            # if the image given has a transparent background, discard it
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
                im.save(out_file, format="JPEG")


@error_handler
def to_png(files):
    for file in tqdm(files, desc="Converting to PNG", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".png"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="PNG")


@error_handler
def to_ico(files):
    for file in tqdm(files, desc="Converting to ICO", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".ico"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="ICO")


@error_handler
def to_webp(files):
    for file in tqdm(files, desc="Converting to WEBP", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".webp"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="WEBP")


@error_handler
def to_dds(files):
    for file in tqdm(files, desc="Converting to DDS", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".dds"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="DDS")


@error_handler
def to_tga(files):
    for file in tqdm(files, desc="Converting to TGA", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".tga"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="TGA")


@error_handler
def to_tiff(files):
    for file in tqdm(files, desc="Converting to TIFF", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".tiff"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="TIFF")


def to_xbm(files):
    for file in tqdm(files, desc="Converting to XBM", unit="file", colour="#00ff00"):
        out_file = os.path.splitext(file)[0] + ".xbm"
        out_file = os.path.join(out_file)
        with Image.open(file) as im:
            im.save(out_file, format="XBM")
