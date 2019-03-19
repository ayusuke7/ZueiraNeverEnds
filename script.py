#!/usr/bin/python3
import os
import sys
import requests

#----------------------------#
#							 #
# Script for Zuera NeverEnds #
#							 #
#----------------------------#


def open_browser():
	
	#mode anonimo
	for i in range(50):
		if sys.platform == 'linux':
			os.system("google-chrome --new-window https://bit.ly/2K2BwVZ && google-chrome --new-window https://bit.ly/2S0QKun")			
		elif sys.platform.find('win') > 1:
			os.system('FOR /L %x IN (1,1, 30) DO (start chrome https://bit.ly/2K2BwVZ)')
			os.system('FOR /L %x IN (1,1, 30) DO (start chrome https://bit.ly/2S0QKun)')

def alter_paper(path_screen):
	if sys.platform == 'linux':
		if os.path.isfile(path_screen):
			os.system('gsettings set org.gnome.desktop.background picture-uri file://'+path_screen)
	elif sys.platform.find('win') > 1:
		if os.path.isfile(path_screen):
			os.system('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d '+path_screen+' /f')

def change_audio():
    if sys.platform == 'linux':
    	os.system("amixer -D pulse sset Master 100%")
    elif sys.platform.find('win') > 1:
    	print('windows-commandline')

def download_image():
	url_image = "https://bit.ly/2SyWH6W"
	r = requests.get(url_image, stream=True)

	if r.status_code == 200:
		path = os.environ['HOME']+'/screen.jpg'
		t = open(path, 'wb').write(r.content)
	if t > -1:
		alter_paper(path)

if __name__ == "__main__":

	download_image()
	open_browser()
	change_audio()