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

class TestAgrega2directores():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agrega2directores(self):
    self.driver.get("http://localhost:3030/")
    self.driver.set_window_size(1512, 886)
    self.driver.find_element(By.ID, ":r1:-tab-1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element_with_offset(element, 0, 0).perform()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Stanley Kubrick")
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Quentin Tarantino")
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
  
