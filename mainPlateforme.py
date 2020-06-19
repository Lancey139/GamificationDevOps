# -*- coding: utf-8 -*-
'''
Created on 9 janv. 2019

@author: Nicolas MEO
'''
from Plateforme.SerialPlateforme import SerialPlateforme
from Plateforme.Servo_Controller import Servo_Controller
from SerialCom.SerialIdentifiant import IDENT_CONF
import time
from Plateforme.ThreadEcran import ThreadEcran

if __name__ == '__main__':
    """
    Main de l'applicaiton cote plateforme d'integration
    """
    
    # Etablissement de la communicaiton
    lSerial = SerialPlateforme("/dev/ttyUSB0",9600)
    
    # Création du servo controler instancié plus tard
    lServoControler = None
    
    # Compteur permettant d envoyer le message regulierement 
    # pour recevoir les infos dinit
    lCompteurInit = 100
    
    # Thread permettant d'afficher des informations a lecran
    lThreadEcran = ThreadEcran() 
    lThreadEcran.Set_Messages(True, "PLATEFORM READY")
    lThreadEcran.start()
    
    lSerial.threadEcran = lThreadEcran
    
    
    # Lecture des messages series
    while True:
        lCompteurInit+=1
        lSerial.lireMessage()
        
        if lSerial.updateIni: 
			# On informe le serveur qu'on est initialisé
            lSerial.construireMessage([IDENT_CONF, '1'])
            lSerial.updateIni = False
            # Message d'initialisation recu, on initialise le ServoControler si ce n'est pas deja fait
            lServoControler = Servo_Controller(lSerial.iniPlateforme)
        elif -1 in lSerial.iniPlateforme and lCompteurInit > 100:
            lSerial.construireMessage([IDENT_CONF, '0'])
            lCompteurInit = 0		    
            
        if -1 not in lSerial.etatPlateforme and lSerial.update:
            for i, lEtat in enumerate(lSerial.etatPlateforme):
                lServoControler.ChangerEtatPalteforme(i+1, bool(lEtat))
                
            lSerial.update = False
