import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAgregapelculaBastardosSinGloria():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agregapelculaBastardosSinGloria(self):
    self.driver.get("http://localhost:3030/")
    self.driver.set_window_size(1512, 886)
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn > .flex").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("Bastardos sin gloria")
    self.driver.find_element(By.ID, "description").send_keys("Película bélica que retrata una perspectiva diferente de la segunda guerra mundial")
    self.driver.find_element(By.ID, "year").send_keys("2009")
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Quentin Tarantino']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
