#!/usr/bin/env python3
# Author: pabloheralm@gmail.com
#			@pablololo12

import pygame
from pygame.locals import *
import os

def main():
	pygame.init()
	w=640
	h=480
	size=(w,h)
	size_image = (0,0)
	screen = pygame.display.set_mode(size, pygame.HWSURFACE)
	exit = False
	ticks = 0
	mayus = 0

	while not exit:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit = True
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				pos = pygame.mouse.get_pos()
				real_pos = (int((pos[0]/w)*size_image[0]),
							int((pos[1]/h)*size_image[1]))
				print(real_pos)
				os.system("adb shell input tap "+str(real_pos[0])+
									" "+str(real_pos[1]))
			if event.type == KEYDOWN:
				if event.key == K_UP:
					print("UP")
					os.system("adb shell input keyevent 19")
				elif event.key == K_DOWN:
					print("Down")
					os.system("adb shell input keyevent 20")
				elif event.key == K_LEFT:
					print("left")
					os.system("adb shell input keyevent 21")
				elif event.key == K_RIGHT:
					print("Right")
					os.system("adb shell input keyevent 22")
				elif event.key == K_BACKSPACE:
					print("Back")
					os.system("adb shell input keyevent 67")
				elif event.key == K_RSHIFT or event.key == K_LSHIFT:
					mayus = 1
				else:
					# In case of space
					if event.key == 32:
						os.system("adb shell input text \"%s\"")
						print("adb shell input text \"%s\"")
					else:
						stringo = event.key if mayus == 0 else event.key-32 
						stringB = "adb shell input text \"%s\"" % chr(stringo)
						print(stringB)
						os.system(stringB)
			if event.type == KEYUP:
				if event.key == K_RSHIFT or event.key == K_LSHIFT:
					mayus = 0

				
		if ticks == 30:
			os.system("adb exec-out screencap -p >screen.png")
			img = pygame.image.load("screen.png")
			size_image = img.get_size()
			img = img.convert()
			img = pygame.transform.scale(img, size)
			screen.blit(img,(0,0))
			pygame.display.flip()
			ticks = 0
		ticks = ticks + 1

	pygame.quit()

if __name__ == "__main__" :
	main()
