# -*- coding: utf-8 -*-
'''
Created on 9 janv. 2019

@author: Nicolas MEO
'''

from Plateforme.Adafruit_PWM_Servo_Driver import PWM
import time

# Definition des constantes de positions des servo-controller
CONST_TRUE_PL1 = 355
CONST_TRUE_PL2 = 120
CONST_TRUE_PL3 = 140
CONST_TRUE_PL4 = 225
CONST_TRUE_PL5 = 125
CONST_TRUE_PL6a = 420
CONST_TRUE_PL6b = 520

CONTS_FALSE_PL1 = 155
CONST_FALSE_PL2 = 632
CONST_FALSE_PL3 = 400
CONST_FALSE_PL4 = 450
CONST_FALSE_PL5 = 635
CONST_FALSE_PL6a = 125
CONST_FALSE_PL6b = 125

class Servo_Controller(object):
	"""
	Classe en charge du control des moteurs
	"""
	
	def __init__(self, pListState):
		"""
		Constructeur : configuration des etat faux des moteurs
		:param pListState: Liste contenant la configuration de chaque plateforme
		:ptype pListState: list
		"""
		# Initialise the PWM device using the default address
		# Set frequency to 60 Hz
		self._pwm = PWM(0x40)
		self._pwm.setPWMFreq(60)  
		
		
		# Mise en place de l'etat faux pour la plateforme 1
		self._sfconf1 = bool(int(pListState[0]))
		if(self._sfconf1):
			self._pwm.setPWM(3, 0,CONST_TRUE_PL1)
			self._Plateforme1 = False
		else:
			self._pwm.setPWM(3, 0,CONTS_FALSE_PL1)
			self._Plateforme1=False
		time.sleep(1)
		
		
		# Mise en place de l'etat faux pour la plateforme 2
		# Aucune configuration requise pour cette plateforme
		self._sfconf2 = False
		self._Plateforme2=False
		self._pwm.setPWM(2, 0,CONST_FALSE_PL2)
		time.sleep(1)
		
		
		# Mise en place de l'etat faux pour la plateforme 3
		self._sfconf3 = bool(int(pListState[2]))
		if(self._sfconf3):
			self._pwm.setPWM(0, 0,CONST_TRUE_PL3)
			self._Plateforme3 = False
		else:
			self._pwm.setPWM(0, 0,CONST_FALSE_PL3)
			self._Plateforme3=False
		time.sleep(1)
		
		# Mise en place de l'etat faux pour la plateforme 4
		self._sfconf4 = bool(int(pListState[3]))
		if(self._sfconf4):
			self._pwm.setPWM(6, 0,CONST_TRUE_PL4)
			self._Plateforme4 = False
		else:
			self._pwm.setPWM(6, 0,CONST_FALSE_PL4)
			self._Plateforme4=False
		time.sleep(1)
		
		
		# Mise en place de l'etat faux pour la plateforme 5
		self._sfconf5 = bool(int(pListState[4]))
		if(self._sfconf5):
			self._pwm.setPWM(4, 0, CONST_TRUE_PL5)
			self._Plateforme5 = False
		else:
			self._pwm.setPWM(4, 0, CONST_FALSE_PL5)
			self._Plateforme5=False
		time.sleep(1)
		
		"""
		Commentee pour cause d usure materielle
		
		# Mise en place de l'etat faux pour la plateforme 6
		self._sfconf6 = bool(int(pListState[5]))
		if(self._sfconf6):
			self._pwm.setPWM(1, 0, CONST_TRUE_PL6a)
			self._pwm.setPWM(5, 0, CONST_TRUE_PL6b)
			self._Plateforme6 = False
		else:
			self._pwm.setPWM(1, 0, CONST_FALSE_PL6a)
			self._pwm.setPWM(5, 0, CONST_FALSE_PL6b)
			self._Plateforme6=False
		time.sleep(1)
		"""
		
		
	def ChangerEtatPalteforme(self, pNumPlateforme, pIsOk):	
		"""
		Methode en charge de changer letat des palteformes
		:param pNumPlateforme: Numero de la plateforme a changer
		:ptype pNumPlateforme: int
		
		:param pIsOk: Etat de la plateforme
		:ptype pIsOk: bool 
		"""
		if pNumPlateforme > 0 and pNumPlateforme < 7:
			
			if pNumPlateforme == 1:
				if pIsOk == self._sfconf1 and self._Plateforme1 != self._sfconf1 :
					self._Plateforme1 = self._sfconf1
					self._pwm.setPWM(3, 0,CONTS_FALSE_PL1)
				elif pIsOk != self._sfconf1 and self._Plateforme1 == self._sfconf1 :
					self._Plateforme1 = not self._sfconf1
					self._pwm.setPWM(3, 0,CONST_TRUE_PL1)
					
			if pNumPlateforme == 2:
				if pIsOk == self._sfconf2 and self._Plateforme2 != self._sfconf2:
					self._Plateforme2 = self._sfconf2
					self._pwm.setPWM(2, 0,CONST_FALSE_PL2)
				elif pIsOk != self._sfconf2 and self._Plateforme2 == self._sfconf2:
					self._Plateforme2 = not self._sfconf2
					self._pwm.setPWM(2, 0,CONST_TRUE_PL2)
					
			if pNumPlateforme == 3:
				if pIsOk == self._sfconf3 and self._Plateforme3 != self._sfconf3:
					self._Plateforme3 = self._sfconf3
					self._pwm.setPWM(0, 0,CONST_FALSE_PL3)
				elif pIsOk != self._sfconf3 and self._Plateforme3 == self._sfconf3:
					self._Plateforme3 = not self._sfconf3
					self._pwm.setPWM(0, 0,CONST_TRUE_PL3)
					
			if pNumPlateforme == 4:
				if pIsOk == self._sfconf4 and self._Plateforme4 != self._sfconf4:
					self._Plateforme4 = self._sfconf4
					self._pwm.setPWM(6, 0,CONST_FALSE_PL4)
				elif pIsOk != self._sfconf4 and self._Plateforme4 == self._sfconf4:
					self._Plateforme4 = not self._sfconf4
					self._pwm.setPWM(6, 0,CONST_TRUE_PL4)
					
			if pNumPlateforme == 5:
				if pIsOk == self._sfconf5 and self._Plateforme5 != self._sfconf5:
					self._Plateforme5 = self._sfconf5
					self._pwm.setPWM(4, 0, CONST_FALSE_PL5)
				elif pIsOk != self._sfconf5 and self._Plateforme5 == self._sfconf5:
					self._Plateforme5 = not self._sfconf5
					self._pwm.setPWM(4, 0, CONST_TRUE_PL5)
			"""
			Commente pour cause d usure materielle		
			if pNumPlateforme == 6:
				if pIsOk == self._sfconf6 and self._Plateforme6 != self._sfconf6:
					self._Plateforme6 = self._sfconf6
					self._pwm.setPWM(1, 0, CONST_FALSE_PL6a)
					self._pwm.setPWM(5, 0, CONST_FALSE_PL6b)
				elif pIsOk != self._sfconf6 and self._Plateforme6 == self._sfconf6:
					self._Plateforme6 = not self._sfconf6
					self._pwm.setPWM(1, 0, CONST_TRUE_PL6a)
					self._pwm.setPWM(5, 0, CONST_TRUE_PL6b)
			"""											
		else:
			print("ERR : Numero de plateforme incorrect ")		
			
		time.sleep(1)			
	
		
		
