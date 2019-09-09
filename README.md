# MyRandomFilePlayer
Program to randomly play video files on VLC player.

### Usage
Use with Python3. 
There are two command line arguments: 
- `-n` is the number of files to play,
- `-p` is the path to the directory containing the season directories. 

I have set up an alias in my `.bashrc` file for each series, for example:
```
alias simpsons="python3 ~/src/github.com/gurjindermassan/MyRandomFilePlayer/vlc_player.py -p ~/Movies/The\ Simpsons/"
```