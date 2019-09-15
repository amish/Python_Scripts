'''pip3 install mutagen'''
'''Automate metadata ID3 tagging of .mp3 files on the basis of its file name'''

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import re, os

location = 'D:/mp3-files'
os.chdir(location)

for file in os.listdir(location):
	if file.endswith('.mp3'):
		file1 = file[:-4]
		names = re.split(' - ', file1)
		audio = MP3(file, ID3=EasyID3)
		#print(audio.keys())
		#print(audio.pprint())
		audio["artist"] = names[0]
		audio["title"] = names[1]

		for i in audio.keys():
			if(i == 'album'):
				a = str(audio['album']).lower()
				if(('single' in a) or ('billboard' in a) or ('chart' in a) or ('now 50' in a)):
					del audio["album"]
					if (audio.get('albumartist')):
						del audio["albumartist"]
			if(i == 'copyright'):
				del audio["copyright"]
			if(i == 'discnumber'):
				del audio["discnumber"]
			if(i == 'tracknumber'):
				del audio["tracknumber"]
			if(i == 'comments'):
				del audio["comments"]
			if(i == 'encodedby'):
				del audio["encodedby"]
			if(i == 'composer'):
				del audio["composer"]
			if(i == 'bpm'):
				del audio["bpm"]
			if(i == 'publisher'):
				del audio["publisher"]

		audio.save()