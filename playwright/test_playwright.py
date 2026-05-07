import pytest
import time
from playwright.sync_api import Page, expect, Playwright
#how to gọi broser trong playwright
#trong playwwright đã có sẵn fixture nên khác với pytesst không cần thủ công tạo nữa 
#chormium cho phép test trên trình duyệt Chrome, firefox cho phép test trên trình duyệt Firefox, webkit cho phép test trên trình duyệt Safari
#nghĩa là những cgi mà chạy được trên chromium thì sẽ auto chạy được trên chrome, những cgi mà chạy được trên firefox thì sẽ auto chạy được trên firefox, những cgi mà chạy được trên webkit thì sẽ auto chạy được trên safari
#có headless mode là chế độ chạy trình duyệt mà không hiển thị giao diện người dùng, nó thường được sử dụng trong các môi trường không có giao diện đồ họa như server hoặc trong quá trình chạy tự động hóa để tiết kiệm tài nguyên hệ thống, khi chạy ở chế độ headless thì trình duyệt sẽ hoạt động giống như bình thường nhưng không hiển thị cửa sổ trình
#new_context = tạo một phiên trình duyệt riêng biệt — giống như mở cửa sổ ẩn danh mới.
#page = context.new_page() = tạo một tab mới trong phiên trình duyệt đó.
#goto() = điều hướng tab đó đến URL bạn muốn kiểm thử.
#Playwright  =  công cụ điều khiển trình duyệt
# pytest      =  công cụ chạy và quản lý test
def test_playWrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.udemy.com/course/playwright-python-automation-testing-pytest/learn/lecture/46551437#overview")



#playwright có một fixture nữa gọi là page, nó sẽ tự động tạo một trình duyệt mới và một tab mới cho mỗi test function, nên không cần phải gọi browser, context và page nữa, chỉ cần gọi page là có thể sử dụng được luôn
#nhưng nếu muốn sử dụng những trình duyệt khác nhau thì phải gọi browser, context và page như trên, còn nếu muốn sử dụng trình duyệt mặc định thì chỉ cần gọi page là được
#trình duyệt mặc định của playwright là chromium, nên nếu muốn sử dụng trình duyệt khác thì phải gọi browser, context và page như trên, còn nếu muốn sử dụng trình duyệt mặc định thì chỉ cần gọi page là được
#chạy headless mode 
#trong những trường hợp api test, ... thì kh nên dùng 
#gọi import thì khai báo ở dưới
#sự khác nhau khi kh dùng global fixtrure của playwight là một cái sẽ cho ra đầy đủ chức năng gợi ý trong khi cái còn lại thì không có, nếu muốn sử dụng đầy đủ chức năng gợi ý thì phải gọi global fixture của playwight, còn nếu muốn sử dụng trình duyệt mặc định thì chỉ cần gọi page là được
#thêm --headed vào lệnh pytest để chạy ở chế độ headless
# @pytest.mark.test1 
#get by  text có thể dùng để tìm kiếm phần tử dựa trên văn bản hiển thị của nó, nó sẽ trả về phần tử đầu tiên mà nó tìm thấy có văn bản hiển thị giống với văn bản mà bạn đã cung cấp, nếu có nhiều phần tử có văn bản hiển thị giống nhau thì nó sẽ trả về phần tử đầu tiên mà nó tìm thấy, nếu không tìm thấy phần tử nào có văn bản hiển thị giống với văn bản mà bạn đã cung cấp thì nó sẽ trả về lỗi
def test_playWrightShortCut(page:Page):
    page.goto("https://www.udemy.com/course/playwright-python-automation-testing-pytest/learn/lecture/46551437#overview")

@pytest.mark.test2
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("radio", name = "User").check()#có thể dùng click 
    page.get_by_role("combobox").select_option(label = "Consultant")
    #select option có thể chọn value label hoặc index của option đó, nếu muốn chọn nhiều option thì có thể truyền vào một list các value label hoặc index của option đó
    #có thể cho time.sleep để xem kết quả
    time.sleep(10)
    #phải có label tag thì mới gắn label đc
    #select_option() chỉ dùng cho <select> (dropdown)
# "button" thì không có option để select
    page.locator("#terms").check() #có thể dùng click
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    expect(page.get_by_text("Old password")).to_be_visible()
#có thể dùng expect để kiểm tra kết quả
#khi viết code locator.click() thì nó sẽ tự động chờ cho đến khi phần tử đó có thể click được, nên không cần phải dùng time.sleep để chờ, nếu phần tử đó không xuất hiện trong một khoảng thời gian nhất định thì nó sẽ trả về lỗi
#5 điều kiện để playwright tự động chờ: element xuất hiện, element có thể click được, element có thể fill được, element có thể select được, element có thể check được

#Vì thông báo quá dài và có ký tự đặc biệt như " $ @ dễ gây lỗi khi gõ, nên chỉ cần lấy một phần ngắn đặc trưng là Playwright vẫn tìm được! ✅ 

#dùng thẳng page.goto thì sẽ sử dụng trình duyệt mặc định của playwright là chromium, còn nếu muốn sử dụng trình duyệt khác thì phải gọi browser, context và page như trên, còn nếu muốn sử dụng trình duyệt mặc định thì chỉ cần gọi page là được

@pytest.mark.test3 
def test_FirefoxBrowser(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("radio", name = "User").check()#có thể dùng click 
    page.get_by_role("combobox").select_option(label = "Consultant")
    #select option có thể chọn value label hoặc index của option đó, nếu muốn chọn nhiều option thì có thể truyền vào một list các value label hoặc index của option đó
    #có thể cho time.sleep để xem kết quả
    time.sleep(10)
    #phải có label tag thì mới gắn label đc
    #select_option() chỉ dùng cho <select> (dropdown)
# "button" thì không có option để select
    page.locator("#terms").check() #có thể dùng click
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    expect(page.get_by_text("Old password")).to_be_visible()


#không nên dùng index để tìm kiếm phần tử vì nó có thể thay đổi khi có sự thay đổi về giao diện người dùng, nên nên dùng các locator khác như id, class, name, ... để tìm kiếm phần tử một cách chính xác hơn và tránh bị lỗi khi có sự thay đổi về giao diện người dùng, hoặc name 

