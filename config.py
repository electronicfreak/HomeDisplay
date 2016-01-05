#!/usr/bin/python

cBACKGROUND = "bg.png"
cFONT = (255,255,255)
cBUTTON = (0,0,0)
screensaver = 5 * 30

# ({pos:(x,y),dia:(w,h),col:(R,G,B),text:"text",img:"path",exec:""},...)
btnMap = {}
btnMap['main'] = ({"pos":(0,0),"dia":(70,100),"img":"menu_header.png"},
	{"pos":(200,200),"dia":(100,100),"col":(255,128,64),"exec":"music_toggle.sh"},
	{"pos":(325,200),"dia":(100,100),"col":(255,0,64),"exec":"music_next.sh"},
	{"pos":(450,200),"dia":(100,100),"col":(0,128,64),"exec":"music_volup.sh"},
	{"pos":(575,200),"dia":(100,100),"col":(255,128,0),"exec":"music_voldwn.sh"},
	{"pos":(0,550),"dia":(50,50),"col":255,0,0),"screen":"exit"})
btnMap['exit'] = ({"pos":(100,100),"dia":(800,400),"col":(255,128,128,128)},
	{"pos":(150,150),"dia":(325,300),"col":(0,255,0),"exec":"quit.sh"},
	{"pos":(525,150),"dia":(325,300},"col":(255,0,0),"screen":"main"})
