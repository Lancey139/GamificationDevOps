from threading import Thread, RLock
from Plateforme.lcddriver import lcd
import time

verrou_Ecran = RLock()

class ThreadEcran(Thread):
	#Initialisation : Parametre instance vers un objet lcd
	def __init__(self):
		Thread.__init__(self)
		self.lcd = lcd()
		self.message_l1 = ""
		self.message_l2 = ""
		self.stop_affiche = True
	#Thread qui met a jour en permanence lecran en fonction du message
	#Si le message est trop long, on met en place un defilement	
	def run(self):
		self.lcd.lcd_clear()
		self.stop_affiche = False
		i = 0
		j = 0
		l = 0
		m = 0
		while not self.stop_affiche:
			with verrou_Ecran:
				if self.message_l1.__len__() > 16:
					if m+16 <= self.message_l1.__len__():
						message_a_affiche = self.message_l1[m:m+16]
					else:
						l = l + 4
						message_a_affiche = self.message_l1[m:] +" "+ self.message_l1[:l-1]

					self.lcd.lcd_display_string(message_a_affiche, 1)
				else:
					self.lcd.lcd_display_string(self.message_l1, 1)
				if self.message_l2.__len__() > 16:
					if i+16 <= self.message_l2.__len__():
						message_a_affiche = self.message_l2[i:i+16]
					else:
						j = j + 2
						message_a_affiche = self.message_l2[i:] +" "+ self.message_l2[:j-1]
					self.lcd.lcd_display_string(message_a_affiche, 2)
				else:
					self.lcd.lcd_display_string(self.message_l2, 2)
							
				i = i + 2
				m = m + 2
				if i >= self.message_l2.__len__():
					i = 0	
					j = 0
				if m >= self.message_l1.__len__():	
					l = 0
					m = 0
			time.sleep(0.9)
	#Stop provisoirement l affichage en mettant en pause le thread
	def stop_affiche(self):
		self.stop_affiche = True
		self.lcd.lcd_clear()
	#Reprend laffichage suite a un stop
	def start_affiche(self):
		self.stop_affiche = False
	#Met a jour les messages a afficher	
	# Prend en parametres les nouveaux messages et un booleen indiquant si l on 
	#veut reset lecran ou non
	def Set_Messages(self, clear, messagel1, messagel2=""):
		with verrou_Ecran:
			if clear : 
				self.lcd.lcd_clear()
			self.message_l1 = messagel1
			self.message_l2 = messagel2
			print (messagel1)
