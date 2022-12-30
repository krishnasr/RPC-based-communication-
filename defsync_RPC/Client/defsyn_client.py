import socket
import os

# the below variables are constant vairables used for coding the program
port_num=8080 # using port number 8080
server_num=socket.gethostbyname(socket.gethostname()) # gethostname returns the current computer's ip address
server_address=(server_num,port_num)
message_format='utf-8'
server_connected=1



class switch_process:
    def __init__(self, process):
        self.process=process

    def calculatepi_process(self):
        curr_processmessage="c"+" "
        processto_send=curr_processmessage.encode(message_format)
        socket_server.send(processto_send)
        
    def add_process(self):
        x= input("enter the first number: ")
        y=input(" enter the second number: ")
        curr_processmessage="a"+" "+str(x)+" "+str(y)
        processto_send=curr_processmessage.encode(message_format)
        socket_server.send(processto_send)
        
    def sort_process(self):
        get_array=input("enter the array with space seperated values")
        curr_processmessage="s"+" "+get_array
        processto_send=curr_processmessage.encode(message_format)
        socket_server.send(processto_send)
        
    def matmultiply_process(self):
        martrix1=input(" enter the first matrix like this one 1 3,3 4,5 6: ")
        martrix2=input(" enter the second matrix like this one 1 3,3 4,5 6: ")
        martrix3=input(" enter the third matrix like this one 1 3,3 4,5 6: ")
        curr_processmessage="m"+"."+martrix1+";"+martrix2+";"+martrix3
        processto_send=curr_processmessage.encode(message_format)
        socket_server.send(processto_send)

    def gettable_process(self):
        curr_processmessage="g "
        processto_send=curr_processmessage.encode(message_format)
        socket_server.send(processto_send)
        flag="available" 
        while flag=="available" :
            curr_filedata=socket_server.recv(1024).decode(message_format)
            if curr_filedata:
                print(curr_filedata)
            else:
                flag="notavailable"   

while server_connected==1:
    socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating socket
    socket_server.connect(server_address) #connecting to IPV4 server hence we used AF_INET
    print(" select one of these process calculate_pi, add, sort, matrix_multiply, get_table ")
    process=input("Please enter the type of process ")
    curr_process=process
    if curr_process=="calculate_pi": # this condition does calculate_pi process
        process_switch=switch_process("calculate_pi")
        process_switch.calculatepi_process()
    elif curr_process=="add": # this condition does add process
        process_switch=switch_process("add")
        process_switch.add_process()

    elif curr_process=="sort": # this condition does sort process
        process_switch=switch_process("sort")
        process_switch.sort_process()

    elif curr_process=="matrix_multiply": # this condition does matrix multiply process
        process_switch=switch_process("matrix_multiply")
        process_switch.matmultiply_process()

    elif curr_process=="get_table": # This condition does get table process
        process_switch=switch_process("get_table")
        process_switch.gettable_process()
        server_connected=0
        




