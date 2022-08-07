ytget-script
=============

Script created to simply download videos and music from YouTube.  
Tested on - Python 3.10

Functions
----------
- download single video from link (**mp4 format**)
- download multiple videos using file: `list_videos.txt`
- download single music from link (**mp3 format**)
- download multiple music using file: `list_music.txt`

### Python modules
For the app to run correctly:

- pytube

### Setting up virtual environment
Windows
```commandline
py -m venv venv
venv\Scripts\activate
pip install pytube
```

Linux etc.
```commandline
python -m venv venv
source venv/bin/activate
pip install pytube
```

### Optional executable file for Windows
Download `script_windows.exe` to use. All compilled.

### Versions
- 1.0 - First project, just only with videos
- 1.1 - Small adjustments and possibility to download music in mp3