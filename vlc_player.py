# Ask user to specify number of episodes.
# Generate a list of random episodes from a specified folder with subfolders.
# Play generated list as a playlist on VLC.

import os
import random
import subprocess
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-n", "--num_episodes", help="Choose the number of episodes to play.",type=int,default=2)
parser.add_argument("-a","--ad_time", help="Select Adventure Time files.", action='store_true')
parser.add_argument("-s","--simpsons", help="Select Simpsons files.", action='store_true')
args=parser.parse_args()

def choose_episode(path):

	all_seasons=os.listdir(path)
	all_seasons.remove(".DS_Store")

	season=random.choice(all_seasons)
	season_path=path+season

	season_episodes=os.listdir(season_path)
	if ".DS_Store" in season_episodes:
		season_episodes.remove(".DS_Store")

	episode=random.choice(season_episodes)

	chosen_episode="\""+season_path+"/"+episode+"\""
	return chosen_episode

adventure_path="/Users/gurjindermassan/Desktop/Adventure Time/"
simpsons_path="/Users/gurjindermassan/Desktop/The Simpsons/"

if args.ad_time:
	path=adventure_path
	
elif args.simpsons:
	path=simpsons_path

n=args.num_episodes
playlist=""
for i in range(n):
	playlist=playlist+ choose_episode(path)+" "


vlc_path="/Applications/VLC.app/Contents/MacOS/VLC"
vlc_command=(vlc_path +" "+ playlist).strip()

print(vlc_command)

subprocess.run(vlc_command, shell=True, check=True)

