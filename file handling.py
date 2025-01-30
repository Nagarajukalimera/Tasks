mode --- 'r' ---> read operations 
file = open("demo.txt", mode='r')
read_data = file.read()
print(read_data)
file.close()


file = open("demo.txt", mode='r')
read_data = file.readline()
print(read_data)
file.close()


file = open("demo.txt", mode='r')
read_data = file.readlines()
print(read_data)
file.close()


read ---> total data read
realine ---> single line read(first line)
readlines --> total data in list format (list of substring)


mode = 'a'--> append operations
file = open("demo.txt",mode = 'a')
write_data = file.write("\n this is write operation using mode ='r' ")
file.close()

file = open("demo123.txt",mode = 'a')
write_data = file.write("\n this is write operation using mode ='r' ")
file.close()



mode = 'w' ---> write operations 
file = open("demo.txt", mode='w')
write_data = file.write("using w mode to perform write operations")
file.close()

file = open("nanadana.txt", mode = 'w')
write_data = file.write("some data")
file.close()


mode = 'w+'
file = open("python.txt", mode = 'w+')
write_data = file.write("sample data")
file.seek(5)
print(file.tell())
read_data = file.read()
print(read_data)
file.close()


list_1 = ["vasu\n","bharat\n","suresh\n","seshu"]
file = open("seshu.txt",mode='a' )
write_data = file.writelines(list_1)
file.close()


file= open("C:\\Users\\tarak\\Desktop\\python123456.txt",mode='w')
# read_data = file.read()
# print(read_data)
file.close()