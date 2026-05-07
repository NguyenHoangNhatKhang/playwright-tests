str = "kelvin.com"
print(str[1])
#0 to n minus 1
#-1 là phần tử cuối cùng, -2 là phần tử thứ 2 từ cuối, -3 là phần tử thứ 3 từ cuối, ...
print(str[0:6])
print(str[0:]) #từ 0 đến hết
print(str[:6]) #từ đầu đến 6
print(str[:]) #từ đầu đến hết
print(str[-1]) #lấy phần tử cuối cùng
print(str[-3:]) #lấy 3 phần tử cuối cùng
print(str[:-3]) #lấy phần tử từ đầu đến phần tử thứ 3 từ cuối
print(str[-6:-3]) #lấy phần tử từ phần tử thứ 6 từ cuối đến phần tử thứ 3 từ cuối
print(str[::2]) #lấy phần tử từ đầu đến hết với bước nhảy là 2
print(str[1::2]) #lấy phần tử từ phần tử thứ 1 đến hết với bước nhảy là 2
print(str[::-1]) #lấy phần tử từ cuối đến đầu với bước nhảy là 1, tức là đảo ngược chuỗi
print(str[-1::-1]) #lấy phần tử từ cuối đến đầu với bước nhảy là 1, tức là đảo ngược chuỗi
print(str[-1:0:-1]) #lấy phần tử từ cuối đến phần tử thứ 1 với bước nhảy là 1, tức là đảo ngược chuỗi nhưng không lấy phần tử đầu tiên 
#in là toán tử để kiểm tra xem một chuỗi có tồn tại trong chuỗi khác hay không, nó trả về True nếu tồn tại và False nếu không tồn tại
print("kelvin" in str) #True
print("com" in str) #True
print("kelvin.com" in str) #True
print("kelvin.net" in str) #False 
#cách split strin
str2 = "hello world"
print(str2.split()) #mặc định là split theo khoảng trắng, nó sẽ trả về một list chứa các phần tử được split ra
str3 = "hel.lso,world,python"
print(str3.split(",")) #split theo dấu phẩy, nó sẽ trả về một list chứa các phần tử được split ra
str4 = "hello world python"
print(str4.split("o")) #split theo chữ o, nó sẽ trả về một list chứa các phần tử được split ra
print(str3.split(".")) #split theo dấu chấm, nó sẽ trả về một list chứa các phần tử được split ra, nếu không có dấu chấm thì nó sẽ trả về một list chứa toàn bộ chuỗi đó
var = str3.split(".")
print(var[0]) #lấy phần tử đầu tiên của list var 
#strip là một phương thức của chuỗi trong Python được sử dụng để loại bỏ các ký tự trắng (space) ở đầu và cuối của chuỗi. Nếu không truyền vào tham số nào thì nó sẽ loại bỏ tất cả các ký tự trắng, nếu truyền vào một chuỗi thì nó sẽ loại bỏ tất cả các ký tự trong chuỗi đó ở đầu và cuối của chuỗi gốc. Ví dụ:
str5 = "   hello world   "
print(str5.strip()) #loại bỏ tất cả các ký tự trắng ở đầu và cuối của chuỗi str5, kết quả là "hello world"
str6 = "xxxhelloxxx"
print(str6.strip("x")) #loại bỏ tất cả các ký tự "x" ở đầu và cuối của chuỗi str6, kết quả là "hello"
str7 = "   hello world   "
print(str7.strip(" ")) #loại bỏ tất cả các ký tự trắng ở đầu và cuối của chuỗi str7, kết quả là "hello world"