from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://$IP:$PORT')

assert 'django' in browser.title