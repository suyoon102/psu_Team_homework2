from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
chromedriver = 'C:/Users/Win10Pro/PycharmProjects/chromedriver.exe' # chromedriver.exe 파일 위치에 따라
driver = webdriver.Chrome(chromedriver, options=options)
driver.get('https://www.airportal.go.kr/knowledge/statsnew/employee/license.jsp')

#print('항공종사자 자격증명 발급현황')
#print(driver.current_url)
#search_box = driver.find_elements_by_tag_name()

mySheet_table = driver.find_element_by_xpath('//*[@id="mySheet-table"]')
#print(mySheet_table)
#print(mySheet_table.text, end=" [] ")
for i in mySheet_table.text:
    print(i, end=" ")

# mySheet_table = driver.find_element_by_xpath('//*[@id="mySheet-table"]')
# mySheet_table_tr_list = mySheet_table.find_elements_by_tag_name("tr")
# for mySheet_table_tr in mySheet_table_tr_list:
#     mySheet_table_tr_td_list = mySheet_table_tr.find_elements_by_tag_name("td")
#     for mySheet_table_tr_td in mySheet_table_tr_td_list:
#         print("\t", mySheet_table_tr_td.text, end="\tl-l\t")
#     print("")

driver.close()