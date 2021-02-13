import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.43.245" #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

player_pos = {}

def handle_client(conn, addr, name='supper'):
    print(f"[NEW CONNECTION] {addr} {name} connected.")

    #player_pos contains the position of each user
    player_pos[name] = (0,0)
    player_index = len(player_pos)-1
    msg = conn.recv(2048).decode(FORMAT)
    player_pos[name] = eval(msg)
    if player_index == 0:
        player_pos[name] = player_pos[name][:-1] + (True, )
    player_pos[name] = str(player_pos[name])
    conn.send(str(player_pos).encode(FORMAT))

    connected = True

    while connected:
        
        #disconnect properly only if disconnect message comes
        msg = conn.recv(2048).decode(FORMAT)
        #print(player_pos)
        if 'disconnect' in msg.lower():
            connected = False
        else:        
            #print(f"[{addr}] {msg}")
            player_pos[name] = msg[:-1] + ', ' + str(player_index) +', "' + name + '")'
            conn.send(str(player_pos).encode(FORMAT))
    conn.close()
    del player_pos[name]
    print(f"[SERVER] {addr} lost connection..")

def start():

    #listen for incomming connections
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")

    while True:

        #getting the address of the user
        conn, addr = server.accept()
        if len(player_pos) > 10:
            conn.send('hey um 10 players are playing'.encode(FORMAT))
        
        #starting the thread for a perticular address
        name = conn.recv(2048).decode(FORMAT)
        conn.send(f'hey {name} u are connected. ENJOY.'.encode(FORMAT))
        thread = threading.Thread(target=handle_client, args=(conn, addr, name))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


print("[STARTING] server is starting...")
start()
