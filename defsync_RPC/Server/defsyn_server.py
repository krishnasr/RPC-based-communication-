
import numpy as np
import socket
import threading
import os
import math


# the below variables are constant vairables used for coding the program
port_num=8080 # using port number 8080
server_num=socket.gethostbyname(socket.gethostname()) # gethostname returns the current computer's ip address
server_address=(server_num,port_num)
server_connected=True
message_format="utf-8"

socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating socket
socket_server.bind(server_address) #binding to IPV4 server hence we used AF_INET

def calculate_pi():
    return math.pi

def add(i,j):
    return i+j

def make_matrix(mat):
    mat1=mat.split(",")
    matrix=[]
    for i in range(0,len(mat1)):
        k=mat1[i].split(" ")
        kint=[eval(item) for item in k]
        
        matrix.append(kint)
    return matrix

class switch_process:
    def __init__(self, process,client_connect,client_message):
        self.process=process
        self.client_connect=client_connect
        self.client_message=client_message

    def calculatepi_process(self):
        pi_result=calculate_pi()
        curr_file=open("table.txt","a")
        curr_file.write(str(pi_result))
        curr_file.write("\n")
        curr_file.close()
        
    
    def add_process(self):
        client_messagelist=self.client_message.split(" ")
        x=client_messagelist[1]
        y=client_messagelist[2]
        add_result=add(int(x),int(y))
        curr_file=open("table.txt","a")
        curr_file.write(str(add_result))
        curr_file.write("\n")
        curr_file.close()
    
    def sort_process(self):
       client_messagelist=self.client_message.split(" ")
       list_integer=[]
       for i in range(0,len(client_messagelist)-1):
            list_integer.append(int(client_messagelist[i+1]))
       list_integer.sort()
       list_string=""
       for item in list_integer:
            list_string=list_string+str(item)+" "
       curr_file=open("table.txt","a")
       curr_file.write(list_string)
       curr_file.write("\n")
       curr_file.close()
        

    def matmultiply_process(self):
        client_message1=self.client_message.split(".")
        matrices=client_message1[1].split(";")
        mat1=matrices[0]
        mat2=matrices[1]
        mat3=matrices[2]
        matrix1=make_matrix(mat1)
        matrix2=make_matrix(mat2)
        matrix3=make_matrix(mat3)
        Result_mat1and2=np.dot(matrix1,matrix2)
        Result_mat123=np.dot(Result_mat1and2,matrix3)
        result_mult=""
        for i in range(0,len(Result_mat123)):
            for j in range(0,len(Result_mat123[i])):
                result_mult=result_mult+str(Result_mat123[i][j])+" "
            result_mult=result_mult+"," 
        curr_file=open("table.txt","a")
        curr_file.write(result_mult)
        curr_file.write("\n")
        curr_file.close()  

    def gettable_process(self):
        curr_file=open("table.txt","rb")
        flag="available"
        while flag=="available":
            curr_filedata=curr_file.read(1024)
            if curr_filedata:
                self.client_connect.send(curr_filedata) 
            else:
                flag="notavailable"
        curr_file.close()
        curr_file=open("table.txt","w")
        curr_file.write(" ")  
        curr_file.close()
       


def process_types(client_connect,client_address):
    while server_connected==1:
        client_message=client_connect.recv(2048).decode(message_format)
        process_chosen=client_message[0]
        curr_process=process_chosen
        

        if curr_process=="c": # this condition does calculates_pi process
            print("Current process running in server: calculate_pi")
            process_switch=switch_process("calculate_pi",client_connect,client_message)
            process_switch.calculatepi_process()
            break

        if curr_process=="a": # this condition does add process
           print("Current process running in server: add")
           process_switch=switch_process("add",client_connect,client_message)
           process_switch.add_process()
           break

        if curr_process=="s": # This condition does sort process
            print("Current process running in server: sort")
            process_switch=switch_process("sort",client_connect,client_message)
            process_switch.sort_process()
            break

        if curr_process=="m": #this condition does matrix_multiply process
            print("Current process running in server: matrix_multiply")
            process_switch=switch_process("matrix_multiply",client_connect,client_message)
            process_switch.matmultiply_process()
            break

        if curr_process=="g": #this condition does matrix_multiply process
            print("Current process running in server: get_table")
            process_switch=switch_process("get_table",client_connect,client_message)
            process_switch.gettable_process()
            break       
    client_connect.close()

def multi_connection():
    socket_server.listen() # the server is listening to the client to receive any commands
    print("the connected server "+str(server_num)+" is listening ")
    while server_connected:
        client_connect,client_address=socket_server.accept()
        print("the client is connected ")
        multi_thread=threading.Thread(target=process_types, args=(client_connect,client_address))
        multi_thread.start()
        print("No of connections are "+str(threading.activeCount()-1))

multi_connection()