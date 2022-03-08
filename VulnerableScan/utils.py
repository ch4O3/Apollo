import os
import random
import threading
import subprocess
from .models import VulnerableScanTasks, ExploitRegister


class Scan(threading.Thread):
    def __init__(self, task_id):
        threading.Thread.__init__(self, name=str(random.sample('zyxwvutsrqponmlkjihgfedcba0123456', 6)))
        self.task_id = task_id

    def run(self):
        pass
        '''
        task_name = VulnerableScanTasks.objects.filter(id=self.task_id).values_list("name")[0][0]
        exploit_id = VulnerableScanTasks.objects.filter(id=self.task_id).values_list("exploit_id")[0][0]
        vulnerable_id = ExploitRegister.objects.filter(id=exploit_id).values_list("vulnerable_id")[0][0]
        ip_address = VulnerableScanTasks.objects.filter(id=self.task_id).values_list("target")[0][0]
        path = ExploitRegister.objects.filter(id=expid).values_list("fileobj")[0][0]
        filepath = str(os.getcwd()) + "/" + str(path)
        port = VulnerableScanTasks.objects.filter(id=self.id).values_list("port")[0][0]
        command_string = ExploitRegister.objects.filter(id=expid).values_list("command")[0][0]
        command = command_string % (str(filepath), str(self.task_id), str(task_name), str(vulnid), str(ipaddress), str(port))
        logfile = str(os.getcwd()) + "/Work/ScanLogs/%s.txt" % self.thread_name
        print(logfile)
        subprocess.Popen(command, stdout=open(logfile, "w"), shell=True)
        # os.system(command)
        '''