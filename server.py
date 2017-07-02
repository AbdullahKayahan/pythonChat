import select, socket, sys, pdb
from siniflar import Selection, Room, User # ilgili siniflarin bulundugu dosya import ediliyor
import siniflar

READ_BUFFER = 4096

host = '127.0.0.1'
listen_sock = siniflar.create_socket((host, siniflar.PORT))

menu = Selection()
connection_list = []
connection_list.append(listen_sock)

while True:
    
    read_users, write_users, error_sockets = select.select(connection_list, [], [])
    for user in read_users:
        if user is listen_sock: # Yeni Baglanti
            new_socket, add = user.accept()
            new_user = User(new_socket) # user ile soket esleniyor
            connection_list.append(new_user)
            menu.login(new_user)

        else: # new message
            msg = user.socket.recv(READ_BUFFER)
            if msg:
                msg = msg.decode().lower()
                menu.parse_message(user, msg)
            else:
                user.socket.close()
                connection_list.remove(user)

    for sock in error_sockets: # close error sockets
        sock.close()
        connection_list.remove(sock)
