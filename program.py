import json
import yaml
import os
import sys



EXTENTIONS = {".json", ".yml", ".yaml", ".xml"}


def verify(readPath, writePath):

    if readPath == writePath:
        exit("BARDZO ŚMIESZNE")

    print(os.path.splitext(readPath)[1])
    if (os.path.splitext(readPath)[1] in EXTENTIONS) == False:
        exit("Nie obsługiwane rozszerzenie pliku wejściowego")

    if (os.path.splitext(writePath)[1] in EXTENTIONS) == False:
        exit("Nie obsługiwane rozszerzenie pliku wyjściowego")



    try:
        if os.path.isfile(readPath) == False:
            exit("Plik wejściowy nie istnieje")
        if os.access(readPath, os.R_OK) :
            print("READ OK")
    except PermissionError:
        print("Błąd: Brak dostępu do \"" + readPath + "\" ")



    try:
        if os.path.isfile(writePath):
            print("Plik docelowy już istnieje, czy chcesz kontynuować? [t/n]")
            while True:
                inValue = input("> ")
                if inValue == "t" or inValue == "T":
                    break
                if inValue == "n" or inValue == "N":
                    exit("Program zatrzymany przez użytkownika")
                if os.access(writePath, os.W_OK):
                    print("WRITE OK")
    except PermissionError:
        print("Błąd: Nie można zapisać do \"" + writePath + "\" ")


def load(filePath):

    fileExt = os.path.splitext(filePath)[1]

    if fileExt == ".json":
        try:
            with open(filePath, "r") as stream:
                dic = json.load(stream)
        except:
            pass

    elif fileExt == ".yml" or fileExt == ".yaml":
        with open(filePath, "r") as stream:
            dic = yaml.safe_load(stream)
    elif fileExt == ".xml":
        print("placeholder")
    else:
        exit("Nieznane rozszerzenie.")
    print("odczyt zakończony sukcesem")
    return dic

def save(filePath, dic):
    fileExt = os.path.splitext(filePath)[1]
    try:
        if fileExt == ".json":
            with open(filePath, "w") as stream:
                stream.write(json.dumps(dic))
        elif fileExt == ".yml" or fileExt == ".yaml":
            with open(filePath, "w") as stream:
                stream.write(yaml.dumps(dic))
        elif fileExt == ".xml":
            print("placeholder")
        else:
            exit("Nieznane rozszerzenie.")
    except:
        exit("Błąd zapisu")
    print("zapis zakończony sukcesem")


def main():
    #weryfikacja argumentów
    if len(sys.argv) != 3:
        print("Błąd, program oczekuje dwóch argumentów")
        exit()
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    verify(path1, path2)
    dic = load(path1)
    save(filePath=path2, dic=dic)



def test():
    verify("plik1","plik2")

if __name__ == '__main__':
    main()
    #test()