### Author: George Shvartsman <stinger.xiii@gmail.com>

class dstat_plugin(dstat):
    """
    Connection count on TCP port. 
    
    Shows statistics on tcp port defined by DOOL_TCP_PORT environment variable.
    """

    monitored_port = 0

    def __init__(self):
        self.monitored_port = int(os.environ.get('DOOL_TCP_PORT'))
        self.name = str(self.monitored_port)
        self.nick = ('EST', )
        self.vars = ('established', )
        self.type = 'd'
        self.width = 5
        self.scale = 0
        self.open('/proc/net/tcp')

    def extract(self):        
        established_count = 0
        for line in islice(self.readlines(),1,None):
            l = line.split()
            local_port = int(l[1].split(':')[1],16)
            st = int(l[3],16)            
            if (local_port == self.monitored_port):  
                if (st == 1): # TCP_ESTABLISHED
                    established_count += 1
        self.val['established'] = established_count
