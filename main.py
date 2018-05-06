import codecs
import re
f = codecs.open('türkçe.txt', encoding='utf-8')
dic = f.read()

s = r'\r\n[^sztdnmrlçşjkfvpb]*'
number = '1123'

for i in number:
    if i == '1':
        s = s + r'[td]'
    elif i == '2':
        s = s + r'n'
    elif i == '3':
        s = s + r'm'
    s = s + r'[^sztdnmrlçşjkfvpb]*'

s = s + r'\r\n'

phoneNumRegex = re.compile(s)
mo = phoneNumRegex.findall(dic)

for i in mo:
    print(i.replace('\r\n',''))
