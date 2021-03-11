class K:
    taypmv = "PD"
    lim = 1
class p:
    taypmv ='p'
    f1 = 1
    lim = 10
class Q:
    taypmv = 'PD'
    lim = 10
class L:
    taypmv= 'P'
    lim = 10
class B:
    taypmv="D"
    lim = 10
class H:
    taypmv = 'H'
    lim = 10
Kw = K();Kw.pos = (6,1,0);Kw.name = 'K1w'
Kb = K();Kb.pos = (6,10,9);Kb.name = "K1b"

Q1w = Q();Q1w.name = 'Q1w';Q1w.pos = (4,0,1)
Q1b = Q();Q1b.name = 'Q1b';Q1b.pos = (4,9,10)

b1w = B();b1w.name = "b1w";b1w.pos = (5,0,0)
b2w = B();b2w.name = "b2w";b2w.pos = (5,1,1)
b3w = B();b3w.name = "b3w";b3w.pos = (5,2,2)

b1b = B();b1b.name = "b1b";b1b.pos = (5,10,10)
b2b = B();b2b.name = "b2b";b2b.pos = (5,9,9)
b3b = B();b3b.name = "b3b";b3b.pos = (5,8,8)

l1w = L();l1w.name = 'l1w';l1w.pos = (8, 3, 0)
l2w = L();l2w.name = 'l2w';l2w.pos = (2,0,3)

l1b = L();l1b.name = 'l1b';l1b.pos = (8,10,7)
l2b = L();l2b.name = 'l2b';l2b.pos = (2,7,10)

h1w = H();h1w.name = "h1w";h1w.pos = (7,2,0)
h2w = H();h2w.name = "h2w";h2w.pos = (3,0,2)

h1b = H();h1b.name = "h1b";h1b.pos = (7,10,8)
h2b = H();h2b.name = "h2b";h2b.pos = (3,8,10)

p1w = p();p1w.name = "p1w";p1w.pos = (1,0,4)
p2w = p();p2w.name = "p2w";p2w.pos = (2,1,4)
p3w = p();p3w.name = "p3w";p3w.pos = (3,2,4)
p4w = p();p4w.name = "p4w";p4w.pos = (4,3,4)
p5w = p();p5w.name = "p5w";p5w.pos = (5,4,4)
p6w = p();p6w.name = "p6w";p6w.pos = (6,4,3)
p7w = p();p7w.name = "p7w";p7w.pos = (7,4,2)
p8w = p();p8w.name = "p8w";p8w.pos = (8,4,1)
p9w = p();p9w.name = "p9w";p9w.pos = (9,4,0)

p1b = p();p1b.name = "p1b";p1b.pos = (1,6,10)
p2b = p();p2b.name = "p2b";p2b.pos = (2,6,9)
p3b = p();p3b.name = "p3b";p3b.pos = (3,6,8)
p4b = p();p4b.name = "p4b";p4b.pos = (4,6,7)
p5b = p();p5b.name = "p5b";p5b.pos = (5,6,6)
p6b = p();p6b.name = "p6b";p6b.pos = (6,7,6)
p7b = p();p7b.name = "p7b";p7b.pos = (7,8,6)
p8b = p();p8b.name = "p8b";p8b.pos = (8,9,6)
p9b = p();p9b.name = "p9b";p9b.pos = (9,10,6)
chmanpos = [p1b,p2b,p3b,p4b,p5b,p6b,p7b,p8b,p9b,p1w,p2w,p3w,p4w,p5w,p6w,p7w,p8w,p9w,b1w,b2w,b3w,b1b,b2b,b3b,
            l1w,l2w,l1b,l2b,h1w,h1b,h2w,h2b,Q1w,Q1b,Kw,Kb]
