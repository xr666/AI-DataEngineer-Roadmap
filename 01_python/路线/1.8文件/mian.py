# file = open("c:\\Users\\26243\\Desktop\\AI_DataEngineer\\AI-DataEngineer-Roadmap\\01_python\\路线\\1.8文件\\test.txt")
# content = file.read()
# print(content)
 
with open("c:\\Users\\26243\\Desktop\\AI_DataEngineer\\AI-DataEngineer-Roadmap\\01_python\\路线\\1.8文件\\test.txt") as file:
    content = file.read()
print(content)


with open("c:\\Users\\26243\\Desktop\\AI_DataEngineer\\AI-DataEngineer-Roadmap\\01_python\\路线\\1.8文件\\test.txt") as file:
    content = file.readline()
print(content)

with open("c:\\Users\\26243\\Desktop\\AI_DataEngineer\\AI-DataEngineer-Roadmap\\01_python\\路线\\1.8文件\\test.txt") as file:
    content = file.readlines()
print(content)