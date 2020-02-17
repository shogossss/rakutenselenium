from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3


chrome = webdriver.Chrome(executable_path="./driver/chromedriver")
# chrome.execute_script("window.open('','_blank');")

ID = "shogo03040tennis@gmail.com"
password = "AbCdEfGhI"
# 操作するページを開く
def click(hotels,i):
    db = sqlite3.connect('instance/data.db')
    db.row_factory = sqlite3.Row
    d = db.cursor()
    hotels[i].click()
    # chrome.find_element_by_xpath("(//div[@class='hotel'])//div[contains(@class,'hotel')])[2]")
    # chrome.find_element_by_xpath("(//div[@class='hotel']").click()
    # chrome.find_element_by_class_name('hotel')[i].click()
    text1 = chrome.find_element_by_xpath("//h3/span").text
    text2 = chrome.find_element_by_xpath("//h3/span").text
    d.execute('select * from datafile')

    textfile=[]
    for d2 in d:
        textfile.append(d2["log1"])

    if(text1 in textfile):
        print("これはもうすでにやりました。")
        db.close()

    else:
        try:
            db.execute("INSERT INTO datafile (log1,log2) values(?,?)", (text1,text2))
            db.commit()
            chrome.find_element_by_class_name('imgover').click()
            try:
                search_a= chrome.find_element_by_name("u")
                search_b= chrome.find_element_by_name("p")
            except Exception as f:
                search_a= chrome.ind_element_by_xpath("//input[@type='text']")
                search_b= chrome.ind_element_by_xpath("//input[@type='password']")
            search_a.send_keys(ID)
            search_b.send_keys(password)
            search_d = chrome.find_element_by_id("l_submit").click()
            try:
                search_e = chrome.find_element_by_xpath("//input[@type='submit']").click()
            except Exception as g:
                search_e = chrome.find_element_by_xpath("//input[@value='応募する！！']").click()
            print("やったよー")
        except Exception as e:
           print (e)

    db.close()
# #
for i in range(30):
         chrome.get("https://prize.travel.rakuten.co.jp/frt/search.do?f_query=&f_large=staying_ticket&f_large=other_prize&f_large=yutaiken&f_large=discount_ticket&f_large=food_beverage&f_large=amenity_goods&f_tiku=kitakanto&f_tiku=shikoku&f_tiku=tohoku&f_tiku=kaigai&f_tiku=hokuriku&f_tiku=koshinetsu&f_tiku=tokai&f_tiku=chugoku&f_tiku=kinki&f_tiku=metropolitanarea&f_exy=null&f_sort=sin&f_next=1")
         hotels = chrome.find_elements_by_class_name("hotel")
         click(hotels,i)

# # for t in range(20):
# chrome.get("https://prize.travel.rakuten.co.jp/frt/search.do?f_query=&f_large=staying_ticket&f_large=yutaiken&f_large=discount_ticket&f_large=food_beverage&f_large=amenity_goods&f_large=other_prize&f_tiku=hokkaido&f_tiku=tohoku&f_tiku=kitakanto&f_tiku=metropolitanarea&f_tiku=koshinetsu&f_tiku=hokuriku&f_tiku=tokai&f_tiku=kinki&f_tiku=chugoku&f_tiku=shikoku&f_tiku=kyushu&f_tiku=okinawa&f_tiku=kaigai&f_exy=&f_sort=sin&f_next="+str(1))
#
#i=0
#for t in range(20):
#    for i in range(30):
#        chrome.get("https://prize.travel.rakuten.co.jp/frt/search.do?f_query=&f_large=staying_ticket&f_large=other_prize&f_large=yutaiken&f_large=discount_ticket&f_large=food_beverage&f_large=amenity_goods&f_tiku=kitakanto&f_tiku=shikoku&f_tiku=tohoku&f_tiku=kaigai&f_tiku=hokuriku&f_tiku=koshinetsu&f_tiku=tokai&f_tiku=chugoku&f_tiku=kinki&f_tiku=metropolitanarea&f_exy=null&f_sort=sin&f_next="+str(t+7))
#        # chrome.get("https://prize.travel.rakuten.co.jp/frt/search.do")
#        # chrome.find_element_by_class_name("pagingNext").click()
#        hotels = chrome.find_elements_by_class_name("hotel")
#        click(hotels,i)
