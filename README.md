<p align="center">
  <img src="./logo.png">
</p>

<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=plastic&logo=python&color=3c7cae&labelColor=ffd841&logoColor=3c7cae">
  </a>
  
  <a href="https://www.gnu.org/licenses/gpl-3.0.html">
    <img src="https://img.shields.io/badge/license-GPL-brightgreen.svg?style=plastic&logo=GNU&label=License">
  </a>
  
  <a href="https://github.com/astra1dev/PowerConverter/releases/latest">
    <img src="https://img.shields.io/badge/version-1.6.4-blue.svg?style=plastic&logo=GitHub&color=ff5500&label=Version">
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
python3 main.py [-h] [-c converter] [-f file(s)]
```

## 🤝 Supported file types
Almost any file can be used as an input format. The following file types are supported as output formats:
| Image | Video | Audio |
|-------|-------|-------|
| PNG   | MP4   | MP3   |
| JPG   | AVI   | WAV   |
| ICO   | MOV   |       |
| WEBP  | FLV   |       |
