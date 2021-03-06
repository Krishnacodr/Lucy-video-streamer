<p align="center"><a href="https://t.me/LUCY_20_BOT"><img src="https://telegra.ph/file/cff60c353d1e83d06f7af.jpg"></a></p>
<p align="center">
    <br><b>Video Stream is an Advanced Telegram Bot that's allow you to play Video & Music on Telegram Group Video Chat</b><br>

## ๐ Stats
[![CodeFactor](https://www.codefactor.io/repository/github/Krishnacodr/Lucy-video-streamer/badge)](https://www.codefactor.io/repository/github/Krishnacodr/Lucy-video-streamer)

## ๐งช Get `SESSION_NAME` from below:

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@levinalab/StringSession#main.py) ``Pyrogram``

## ๐ญ Preview
<p align="center">
  <img src="https://telegra.ph/file/b8c1461bcbbad5664aa48.png">
</p>

## โจ Features
- Music & Video stream support
- MultiChat support
- Playlist & Queue support
- Skip, Pause, Resume, Stop feature
- Music & Video downloader feature
- Inline Search support
- YouTube direct search support
- YouTube/Local/Live/m3u8 stream support
- Inline Search support
- Control With Button support
- Volume Control
- Userbot Auto Join

## ๐  Commands:
- `/play (query)` - play music from youtube
- `/stream (radio link)` - stream a live streaming music
- `/vplay (query)` - play video from youtube
- `/vstream (live link)` - play video live streaming video
- `/pause` - pause the streaming (admin only)
- `/resume` - resume the streaming (admin only)
- `/skip` - switch to next stream (admin only)
- `/stop` - end the streaming (admin only)
- `/vmute` - for mute the userbot on voice chat
- `/vunmute` - for unmute the userbot on voice chat
- `/volume 1-200` - adjust the volume of userbot (userbot must be admin)
- `/playlist` - show you all the current stream list
- `/song (query)` - download music from youtube
- `/video (query)` - download video from youtube
- `/userbotjoin` - invite the userbot to join group (admin only)
- `/userbotleave` - instruct userbot to leave the group (admin only)
- `/leaveall` - order the userbot to leave from all group (sudo only)
- `/clean` - clean all raw files
- `/rmd` - clean all downloaded files

## Heroku Deployment ๐
The easy way to host this bot, deploy to Heroku, Change the app country to Europe (it will help to make the bot stable).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Krishnacodr/Lucy-video-streamer)

## VPS Deployment ๐ก
Get the best Quality of streaming performance by hosting it on VPS, here's the step's:

```sh
sudo apt update && apt upgrade -y
sudo apt install git curl python3-pip ffmpeg -y
pip3 install -U pip
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt-get install -y nodejs
npm i -g npm
git clone https://github.com/levina-lab/video-stream # clone the repo.
cd video-stream
pip3 install -U -r requirements.txt
cp example.env .env # use vim to edit ENVs
vim .env # fill up the ENVs (Steps: press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file).
python3 main.py # run the bot.

# continue the host with screen or anything else, thanks for reading.
```
