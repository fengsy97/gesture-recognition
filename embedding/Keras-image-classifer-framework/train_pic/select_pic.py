import random
import os

filePath = "./scissors"

os.system("mkdir "+filePath+"-train")
os.system("mkdir "+filePath+"-test")


names =os.listdir(filePath)
# print(names)
for name in names:
    # print(name)
    # break
    rand = random.randint(0,9)
    # print("mv "+filePath+"/"+name+" "+filePath+"-train")
    if rand > 6:
        # print("mv "+filePath+"/"+name+" "+filePath+"-train")
        os.system("mv "+filePath+"/"+name+" "+filePath+"-test")
    else:
        os.system("mv "+filePath+"/"+name+" "+filePath+"-train")
