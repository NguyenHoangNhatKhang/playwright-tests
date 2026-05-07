#oop princible 
#methods, class vảiable, instance vảiables , constructor, self, inheritance, polymorphism, encapsulation, abstraction
#method là ý chỉ mấy cái function trong class, còn class variable là biến dùng chung cho tất cả instance của class đó, còn instance variable là biến riêng biệt cho mỗi instance của class đó
#attributes là variable trong class, còn method là function trong class
#constructor là hàm đặc biệt được gọi khi tạo object của class, nó thường được dùng để khởi tạo giá trị cho instance variable, còn self là tham số đầu tiên của tất cả method trong class, nó đại diện cho instance hiện tại của class đó
#nếu không có constructor thì nó sẽ gọi default constructor, còn nếu có constructor thì nó sẽ gọi constructor đó, nếu có nhiều constructor thì nó sẽ gọi constructor phù hợp với số lượng và kiểu dữ liệu của tham số được truyền vào khi tạo object
#class vảiable và instance vảiable khác nhau ở chỗ class variable được chia sẻ giữa tất cả instance của class đó, còn instance variable là biến riêng biệt cho mỗi instance của class đó, khi thay đổi giá trị của class variable thì tất cả instance của class đó sẽ bị ảnh hưởng, còn khi thay đổi giá trị của instance variable thì chỉ có instance đó bị ảnh hưởng
#variables được tạo trong constructor được gọi là instance variable, còn variables được tạo trong class nhưng ngoài constructor được gọi là class variable, còn variables được tạo trong method được gọi là local variable
#class variable là constant không thay đổi
#parameter là biến được truyền vào method
#self nghĩa là object hiện tài của class đó, nó được sử dụng để truy cập các thuộc tính và phương thức của class đó, khi gọi phương thức của class thì phải truyền self vào làm tham số đầu tiên, nếu không sẽ bị lỗi
#🔴 num1, num2 chỉ tồn tại trong __init__
# def __init__(self, num1, num2):

# 👉 num1, num2 ở đây là:
# biến local
# chỉ sống trong hàm __init__
# 🔵 Bên phải: num1

# 👉 là tham số (parameter) của hàm __init__

# def __init__(self, num1, num2):

# → giá trị được truyền vào khi tạo object
# 👉 ra khỏi hàm là biến mất
#“Lưu cái giá trị num1 vào trong object, đặt tên là num1”
#trong python lúc nào cũng phải có self để lưu giá trị vào trong object, nếu không sẽ bị lỗi, còn trong các ngôn ngữ khác thì không cần phải có self, nó sẽ tự động lưu giá trị vào trong object khi gọi phương thức của class đó
class Calculator: 
    num = 100 #class variable
    #default constructor
    #khi tạo constructor thì sẽ gọi tên của class luôn ở các ngôn ngữ khác nên python cũng vây 
    def __init__(self,num1,num2): #constructor
        self.firstnumber = num1 #instance variable, self là tham số đầu tiên của tất cả method trong class, nó đại diện cho instance hiện tại của class đó, khi gọi phương thức của class thì phải truyền self vào làm tham số đầu tiên, nếu không sẽ bị lỗi
        self.secondnumber = num2 
        print("constructor called automatically when object is called") #constructor body
    def getData(self): 
        print("iam a calculator") #method

    def Summation(self):
        return self.firstnumber + self.secondnumber #method
# obj = Calculator(3,4)
# sum = obj.Summation()
# print(sum)
# print(obj.num) #accessing class variable through instance
# print(Calculator.num) #accessing class variable through class name

# obj1 = Calculator(4,6)
# print(obj.num) #accessing class variable through instance
# print(Calculator.num) #accessing class variable through class name

#trong trường hợp gắn parameter vào constructor thì khi tạo object thì phải truyền giá trị cho parameter đó, nếu không sẽ bị lỗi