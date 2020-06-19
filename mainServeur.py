# -*- coding: utf-8 -*-
'''
Created on 2 janv. 2019

@author: nmeo
'''
from ServeurJenkins.TCPJenkins import TCPJenkins
from ServeurJenkins.ParseurXML import ParseurXML
import time
import datetime
from SerialCom.SerialIdentifiant import IDENT_CONF, IDENT_ETAT, IDENT_MSG
from ServeurJenkins.SerialServeur import SerialServeur
from time import sleep
from ServeurJenkins.PhraseAffichage import G_TEXT_OK1, G_TEXT_OK2


if __name__ == '__main__':
    print("Lancement du programme d'integration continue personalisée USB")
    
    print("Parsing du fichier xml de configuration")
    
    lParseur = ParseurXML("ServeurJenkins/conf.xml")
    lTCPJenkins = TCPJenkins(lParseur)
    lTCPJenkins.ConnectionServeurJenkins()
    
    lSerial = SerialServeur("/dev/ttyUSB0",9600)
    
    # Création du tableau contenant l'etat des plateforme
    lEtatPlateforme = [1, 1, 1, 1, 1, 1]
    
    # Création des variables contenant les heures de début et de fin
    lListeTemps = lParseur.getTempsConfig()
    lTempsDebut = datetime.time(int(lListeTemps[0]), int(lListeTemps[1]), 0, 0)
    lTempsFin = datetime.time(int(lListeTemps[2]), int(lListeTemps[3]), 0, 0)
    while True:
        
        # On passe en sleep tout en lisant les messages du port série
        lTemps = datetime.datetime.now()
        lTempsTempo =  datetime.datetime.now() - lTemps
       
        while lTempsTempo.seconds < float(lListeTemps[4])*60:
            lSerial.lireMessage()
            # Si la plateforme vient de s'initialiser, on lui envoi l'état inital
            if lSerial.iniPlateforme == True:
                print("Envoi de la configuration initiale des plateformes")
                lTableauMessage = [IDENT_CONF]
                lTableauMessage.extend(lParseur.getEtatFauxPlateforme())
                lSerial.construireMessage(lTableauMessage)
                lSerial.iniPlateforme = False
                # On a update l'etat de la plateforme, on sort de la boucle pour 
                # forcer l'envoi d'un message d'update
                break
            lTempsTempo =  datetime.datetime.now() - lTemps
        
        # Verification de l'heure : pas de check durant la nuit
        lTemps = datetime.datetime.now()
        
        if((lTemps.time() < lTempsFin) and (lTemps.time() > lTempsDebut)):
            #Verification de l'etat des jobs
            lTCPJenkins.ConnectionServeurJenkins()
            for i in range(1,7):
                # Verification de l'état des jobs
                for lJob in lParseur.getJobsPlateforme(i):
                    lEtatJob = lTCPJenkins.getBuildState(lJob)
                    # Si l'un job sur le drapeau est instable, on le lève
                    # Le drapeau étant un indicateur sur la qualité
                    if lEtatJob == 2 and i == 1:
                        lEtatPlateforme[i-1] = 0
                        lTableauMessage = [IDENT_MSG]
                        lTableauMessage.append("Regression de la qualite !")
                        lTableauMessage.append(lJob)
                        lSerial.construireMessage(lTableauMessage)
                        break                        
                    elif lEtatJob == 0 and i != 1:
                        lEtatPlateforme[i-1] = 0
                        lTableauMessage = [IDENT_MSG]
                        lTableauMessage.append("ERREUR ----> Plateforme %d"%(i))
                        lTableauMessage.append(lJob)
                        lSerial.construireMessage(lTableauMessage)
                        break
                    else:
                        lEtatPlateforme[i-1] = 1
            lTCPJenkins.Deconnexion()            
            # Envoie du message a la plateforme    
            print("Envoi du message a la plateforme")
            lTableauMessage = [IDENT_ETAT]
            lTableauMessage.extend(lEtatPlateforme)
            lSerial.construireMessage(lTableauMessage)
            print("Actualisation de l'affichage")
            if 0 not in lEtatPlateforme:
                lTableauMessage = [IDENT_MSG]
                lTableauMessage.append(G_TEXT_OK1)
                lTableauMessage.append(G_TEXT_OK2)
                lSerial.construireMessage(lTableauMessage)
            
        else:
            print("Mode Nuit")
