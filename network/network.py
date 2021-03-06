import socket
from network import parser as Parser

import sys
sys.path.append("./IA")
from IA import ia as IA

sys.path.append("./GameObjects")
from GameObjects import Callais



DEFAULT_PORT = 1337
DEFAULT_IP = "127.0.0.1"
DEFAULT_NAME = "Undefined"
DEFAULT_ENCODE = "utf-8"

BUFFSIZE_RECV = 2048



class Network ():

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

    if(len(sys.argv) != 4):
        exit()
    else:
        try:
            ip = sys.argv[1]
            port = int(sys.argv[2])
            name = sys.argv[3]
        except e:
            exit()
    moves = ['N', 'S', 'E', 'O']
    i = 0

    net = Network(ip, port, name)
    # print("Numero de joueur : "+str(net.getNumPlayer()))

    mouleFixed = None
    while 1:
        # print("RECEPTION DU PLATEAU ")
        game = net.getBoardState()

        if not game:
            break

        myself = game.players[net.getNumPlayer()]
        # print("COMPUTING DE L'IA")
        depart = game.getPlayerCase(myself)


        if mouleFixed and type(game.getCase(mouleFixed.y, mouleFixed.x)) != Callais.Moule:
            # print("MA MOULE ELLE SES BARRE LA PUTE")
            mouleFixed = None
        # goal = #IA.find_goal(depart,game.getMoule(),game.listeDepartOthers(myself,game.players),game)
        if not mouleFixed:
            goal = IA.sortMoule(game.getMoule(),depart)[0]
            mouleFixed = goal
            move = IA.shorter_way(depart,goal,game)[0]
        elif mouleFixed.distance(game.getPlayerCase(myself)) <= 1:
            goal = IA.sortMoule(game.getMoule(),depart)[0]
            mouleFixed = goal
            move = IA.shorter_way(depart,goal,game)[0]
        else:
            move = IA.shorter_way(depart,goal,game)[0]



        # print("ENVOI DU MOVE")

        net._send(move)
        i+=1

