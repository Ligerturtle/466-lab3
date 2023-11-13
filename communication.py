import socket

MAX_CHAR = 4096

def main():
    print("===The Python Communicator===\n" +
          "1) send message\n2) receive message\n0) exit")
    num = input("Enter option: ")
    i = 1
    while i != 0:
        if num == 0:
            print("Goodbye!")
            i = 0
        elif num == 1:
            send()
            i = 0
        elif num == 2:
            receive()
            i = 0
        else:
            print("Error, invalid input")
    
def receive():
    VM_IP = "192.168.1.15"
    ALL_IP = ""
    PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

    message = input("Enter message (max 4096 characters): ")
    recipIP = input("Inter Recipient IP: ")
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

def send():
    SERVER = "192.168.56.102" #IP Address of the recipient.
    PORT = 65432 # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(30.0)#Time out of 30 seconds if not received
        s.connect((SERVER, PORT))
        s.settimeout(None)#Always set timeout to none before sending.
        s.sendall(b"Hello, world")
        data = s.recv(1024)