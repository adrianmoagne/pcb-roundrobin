class Pcb:
    def __init__(self,name,pid,prior,data_hour,inicial_adress,burst_time):
        self.name = name
        self.pid = pid
        self.prior = prior
        self.data_hour = data_hour
        self.incial_adress = inicial_adress
        self.burst_time = burst_time
        self.wating_time = 0
        self.turn_around_time = 0