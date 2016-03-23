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
	446 Mhz sender

http://jeremyblythe.blogspot.de/2014/09/raspberry-pi-pygame-ui-basics.html

http://markamc.cybaman.net/?p=168
https://www.theragnarbay.org/banana-pi-fernbedienung/
https://pypi.python.org/pypi/paho-mqtt/1.1
http://mosquitto.org/download/

ir fernbedienung
446 Fernbedienung
------------------------------------------------------------------
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
	
GPIO hinzufgen
	git clone https://github.com/LeMaker/RPi.GPIO_BP -b bananapi
	apt-get update
	apt-get install python-dev
	cd RPi.GPIO_BP
	python setup.py install                 
	reboot

PyGame installieren
	apt-get install python-pygame
	
mqtt server???
node-red???

