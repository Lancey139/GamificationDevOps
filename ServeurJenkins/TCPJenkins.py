# -*- coding: utf-8 -*-
'''
Created on 3 janv. 2019

@author: Nicolas MEO
'''

import jenkins
import sys


class TCPJenkins(object):
    '''
    Classe assurant la communication avec le serveur Jenkins
    '''


    def __init__(self, pParseurXML):
        '''
        Constructeur
        :param pParseurXML: Contient une instance de la classe ParseurXML
        :type pParseurXML: str
        '''
        
        self.parseurXML = pParseurXML
        
        self.serveur = None
        
        
    def ConnectionServeurJenkins(self):
        """
        Méthode en charge d'etablir la connection
        """

        if(self.parseurXML.getInfoConnection(1) == None or self.parseurXML.getInfoConnection(2) == None or
           self.parseurXML.getInfoConnection(3) == None):
            print("ERR : information de connection non renseignee")
            sys.exit(0)
        else:
            self.server = jenkins.Jenkins(self.parseurXML.getInfoConnection(1), username=self.parseurXML.getInfoConnection(2),
                                           password=self.parseurXML.getInfoConnection(3))
        
    def getBuildState(self, pNomJob):
        """
        Methode permettant de recuperer l'etat d'un build
        
        :param pNomJob: Nom du job a recupere
        :type pNomJob: str 
        
        :return : Etat de la plateforme 0 si FAILURE, 1 si SUCCES ou 2 si UNSTABLE
        """
        
        #On recupere ici le numero du dernier build et les infos associe
        last_build_number = self.server.get_job_info(pNomJob)['lastCompletedBuild']['number']
        
        #On interroge ensuite l etat du job en question
        if((self.server.get_build_info(name=pNomJob, number=last_build_number, depth=0)['result'] == 'FAILURE')):
            return 0
        elif((self.server.get_build_info(name=pNomJob, number=last_build_number, depth=0)['result'] == 'UNSTABLE')):
            return 2
        else:
            return 1
        
    def Deconnexion(self):
        """
        Methode permettant de se deconnecter du serveur
        """
        
        self.serveur = None
