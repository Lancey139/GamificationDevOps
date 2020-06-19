# -*- coding: utf-8 -*-
'''
Created on 4 janv. 2019

@author: Nicolas MEO
'''
from lxml import etree

class ParseurXML(object):
    '''
    Classe en charge du parsing du fichier XML de configuration
    '''


    def __init__(self, pCheminVersFichierXML):
        '''
        Constructeur de la classe
        :param pCheminVersXML: Contient le chemin vers le fichier xml de conf
        :type pCheminVersXML: str
        '''
        
        self.cheminVersXML = pCheminVersFichierXML
        
    def getInfoConnection(self, pId):
        """
        Methode permettant de recuperer les informations de connection via un identifiant
        -> 1 : URL / IP du serveur
        -> 2 : Nom d'utilisateur
        -> 3 : Mot de passe
        
        :param pId: Numero de l'identifiant
        :type pId: int
        
        :return: Information requise
        :rtype : str
        """
        lTree = etree.parse(self.cheminVersXML)
        for lConnection in lTree.xpath("/box/connections/connection[number='" + str(pId) + "']/information"):
            if(lConnection.text == ""):
                return None
            else:
                str_info=lConnection.text
        return str_info    

    def getJobsPlateforme(self, pNumeroPlateforme):
        """
        Methode permettant de recuperer la liste des jobs pour la plateforme X
        :param pNumeroPlateforme: Numero de la recupere
        :type pNumeroPlateforme: int
        
        :return : Liste des jobs associés a la plateforme
        :rtype : Liste
        
        """
        lTree = etree.parse(self.cheminVersXML)
        
        for lPlateform in lTree.xpath("/box/plateforms/plateform[number='" + str(pNumeroPlateforme) + "']/jobs"):
            lStrJobs=lPlateform.text
            
        lListJobs = lStrJobs.split('/')

        return lListJobs
    
    def getTempsConfig(self):
        """
        Methode permettant de recupere les parametres de gestion du temps
        
        :return : [ Heure début , Min Début, Heure Fin, Min Fin, Temps entre 2 check ]
        :rtyep : list
        """
        
        # Lecture dans le fichier xml
        ltree = etree.parse(self.cheminVersXML)
        str_time = ltree.xpath("/box/looptime/time[number='1']/def")[0].text
        str_hour_start = ltree.xpath("/box/looptime/time[number='2']/def")[0].text
        str_hour_end = ltree.xpath("/box/looptime/time[number='3']/def")[0].text
        
        #Construction de la sortie
        list_hour = str_hour_start.split(':')
        list_hour.extend(str_hour_end.split(':'))
        list_hour.append(str_time)
        
        return list_hour
    
    def getEtatFauxPlateforme(self):
        """
        Methode permettant de recuperer l'etat faux des plateformes
        
        :return : Tableau de str representant l'etat faux des plateformes
        :rtype : list
        
        """
        lTree = etree.parse(self.cheminVersXML)
        lStrState = []
        
        for li in range(1,7):
            lStrState.append(lTree.xpath("/box/plateforms/plateform[number='" + str(li) + "']/stateatfalse")[0].text)
        
        return lStrState