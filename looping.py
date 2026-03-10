##############for loop
#for i in range(1,101):
       # print(i)

#word="adithya"
#for letter in word:
       # print(word)
    #   print(letter)
##############while loop
#i=1
# while i<=10:
   # print(i)
  #  i=i+1

#############nested loop
#for i in range(2):
  #  for j in range(3):
   #     print("*",end="")
   # print()

###########break and contine
# for i in range(100):
    # if(i==50):
      #  continue
   # print(i)


#for i in range(100):
   # if(i==50):
    #    break
   # print(i)

#####################string method

#name ="python programming"
#print(name.upper())

#print(name.lower())

#value="adithya"
#print(value.capitalize())

#demo="  adithya ajayan  "

#print(demo.title())

#print(demo.strip())

#print(demo.lstrip())

#print(demo.rstrip())


#print(demo.replace("adithya","ajayan"))

#print(demo.split())

#words=["synnefo","solutions"]
#sentence = "|".join(words)
#print(sentence)

#text= "python programming "

#print(text.find("pro"))

######task
#text = "banana"
#print(text.count("a"))

#text = "Python programming"
#print(text.startswith("Python"))

#text = "report.pdf"
#print(text.endswith(".pdf"))

#text = "Python"
#print(text.isalpha())

#text = "Python123"
#print(text.isalpha())

#num = "12345"
#print(num.isdigit())


text ="python"
for char in text:
    print(char)


text ="hello"
count = 0
for char in text:
    count += 1
print(count)


text ="education"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)


text ="python"
for char in text:
    print(char.upper())


text ="python"
reverse = ""
for i in range(len(text) - 1, -1, -1):
    reverse += text[i]
print(reverse)