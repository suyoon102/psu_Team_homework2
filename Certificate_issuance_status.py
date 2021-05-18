from selenium import webdriver
import matplotlib.pyplot as plt
import matplotlib

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver',options=options)
driver.get('https://www.airportal.go.kr/knowledge/statsnew/employee/license.jsp')

mySheet_table = driver.find_element_by_xpath('//*[@id="mySheet-table"]/tbody/tr[2]/td/div/div[1]/table/tbody')

cyc = 0
lists = []
for i in mySheet_table.find_elements_by_css_selector('tr'):
    count = 0
    cyc += 1
    list = []
    for m in i.find_elements_by_css_selector('td'):
        count += 1

        if count == 1:
            continue

        print(m.text,end=' ')
        list.append(m.text)

        if count == 5:
            break

    print('')
    lists.append(list)

    if cyc == 14:
        break

del lists[0]
driver.close()

year_list = []
list1 = []
list2 = []
list3 = []

for i in lists:
    year_list.append(int(i[0]))
    i[1] = i[1].replace(',','')
    i[2] = i[2].replace(',', '')
    i[3] = i[3].replace(',', '')
    list1.append(int(i[1]))
    list2.append(int(i[2]))
    list3.append(int(i[3]))

print('')
print(year_list)
print(list1)
print(list2)
print(list3)

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')

plt.plot(range(1,14),list1,color='lightskyblue',linewidth=2.5,label='운송용')
plt.plot(range(1,14),list2,color='lightpink',linewidth=2.5,label='사업용')
plt.plot(range(1,14),list3,color='lightgreen',linewidth=2.5,label='자가용')
plt.suptitle('항공종사자 자격증명 발급현황')
plt.xticks(range(1,14),year_list,fontsize=9)
plt.xlabel('년도',fontsize=9)
plt.ylabel('(단위:명)',fontsize=9)
plt.legend()
plt.show()