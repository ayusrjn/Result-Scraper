# Result Scraping Project

This project is a web scraping tool that automates the process of scraping student result data from a university results website and filling out a registration form on another website. The project uses Selenium WebDriver to interact with web pages and extract data.

## Project Structure

### Files

- [`practise_os.py`](practise_os.py): A simple script to print environment variables.
- [`scraped_data.csv`](scraped_data.csv): Contains scraped result data for all students.
- [`scraped_data_CSE.csv`](scraped_data_CSE.csv): Contains scraped result data for CSE students.
- [`scraped_data_EEE.csv`](scraped_data_EEE.csv): Contains scraped result data for EEE students.
- [`scrapper-prac.py`](scrapper-prac.py): Automates the process of filling out a registration form on a website.
- [`scrapper.py`](scrapper.py): Scrapes student result data from a university results website.

## Setup

1. Install the required Python packages:
    ```sh
    pip install selenium
    ```

2. Download the Edge WebDriver from the [official site](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in a known directory.

3. Update the [path_to_driver](http://_vscodecontentref_/6) variable in [scrapper-prac.py](http://_vscodecontentref_/7) and [scrapper.py](http://_vscodecontentref_/8) to point to the location of the Edge WebDriver executable.

## Usage

### Scraping Results

To scrape student result data, run the [scrapper.py](http://_vscodecontentref_/9) script:
```sh
python scrapper.py