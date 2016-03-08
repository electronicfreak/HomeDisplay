# HomeDisplay

am oberen rand diverse reiter für verschiedene funktionsbereicht

Seiten
	übersicht
		verfügbare und verbundene funktionen
		Gesamt programme starten (modul übergreifende funktionen wie licht auf ambient musik chill raum temperatur auf 22 grad)
	licht
		steuerung des lichts
		killtimer
	heizung
		steuerung der heizung
		timer
	notizzettel
		freizeichnen und speichern
		

http://jeremyblythe.blogspot.de/2014/09/raspberry-pi-pygame-ui-basics.html

http://jeremyblythe.blogspot.de/2014/09/raspberry-pi-pygame-ui-basics.html
http://www.pygame.org/docs/ref/display.html#pygame.display.update
http://www.bananapi-kaufen.de/gpios-steuern-mit-wiringpi/
http://hardware-libre.fr/2014/07/banana-pi-gpio-now-supported/

http://markamc.cybaman.net/?p=168

APT: python python-pip gcc

ir fernbedienung


anleitung
bananian installieren
user root pw pi


configurieren
	bananian-config
	bananian-update
	reboot
	
git installieren
	apt-get update
	apt-get install git
	
display anklemmen

fex daten holen
	git clone https://github.com/LeMaker/fex_configuration.git
	cd fex_configuration/bin
	
boot modden
	mount /dev/mmcblk0p1 /mnt
	cp banana_pro_Xlcd.bin /mnt/script.bin
	sync
	umount /mnt