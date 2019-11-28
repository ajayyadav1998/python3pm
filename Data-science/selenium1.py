
browser = webdriver.Firefox()

browser.get("https://litemind.com/best-famous-quotes/")

ele = browser.find_elements_by_class_name("wp_quotepage_quote")

for var in ele:
    print(str(var.text))
