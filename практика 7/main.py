import csv


def get_books(name: str):
    word: list = []
    with open('text.csv', 'r', encoding='UTF-8') as file:
        text_reader = csv.reader(file, delimiter='|')
        for i in text_reader:
            if name.lower() in i[1].lower():
                word.append(i)
    return word


print(get_books('python'))
def get_totals(name: list):
    word: list = []
    for i in name:
        x = float(i[3]) * float(i[4])
        if x < 500:
            x += 100
    word.append((i[0], str(x)))
    return word

print(get_totals(get_books('python')))
