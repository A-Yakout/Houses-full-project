from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

houses_data = []

for i in range(50, 101):  
    url = f'https://www.propertyfinder.eg/en/search?l=2254&c=1&fu=0&ob=mr&page={i}'
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    
    soup = BeautifulSoup(driver.page_source,'html.parser')
    
    houses_block = soup.find('div', {'class': 'view_desktop_column__zp9j7'})
    
    houses = houses_block.find_all('li', attrs={'data-testid': True})
    
    for house in houses:
        try:
            price_tag= house.find('div',{'class':'styles-module_content__price-area__I0781'})
            price = price_tag.find('p',{'class':'styles-module_content__price__SgQ5p'}).text.strip()
            location_tag = house.find('div',{'class':'styles-module_content__specs__AKNWy'})
            location = location_tag.find('p',{'class':'styles-module_content__location__bNgNM'}).text
            property_type = house.find('p',{'class':'styles-module_content__property-type__QuVl4'}).span.text.strip()
            time_tag = house.find('div',{'class':'styles-module_footer__content__QxMhm'})
            time_listed = time_tag.find('p',{'class':'styles-module_footer__publish-info__UVabq'}).text.strip()
            area_tag = house.find('div',{'data-testid':'property-card-details'})
            bedrooms = area_tag.find_all('p',{'class':'styles-module_content__details-item__mlu9B'})[0].get_text(strip=True)
            bathrooms = area_tag.find_all('p',{'class':'styles-module_content__details-item__mlu9B'})[1].get_text(strip=True)
            area = area_tag.find_all('p',{'class':'styles-module_content__details-item__mlu9B'})[2].get_text(strip=True)
            telephone = house.find('a',{'data-testid':'property-card-contact-action-CALL'})['href']
            print("property got Scraped ! ")
            
            houses_data.append({'Property_type':property_type,
                                'Price':price,
                                'Area':area,
                                'Location':location,
                                'Date_listed':time_listed,
                                '#bedrooms':bedrooms,
                                '#bathrooms':bathrooms,
                                'Telephone':telephone})
        except Exception as e:
                print(f"Error scraping job: {e}")
                
df = pd.DataFrame(houses_data)
df.to_excel('property_finder_data_cairo2.xlsx', index=False)
print("Data has been written to 'property_finder_data.xlsx'")    
    