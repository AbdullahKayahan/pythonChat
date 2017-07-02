import socket, select, sys


def prompt():
    sys.stdout.write('>')
    sys.stdout.flush()



if __name__ == "__main__":

    if (len(sys.argv) < 3):
        print 'Usage : python telnet.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # uzak sunucuya baglanilir
    try:
        s.connect((host, port))
    except:
        print 'Unable to connect'
        sys.exit()

    print 'Servera baglanildi.'
    prompt()

    while 1:

        socket_list = [sys.stdin, s]

        # okunabilir soket listesi alinir
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            #uzak sunucudan mesaj gelir
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    # print data
                    sys.stdout.write(data)
                    prompt()

            # kullanici mesaj gonderir
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
