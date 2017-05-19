import socket
import parser as Parser
import sys
sys.path.append("../IA")
import ia as IA


DEFAULT_PORT = 1337
DEFAULT_IP = "127.0.0.1"
DEFAULT_NAME = "Undefined"
DEFAULT_ENCODE = "utf-8"

BUFFSIZE_RECV = 2048



class Network():

    def __init__(self, ip=DEFAULT_IP, port=DEFAULT_PORT, name=DEFAULT_NAME):
        self.skt = socket.socket()
        self.ip = ip
        self.port = port
        self.name = name
        self.playerNumber = -1


        self.parser = Parser.Parser()
        self._connect()

    def _connect(self):
        self.skt.connect((self.ip, self.port))
        self._send_name()
        self.playerNumber = self._get()

    def _send_name(self):
        self._send(self.name)

    def _close(self):
        self.skt.close()

    def _send(self, msg):
        msg += "\n"
        msg = msg.encode(DEFAULT_ENCODE)
        self.skt.send(msg)

    def _get(self):
        return self.skt.recv(BUFFSIZE_RECV).decode('utf-8')

    def getNumPlayer(self):
        return int(self.playerNumber)

    def getBoardState(self):
        return Parser.Parser().parseIn(self._get())




if __name__ == "__main__":

    moves = ['N', 'S', 'E', 'O']
    i = 0

    net = Network()
    print("Numero de joueur : "+str(net.getNumPlayer()))

    while 1:
        print("RECEPTION DU PLATEAU ")
        game = net.getBoardState()


        myself = game.players[net.getNumPlayer()]
        print("MYSELF : ")
        print(myself)
        print("COMPUTING DE L'IA")
        depart = game.getPlayerCase(myself)
        move = IA.shorter_way(depart,game.getCase(5,5),game)[0]


        print("ENVOI DU MOVE")
        #move = moves[i%4]

        net._send(move)
        i+=1

