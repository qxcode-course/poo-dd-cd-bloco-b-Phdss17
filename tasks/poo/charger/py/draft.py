class charger:
    def __init__(self, power: int) -> None:
        self.__power: int = power 

    def getPower(self) -> int:
        return self.__power

    def __str__(self) -> str:
        return f"{self.__power}W"

class battery:
    def __init__(self, charge) -> None:
        self.__maxCharge: int = charge
        self.__charge: int = charge

    def getMaxCharge(self) -> int:
        return self.__maxCharge

    def getCharge(self) -> int:
        return self.__charge
    
    def setCharge(self, ch: int) -> None:
        if ch > self.__maxCharge:
            self.__charge = self.__maxCharge
        else:
            self.__charge = ch
    
    def __str__(self) -> str:
        return f"{self.__charge}/{self.__maxCharge}"

class notebook:
    def __init__(self) -> None:
        self.__ligado: bool = False
        self.__battery: battery | None = None
        self.__charger: charger | None = None
        self.__timeOn: int = 0

    def turn_on(self) -> None:
        if self.__battery == None and self.__charger == None:
            print("fail: não foi possível ligar")
        else:
            self.__ligado = True

    def turn_off(self) -> None:
        self.__ligado = False
        self.__timeOn = 0

    def use(self, time: int) -> None:
        if self.__ligado == False:
            print("fail: desligado")
        else:
            if self.__battery is not None and self.__battery.getCharge() > time:
                if self.__charger is not None:
                    self.__battery.setCharge(self.__battery.getCharge() + self.__charger.getPower() * time)
                else:
                    self.__battery.setCharge(self.__battery.getCharge() - time)
                self.__timeOn += time
            elif self.__battery is not None and self.__battery.getCharge() <= time:
                if self.__charger is not None:
                    self.__battery.setCharge(self.__battery.getCharge() + self.__charger.getPower() * time)
                    self.__timeOn += time
                else: 
                    self.__timeOn += self.__battery.getCharge()
                    self.__battery.setCharge(0)
                    self.__on_off()
                    print("fail: descarregou")
            elif self.__battery is None and self.__charger is not None:
                self.__timeOn += time


    def setCharger(self, charger: charger) -> None:
        if self.__charger is not None:
            print("fail: carregador já conectado")
        else:
            self.__charger = charger

    def rm_charger(self) -> charger | None:
        if self.__charger is None:
            print("fail: Sem carregador")
            return None
        else:
            aux = self.__charger
            self.__charger = None
            self.__on_off()
            return aux

    def set_battery(self, bat: battery) -> None:
        if self.__battery is not None:
            print("fail: bateria já conectado")
        else:
            self.__battery = bat

    def rm_battery(self) -> battery | None:
        if self.__battery is None:
            print("fail: Sem bateria")
            return None
        else:
            aux = self.__battery
            self.__battery = None
            self.__on_off()
            return aux

    def __on_off(self) -> None:
        if (self.__battery is not None and self.__battery.getCharge() > 0) or self.__charger is not None:
            self.__ligado = True
        else:
            self.__ligado = False

    def __str__(self) -> str:
        note = f"Notebook: {"desligado" if not self.__ligado else f"ligado por {self.__timeOn} min"}"
        bat = f", Bateria {self.__battery}" if self.__battery is not None else ""
        ch = f", Carregador {self.__charger}" if self.__charger is not None else ""
        return note + ch + bat

def __main__() -> None:
    note = notebook()

    while True:
        line: str = input()
        print("$" + line )
        args: list[str] = line.split(" ")

        match args[0]:
            case "end":
                break
            case "show":
                print(note)
            case "turn_on":
                note.turn_on()
            case "turn_off":
                note.turn_off()
            case "use":
                note.use(int(args[1]))
            case "set_charger":
                ch = charger(int(args[1]))
                note.setCharger(ch)
            case "rm_charger":
                ch = note.rm_charger()
                if ch is not None:
                    print(f"Removido {ch.getPower()}W")
            case "set_battery":
                bat = battery(int(args[1]))
                note.set_battery(bat)
            case "rm_battery":
                bat = note.rm_battery()
                if bat is not None:
                    print(f"Removido {bat}")

__main__()