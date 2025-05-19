from playwright.sync_api import sync_playwright
import time 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://monkeytype.com", timeout=0, wait_until="domcontentloaded")
    
    while not page.query_selector('.rejectAll'):
        time.sleep(0.1)
    page.click('.rejectAll')
    
    tp = input("Want to Login? (y/n) : ")
    if tp=="y":
        username = input("Enter Username : ")
        password = input("Enter Password : ")

        page.goto("https://monkeytype.com/login",timeout=0,wait_until='domcontentloaded')

        page.fill('input[name="current-email"]',username)
        page.fill('input[name="current-password"]',password)
        with page.expect_navigation():
            page.click('.signIn')

        while page.url!="https://monkeytype.com/account":
            time.sleep(0.1)
            # print(page.url)

        page.goto("https://monkeytype.com", timeout=0, wait_until="domcontentloaded")
    

    tp = input("Want a Particular Speed? (y/n) : ")
    if tp == "y":
        speed = int(input("Enter the speed: "))
        wordcount = 0
        while 2*wordcount+2<speed:
            try:
                page.wait_for_selector('.word.active',timeout=1000)
                element = page.query_selector('.word.active')
                page.keyboard.type(element.inner_text()+" ")
            except:
                break
            wordcount += 1
    else:
        while True:
            try:
                page.wait_for_selector('.word.active',timeout=1000)
                element = page.query_selector('.word.active')
                page.keyboard.type(element.inner_text()+" ")
            except:
                break
    # print(element.inner_text())
    input("Press Enter to continue...")