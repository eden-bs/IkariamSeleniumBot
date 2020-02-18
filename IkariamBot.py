import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
firefox = webdriver.Firefox()
firefox.maximize_window()
firefox.get("https://lobby.ikariam.gameforge.com/he_IL/")
tabs_list = firefox.find_element_by_class_name("tabsList")
button = tabs_list.find_element_by_tag_name("li")
button.click()

email = WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located((By.NAME, "email")))

email.send_keys("my_email")

(firefox.find_element_by_name("password")
       .send_keys("my_password"))

(firefox.find_element_by_id("loginForm")
      .find_element_by_tag_name("button")
      .click())

join_game = WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located((By.ID, "joinGame")))

join_game.find_element_by_tag_name("button").click()

accounts_list = (firefox.find_element_by_id("accountlist")
                       .find_element_by_class_name("rt-tbody")
                       .find_elements_by_class_name("rt-tr-group"))

for account_row in accounts_list[:2]:
    if account_row.find_element_by_class_name("player-cell").text != "my_email":
        continue

    (account_row.find_element_by_class_name("action-cell")
                .find_element_by_tag_name("button")
                .click()) 

    firefox.switch_to.window(firefox.window_handles[1])

    time.sleep(4)
    port = (firefox.find_element_by_class_name("port")
                      .find_element_by_tag_name("a"))

    firefox.execute_script("arguments[0].click();", port)  

    cities = WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cities")))

    city_boxes = [city_box.get_attribute("id") for city_box in firefox.find_elements_by_class_name("cityBox")]

    for city_id in city_boxes[:-1]:
        city_element = WebDriverWait(firefox, 10, poll_frequency=0.1).until(
            EC.element_to_be_clickable((By.ID, city_id)))
        city_element.click()
        text_field = WebDriverWait(firefox, 10).until(
            EC.presence_of_element_located((By.ID, "textfield_wine")))
        text_field.send_keys("8000")
        submit_button = firefox.find_element_by_id("submit")
        firefox.execute_script("arguments[0].click();", submit_button)
        time.sleep(1)
    firefox.close()
    firefox.switch_to.window(firefox.window_handles[0])
   
firefox.quit()
