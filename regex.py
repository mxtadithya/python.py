import re
num = "8905834999"
result = re.search(r"^[6-9]\d{9}$", num)
print(result.group())
print(result.start())
print(result.end())
print(result.span())


text="i love dogs"
text1="dogs are smart"
# print(f"python\bfullstack")
# print(r"python\bfullstack")
# print(re.search(r"^dog",text))
# print(re.search(r"^dog",text1).group())

print(re.match("dog",text))
print(re.match("dog",text1))


str1 = 'mishal is 23 and adhiee is 21 of ages'  #['mishal is ',' and adhiee is ',' of ages']
print(re.findall(r'\d+',str1))
print(re.search(r'\d+',str1))
print(re.split(r'\d+',str1))
print(re.sub(r'\d+','age',str1))
 
