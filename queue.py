from pcb import PCB
import random
class Queue:
    def __init__(self,queue_id) -> None:
        self.queue_id = queue_id
        self.prior = random.randint(0,5) 
        self.quantum = random.randint(1,8) 
        self.processos = []
        self.atual_processo = 0

    def add_processo(self, novo_processo: PCB):
        self.processos.append(novo_processo)
    

    def executar(self):
        self.processos[self.atual_processo].executar(self.quantum)

        if self.processos[self.atual_processo].tempo_execucao == 0:
            self.processos.pop(self.atual_processo)
            self.atual_processo = 0 if (len(self.processos) == 0) else (self.atual_processo % (len(self.processos)))
            return 
        self.atual_processo = (self.atual_processo + 1) % (len(self.processos))
    
    def __str__(self) -> str:
        return 'QUEUE ID: ' + str(self.queue_id) +  '\t' +' PRIOR: ' + str(self.prior) + '\t' + ' QUANTUM: ' + str(self.quantum) +  '\t' +' PROCESSOS: ' + str(len(self.processos))

    def tabela(self):
        return 'PID' + '\t' + 'PR' + '\t' + 'TIME' + '\t'*4 + 'COMMAND' 