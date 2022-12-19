import re
inf1 = re.compile(r"^Рейс (\d+) (?:прибыл|отправился) (из|в) (\S+) в (\d{2}:\d{2}:\d{2}$)")
first = open('info.txt', 'r', encoding='UTF-8')
second = open('new_info.txt', 'w+', encoding='UTF-8')
for i in first:
    res = re.search(inf1, i)
    if res:
        second.write(
            f"[{res.groups()[3]}] Поезд № {res.groups()[0]} {res.groups()[1]} {res.groups()[2]}\n"
        )
