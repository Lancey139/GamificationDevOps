'''
Created on 10 janv. 2019

@author: local
'''

from SerialCom.Serial import SerialCom
from SerialCom.SerialIdentifiant import IDENT_CONF, IDENT_ETAT, IDENT_MSG

class SerialPlateforme(SerialCom):
    '''
    En charge de decoder les messages provenant du serveur
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
        
        # Contient les valeurs d'initialisation des plateforme
        # :ptype : list[int]
        self.iniPlateforme = [-1]*6
        
        # Contient les etats des plateformes
        self.etatPlateforme = [-1]*6
        
        # Booleen indiquant qu'une update de la plateforme est necessaire
        self.update = False
 
        # Booleen indiquant qu'une initialisation de la plateforme est necessaire
        self.updateIni = False
        
        # Pointeur vers le thread ecran
        self.threadEcran = False
        
        
    def lireBufferReception(self):
        """
        Méthode à surcharger
        """
        print("Message recu Plateforme", self.mBufferReception)
        
        lBufferSplit = self.mBufferReception.split(';')
        lBufferSplit = lBufferSplit[1:-1]
        
        if self.mBufferReception[0] == IDENT_CONF:
            for i, lChar in enumerate(lBufferSplit):
                self.iniPlateforme[i] = int(lChar)
            self.updateIni = True
        if self.mBufferReception[0] == IDENT_ETAT:
            self.update = True
            for i, lChar in enumerate(lBufferSplit):
                self.etatPlateforme[i] = int(lChar)
        if self.mBufferReception[0] == IDENT_MSG:
            if lBufferSplit.__len__() == 1:
                self.threadEcran.Set_Messages(True,lBufferSplit[0])
            elif lBufferSplit.__len__() == 2:
                self.threadEcran.Set_Messages(True,lBufferSplit[0], lBufferSplit[1])
                   
        
