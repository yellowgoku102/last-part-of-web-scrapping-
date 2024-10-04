


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()




























# URL,Target_Price 
# https://example.com/product1,100
# https://example.com/product2,200













# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Function to get the price from the product page
# def get_price(url):
#     headers = {"User-Agent": "Mozilla/5.0"}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     price = soup.find('span', {'class': 'price'}).get_text()
#     return float(price.replace('$', '').replace(',', ''))

# # Function to send email
# def send_email(subject, body):
#     from_email = "      "
#     to_email = "       "
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))
#     server = smtplib.SMTP('smtp.example.com', 587)
#     server.starttls()
#     server.login(from_email, "your_password")
#     server.send_message(msg)
#     server.quit()

# # Main function to check prices and send alerts
# def check_prices():
#     df = pd.read_csv('products.csv')
#     for index, row in df.iterrows():
#         url = row['URL']
#         target_price = row['Target_Price']
#         current_price = get_price(url)
#         if current_price <= target_price:
#             send_email(
#                 subject=f"Price Alert for {url}",
#                 body=f"The price for {url} has dropped to {current_price}."
#             )

# if __name__ == "__main__":
#     check_prices()

