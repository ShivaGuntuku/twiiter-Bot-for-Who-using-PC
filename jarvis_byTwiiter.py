import re
import Music_player 
import Twitter_what 
 

"""test with twitter"""
twit = Twitter_what.tweeterPost()
if bool(re.search(r'\bmusic|songs|tracks\b', twit, re.IGNORECASE)):
 	#voiceOut.Speak ("playing Songs wait.")
 	Music_player.playFile()

elif bool(re.search(r'\bwho|trace|find\b', twit, re.IGNORECASE)):
	Twitter_what.jarvis_replay()
