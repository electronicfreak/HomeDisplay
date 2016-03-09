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
http://wiki.lemaker.org/BananaPro/Pi:LCD_Module
https://www.theragnarbay.org/banana-pi-fernbedienung/

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
	apt-get install git mc nano htop screen watch
	
display anklemmen

fex daten holen
	git clone https://github.com/LeMaker/fex_configuration.git
	cd fex_configuration/bin
	
boot modden
	mount /dev/mmcblk0p1 /mnt
	cp banana_pi_7lcd.bin /mnt/script.bin
	sync
	umount /mnt
	reboot
	
touchscreen treiber starten
	modprobe ft5x_ts
	
in /etc/modules unten hinzufügen
	ft5x_ts

python installieren und alles was man so braucht
	apt-get install python python-pip gcc evtest
	
mit evtest den ft5 treiber aufrufen und testen 
	evtest
	
homedisplay importieren
	git clone https://github.com/electronicfreak/HomeDisplay.git
	
git clone https://github.com/LeMaker/RPi.GPIO_BP -b bananapi
apt-get update
apt-get install python-dev
cd /RPi.GPIO_BP
python setup.py install                 
reboot

apt-get install python-pygame