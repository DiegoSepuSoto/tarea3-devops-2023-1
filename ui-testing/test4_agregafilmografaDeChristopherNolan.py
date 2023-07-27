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

class TestAgregafilmografadeChristopherNolan():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agregafilmografadeChristopherNolan(self):
    self.driver.get("http://localhost:3030/")
    self.driver.set_window_size(1512, 886)
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element_with_offset(element, 0, 0).perform()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("Memento")
    self.driver.find_element(By.ID, "description").send_keys("Película que retrata dos lineas de tiempo entrecruzadas")
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys("2000")
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Cristopher Nolan']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
    self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element_with_offset(element, 0, 0).perform()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("Interestelar")
    self.driver.find_element(By.ID, "description").send_keys("Película de ciencia ficción sobre viaje entre dimensiones")
    self.driver.find_element(By.ID, "year").click()
    self.driver.find_element(By.ID, "year").send_keys("2014")
    self.driver.find_element(By.ID, "director_id").click()
    dropdown = self.driver.find_element(By.ID, "director_id")
    dropdown.find_element(By.XPATH, "//option[. = 'Cristopher Nolan']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
  
