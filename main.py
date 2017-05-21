import sys

sys.path.append("./network")
from network import network

sys.path.append("./IA")
from IA import ia as IA

sys.path.append("./GameObjects")
from GameObjects import Callais

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

    net = network.Network(ip, port, name)

    mouleFixed = None
    while 1:
        game = net.getBoardState()

        if not game:
            break

        myself = game.players[net.getNumPlayer()]
        depart = game.getPlayerCase(myself)


        if mouleFixed and type(game.getCase(mouleFixed.y, mouleFixed.x)) != Callais.Moule:
            mouleFixed = None
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


        net._send(move)
