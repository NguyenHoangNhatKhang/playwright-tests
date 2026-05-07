#conftest là một file đặc biệt trong pytest, nó được sử dụng để định nghĩa các fixtures và các thiết lập chung cho tất cả các bài kiểm thử trong một thư mục hoặc một dự án. Khi bạn đặt một fixture trong conftest.py, nó sẽ tự động được chia sẻ và có thể sử dụng trong tất cả các bài kiểm thử mà không cần phải import hay định nghĩa lại fixture đó trong từng file test riêng biệt.
#thứ tự local fixture > conftest fixture > builtin fixture
#nếu có nhiều fixture cùng tên thì pytest sẽ ưu tiên sử dụng fixture được định nghĩa
import pytest
def test_thirdCheck(preSetupWork):
    print("this is a test function")

def test_fourthCheck(preSetupWork):
    print("this is another test function")