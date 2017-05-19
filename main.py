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
    moves = ['N', 'S', 'E', 'O']
    i = 0

    net = network.Network(ip, port, name)
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