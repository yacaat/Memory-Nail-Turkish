import random
import pyperclip


suits = ['Kupa', 'Maça', 'Karo', 'Sinek']
deck = []
memory_hanger = ['Bahçe Giriş', 'Apartman ön bahçe', 'Büro kapı', 'Büro tahta tabure', 'Büro anne misafir', 'Büro anne koltuk', 'Apartman otopark yeri', 'Büro benim masa', 'Büro benim toplantı', 'Büro sekreter hulya masa', 'Büro kırmızı dolap', 'Büro mutfak', 'Büro tuvalet', 'Büro mimar hulya masa', 'Büro baba masa', 'Büro misafir masa', 'Apartman dış koridor', 'Apartman arka bahçe', 'Apartman dış kapı', 'Apartman kapı-merdiven Gülseren', 'Gülseren mutfak', 'Gülseren balkon', 'Gülseren salon ', 'Gülseren oturma', 'Gülseren yemek', 'Gülseren kiler', 'Gülseren büyük yatak odası', 'Gülseren Ertürk yatak odası', 'Gülseren tuvalet', 'Gülseren Küçük yatak odası', 'Apartman kapı-merdiven bizim ev', 'Bizim ev antre', 'Bizim ev benim oda', 'Bizim ev benim tuvalet', 'Bizim ev mutfak', 'Bizim ev okey', 'Bizim ev salon', 'Bizim ev kitap', 'Bizim ev televizyon', 'Bizim ev aşağı tuvalet', 'Bizim ev duru oda', 'Bizim ev merdiven', 'Bizim ev anıl yatak odası', 'Bizim ev ara', 'Bizim ev anne-baba tuvalet', 'Bizim ev anne-baba yatak odası', 'Bizim ev ara teras', 'Bizim ev teras', '', '' , '']
print(len(memory_hanger))
for suit in suits:
    for i in range(2, 11):
        deck.append(suit + ' ' + str(i))
    face = ['J', 'Q', 'K', 'A']
    for rank in face:
        deck.append(suit + ' ' + rank)

for i in range(1,52):
    print(str(i) + ' / ' + memory_hanger[i] + ' / ' + deck.pop(random.randint(0, len(deck)-1)))
    input('', )
    #print(random.randint(0,3))