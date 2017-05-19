data = '4x2/D-E-N-F-D-D-D-D/3-1,1-11,9-11,1'


class Parser(object):
    def __init__(self):
        super(Parser, self).__init__()

    def parseIn(self, indata):
        p = indata.split('/')
        sz = p[0].split('x')
        board = p[1].split('-')
        players = p[2].split('-')
        if not len(board) == int(sz[0]) * int(sz[1]):
            print("Incorrect data")
            return None
        else:
            print('size:', sz[0], 'x', sz[1])
            for i,p in enumerate(players):
                if i != 0:
                    print('player%d :'%i, p)

            print()
            for (i, e) in enumerate(board):
                print('case en ', int(i/(int(sz[0]))), ';', i % int(sz[0]), ' contenant ', e, sep='')

    def parseOut(self, outdata):
        if():
            return outdata


p = Parser()
p.parseIn(data)