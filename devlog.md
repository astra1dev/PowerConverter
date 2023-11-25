V.1.1: 
- [🛠️] Bugfix: Not downloading valid MP3 file from YouTube
- [➡️] Now using pytube instead of YouTube_dl (deprecated)
- [✔️] Added requirements.txt file

V.1.2:
- [➡️] New design, window size is now 1300x650

V.1.3:
- [🛠️] Bugfix: Overlapping buttons when switching converters
- [✔️] Added pdf button

V.1.3.1:
- [✔️] Added PNG2ICO to test ICO converter

V.1.3.2:
- [✔️] Added full support for .ico files
- [✔️] Added full support for .webp files

V.1.3.3:
- [✔️] Added missing converters for some files (e.g. webp2ico)
- [➡️] Improved banner + description

V.1.3.4:
- [✔️] Added full support for avi & flv files

V.1.4:
- [✔️] Added coloured font
- [✔️] Added error catchers for all converters
- [✔️] Added tags like SUCCESS and ERROR

V.1.5:
- [✔️] Added yt-thumb to download thumbnails of YouTube videos
- [➡️] Better converter list / menu
- [➡️] Changed converter usage
- [✔️] Added loop to keep program running until user ends it

V.1.6:
- [➡️] YouTube downloader now always downloads videos in the best quality
- [✔️] Added "advanced" mode (using command line arguments)
- [➡️] Improved structure of main program

V.1.6.1:
- [❗] Massively reduced folder size by removing unnecessary FFmpeg executables [80MB -> 4KB]


V.1.6.2:
- [➡️] Improved code readability and maintainability
- [✔️] Added screen clear after each conversion process to avoid confusion
- [✔️] Added centralized error handler inside console_converters.py
- [➡️] Renamed files to 'main.py' and 'converters.py'

V.1.6.3:
- [➡️] Now using `with open` to convert image files
- [✔️] Added config.json and config.md to explain the config options
- [✔️] Added default YouTube download directory in config
- [✔️] Now supporting conversion of multiple files / videos
