import re
num = "8905834999"
print(re.search(r"^[6-9]\d{9}$", num))



password = "Aditya@123"
pattern = re.match(r"^[A-Za-z0-9@#$%^&+=]{8,}$", password)
print(pattern)



date = "27-03-2026"
pattern = re.match(r"^\d{2}-\d{2}-\d{4}$", date)
print(pattern)