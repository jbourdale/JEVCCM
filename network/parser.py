# data = '4x2/D-E-N-F-D-D-D-D/3-1,1-11,9-11,1'
import re

import sys

sys.path.append("./GameObjects")
from GameObjects import Callais



class Parser(object):
    def __init__(self):
        super(Parser, self).__init__()

    def parseIn(self, indata):
        # print("INDATA")
        # print(indata)
        # print(type(indata))
        if indata is "FIN":
            return None

        try:
            p = indata.split('/')
            sz = p[0].split('x')
            board = p[1].split('-')
            players = p[2].split('-')
        except:
            return None

        if not len(board) == int(sz[0]) * int(sz[1]):
            #print("Incorrect data")
            return None
        else:
            # print('size:', sz[0], 'x', sz[1])

            game = Callais.Callais(sz[0], sz[1])

            players_arr = []
            for i,p in enumerate(players):
                if i != 0:
                    #print('player%d :'%i, p)
                    x = int(p.split(",")[0])
                    y = int(p.split(",")[1])
                    players_arr.append(Callais.Player((i-1),x,y))

            game.setPlayers(players_arr)

            for (i, e) in enumerate(board):

                coords = ( int(i/(int(sz[0]))) , i % int(sz[0]) )
                # print("case en : "+str(coords)+" , de type : ", end="")

                case = Callais.Case(coords[0], coords[1])

                if e == "D":
                    case = Callais.Dune(coords[0], coords[1])
                elif e == "S":
                    case = Callais.Sable(coords[0], coords[1])
                elif e == "F":
                    case = Callais.Frite(coords[0], coords[1])
                elif e == "B":
                    case =  Callais.Biere(coords[0], coords[1])
                else:
                    case = Callais.Moule(e, coords[0], coords[1])

                #print("AJOUT CASE : "+str(coords[0])+";"+str(coords[1]))

                game.setCase(coords[0], coords[1], case)

            return game


    def parseOut(self, outdata):
        pass


# p = Parser()
# p.parseIn(data)
