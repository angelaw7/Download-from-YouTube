# Download from YouTube
A script and GUI to download videos and audio files from YouTube, using PyTube

## Preview
![image](https://user-images.githubusercontent.com/74735037/148842799-497d3b54-125a-4544-a0d1-e74c85ff0ea0.png)

## .env configuration
```
CONFIG_KEY=<config_key>
SAVE_PATH=<save_path>
```
You can change the save path on the GUI after, this is just for the default location

## Setup
- Create .env file with variables listed above
- ```pip install virtualenv```
- For Windows: `py -3 -m venv venv`, then `venv\Scripts\activate`
- For MacOS/Linux: `python3 -m venv venv`, then `. venv/bin/activate`
- ```pip install -r requirements.txt``` to download dependencies

## To run
- `cd download_from_yt` to change into directory
- `venv\Scripts\activate` to activate virtual environment
- `python yt_dowbload.py` to launch GUI

Note: You can change the directory "download_from_yt" to something shorter to make it easier next time
