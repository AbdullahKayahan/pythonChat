import socket, pdb

MAX_CLIENTS = 30
PORT = 5000
QUIT_STRING = '<$quit$>'


def create_socket(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(0)
    s.bind(address)
    s.listen(MAX_CLIENTS)
    print("Suan Adres Dinleniyor:  ", address)
    return s

class Selection:
    def __init__(self):
	self.chat_rooms = {"room1": Room("room1"), "room2": Room("room2"), "room3": Room("room3"),
		           "room4": Room("room4")}
	self.chat_room_user_map = {} 
	self.registered_user = {"ali": "123", "veli": "1234", "ahmet": "12345", "mehmet": "12345"}

	self.is_loged = False
	self.login_description = b'[<giris> kullaniciAdi password ]Giris Yap:\n' \
		                 + b'[<kayit> kullaniciAdi password ] Kayit ol\n'

	self.menu_description = b'\n\n Menu! \n' \
		                + '[<listele>] Chat odalarini listele! \n' \
		                + '[<katil> oda_ismi] odaya katil! \n'

    def login(self, new_user):  # Giris Ekrani
        new_user.socket.sendall(self.login_description)

    def list_chat_rooms(self, user):  # Chat odalarini listeler
        msg = 'Chat Odalari...\n'
        for chat_room in self.chat_rooms:
            msg += chat_room + ": " + str(len(self.chat_rooms[chat_room].users)) + " kisi\n"
        user.socket.sendall(msg.encode())

    def parse_message(self, user, msg):


        if "<giris>" in msg:
            if len(msg.split()) >= 3:  # parametre kontrolu
                username = msg.split()[1]
                password = msg.split()[2]
                if username in self.registered_user:  # kullanici adi listede var mi kontrolu
                    if self.registered_user[username.strip()] == password:  # eger kullanici adi var ise sifre kontrolu
                        user.name = username
                        user.socket.sendall(
                            b'Giris Yapildi: ' + username.encode() + self.menu_description)  # eger bilgiler uyusuyorsa giris yapiliyor.
                        self.is_loged = True
                    else:  # sifreler uyusmaz ise tekrar giris ekrani geliyor
                        user.socket.sendall(
                            b"\n\nSifre veya kullanici adi hatali\n" + self.login_description.encode())
                else:  # kullanici adi listede yok ise tekrar giris ekrani geliyor
                    user.socket.sendall(b"\n\nBoyle bir kullanici bulunmamaktadir.\n".encode())
                    user.socket.sendall(self.login_description)
            else:  # Eger uygun formatta girmez ise tekrar giris ekrani geliyor
                user.socket.sendall(b"\n\nLutfen kullanici adinizi ve sifrenizi giriniz.\n".encode())
                user.socket.sendall(self.login_description.encode())

        elif "<kayit>" in msg:  # kayit ekrani
            username = msg.split()[1]
            password = msg.split()[2]
            self.registered_user[username] = password
            self.is_loged = True
            user.socket.sendall(b'Kayit oldunuz.Giris Yapiniz: ' + username.encode() + "\n" \
                                  + self.login_description.encode())


        elif "<katil>" in msg:  # bir gruba katilma ekrani
            same_chat_room = False
            if len(msg.split()) >= 2:
                room_name = msg.split()[1]
                if user.name in self.chat_room_user_map:  # kisi oda'da mi diye bakiyor ona gore oda degistiriyor
                    old_room = self.chat_room_user_map[user.name]
                    self.chat_rooms[old_room].remove_user(user)
                if not same_chat_room:  # kisinin yazdigi oda yok ise yeni oda olusturuyor
                    self.chat_rooms[room_name].users.append(user)
                    self.chat_rooms[room_name].welcome_new(user)
                    self.chat_room_user_map[user.name] = room_name

            else:

                user.socket.sendall(self.menu_description)


        elif "<listele>" in msg:  # chat odalarini listeleyen method'u cagiriyor
            self.list_chat_rooms(user)

        elif "<cikis>" in msg:  # odadan cikiyor
            user.socket.sendall("<cikis>".encode())
            self.remove_user(user)

        elif self.is_loged == False:
            user.socket.sendall(b"\n\nLutfen istenilen formatta giris yapiniz\n".encode())
            user.socket.sendall(self.login_description.encode())

        else:
            if user.name in self.chat_room_user_map:  # eger bir chat odasinda ise mesaj gidiyor degil ise menu cikiyor
                self.chat_rooms[self.chat_room_user_map[user.name]].broadcast(user, msg.encode())
            else:
                user.socket.sendall(self.menu_description.encode())

    def remove_user(self, user):
        if user.name in self.chat_room_user_map:
            self.chat_rooms[self.chat_room_user_map[user.name]].remove_user(user)
            del self.chat_room_user_map[user.name]
        print("Kisi: " + user.name + " ayrildi \n")
    
class Room:
    def __init__(self, name):
        self.users = [] # a list of sockets
        self.name = name

    def welcome_new(self, from_user):
        msg = self.name + " Odaya Katidi: " + from_user.name + '\n'
        for user in self.users:
            user.socket.sendall(msg.encode())
    
    def broadcast(self, from_user, msg):
        msg = from_user.name.encode() + b":" + msg
        for user in self.users:
            user.socket.sendall(msg)

    def remove_user(self, user):
        self.users.remove(user)
        leave_msg = user.name.encode() + b"Odadan Ayrildi\n"
        self.broadcast(user, leave_msg)



class User:
    def __init__(self, socket, name = "new"):
        socket.setblocking(0)
        self.socket = socket
        self.name = name

    def fileno(self):
        return self.socket.fileno()
