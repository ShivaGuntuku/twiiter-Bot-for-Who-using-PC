import random
import mp3play
import time
from mutagen.mp3 import MP3
from mp3Graber import mp3files
from math import floor


def length(file):
	"""This function main role is find the time length of Mp3 file """
	audio = MP3(file)
	return audio.info.length


def playFile():
	"""function role is to play the random music files collected from
	HDD"""
	mp3list = mp3files()  # collected mp3 files list
	count = len(mp3list)
	for i in random.sample(mp3list, count):
		print i  # which file is played
		clip = mp3play.load(i)
		clip.play()
		filelength = length(i)
		# Let it play for up to 30 seconds, then stop it.
		time.sleep(min(filelength, clip.seconds()))
		clip.stop()


#playFile()  # for testing process script is working or not.
