#!/usr/bin/python

import RPi.GPIO as g
import urllib2 as u
import pygame as p
import config as c
import os,thread,socket,json
from subprocess import call
from time import sleep

debug = True
btnMap = c.btnMap

d = False #display handler
cur_screen = "main"

link_map = []
# ({pos1:{x,y},pos2:(x,y),exec:"exec"},...)
var_map = {}
#

# schaltet monitor ein oder aus
# untested
def switchMonitor(status):
	if debug:
		print("[switchMonitor]")
	g.setmode(g.RAW)
	g.setup(g.PB+02, g.OUT)
	g.output(g.PB+02, bool(status))

# sendet einen get request an eine adresse
# untested
def getRequest(link):
	if debug:
		print("[getRequest]")
	u.urlopen(link).read()

# monitor initiieren
# untested
def initGUI(bg=(0,0,0),dim=(1024,600)):
	if debug:
		print("[initGUI]")
	global d
	d = p.display.set_mode(dim)
	p.mouse.set_visible(True)
	if isinstance(bg, str):
		d.fill((0,0,0))
		bg_img = p.image.load(os.path.join('img', bg))
		d.blit(bg_img,(0,0))
	else:
		p.fill(bg)
	p.display.flip()
	return d
	
# button malen	
# untested
def makeButton(button_map):
	if debug:
		print("[makeButton]")
	#try:
		global d
		for i in button_map:
			if debug:
				print(i)
			
			if "img" in i.keys():
				if debug:
					print("img:"+i["img"]+" - "+str(i["pos"]))
				img = p.image.load(os.path.join('img', i["img"]))
				d.blit(img,i["pos"])
			else:
				if debug:
					print("btn")			
				p.draw.rect(d,i["col"],p.Rect(i["pos"],i["dia"]))
				
			p.display.flip()
		return True
	#except:
		return False

# links eintragen
# untested	
def makeLinks(button_map):
	if debug:
		print("[makeLinks]")
	global link_map
	link_map = []
	try:
		for i in button_map:
			if "exec" in i.keys() or "screen" in i.keys():
				pos2x = i["pos"][0] + i["dia"][0]
				pos2y = i["pos"][1] + i["dia"][1]
				elem = {}
				elem["pos1"] = i["pos"]
				elem["pos2"] = (pos2x,pos2y)
				if "exec" in i.keys():
					elem["exec"] = i["exec"]
				if "screen" in i.keys():
					elem["screen"] = i["screen"]
				link_map.append(elem)
		
		if debug:
			print(link_map)
		return True
	except:
		return False

# prueft auf maus aktivitaet
# untested
def checkEvent(onlyEv=False):
	if debug:
		print("[checkEvent]")
	global link_map
	#warte auf mouseup
	try:
		for ev in p.event.get(6):
			#hole coords
			pos = ev.pos
			
			if onlyEv:
				return True
		
			#vergleiche mit linkmap
			for ln in link_map:
			#fuehle ersten treffer aus
				if ln["pos1"][0] <= pos[0] and ln["pos2"][0] >= pos[0] and ln["pos1"][1] <= pos[1] and ln["pos2"][1] >= pos[1]:
					if debug:
						print(pos)
						print(ln)
						#exit()

					if "exec" in ln.keys():
						call('bin/'+ln["exec"])
						
					if "screen" in ln.keys():
						updateScreen(ln["screen"])
					#verwerfe rest
					return True
	except:
		pass
	return False

# socket anbieten
# untested
def openSocket():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#socket.setdefaulttimeout(5.0)
	s.bind((, c.cPORT))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		data = conn.recv(1024)
		
		d = json.loads(data)
		k = d.keys()
		if 'var' in k and 'text' in k:
			
			
				
			conn.sendall("0")
		else:
			conn.sendall("-1")
		conn.close()
	
# screen konfiguration aendern
# untested
def updateScreen(bmIndex=""):
	if not bmIndex == "":
		cur_screen = bmIndex
	if debug:
		print("[updateScreen]")
	initGUI(c.cBACKGROUND)
	makeButton(btnMap[cur_screen])
	makeLinks(btnMap[cur_screen])
	
switchMonitor(True)
updateScreen()
t = 0
while True:
	if t < c.screensaver:
		t=t+1
	else:
		switchMonitor(False)
		while t >= c.screensaver:
			sleep(2)
			if checkEvent(True):
				t = 0
				switchMonitor(True)
	
	if checkEvent():
		t = 0
	sleep(0.2)
	
# ################################################
