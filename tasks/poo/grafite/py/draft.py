class Grafite:
    def __init__ (self, calibre:float, hardness:str, size:int ):
        self.__calibre = calibre
        self.__hardness = hardness
        self.__size = size

    def getcalibre(self):
        return self.__calibre
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size:int):
        self.__size = size
    
    def usagepersheet(self) -> int:
        if self.__hardness == 'HB':
            return 1
        elif self.__hardness == '2B':
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        return 0
    
    def __str__(self):
        return f"[{self.__calibre}:{self.__hardness}:{self.__size}]"
    
class Pencil:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__ponta: Grafite | None = None

    def HasGrafite(self) -> bool:
        if self.__ponta != None:
            return True
        else:
            return False
        
    def insert(self, grafite: Grafite) -> bool:
        if self.__calibre != grafite.getcalibre(): #primeiro voce verifica se o grafite é do mesmo calibre que a lapiseira, os dois tem que ser 0.7 por exemplo
            print("fail: calibre incompativel")
            return False
        
        if self.HasGrafite(): #depois voce verifica se já tem um grafite dentro da lapiseira
            print("fail: ja existe grafite")
            return False
        
        self.__ponta = grafite #se o calibre for igual e não tiver grafite dentro, ai vc coloca o grafite na lasipeira
        return True
   
    def remove(self) -> Grafite | None:
        if self.HasGrafite() == False: #verifica se a lapiseira ta vazia
            print("fail: nao existe grafite")
            return None
           
        aux = self.__ponta #se nao tiver vazia, tira o grafite
        self.__ponta = None
        return aux

    def writePage(self) -> None:
        if self.HasGrafite() == False: #ve se tem grafite pra poder escrever
            print("fail: nao existe grafite")
            return
        
        assert self.__ponta is not None # isso aqui é legal
        if self.__ponta.getSize() <= 10: #ve se ainda tem grafite suficiente pra escrever
            print("fail: tamanho insuficiente")
            return

        gasto = self.__ponta.usagepersheet() #quanto de grafite voce gasta enquanto escreve
        tam_A = self.__ponta.getSize() #o tamanho do grafite

        if tam_A - gasto < 10: #ve se ainda sobra grafite depois de usar
            self.__ponta.setSize(10)
            print("fail: folha incompleta")
            return
        
        self.__ponta.setSize(tam_A - gasto)

    def __str__(self) -> str:
        aux = f"{self.__ponta}" if self.__ponta != None else "null"
        
        return f"calibre: {self.__calibre}, grafite: {aux}"
    

def main():
    pencil: Pencil = Pencil(0.5) #aqui eu to colocando um valor qualquer só pra ser substituido depois
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "init":
            calibre = float(args[1])
            pencil = Pencil(calibre)
        elif args[0] == "remove":
            pencil.remove() #nessa atividade ele não quer que print o remove
        elif args[0] == "insert":
            grafite = Grafite(float(args[1]), args[2], int(args[3])) #fazendo um grafite pra colocar na lapiseira
            pencil.insert(grafite) #colocando na lapiseira
        elif args[0] == "write":
            pencil.writePage()

main()