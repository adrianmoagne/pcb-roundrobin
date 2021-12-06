from datetime import datetime
import random
from time import sleep

nomes = [ 
    'chrome',
    'spotify',
    'discord',
    'gnome-terminal',
    'gnome-shell',
    'firefox',
    'code',
    'pulseaudio',
    'Xorg',
    'nautilus'
]
class PCB:
    def __init__(self,pid,prior,endereco) -> None:
        self.pid = pid #processo id
        self.name = nomes[random.randint(0,len(nomes)-1)] #nome do processo
        self.prior = prior #prioridade
        self.data_hora = datetime.now() #hora de criação
        self.endereco_incial = endereco 
        self.tempo_execucao = random.randint(1,15) #tempo necessário para o processo executar
        self.endereco_final = self.endereco_incial
        
   

    def executar(self, quantum):
        while quantum != 0 and self.tempo_execucao != 0:
            sleep(1)
            quantum -= 1
            self.tempo_execucao -= 1
            
            
    def __str__(self) -> str:
        return f'[{self.pid}]' + '\t' + str(self.prior) +'\t' + str(self.data_hora) + '\t' + str(self.name)