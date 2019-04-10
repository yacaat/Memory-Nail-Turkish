import sys
import codecs
import re

try:
    f = codecs.open('türkçe.txt', encoding='utf-8')
    dic = f.read()

    s = r'\r\n[^sztdnmrlçşjkfvpb]*'
    number = sys.argv[1]

    for i in number:
        if i == '1':
            s = s + r'[td]'
        elif i == '2':
            s = s + r'n'
        elif i == '3':
            s = s + r'm'
        elif i == '4':
            s = s + r'r'
        elif i == '5':
            s = s + r'l'
        elif i == '6':
            s = s + r'[çjş]'
        elif i == '7':
            s = s + r'k'
        elif i == '8':
            s = s + r'[fv]'
        elif i == '9':
            s = s + r'bp'
        s = s + r'[^sztdnmrlçşjkfvpb]*'

    s = s + r'\r\n'

    phoneNumRegex = re.compile(s)
    mo = phoneNumRegex.findall(dic)

    for i in mo:
        print(i.replace('\r\n',''))

    print("By Grok")

except:
    print("Parametre olarak direkt sayı girilmelidir.")