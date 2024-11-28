import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url, output_file):
    print(f"Connecting to {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    print("Parsing data...")

    # Пример парсинга таблицы (измените селектор для вашего сайта)
    data = []
    table = soup.find('table')  # Найдите таблицу
    if not table:
        print("Error: No table found on the page. Check the website structure.")
        return

    table_rows = table.find_all('tr')
    for row in table_rows:
        columns = [col.text.strip() for col in row.find_all(['th', 'td'])]
        if columns:
            data.append(columns)

    if not data:
        print("No data found. Ensure the selectors match the website structure.")
        return

    print(f"Saving data to {output_file}...")
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    output_file = "data.csv"  # Имя файла для сохранения
    scrape_data(url, output_file)
