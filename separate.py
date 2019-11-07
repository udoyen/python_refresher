import re

sentence = 'I was here | {universe, galaxy, world}'
# print(sentence.split('|', 2)[1])
collect = sentence.split('|', 2)[1]

dsrc = re.findall(r'\w+', collect)

sentb = sentence.split('|', 2)[0]
print(sentb)

for i in range(0, 3):
    print(sentb + dsrc[i])
    # print(i)