class move:
    bord = {(0, 0, 5): '-', (0, 1, 6): '-', (0, 2, 7): '-', (0, 3, 8): '-', (0, 4, 9): '-', (0, 5, 10): '-',
(1, 0, 4): '-', (1, 1, 5): '-', (1, 2, 6): '-', (1, 3, 7): '-', (1, 4, 8): '-', (1, 5, 9): '-', (1, 6, 10): '-',
(2, 0, 3): '-', (2, 1, 4): '-', (2, 2, 5): '-', (2, 3, 6): '-', (2, 4, 7): '-', (2, 5, 8): '-', (2, 6, 9): '-', (2, 7, 10): '-',
(3, 0, 2): '-', (3, 1, 3): '-', (3, 2, 4): '-', (3, 3, 5): '-', (3, 4, 6): '-', (3, 5, 7): '-', (3, 6, 8): '-', (3, 7, 9): '-', (3, 8, 10): '-',
(4, 0, 1): '-', (4, 1, 2): '-', (4, 2, 3): '-', (4, 3, 4): '-', (4, 4, 5): '-', (4, 5, 6): '-', (4, 6, 7): '-', (4, 7, 8): '-', (4, 8, 9): '-', (4, 9, 10): '-',
(5, 0, 0):'-',(5, 1, 1):'-',(5, 2, 2):'-',(5, 3, 3):'-',(5, 4, 4):'-',(5, 5, 5):'-',(5, 6, 6):'-',(5, 7, 7):'-',(5, 8, 8):'-',(5, 9, 9):'-',(5, 10, 10):'-',
(6, 1, 0):'-',(6, 2, 1):'-',(6, 3, 2):'-',(6, 4, 3):'-',(6, 5, 4):'-',(6, 6, 5):'-',(6, 7, 6):'-',(6, 8, 7):'-',(6, 9, 8):'-',(6, 10, 9):'-',
(7, 2, 0):'-',(7, 3, 1):'-',(7, 4, 2):'-',(7, 5, 3):'-',(7, 6, 4):'-',(7, 7, 5):'-',(7, 8, 6):'-',(7, 9, 7):'-',(7, 10, 8):'-',
(8, 3, 0):'-',(8, 4, 1):'-',(8, 5, 2):'-',(8, 6, 3):'-',(8, 7, 4):'-',(8, 8, 5):'-',(8, 9, 6):'-',(8, 10, 7):'-',
(9, 4, 0):'-',(9, 5, 1):'-',(9, 6, 2):'-',(9, 7, 3):'-',(9, 8, 4):'-',(9, 9, 5):'-',(9, 10, 6):'-',
(10, 5, 0):'-',(10, 6, 1):'-',(10, 7, 2):'-',(10, 8, 3):'-',(10, 9, 4):'-',(10, 10, 5):'-'}
    ippl = "w"
    def __init__(self):
        self.check = 0
        for i in range(-5, 6):
            for j in range(11 - abs(i)):
                if i < 0:
                    for k in range(len(chmanpos)):
                        if self.bord.get((5 + i, j, abs(i) + j)) == "-" and chmanpos[k].pos == (5 + i, j, abs(i) + j):
                            self.bord[(5 + i, j, abs(i) + j)] = chmanpos[k]
                else:
                    for k in range(len(chmanpos)):
                        if self.bord.get((5+i,i+j,j)) == "-" and chmanpos[k].pos == ((5+i,i+j,j)):
                            self.bord[(5+i,i+j,j)] = chmanpos[k]

    def chekpos(self,p,bord):
        if bord.get(p) == '-':
            self.psm.append(p)
            return 1
        elif bord.get((p[0], p[1], p[2])) == None:
            return 0
        elif bord.get((p[0], p[1], p[2])).name == 'K1b' and self.ippl == "w":
            self.check = "b"
        elif bord.get((p[0], p[1], p[2])).name == 'K1w' and self.ippl == "b":
            self.check = "w"
            return 0
        elif bord.get((p[0], p[1], p[2])).name[2] != self.chman.name[2]:
            self.psm.append((p[0], p[1], p[2]))
            self.eda.append((p[0], p[1], p[2]))
            return 0
        elif bord.get((p[0], p[1], p[2])).name[2] == self.chman.name[2]:
            return 0
        else:
            return 0

    def checkmv(self,chman,bord):
        self.chman = chman
        p=list(chman.pos)
        taypmv = chman.taypmv
        lim = chman.lim
        self.psm = list()
        self.eda = list()
        check = 0
        # P - Движение по прямой
        # D - По диагонали
        # PD - Королева король
        # H - Коннь
        # p - Пешка
        if taypmv == "P" or taypmv == 'PD':
            # Поперек Left справа налево
            for i in range(1,lim+1):
                if self.chekpos((p[0]+i,p[1]+i,p[2]),bord) == 1: pass
                else: break
            # Поперек Left слева направо
            for i in range(1,lim+1):
                if self.chekpos((p[0]-i,p[1]-i,p[2]),bord) == 1: pass
                else: break
            # Поперек right справа налево
            for i in range(1,lim+1):
                if self.chekpos((p[0]+i,p[1],p[2]-i),bord) == 1: pass
                else: break
            # Поперек right слева направо
            for i in range(1,lim+1):
                if self.chekpos((p[0]-i,p[1],p[2]+i),bord) == 1: pass
                else: break
            # По x вверх
            for i in range(1,lim+1):
                if self.chekpos((p[0],p[1]+i,p[2]+i),bord) == 1: pass
                else: break
            # По x вниз
            for i in range(1,lim+1):
                if self.chekpos((p[0],p[1]-i,p[2]-i),bord) == 1: pass
                else: break
        if taypmv == "D" or taypmv == "PD":
            #Вправо вверх
            for i in range(1,lim+1):
                if self.chekpos((p[0]+i,p[1]+2*i,p[2]+i),bord) == 1: pass
                else: break
            #Вправо вниз
            for i in range(1,lim+1):
                if self.chekpos((p[0]+i,p[1]-i,p[2]-i*2),bord) == 1: pass
                else: break
            #Влево вверх
            for i in range(1,lim+1):
                if self.chekpos((p[0]-i,p[1]+i,p[2]+i*2),bord) == 1: pass
                else: break
            #Влево вниз
            for i in range(1,lim+1):
                if self.chekpos((p[0]-i,p[1]-i*2,p[2]-i),bord) == 1: pass
                else: break
            #Вправо
            for i in range(1,lim+1):
                if self.chekpos((p[0]+i*2,p[1]+i,p[2]-i),bord) == 1: pass
                else: break
            #Влево
            for i in range(1,lim+1):
                if self.chekpos((p[0]-i*2,p[1]-i,p[2]+i),bord) == 1: pass
                else: break
        if taypmv == "H":
            self.chekpos((p[0]+1, p[1]-2, p[2]-3),bord)
            self.chekpos((p[0]+2, p[1]-1, p[2]-3),bord)
            self.chekpos((p[0]-2, p[1]-3, p[2]-1),bord)
            self.chekpos((p[0]-1, p[1]-3, p[2]-2),bord)
            self.chekpos((p[0]-3, p[1]-1, p[2]+2),bord)
            self.chekpos((p[0]-3, p[1]-2, p[2]+1),bord)
            self.chekpos((p[0]-2, p[1]+1, p[2]+3),bord)
            self.chekpos((p[0]-1, p[1]+2, p[2]+3),bord)
            self.chekpos((p[0]+1, p[1]+3, p[2]+2),bord)
            self.chekpos((p[0]+2, p[1]+3, p[2]+1),bord)
            self.chekpos((p[0]+3, p[1]+2, p[2]-1),bord)
            self.chekpos((p[0]+3, p[1]-1, p[2]-2),bord)
        if taypmv == "p":
            if chman.name[2] == "w":
                if self.bord.get((p[0],p[1]+1,p[2]+1)) == '-':
                    self.psm.append((p[0], p[1] + 1, p[2] + 1))
                    if chman.f1 == 1 and self.bord.get((p[0],p[1]+2,p[2]+2)) == '-':
                        self.psm.append((p[0],p[1]+2,p[2]+2))
                if self.bord.get((p[0]-1,p[1],p[2]+1)) != None:
                    if self.bord.get((p[0]-1,p[1],p[2]+1)) != "-" and self.bord.get((p[0]-1,p[1],p[2]+1)).name[2] != chman.name[2]:
                        self.eda.append((p[0]-1,p[1],p[2]+1))
                        self.psm.append((p[0]-1,p[1],p[2]+1))
                if self.bord.get((p[0]+1,p[2]+1,p[2])) != None:
                    if self.bord.get((p[0]+1,p[2]+1,p[2])) != "-" and self.bord.get((p[0]+1,p[2]+1,p[2])).name[2] != chman.name[2]:
                        self.eda.append((p[0]+1,p[1]+1,p[2]))
                        self.psm.append((p[0]+1,p[1]+1,p[2]))
            else:
                if self.bord.get((p[0],p[1]-1,p[2]-1)) == '-':
                    self.psm.append((p[0],p[1]-1,p[2]-1))
                    if chman.f1 == 1 and self.bord.get((p[0],p[1]-2,p[2]-2)) == '-':
                        self.psm.append((p[1],p[1]-2,p[2]-2))
                if self.bord.get((p[0]-1,p[1]-1,p[2])) != None:
                    if self.bord.get((p[0]-1,p[1]-1,p[2])) != "-" and self.bord.get((p[0]-1,p[1]-1,p[2])).name[2] != chman.name[2]:
                        self.eda.append((p[0]-1,p[1]-1,p[2]))
                        self.psm.append((p[0]-1,p[1]-1,p[2]))
                if self.bord.get((p[0]-1,p[1],p[2]+1)) != None:
                    if self.bord.get((p[0]-1,p[1],p[2]+1)) != "-" and self.bord.get((p[0]-1,p[1],p[2]+1)).name[2] != chman.name[2]:
                        self.eda.append((p[0]+1,p[1],p[2]-1))
                        self.psm.append((p[0]+1,p[1],p[2]-1))
        return self.psm, self.eda
    def magic(self,p1,p2):
        vmv = list()

        if self.bord.get(p1) == None: return "Error: Нет таких координат!"

        if self.bord.get(p1) == "-": return "Мимо"

        if self.bord.get(p1).name[2] != self.ippl: return "Не тот цвет"

        if self.check == ("w" or "b"):
            self.bord1 = self.bord.copy()
            self.bord1[p1] = "-"
            self.bord1[p2] = self.bord[p1]
            self.ipplv = self.ippl
            if self.ippl == "w":
                self.ippl = "b"
            else:
                self.ippl = "w"
            self.recheck = self.check
            self.check = 0
            for i in chmanpos:
                if i.name[2] == self.ippl:
                    self.checkmv(self.bord1.get(i.pos), self.bord1)
            if self.check != 0:
                self.ippl = self.ipplv
                self.check = self.recheck
                self.bord1 = self.bord.copy()
                return "Ход невозм."
            else:
                self.ippl = self.ipplv
                ret = self.checkmv(self.bord.get(p1), self.bord)
                self.bord = self.bord1.copy()
                self.checkmv(self.bord1.get(p2), self.bord)
                return "ALL RIGHT", ret
        else:
            """for i in chmanpos:
                if i.name[2] == self.ippl and i.name != f"K1{self.ippl}":
                    vmv.append(self.checkmv(i,self.bord)[0])"""

            if p2 in self.checkmv(self.bord.get(p1),self.bord)[0]:
                self.bord1 = self.bord.copy()
                self.bord1[p1] = "-"
                self.bord1[p2] = self.bord[p1]
                self.ipplv = self.ippl
                if self.ippl == "w":
                    self.ippl = "b"
                else:
                    self.ippl = "w"
                for i in chmanpos:
                    if i.name[2]==self.ippl:
                        self.checkmv(self.bord1.get(i.pos),self.bord1)
                if self.check != 0:
                    self.ippl = self.ipplv
                    self.check =0
                    self.bord1 = self.bord.copy()
                    return "Ход невозм."
                else:
                    self.ippl = self.ipplv
                    ret = self.checkmv(self.bord.get(p1),self.bord)
                    self.bord = self.bord1.copy()
                    self.checkmv(self.bord1.get(p2),self.bord)

                    return "ALL RIGHT", ret



            else:
                return "not move"


a = move()
val = (5,4,4)
var = (5,5,5)
print(a.magic(val,var))