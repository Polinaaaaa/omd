import csv

def reader():
    corp_summary=[] 
    with open('Corp_Summary-4i5r1ko1np8o7qyphd7tngu7io.csv', 'r', encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            corp_summary.append(row[0].split(";"))
        return(corp_summary)


def first_ierarchy():
    ierarchy = {}
    for i in reader()[1::]:
        if i[1] not in ierarchy:
            ierarchy[i[1]] = []
        if i[2] not in ierarchy[i[1]]:
            ierarchy[i[1]].append(i[2])
    return ierarchy

def svodka():
    vse_oklady = {}
    for i in reader()[1::]:
        if i[1] not in vse_oklady:
            vse_oklady[i[1]] = []
        
        vse_oklady[i[1]].append(int(i[5]))
        
    svodka_itog = []
    for i in vse_oklady:
        svodka_itog.append({'департамент': i, 'сколько_человек': len(vse_oklady[i]), 'минимальная_зп': min(vse_oklady[i]), 
                            'максимальная_зп': max(vse_oklady[i]), 'средняя_зп': sum(vse_oklady[i])/len(vse_oklady[i])})
    return(svodka_itog)

def svodka_csv():
    vse_oklady = {}
    for i in reader()[1::]:
        if i[1] not in vse_oklady:
            vse_oklady[i[1]] = []
        
        vse_oklady[i[1]].append(int(i[5]))
        
    svodka_itog = [['департамент', 'сколько_человек', 'минимальная_зп', 
                            'максимальная_зп', 'средняя_зп']]
    for i in vse_oklady:
        svodka_itog.append([i, len(vse_oklady[i]),  min(vse_oklady[i]), 
                            max(vse_oklady[i]), sum(vse_oklady[i])/len(vse_oklady[i])])
    with open('output_file.csv', 'w') as file:
        row = csv.writer(file)
        row.writerows(svodka_itog)
    return('Результат в файле output_file.csv')


def main(num):
    if num == 1:
        print(first_ierarchy())
    elif num ==2 :
        print(svodka())
    elif num ==3 :
        print(svodka_csv())

if __name__ == "__main__":
    num = int(input())
    main(num)


