import re
from mp3Player.musicPlayer import playFile
from ingridents.twitter_test import tweeterPost
from ingridents.twitter_content import jarvis_replay

"""test with twitter"""
twit = tweeterPost()
if bool(re.search(r'\bmusic|songs|tracks\b', twit, re.IGNORECASE)):
 	#voiceOut.Speak ("playing Songs wait.")
 	playFile()

elif bool(re.search(r'\bwho|trace|find\b', twit, re.IGNORECASE)):
	jarvis_replay()