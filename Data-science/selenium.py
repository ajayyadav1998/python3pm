browser = webdriver.Firefox()

browser.get('https://www.quora.com/topic/Fashion-and-Style-Advice/all_questions')

elem = browser.find_element_by_tag_name('body')

no_of_pagedown = 15

while no_of_pagedown:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    no_of_pagedown -= 1
    
post_ele = browser.find_elements_by_class_name('ui_qtext_rendered_qtext')

for post in post_ele:
    print(str(post.text))
