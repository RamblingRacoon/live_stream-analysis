# from requests_html import HTMLSession

# def scrap_page(url):
#     session = HTMLSession()
#     r = session.get(url)
#     r.html.render( scrolldown=10000)
#     posts = r.html.find("#chat .post", clean=True)
#     print(len(posts))



url = "https://www.nytimes.com/interactive/2021/01/20/us/politics/live-stream-inauguration.html"

# scrap_page(url)

def post_parser(selenium_post):
    entity = {}
    print(selenium_post.get_attribute("id"))
    # entity["time"]= selenium_post.find_element_by_tag_name('time')
    # print(entity["time"])
    return entity

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True

driver = Firefox(options=options)
driver.set_window_position(0, 0)
driver.set_window_size(2000, 800)
# driver.set_window_size(1024, 500)

driver.get(url)

ids = driver.find_elements_by_xpath('//*[@id]')
# print(ids)
# print(len(content))

ids = driver.find_elements_by_xpath('//*[@id]')
for asfasfs in ids:
    print(asfasfs.get_attribute('id'))    # id name as string
# for post in content:
#     post_data = post_parser(post)