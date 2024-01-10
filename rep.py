import csv
import string
import secrets

def insertionSort(l: list):
    for i in range(1, len(l)):
        temp = l[i]
        j = i - 1
        while (j >= 0 and temp[4] < l[j][4]):
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = temp
    return list(reversed(l))

def fileReading():
    with open("students.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        fields = reader.fieldnames
        result = []
        for x in reader:
            result.append(list(x.values()))
    return result, fields


def ex2(l: list):
    winners = l
    top3Winners = insertionSort(list(filter(lambda x: '10' in x[3], winners)))[0:3]
    count = 1
    for x in top3Winners:
        print('{} место: {}'.format(count, x[1]))
        count += 1

def ex1(result: list):
    user = list(filter(lambda x: 'Хабаров Владимир' in x[1], result))
    if len(user) == 1:
        print('Ты получил: {}, за проект - {}'.format(user[0][4], user[0][2]))
    middleValue = 0
    count = 0
    for x in result:
        count += 1
        middleValue += int(x[4])
    with open('student_new.csv', 'w') as csvwrite:
        writer = csv.DictWriter(csvwrite, fieldnames=['Средняя оценка'])
        writer.writeheader()
        row = {'Средняя оценка': round(middleValue / count, 3)}
        writer.writerow(row)

def search(l, value):
    for x in l:
        if x[2] == value:
            return x

def ex3(l: list):
    while True:
        s = input()
        if s == 'СТОП':
            return
        else:
            result = search(l, s)
            if result != None:
                print('Проект № {} делал: {} он(а) получил(а) оценку - {}'.format(s, result[1], result[4]))
            else:
                print('Ничего не найдено.')

def ex4(file: str):
    """
    Функция для 4 задания. Выполняет создание логинов и паролей и их запись в csv - файл

    file - имя файла с пользователями в формате csv
    """

    with open(file) as csvfile:
        alphabet = string.ascii_letters + string.digits
        reader = csv.DictReader(csvfile, delimiter=';')
        headers = reader.fieldnames
        result = []
        with open('students_password.csv', 'w') as csvwrite:
            fieldnames = headers + ['nickname', 'password']
            writer = csv.DictWriter(csvwrite, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                fio = row['Name'].split(' ')
                nickname = fio[0] + '_' + fio[1][0] + fio[2][0]
                flag = True
                while flag:
                    password = ''.join(secrets.choice(alphabet) for i in range(8))
                    if (sum(c.islower() for c in password) >= 1
                            and sum(c.isupper() for c in password) >= 1
                            and sum(c.isdigit() for c in password) >= 1):
                        flag = False
                row.update({"nickname" : nickname, "password": password})
                writer.writerow(row)

def ex5(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        headers = reader.fieldnames
        p = 67
        with open('students_with_hash.csv', 'w') as csvwrite:
            writer = csv.DictWriter(csvwrite, fieldnames=headers)
            writer.writeheader()
            for row in reader:
                power = 0
                hashValue = 0
                for x in row['Name']:
                    hashValue += (ord(x) - 1039 if x != ' ' else 65) * pow(p, power) / ((pow(10,7) + 9))
                    power += 1
                row['id'] = str(hashValue)
                writer.writerow(row)

def main1():
    data, fields = fileReading()
    filename = 'students.csv'
    flag = True
    print('Выберите действие')
    while flag:
        n = input()
        try:
            n = int(n)
            if n == 1:
                ex1(data)
            elif n == 2:
                ex2(data)
            elif n == 3:
                ex3(data)
            elif n == 4:
                ex4(filename)
            elif n == 5:
                ex5(filename)
        except:
            if n == "±":
                print("Программа завершена")
                flag = False
            else:
                print("Неверный Ввод")
def main():
    data, fields = fileReading()
    filename = 'students.csv'
    l = ex1(data)
    ex2(data)
    ex3(data)
    ex4(filename)
    ex5(filename)

main1()
