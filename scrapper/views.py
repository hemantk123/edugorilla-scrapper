from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import requests
import time
def BestsSellerFinder(request):
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get('https://www.amazon.in/gp/bestsellers/electronics/1805560031/')
	wait = WebDriverWait(driver, 10)
	maindiv = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'p13n-gridRow')))
	driver.execute_script("window.scrollTo(0, 30000)")
	time.sleep(10)
	phones = maindiv.find_elements(By.ID,'gridItemRoot')
	data = []
	for phone in phones:
		try:
			rating = phone.find_element(By.CLASS_NAME,'a-icon-alt').get_attribute('textContent').split()[0]
		except NoSuchElementException:
			rating = 'No rating'
		try:
			name = phone.find_element(By.CLASS_NAME,'_cDEzb_p13n-sc-css-line-clamp-3_g3dy1').text
		except NoSuchElementException:
			name = phone.find_element(By.CLASS_NAME,'_cDEzb_p13n-sc-css-line-clamp-4_2q2cc').text
		except:
			name = 'No name'
		try:
			price = phone.find_element(By.CLASS_NAME,'_cDEzb_p13n-sc-price_3mJ9Z').text
		except NoSuchElementException:
			price = 'No price'
		data.append({'Name':name,'Price':price,'Rating':rating})
	driver.close()
	return JsonResponse(data,safe=False)

def SmartPhoneFinder(request):
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get('https://www.amazon.in/s?k=smartphones')
	wait = WebDriverWait(driver, 10)
	maindiv = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]')))
	phones = maindiv.find_elements(By.CLASS_NAME,'s-asin')
	data = []
	for phone in phones:
		try:
			rating = phone.find_element(By.CLASS_NAME,'a-size-base').text
		except NoSuchElementException:
			rating = 'No rating'
		try:
			name = phone.find_element(By.CLASS_NAME,'a-size-medium').text
		except NoSuchElementException:
			name = 'No name'
		try:
			price = phone.find_element(By.CLASS_NAME,'a-price-whole').text
		except NoSuchElementException:
			price = 'No price'
		data.append({'Name':name,'Price':price,'Rating':rating})
	driver.close()
	return JsonResponse(data,safe=False)