class notebook:
    def __init__(self) -> None:
        self.ligado: bool = False
        self.carga: int = 0

    def __str__(self) -> str:
        return f""
    
def main():
    note = notebook()

    while True:
        line: str = input()
        print("$" + line )
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        if args[0] == "show":
            print(note)