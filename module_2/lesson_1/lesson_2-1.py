'''1. Получите текст из файла.
2. Разбейте текст на предложения.
3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
4. Отберите все ссылки.
5. Ссылки на страницы какого домена встречаются чаще всего?
6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
'''
import re

def getcounter(textlist):
    maxcount = 0
    elements_list = set()
    for ell in textlist:
        ell = ell.lower()
        # print(ell, textlist.count(ell))
        if textlist.count(ell)>maxcount:
            # print('MORE')
            maxcount = textlist.count(ell)
            elements_list.clear()
            elements_list.add(ell)
        elif textlist.count(ell) == maxcount:
            # print('ADDED')
            elements_list.add(ell)
    return maxcount, elements_list

with open('text', 'r', encoding='utf-8') as text_file:
    first_text = text_file.read()
    print('First_text :\n',first_text)

    #                       2. Разбейте текст на предложения.
    predlojeniya = re.split('\.\s',first_text)
    # print('Splitted : \n',predlojeniya)

    #                       3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
    pat = '[а-яА-Я]{4,}'
    liss = re.findall(pat, first_text)
    maxcount, elements_list = getcounter(liss)
    print('Количество повторяющихся элементов = ',maxcount,' Элементы: ',elements_list)

    #                   4. Отберите все ссылки.
    link_pattern = re.compile('\w+\.?\w*\.\w+\/?\w*')
    links = link_pattern.findall(first_text)
    print('LINKS = ', links)
    domain_pattern = re.compile('(\w*\.?\w+\.[\w]+)')
    maxcount, elements_list = getcounter(domain_pattern.findall(first_text))
    print('Количество повторяющихся элементов = ',maxcount,' Элементы: ',elements_list)
    #                   6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
    #totaltext = re.sub(link_pattern,'«Ссылка отобразится после регистрации»',first_text)
    # print('Changed Links :\n', totaltext)