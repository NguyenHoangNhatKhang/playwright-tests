# #đọc file trong python
# #khi mở file chắc chắn phải đóng file
# #mục đích việc mở file là để đọc hoặc ghi dữu liệu


# file = open("text.txt")
# # print(file.read(100)) #đọc toàn bộ nội dung của file, nó sẽ trả về một chuỗi chứa toàn bộ nội dung của file đó
# #nhưng phải in ra kết quả của file.read() thì mới thấy được nội dung của file đó, nếu không sẽ không thấy được gì cả

# #nếu cho số vào trong file.read() thì nó sẽ đọc số lượng ký tự đó từ file, nếu không có số thì nó sẽ đọc toàn bộ nội dung của file
# #một kí tự nữa là dấu /n là kí tự xuống dòng, nó sẽ được tính là một ký tự khi đọc file, nếu có nhiều dòng thì nó sẽ được tính là nhiều ký tự, nếu có nhiều khoảng trắng thì nó cũng sẽ được tính là nhiều ký tự
# #cách khác để mở file là sử dụng with, nó sẽ tự động đóng file sau khi sử dụng xong
# # print(file.readline()) #đọc một dòng của file, nó sẽ trả về một chuỗi chứa nội dung của dòng đó, nếu có nhiều dòng thì nó sẽ trả về nhiều chuỗi, nếu không có dòng nào thì nó sẽ trả về một chuỗi rỗng
# print(file.readlines()) #đọc tất cả các dòng của file, nó sẽ trả về một list chứa các chuỗi, mỗi chuỗi là nội dung của một dòng trong file, nếu không có dòng nào thì nó sẽ trả về một list rỗng
# file.close() #đóng file sau khi sử dụng xong
# #nếu dùng read trước cho số vào thì ở những readline sau nó sẽ bắt đầu đọc từ vị trí tiếp theo của file, nếu dùng readlines trước thì ở những readline sau nó sẽ bắt đầu đọc từ vị trí tiếp theo của file, nếu dùng readline trước thì ở những readline sau nó sẽ bắt đầu đọc từ vị trí tiếp theo của file
file = open("text.txt")
# line = file.readline()
# while line != "": 
#     print(line)
#     line = file.readline()
#còn một cách khác để print từng content
#readlines liệt kê toàn bộ nhưng trả về list
for line in file.readlines():
    print(line)

file.close() 