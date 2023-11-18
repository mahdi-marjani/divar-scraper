## Product Scraper

This repository contains Python scripts for scraping product information from https://divar.ir The scraped data will be saved in a CSV file.

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/hooshmang/divar-scraper.git
   ```

2. Install the required packages:

   ```bash
   pip install requests
   ```

3. Run the `product_scraper.py` script to scrape the data:

   ```bash
   python product_scraper.py
   ```

   The script will prompt for a search query. Enter the product you want to search for (e.g., "airpods").

4. Once the scraping is completed, a CSV file named `{search_query}.csv` will be created, containing the scraped product information.

### Data Sorting

If you want to sort the scraped data based on price, you can use the `data_sorter.py` script.

1. Run the `data_sorter.py` script:

   ```bash
   python data_sorter.py
   ```

   This script will sort the data based on price and create a new CSV file named `{search_query}(sorted).csv`.

   Note: Make sure to have the `{search_query}.csv` file in the same directory before running this script.

That's it! Now you can use these scripts to scrape and sort product information from https://divar.ir
