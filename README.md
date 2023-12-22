<p align="center">
  <img src="./logo.png">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=plastic&logo=python&color=3c7cae&labelColor=ffd841&logoColor=3c7cae">
  <img src="https://img.shields.io/badge/license-GPL-brightgreen.svg?style=plastic&logo=GNU&label=License">
  <img src="https://img.shields.io/badge/version-1.6.-blue.svg?style=plastic&logo=GitHub&color=ff5500&label=Version">
  <img src="https://img.shields.io/badge/FFmpeg-blue.svg?style=plastic&logo=FFMPEG&color=000000&label=Using">
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
python3 main.py [-h] [-c converter] [-f file] [-l list]
```

## 🤝 Supported file types
Almost any file can be used as an input format. The following file types are supported as output formats:
| Image | Video | Audio |
|-------|-------|-------|
| PNG   | MP4   | MP3   |
| JPG   | AVI   | WAV   |
| ICO   | MOV   |       |
| WEBP  | FLV   |       |
