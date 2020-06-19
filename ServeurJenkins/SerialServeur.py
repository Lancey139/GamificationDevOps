'''
Created on 18 janv. 2019

@author: Nicolas MEO
'''
from SerialCom.Serial import SerialCom
from SerialCom.SerialIdentifiant import IDENT_CONF

class SerialServeur(SerialCom):
    '''
    En charge de decoder les messages provenant de la plateforme
    '''


    def __init__(self, pPort, pBaud):
        '''
        Constructeur
        
        :param pPort: Port de comunication
        :ptype pPort: str
        
        :param pBaud: Baud rate
        :ptype pBaud: int
        '''
        SerialCom.__init__(self, pPort, pBaud)
        
        # True si la plateforme doit être initialisée, false sinon
        # :ptype : Bool
        self.iniPlateforme = False
        
        
        
    def lireBufferReception(self):
        """
        Lecture d'un message en provenance de la plateforme
        """
        lBufferSplit = self.mBufferReception.split(';')
        
        print("Message recu Serveur", self.mBufferReception)
        lBufferSplit = lBufferSplit[1:-1]
        if self.mBufferReception[0] == IDENT_CONF:
            if int(lBufferSplit[0]) == 0:
                self.iniPlateforme = True
            elif int(lBufferSplit[0]) == 1:
                self.iniPlateforme = False
