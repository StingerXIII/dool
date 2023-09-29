### Author: George Shvartsman <stinger.xiii@gmail.com>
### Modified from dool-mem: Dag Wieers <dag$wieers,com>

class dool_plugin(dool):
    """
    Process allocated memory size. 
    
    Shows memory info of process defined by DOOL_MONITORED_PID environment variable.
    """

    def __init__(self):
        monitored_pid = str(os.environ.get('DOOL_MONITORED_PID'))
        self.name = 'pid ' + monitored_pid + ' memory'
        self.nick = ('VIRT', 'RES', 'SHR')
        self.vars = ('virtual', 'resident', 'shared')
        self.type = 'd'
        self.open('/proc/%s/statm' % monitored_pid)

    def extract(self):
        l = self.splitline()
        self.val['virtual'] = int(l[0]) * pagesize
        self.val['resident'] = int(l[1]) * pagesize
        self.val['shared'] = int(l[2]) * pagesize
