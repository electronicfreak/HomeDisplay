#!/usr/bin/python

cBACKGROUND = "bg.png"
cFONT 		= (255,255,255)
cBUTTON 	= (0,0,0)
cPORT 		= 5679
screensaver = 5 * 30

# ({pos:(x,y),dia:(w,h),col:(R,G,B),text:"text",img:"path",exec:""},...)
btnMap = {}
btnMap['main'] = (
	{"pos":(0,0),"dia":(70,100),"img":"menu_header.png"},
	{"pos":(125,100),"dia":(200,75),"img":"btn_music_toggle.png","exec":"music_toggle.sh"},
	{"pos":(125,180),"dia":(200,75),"img":"btn_music_next.png","exec":"music_next.sh"},
	{"pos":(125,260),"dia":(200,75),"img":"btn_music_volup.png","exec":"music_volup.sh"},
	{"pos":(125,340),"dia":(200,75),"img":"btn_music_voldown.png","exec":"music_voldwn.sh"},
	{"pos":(0,550),"dia":(50,50),"img":"btn_exit.png","screen":"exit"},
	{"pos":(75,580),"dia":(750.20),"var":"rss","text":"BLA","col":(255,255,255)}
)
btnMap['exit'] = (
	{"pos":(100,100),"dia":(800,400),"col":(255,128,128,128)},
	{"pos":(150,150),"dia":(325,300),"col":(0,255,0),"exec":"quit.sh"},
	{"pos":(525,150),"dia":(325,300),"col":(255,0,0),"screen":"main"}
)
