file=open("examplehandiling.txt","w")
file.write("Hello adithya!\n")
file.write("good morning")
# # content = file.read()
# # print(content)
# file.close()

#using with

#write..............
with open("handiling.txt","w")as file:
    file.write("halooo\n")
#append.............
with open("handiling.txt","a")as file:
    file.write("halooo guys")
#read..........    
with open("handiling.txt","r")as file:
        print(file.read())