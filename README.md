<p align="center">
  <img src="./logo.png">
</p>

<p align="center">
  
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/badge/license-GPL-brightgreen.svg?style=plastic&logo=GNU&label=License">
  </a>
  
  <a href="https://github.com/astra1dev/PowerConverter/actions/workflows/python-app.yml">
    <img src="https://github.com/astra1dev/PowerConverter/actions/workflows/python-app.yml/badge.svg?event=push">
  </a>

  <a href="../../releases/latest">
    <img src="https://img.shields.io/github/release/astra1dev/PowerConverter.svg?label=version&style=plastic">
  </a>

  <a href="../../releases">
    <img src="https://img.shields.io/github/downloads/astra1dev/PowerConverter/total.svg?style=plastic">
  </a>
  
</p>

<p align="center">
A simple file converter written in python.

## 📋 Requirements
- [Python 3](https://python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.htm) for some audio converters

## 🛠️ Installation


Download the latest release of PowerConverter [here](https://github.com/astra1dev/PowerConverter/releases/) and unpack it in the desired location.

```shell
# Install the required packages:
pip install -r requirements.txt
```

## 👉 Usage
- User-friendly mode
```shell
python3 main.py
```
- Advanced mode
```shell
python3 main.py [-h] [-c conversion method] [-f files to convert]
```

## 🤝 Supported file types
Almost any file can be used as an input format. The following file types are supported as output formats:
| Image | Video | Audio |
|-------|-------|-------|
| PNG   | MP4   | MP3   |
| JPG   | AVI   | WAV   |
| ICO   | MOV   |       |
| WEBP  | FLV   |       |
| DDS   |       |       |
| TGA   |       |       |
| TIFF  |       |       |
| XBM   |       |       |
