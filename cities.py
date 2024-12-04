import json

def cities():
    city = open ("russia.json","r",encoding='utf-8')
    cities_data = json.loads(city.read())
    print ("Сыграем в города! Пиши в сообщении 1 город России. Пиши 'стоп' если надоело или сдаешься. Первый город - Москва. Тебе на а")
    letter = 'а' #Русская буква а
    while True:
        user_input = input()
        if user_input.lower() == 'стоп':
            print ("Отлично сыграли!")
            break
        elif user_input.lower()[0] != letter:
            print ("Первая буква не соотвествует с последней буквой загаданного слова")
        else:
            for i in range (0,len(cities_data)-1):
                if cities_data[i]['city'].lower() == user_input.lower():
                    del cities_data[i]
                    break
            else:
                print ("Такого города в России нет, или мы его называли")
                continue
            if user_input.lower()[-1] == 'ь' or user_input.lower()[-1] == 'ы'or user_input.lower()[-1] == 'й':
                letter = user_input.lower() [-2]
            else:
                letter = user_input.lower() [-1]
            print (letter)
            for i in range (0,len(cities_data)-1):
                if cities_data[i]['city'].lower()[0] == letter:
                    print (cities_data[i]['city'])
                    if cities_data[i]['city'].lower()[-1] == 'ь' or cities_data[i]['city'].lower()[-1] == 'ы'or cities_data[i]['city'].lower()[-1] == 'й':
                        letter = cities_data[i]['city'].lower() [-2]
                    else:
                        letter = cities_data[i]['city'].lower() [-1]
                    print (letter)
                    del cities_data[i]
                    break
            else:
                print ("Ты выиграл!")
                return
cities()