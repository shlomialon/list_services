import subprocess
import re
import json
import os.path

class ServicesInfo(object):
    online_services = []
    disconnect_services = []
    undefined_services = []
    update_services = []
    all_services_string = []
    old_services = []
    
    def __init__(self):
        self.filename = 'online_services.json'
        self.service_command_res = subprocess.Popen("service --status-all", shell=True, stdout=subprocess.PIPE)
        self.all_services_string = self.service_command_res.stdout.read()
        self.service_command_res.stdout.close()
        self.service_command_res.wait()
    
        services_line = self.all_services_string.split('\n')
        for line in services_line:
        # status_service = re.findall("\[ [\-\+\?] \]",line)
        # print status_service[0]
            if(len(line) > 0):
                if(line[3] == "+"):
                    self.online_services.append(line)
                if(line[3] == "-"):
                    self.disconnect_services.append(line)
                if(line[3] == "?"):
                    self.undefined_services.append(line)
    
    def save_to_json_file(self):
    # save the old online list    
        self.old_services = open(self.filename, 'r').read().splitlines()
        
        outstream = open(self.filename, 'w')
        outstream.truncate()
        for line in self.online_services:
            outstream.write("%s\n" %line)
        outstream.close()
        
    def compare_online_services(self):
        print "New services: " 
        print set(self.online_services) - set(self.old_services)
        print "Deleted services: " 
        print set(self.old_services) - set(self.online_services)
        
    def read_json_file(self):
        if os.path.isfile(self.filename):
            with open(self.filename) as file_data:
                self.services_list = json.load(file_data)
    
    def get_online_services(self):
        self.save_to_json_file()
        return self.online_services 
    
def main():
    services = ServicesInfo()
    print services.get_online_services()
    print services.old_services
    services.compare_online_services()
main()