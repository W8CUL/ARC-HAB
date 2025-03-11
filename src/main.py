import requests

sondehub_predict = 'https://predict.sondehub.org/?launch_datetime=2025-03-01T14%3A15%3A00Z&launch_latitude=39.6463&launch_longitude=280.0298&launch_altitude=0&ascent_rate=5&profile=standard_profile&prediction_type=single&burst_altitude=28000&descent_rate=10'

#x = requests.get(sondehub_predict)
#print(x.text)


from selenium import webdriver

driver = webdriver.Firefox()
driver.get(sondehub_predict)

source_code = driver.page_source
print(source_code)
