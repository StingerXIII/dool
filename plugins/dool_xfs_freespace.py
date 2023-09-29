### Author: George Shvartsman <stinger.xiii@gmail.com>

class dool_plugin(dool):
    """
    Shows XFS free space by allocation groups.
    
    Provide mount point by setting DOOL_XFS_MOUNTPOINT environment variable.
    """

    mount_point = ""

    def __init__(self):
        self.name = "xfs freespace by AG"
        self.type = 'd'
        self.width = 5
#        self.scale = 0

    def vars(self):
        ret = []
        self.mount_point = os.environ.get('DOOL_XFS_MOUNTPOINT')
        with os.popen("xfs_spaceman -c 'freesp -g' " + self.mount_point) as dataf:
            for line in islice(dataf,1,None):
                data = line.split()
                ret.append(data[0])
        dataf.close()
        print(self.mount_point)
        return ret

    def extract(self):
        with os.popen("xfs_spaceman -c 'freesp -g' " + self.mount_point) as dataf:
            for line in islice(dataf,1,None):
                data = line.split()
                self.val[data[0]] = int(data[2])*4096


