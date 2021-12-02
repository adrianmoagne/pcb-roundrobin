from pcb import PCB
from pcb import PCB
from queue import Queue
import random
queues = []
for i in range(4):
    queues.append(Queue(i))

quantidade_processos = 10

queues.sort(key= lambda x : x.prior, reverse= True)

while True:

    
    while quantidade_processos !=0 :
        sorteada = queues[random.randint(0,3)]
        processo_novo = PCB(
            pid= 10 -  quantidade_processos,
            prior= sorteada.prior,
            endereco= 10 - quantidade_processos
        )

        sorteada.add_processo(processo_novo)
        quantidade_processos -=1

    if all(len(queue.processos) == 0 for queue in queues):
        break
    queue_atual = next(queue for queue in queues if len(queue.processos )!= 0)
    print(queue_atual)
    print(queue_atual.tabela())
    while len(queue_atual.processos) != 0:
        print(queue_atual.processos[queue_atual.atual_processo])
        queue_atual.executar()
        

