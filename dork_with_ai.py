import requests
import csv
from webscrapper import scrap, url_list
from dork_gen_ai import dorkgen_ai
from selenium_data_extraction import selenium_extract
import time


#Searching the web using the generated dorks
def fetch_google_results(query, api_key, cse_id, num_results=10,keyword=""):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cse_id,
        "num": num_results
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        search_results = response.json()
        
        
        urls = [item['link'] for item in search_results.get('items', [])]
        filtered_urls = [url for url in urls if keyword.lower() in url.lower()]
        return filtered_urls
    
    except requests.exceptions.RequestException as e:
        print(f"[+] Error while fetching results: {e}")
        return []

def main():
    print("=== Google Dorking Tool with Google Custom Search ===")
    
    keyword = input("Enter the keyword to search for: ")
    num_results = int(input("Enter the number of results to retrieve (max 10 per request): "))
    
    # Enter Google Custom Search API Key and CSE ID here
    api_key = input("Enter your Google API Key: ")
    cse_id = input("Enter your Google Custom Search Engine ID: ")

    # Define the search queries (dorks)
    # dorks = [
    #     f'site:linkedin.com "{keyword}"',
    #     f'site:github.com "{keyword}"',
    #     f'intitle:"resume" "{keyword}"',
    #     f'inurl:"admin" "{keyword}"',
    #     f'filetype:pdf "{keyword}"',
    #     f'filetype:docx "{keyword}"'
    # ]

    dorks = dorkgen_ai(keyword)
    
    all_results = []
    for dork in dorks:
        print(f"[+] Searching for: {dork}")
        results = fetch_google_results(dork, api_key, cse_id, num_results, keyword)
        all_results.extend(results)
    
    # Remove duplicates
    all_results = list(set(all_results))
    
    # Save results to CSV
    with open("dork_results.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["URL"])
        for result in all_results:
            writer.writerow([result])
    
    #Save results to a text file
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"{keyword}_urls_{timestamp}.txt"
    with open(output_file, "w", newline='', encoding="utf-8" ) as f:
        for result in all_results:
            f.write(f"{result}\n")
            
    print(f"[+] Found {len(all_results)} results.")
    print("Results saved to dork_results.csv")
    selenium_extract(output_file)
    

if __name__ == "__main__":
    main()
