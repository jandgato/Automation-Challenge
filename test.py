import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DynamicControls(unittest.TestCase):
    #Prepara entorno de la prueba. 
    @classmethod
    def setUp(clc):
        clc.driver = webdriver.Chrome('chromedriver')
        driver = clc.driver
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")


    #Casos de prueba
    def test_radio_button(self):
        driver = self.driver
        
        driver.find_element(By.CSS_SELECTOR,"#radio-btn-example > fieldset > label:nth-child(3) > input").click()
        driver.find_element(By.CSS_SELECTOR,"#radio-btn-example > fieldset > label:nth-child(4) > input").click()
        driver.find_element(By.CSS_SELECTOR,"#radio-btn-example > fieldset > label:nth-child(2) > input").click()
        
    def test_suggestion_input(self):
        driver = self.driver
        
        suggestion_text_input = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/fieldset/input')
        suggestion_text_input.send_keys("Me")
        driver.find_element(By.XPATH,'/html/body/ul/li[6]/div').click
        
    def test_checkbox_click(self):
        driver = self.driver
        
        driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/fieldset/label[2]/input').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/fieldset/label[3]/input').click()
        
        
    def test_switch_alert(self):
        driver = self.driver
        
        switch_alert_input = driver.find_element(By.XPATH,'//*[@id="name"]')
        switch_alert_input.clear()
        switch_alert_input.send_keys("Stori Card")
        driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
        
        switch_alert_popup = driver.switch_to.alert
        switch_alert_popup.accept()
        
    def test_is_element_displayed(self):
        
        self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="displayed-text"]'))
    
    def	is_element_present(self, how, what):
        try:  #busca los elementos según el parámetro
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True
            
        

    #Finalizar
    @classmethod
    def tearDow(clc):
        clc.driver.quit() #Revisar con close


if __name__ == "__main__":
    unittest.main(verbosity=2)
