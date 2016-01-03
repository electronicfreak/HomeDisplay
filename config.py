#!/usr/bin/python

cBACKGROUND = "bg.png"
cFONT = (255,255,255)
cBUTTON = (0,0,0)
screensaver = 30

# ({pos:(x,y),dia:(w,h),col:(R,G,B),text:"text",img:"path",exec:""},...)
btnMap = {}
btnMap['main'] = ({"pos":(0,0),"dia":(70,100),"img":"menu_header.png","screen":"main"},{"pos":(400,250),"dia":(200,100),"col":(255,128,64)})