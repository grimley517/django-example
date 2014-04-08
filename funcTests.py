from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://$IP:$PORT')

assert 'django' in browser.title