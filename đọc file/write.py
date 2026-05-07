#with có nghĩa là vửa mở file vừa làm việc với file đó, khi làm xong thì nó sẽ tự động đóng file đó lại, còn nếu không dùng with thì phải tự đóng file đó lại bằng cách gọi phương thức close() của file đó, nếu không

#có thể nói với file là t muốn viết hay đọc read mode thi cho nó tag r write mode thì w
#đề bài 
#read the file and store all the lines in list
#reverse the list
#write the list to a new file
# #abbb
# b 
# c
# d
#bước 1 đọc file 
with open("text.txt", "r") as reader:
     contents = reader.readlines()
     #bước 2 đảo ngược list
     #hoặc có rthể dùng reversed(lines)
     contents = contents[::-1]
     with open("text.txt","w") as writer:
          for line in contents: 
               writer.write(line)
    



          


