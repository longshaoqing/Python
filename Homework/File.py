# 读全部文件
with open("test.txt") as file_object:
    contents=file_object.read()
print(contents.rstrip())
#------------------------------------
# 按行读文件
with open("test.txt") as file_object:
    for line in file_object:
        print(line.rstrip())


#-------------------------------------
#写文件,a-追加,w-覆盖写文件
with open("test.txt","a") as file_object:
    file_object.write("\nI love programing!")