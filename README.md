
# **Jumia TV Scraper**  

This project is a web scraper built with **Scrapy** to extract product data from Jumia TV.  

## **Features**  
- Scrapes product details like name, price, sku, marque and ratings  
- Handles pagination for multiple pages  
- Uses pipelines for data processing
- Saves data in **JSON**, **CSV**,  and in a **database**(with postreSQL)  

## **Installation**  
Make sure you have **Python 3.10+** and **Scrapy** installed:  
```sh
pip install scrapy
```

## **Usage**  
To start scraping, run:  
```sh
scrapy crawl jumiaSpider -o data.json
```
  

## **Project Structure**  
```
jumiaTv/
│── spiders/
│   ├── jumiaSpider.py  # Main spider for scraping
│── pipelines.py  # Processes scraped data
│── settings.py   # Scrapy settings
│── items.py      # Data structure definition
│── middlewares.py  # Middleware settings
scrapy.cfg  # Scrapy configuration file
```
