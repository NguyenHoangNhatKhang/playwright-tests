from playwright.sync_api import Page, expect, Playwright
import time
import pytest
@pytest.mark.test4
def test_UIvalidation1(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("radio", name="Admin").check()
    page.get_by_role("combobox").select_option(label="Teacher")
    page.locator("#terms").check()
    # page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
    #iphone X Nokia Edge Samsung Note 8 Blackberry -> verifying 4 products in the cart 
    #page.locator("app-card")  this will end up finding 4 cards
    #nên bởi vậy có tính năng filter 
    iphoneProducts = page.locator("app-card").filter(has_text="iphone X")
    iphoneProducts.get_by_role("button", name="Add").click()
    nokiaProducts = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProducts.get_by_role("button", name="Add").click()
    samsungProducts = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsungProducts.get_by_role("button", name="Add").click()
    blackberryProducts = page.locator("app-card").filter(has_text="Blackberry")
    blackberryProducts.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()
    #to have count giúp kiểm tra số lượng phần tử mà locator đó tìm thấy, nếu số lượng phần tử mà locator đó tìm thấy bằng với số lượng mà bạn mong đợi thì test sẽ pass, còn nếu số lượng phần tử mà locator đó tìm thấy khác với số lượng mà bạn mong đợi thì test sẽ fail
    expect(page.locator(".media")).to_have_count(4) 
    #Selector Hub là một extension trên trình duyệt giúp bạn tìm selector của element nhanh chóng mà không cần tự viết tay.

@pytest.mark.test4
def test_ChildWindow(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    expect(page.locator(".blinkingText")).to_have_count(2)
    with page.expect_popup() as newPage_info: 
        #cái with sẽ tự động chờ cho đến khi có một popup mới được mở ra, nếu không có popup mới được mở ra trong một khoảng thời gian nhất định thì nó sẽ trả về lỗi
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
    new_Page1 = newPage_info.value
    expect(new_Page1).to_have_url("https://rahulshettyacademy.com/documents-request")
    new_Page1_text = new_Page1.locator(".red").text_content()
    print(new_Page1_text)
        #Please email us at mentor@rahulshettyacademy.com with below template to receive response
    words = new_Page1_text.split("at") #lease email us , mentor@rahulshettyacademy.com with below template to receive response
    email = words[1].strip().split(" ")[0]
    assert email == "mentor@rahulshettyacademy.com"


        # expect(new_Page1_text).to_contain("Free Access to InterviewQues/ResumeAssistance/Material")
        #có thể dùng text_content() để lấy nội dung văn bản của phần tử đó
        #có thể dùng expect để kiểm tra kết quả
    # Click vào link "Free Access..."
# ⚠️ Link này mở TAB MỚI, nên phải switch qua tab mới để kiểm tra URL
# Cách switch qua tab mới:

# @pytest.mark.test4
# def test_ChildWindow2(playwright:Playwright):
#     browser = playwright.firefox.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     expect(page.locator(".blinkingText")).to_have_count(2)
#     page.locator(".blinkingText").filter(has_text="Get Shortlisted by Recruiters - Take QA Skill Assessments on TechSmartHire").click(force=True)
#     expect(page).to_have_url("https://techsmarthire.com/")

@pytest.mark.test4
def test_UIvalidation2(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("radio", name="Admin").check()
    page.get_by_role("combobox").select_option(label="Teacher")
    page.locator("#terms").check()
    # page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")
    #iphone X Nokia Edge Samsung Note 8 Blackberry -> verifying 4 products in the cart 
    #page.locator("app-card")  this will end up finding 4 cards
    #nên bởi vậy có tính năng filter 
    iphoneProducts = page.locator("app-card").filter(has_text="iphone X")
    iphoneProducts.get_by_role("button", name="Add").click()
    nokiaProducts = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProducts.get_by_role("button", name="Add").click()
    samsungProducts = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsungProducts.get_by_role("button", name="Add").click()
    blackberryProducts = page.locator("app-card").filter(has_text="Blackberry")
    blackberryProducts.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()
    #to have count giúp kiểm tra số lượng phần tử mà locator đó tìm thấy, nếu số lượng phần tử mà locator đó tìm thấy bằng với số lượng mà bạn mong đợi thì test sẽ pass, còn nếu số lượng phần tử mà locator đó tìm thấy khác với số lượng mà bạn mong đợi thì test sẽ fail
    expect(page.locator(".media")).to_have_count(4) 

@pytest.mark.test4 
def test_ChildWindow2(playwright:Playwright):
    browser = playwright.firefox.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    expect(page).to_have_url("https://rahulshettyacademy.com/loginpagePractise/")
    with context.expect_page() as newPage_info2: 
        page.locator(".blinkingText").filter(has_text="Get Shortlisted by Recruiters - Take QA Skill Assessments on TechSmartHire").click(force=True)
    new_Page2 = newPage_info2.value 
    expect(new_Page2).to_have_url("https://techsmarthire.com/")


    
