# Дана строка, состоящая из слов, разделенных пробелами. Сформировать новую строку со следующими свойствами: 
# а) все слова в нижнем регистре, кроме первой буквы первого слова; 
# б) все ссылки в словах заменяются на "[ссылка запрещена]";
# в) все email заменяются на "[контакты запрещены]"; 
# г) все слова длины более 3 символов, содержащие только цифры, удаляются.
# показал

import re
text = "1saysomem@rambler.ru 88 helLLo worlD привет 55555 http://url.com/bla1/blah1/ КАК дела http://ныа  123454 google.com сайт"
#б,в
text = re.sub(r'http\S+', '[ссылка запрещена]', text)
text = re.sub(r'https\S+', '[ссылка запрещена]', text)
text = re.sub(r'\S+.com', '[ccылка запрещена]', text)
text = re.sub(r'\S+.ru', '[ccылка запрещена]', text)
text = re.sub(r'\S+@\S+', '[контакты запрещены]', text)

text = text.lower()
text = text.split()
#a
for i in range(len(text)):
    if text[i][0] != '[' and text[i][len(text[i]) - 1] != ']' and not text[i].isdigit():
        text[i] = text[i].capitalize()
        break

#г
for i in text:
    if i.isdigit() and len(i) > 3:
        text.remove(i)

text = ' '.join(text)
print(text)
