#fixtures là một tính năng của pytest giúp thiết lập và dọn dẹp môi trường kiểm thử một cách tự động. Nó cho phép bạn tạo ra các đối tượng hoặc dữ liệu cần thiết cho các bài kiểm thử của bạn, và sau đó tự động dọn dẹp chúng sau khi bài kiểm thử hoàn thành.
#dưới đây chỉ là plain function không phải là test 
#nếu muốn nó trở thành test thì phải đánh dấu tên hàm đó bằng test_ ở trước thì pytest mới nhận diện được
import pytest
#sau khi gọi fixture thì nó sẽ tự động chạy hàm đó trước khi chạy test function, nếu có nhiều fixture thì nó sẽ chạy tất cả các fixture đó trước khi chạy test function, nếu có nhiều test function thì nó sẽ chạy tất cả các test function đó sau khi chạy tất cả các fixture đó
#có thể gọi lại hàm prewrok trong nhiều test function khác nhau mà không cần phải viết lại
#phải gọi fixture thì không inject được prework
#Không có fixture → pytest coi là tham số
#Có fixture → pytest coi là “đồ cần chuẩn bị và tự cung cấp”
#fixtrue inject kết quả không phải code
#pytest inject kết quả (return value) của fixture vào test
#🧠 ví dụ đời thực
# Fixture = đi pha cà phê ☕
# Test = uống cà phê
# fixture không “đưa cả quán cà phê vào”
# nó chỉ đưa ly cà phê đã pha xong
#scope của fixture: function, class, module, package, session
#function: fixture sẽ được tạo ra và dọn dẹp sau mỗi test function
#class: fixture sẽ được tạo ra và dọn dẹp sau mỗi test class
#module: fixture sẽ được tạo ra và dọn dẹp sau mỗi test module
#package: fixture sẽ được tạo ra và dọn dẹp sau mỗi test package
#session: fixture sẽ được tạo ra và dọn dẹp sau mỗi test session
#mặc định scope của fixture là function
#class với module khá dống nhau
#lệnh pytesst đọc tất cả file tring cùng 1 thư mục 
#assert là câu kiểm tra điều kiện đúng sai nếu điều kiện đúng thì test sẽ pass, nếu điều kiện sai thì test sẽ fail
#Cả cuộc trò chuyện xoay quanh pytest fixtures và các khái niệm liên quan:
# yield trong Python

# Khác return ở chỗ hàm có thể tạm dừng và chạy tiếp, thay vì kết thúc ngay
# Tiết kiệm RAM vì sinh giá trị từng cái một thay vì load hết cùng lúc

# yield trong pytest fixture

# Phần trước yield = setup (chuẩn bị)
# Phần sau yield = teardown (dọn dẹp)
# Dùng return thì không có teardown

# Teardown

# Dọn sạch tài nguyên sau khi test xong
# Mục đích chính là tránh leak — tức là tài nguyên bị chiếm mà không trả lại
# Không có teardown → browser/connection chồng chất → RAM cạn dần

# Scope

# Cái thực sự ảnh hưởng hiệu năng
# scope="function" → setup/teardown mỗi test
# scope="module" → chỉ chạy 1 lần cho cả file
# Scope càng rộng → càng tiết kiệm tài nguyên
# Sonnet 4.6
#muốn test từng cái một thì thêm :: vào sau tên file và tên test function
@pytest.fixture(scope="module")
def preWork():
    print("i set up browser instance")
    yield "pass"
    print("i tear down browser instance")

@pytest.fixture(scope="function")
def secondWork():
    print("i set up browser inkkkkstance")
    yield "pass"
    print("i tear down browser instance")
#smoke test là một loại test được sử dụng để kiểm tra xem các chức năng cơ bản của phần mềm có hoạt động đúng hay không. Nó thường được thực hiện sau khi phần mềm đã được xây dựng và trước khi thực hiện các bài kiểm thử chi tiết hơ
# n. Mục đích của smoke test là để đảm bảo rằng phần mềm không bị lỗi nghiêm trọng và có thể chạy được trước khi tiếp tục với các bài kiểm thử khác.
#có thể gắn mác smoke cho test function nào đó để đánh dấu test function đó là smoke test, khi chạy pytest thì chỉ những test function được đánh dấu là smoke test mới được chạy, còn những test function không được đánh dấu sẽ bị bỏ qua
@pytest.mark.smoke
def test_initialCheck(preWork, secondWork): 
    print("this is a test function")
    assert preWork == "pass"
    assert secondWork == "pass"
#nếu muốn bỏ qua test function nào đó thì có thể sử dụng pytest.mark.skip() để đánh dấu test function đó là skip,
#  khi chạy pytest thì test function đó sẽ bị bỏ qua và không được chạy

@pytest.mark.skip()
def test_secondCheck(preWork, secondWork):
    print("this is another test function")
    assert preWork == "pass"
    assert secondWork == "pass"


