import re

sent = 'abc|where is the world in|{"universe","galaxy","milkyway"}'
print(sent.split('|', 2))
print(sent.split('|', 2)[2])
newitems = sent.split('|',)[2]
out_string = ""
for word in newitems:
    out_string += re.sub(r'[\W]', ' ', word) + ""

print(out_string)

# items = [sent.split('|', 2)[2]]

# print(items)