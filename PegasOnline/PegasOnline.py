from selenium import webdriver
from datetime import datetime
import time

# --------------------------------------------------------------------------------------
# 1) Бот будет входить на пару за 5 минут до ее начала.
# 2) Бот не знает, есть ли у тебя пара, до того как не попытается ее найти в расписании.
#    Это значит то, что если он не найдет пару, то выдаст ошибку и крашнется.
#    Если же пара есть, то он зайдет на нее.
# 3) Бот будет сидеть ровно до конца пары, даже если все уже вышли.
# 4) Для всего этого Боту нужны:
#       1. Номер группы (Чтобы найти твое расписание).
#       2. Твой логин от системы Пегас.
#       3. Твой пароль от системы Пегас.
# --------------------------------------------------------------------------------------

def JoinLesson(group, username, password, lesson):
    url = f"https://www.bsu.edu.ru/bsu/resource/schedule/groups/index.php?group={group}"
    options = webdriver.ChromeOptions()

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36")

    driver = webdriver.Chrome(
        executable_path="chromedriver.exe",
        options=options
    )

    try:
        driver.get(url=url)
        time.sleep(2)
        current_lesson = driver.find_elements_by_xpath("//td[@id='lesson'][@class='today']/a[@target='_blank']")
        current_lesson[lesson].click()

        time.sleep(2)

        driver.switch_to.window(driver.window_handles[1])

        time.sleep(2)

        username_input = driver.find_element_by_id("username")
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(1)
        password_input = driver.find_element_by_id("password")
        password_input.clear()
        password_input.send_keys(password)
        login_button = driver.find_element_by_id("loginbtn").click()

        time.sleep(3)
    
        bbb = driver.find_element_by_xpath("//li[@class='activity bigbluebuttonbn modtype_bigbluebuttonbn ']//a").click()

        time.sleep(3)

        connect = driver.find_element_by_id("join_button_input").click()

        time.sleep(3)

        driver.switch_to.window(driver.window_handles[2])

        time.sleep(4)

        try:
            driver.find_element_by_xpath("//button[@aria-label='Listen only']").click()
        except Exception as ex:
            driver.find_element_by_xpath("//button[@aria-label='Только слушать']").click()

        time.sleep(5)

        bbb_input = driver.find_element_by_id("message-input")
        bbb_input.clear()
        bbb_input.send_keys("Здравствуйте")

        try:
            driver.find_element_by_xpath("//button[@aria-label='Send message']").click()
        except Exception as ex:
            driver.find_element_by_xpath("//button[@aria-label='Отправить сообщение']").click()

        time.sleep(6000)

        driver.close()
        driver.quit()

    except Exception as ex:
        print("-----------------------------------------")
        print(f"Exception: {ex}")
        print("-----------------------------------------")
        driver.close()
        driver.quit()
        exit()      

def main():
    group = input("Введите номер группы: ")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    while (True):
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        if (hours == 8 and minutes == 25):
            lesson = 0
            JoinLesson(group, username, password, lesson)
        elif (hours == 10 and minutes == 10):
            lesson = 1
            JoinLesson(group, username, password, lesson)
        elif (hours == 12 and minutes == 15):
            lesson = 2
            JoinLesson(group, username, password, lesson)
        elif (hours == 14 and minutes == 0):
            lesson = 3
            JoinLesson(group, username, password, lesson)
        elif (hours == 15 and minutes == 45 ):
            lesson = 4
            JoinLesson(group, username, password, lesson)
        elif (hours == 17 and minutes == 30):
            lesson = 5
            JoinLesson(group, username, password, lesson)

if (__name__ == "__main__"):
    main()