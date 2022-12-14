def open_file(wqe):
    opened = False
    try:
        text = open(wqe, "r")
        opened = True
        que = int(text.readline())
        return [int(z) for z in [text.readline() for i in range(que)]]
    except FileNotFoundError:
        print("данный файл не существует")
    except ValueError:
        print(f"в файле присутствуют не только числа")
    finally:
        if opened:
            text.close()
while res := input("Введите название файла: "):
    if answ := open_file(res):
        print(answ)
        break
