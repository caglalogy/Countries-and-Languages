import json

# Opening JSON file
with open('country-by-languages.json') as json_file:
    data = json.load(json_file)

listOfLists = list()

for sub_dict in data:
    listOfLists.append(list(sub_dict.values()))

def list_countries(listOfLists):
    i = 1
    country_list = list()
    for countries in listOfLists:
        country_list.append(countries[0])

    country_list.sort()
    for a in country_list:
        print(i ,". ", a )
        i+=1

def list_languages(listOfLists):
    i = 1
    language_list = list()
    for languages in listOfLists:
        subLanList = languages[1]
        for elm in subLanList:
            if elm not in language_list:
                language_list.append(elm)

    language_list.sort()
    for a in language_list:
        print(i ,". ", a )
        i+=1
    
def search_country_for_languages(listOfLists,targetCountry):
    i = 0
    for x in listOfLists:
        if(x[0] == targetCountry):
            for languages in x[1]:
                print(i+1 , ". " , languages)
                i+=1

def search_language_for_countries(listOfLists, targetLang):
    CList = list()
    i = 0
    for counAndLangs in listOfLists:  # [Country , [lan1, lan2, lan3]]
        for lang in counAndLangs[1]: # iterate on [lan1, lan2, lan3]
            if lang == targetLang:
                CList.append(counAndLangs[0])
    
    for a in CList:
        print(i+1 ,". ", a )
        i+=1

def menu(listOfLists):
    choice = int(input('''
    1 - list of languages (alphabetically)
    2 - list of countries (alphabetically)
    3 - search the spoken languages by the country name
    4 - search the countries by the given language

    What do you want to do: (1,2,3,4): 
    '''))

    if choice == 1:
        list_languages(listOfLists)
    elif choice == 2:
        list_countries(listOfLists)
    elif choice == 3:
        tar = input("enter the country name you want to learn which languages are spoken: ")
        search_country_for_languages(listOfLists,tar)
    elif choice == 4:
        tar2 = input("enter the language to list all the countries that is spoken on it: ")
        search_language_for_countries(listOfLists,tar2)

    print("type 1 to load menu again, 2 to quit")
    choice2 = int(input())

    if choice2 == 1:
        menu(listOfLists)
    elif choice2 == 2:
        return
    
menu(listOfLists)

