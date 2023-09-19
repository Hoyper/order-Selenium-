from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def button_click_next():
    driver.find_element(By.ID, 'divNext').click()

def find_by_xpath(xpath):
    driver.find_element(By.XPATH, xpath).click()

def find_by_xpath_send_keys(xpath, value):
    driver.find_element(By.XPATH, xpath).send_keys(value)


mails = open(r'C:\Users\Username\Desktop\mails\mails.txt', 'r') #!!!указать свой путь до .txt файла с почтами
counter = 0
for mail in mails:
    url = 'https://survey.kurogame.com/vm/wkPNv2f.aspx'
    option = webdriver.ChromeOptions()
    #работать скрытно(раскомментировать по необходимости)
    #option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    driver.get(url=url)
    mail_input = driver.find_element(By.ID, 'q1')
    mail_input.send_keys(mail)
    button_click_next()
    # 2 страница
    find_by_xpath('//a[@class="jqcheck"]')
    find_by_xpath('//a[@class="jqcheck"]')
    button_click_next()
    # 3 страница
    find_by_xpath_send_keys("//input[@rowid='1']", '60')
    button_click_next()
    # 4 страница
    find_by_xpath("//div[@for='q4_3']")
    button_click_next()
    # 5страница
    find_by_xpath("//div[@for='q5_8']")
    button_click_next()
    # 6 страница
    find_by_xpath("//div[@for='q6_1']")
    find_by_xpath("//div[@for='q6_13']")
    find_by_xpath("//div[@for='q6_2']")
    button_click_next()
    # 7 страница
    find_by_xpath("//div[@for='q7_8']")
    find_by_xpath("//div[@for='q7_2']")
    find_by_xpath("//div[@for='q7_1']")
    button_click_next()
    # 8 страница
    find_by_xpath("//div[@for='q9_11']")
    find_by_xpath("//div[@for='q9_1']")
    find_by_xpath("//div[@for='q9_12']")
    find_by_xpath("//div[@for='q9_8']")
    button_click_next()
    # 9 страница
    for i in range(1, 18):
        try:
            driver.find_element(By.XPATH, f"//tr[@id='drv10_{i}']/td[7]/a").click()
        except:
            continue
    button_click_next()
    # 10 страница
    find_by_xpath("//div[@for='q20_5']")
    button_click_next()
    # 11 страница
    find_by_xpath("//div[@for='q21_5']")
    button_click_next()
    # 12 страница
    find_by_xpath("//div[@for='q22_9']")
    button_click_next()
    # 13 страница
    for i in range(23, 35):
        try:
            find_by_xpath(f"//div[@for='q{i}_5']")
        except:
            continue
    button_click_next()
    # 14 страница
    for i in range(23, 35):
        try:
            find_by_xpath(f"//div[@for='q{i}_5']")
        except:
            continue
    button_click_next()
    # 15 страница
    for i in range(23, 35):
        try:
            driver.find_element(By.XPATH, f"//div[@for='q{i}_9']").click()
        except:
            continue
    button_click_next()
    # 16 страница
    for i in range(23, 35):
        try:
            driver.find_element(By.XPATH, f"//div[@for='q{i}_5']").click()
        except:
            continue
    button_click_next()
    # 17 страница
    for i in range(23, 35):
        try:
            driver.find_element(By.XPATH, f"//div[@for='q{i}_5']").click()
        except:
            continue
    button_click_next()
    # 18 страница
    for i in range(23, 35):
        try:
            driver.find_element(By.XPATH, f"//div[@for='q{i}_9']").click()
        except:
            continue
    button_click_next()
    # 19 страница
    find_by_xpath("//div[@for='q35_7']")
    find_by_xpath("//div[@for='q35_12']")
    find_by_xpath("//div[@for='q35_25']")
    button_click_next()
    # 20 страница
    find_by_xpath("//tr[@id='drv36_7']/td[6]/a")
    find_by_xpath("//tr[@id='drv36_12']/td[6]/a")
    find_by_xpath("//tr[@id='drv36_25']/td[6]/a")
    button_click_next()
    # 21 страница
    find_by_xpath("//div[@for='q37_4']")
    find_by_xpath("//div[@for='q37_20']")
    find_by_xpath("//div[@for='q37_16']")
    button_click_next()
    # 22 страница
    find_by_xpath("//div[@for='q38_1']")
    find_by_xpath("//div[@for='q38_8']")
    find_by_xpath("//div[@for='q38_2']")
    button_click_next()
    # 23 страница
    find_by_xpath("//div[@for='q39_9']")
    find_by_xpath("//div[@for='q39_7']")
    find_by_xpath("//div[@for='q39_4']")
    button_click_next()
    # 24 страница
    find_by_xpath("//div[@for='q40_15']")
    find_by_xpath("//div[@for='q40_4']")
    find_by_xpath("//div[@for='q40_14']")
    button_click_next()
    # 25 страница
    find_by_xpath("//div[@for='q41_2']")
    find_by_xpath("//div[@for='q41_1']")
    find_by_xpath("//div[@for='q41_7']")
    button_click_next()
    # 26 страница
    find_by_xpath("//div[@for='q42_8']")
    find_by_xpath("//div[@for='q42_6']")
    find_by_xpath("//div[@for='q42_3']")
    button_click_next()
    # 27 страница
    find_by_xpath("//div[@for='q43_1']")
    find_by_xpath("//div[@for='q43_3']")
    button_click_next()
    # 28 страница
    find_by_xpath("//div[@for='q44_1']")
    button_click_next()
    # 29 страница
    find_by_xpath("//div[@for='q45_5']")
    button_click_next()
    # 30 страница
    find_by_xpath("//div[@for='q49_1']")
    button_click_next()
    # 31 страница
    find_by_xpath("//div[@for='q51_1']")
    button_click_next()
    # 32 страница
    find_by_xpath("//div[@for='q52_3']")
    button_click_next()
    # 33 страница
    find_by_xpath("//div[@for='q53_4']")
    button_click_next()
    # 34 страница
    find_by_xpath("//div[@for='q54_4']")
    button_click_next()
    # 35 страница
    find_by_xpath("//div[@for='q55_1']")
    button_click_next()
    # 36 страница
    find_by_xpath("//div[@for='q56_8']")
    button_click_next()
    # 37 страница
    find_by_xpath("//div[@for='q57_2']")
    button_click_next()
    # 38 страница
    find_by_xpath_send_keys("//input[@id='q58']", '24')
    button_click_next()
    # 39 страница
    find_by_xpath("//div[@for='q59_2']")
    button_click_next()
    # 40 страница
    find_by_xpath("//div[@for='q60_1']")
    button_click_next()
    # 41 страница
    find_by_xpath("//div[@for='q61_5']")
    button_click_next()
    # 42 страница
    select = Select(driver.find_element(By.XPATH, "//select[@id='q62']"))
    select.select_by_index(1)
    driver.find_element(By.ID, 'divSubmit').click()
    print(f"{counter} SUCCESS")
    counter += 1
    driver.close()