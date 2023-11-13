import socket
import re
import ipaddress

MAX_CHAR = 4096
    
def receive():
    VM_IP = "192.168.1.15"
    ALL_IP = ""
    PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

    


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ALL_IP, PORT)) #Inner brackets define a tuple
        s. settimeout(30.0)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            exit = False
            while not exit:
                data = conn.recv(1024)
                if not data:
                    exit = True
                else:
                    print(data.decode(),end="#")
                conn.sendall(data)

def send(server, message):
    PORT = 65432 # The port used by the server
    
    mesg_len = False
    while mesg_len == False:
        message = input("Enter message (max 4096 characters): ")
        if message.len() > 4096:
            print("message length exceeds the limit")
        else:
            mesg_len = True

    check == False
    while(check == False):
        recipIP = input("Inter Recipient IP: ")
        check = validate(recipIP)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(30.0)#Time out of 30 seconds if not received
        s.connect((server, PORT))
        s.settimeout(None)#Always set timeout to none before sending.
        s.sendall(message.encode())
        data = s.recv(1024)
    # SERVER = "192.168.56.102" #IP Address of the recipient.
    # PORT = 65432 # The port used by the server

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.settimeout(30.0)#Time out of 30 seconds if not received
    #     s.connect((SERVER, PORT))
    #     s.settimeout(None)#Always set timeout to none before sending.
    #     s.sendall(b"Hello, world")
    #     data = s.recv(1024)

def validate(ip_addr):
    check = True
    split_IP = ip_addr.split()
    if((len(split_IP) < 5) and (len(split_IP) > 0)):
        for i in range(len(split_IP)):
            if not isinstance(int(split_IP[i]), int):
                print("Error not a valid IPv4 Address:")
                i == len(split_IP)
                check == False
            if (int(split_IP[i]) < 0) or (int(split_IP[i]) > 255):
                print("Error not a valid IPv4")
                i == len(split_IP)
                check == False
    else:
        print("Invalid IP Address length")
        check == False
    return check

def menu():
    print("===The Python Communicator===\n" +
          "1) send message\n2) receive message\n0) exit")
    # num = input("Enter option: ")
    i = 1
    while i != 0:
        num = input("Enter option: ")
        if num == "0":
            print("\nGoodbye!")
            i = 0
        elif num == "1":
            send()
            i = 0
        elif num == "2":
            receive()
            i = 0
        else:
            print("Error, invalid input")

def main():
    menu()