# AIDORK
### Description
This project automates Google Dorking, web scraping, and PDF data extraction using AI-generated dorks. 
It leverages Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf (via GPT4All) to generate optimized search queries (dorks) for targeted information gathering, then uses Selenium and PyMuPDF to extract relevant content from web pages and PDFs.
## Features
✅ AI-Powered Google Dork Generation (via Nous-Hermes-2-Mistral-7B-DPO) <br>
✅ Automated Web Scraping (via Selenium) <br>
✅ PDF Text Extraction (via PyMuPDF) <br>
✅ Data Storage & Analysis <br>
✅ Error Handling & Robust Performance

### Installation and Execution
1. Clone the repository
   ```
      git clone https://github.com/Bharath-2204/Dorking-with-AI
      cd Dorking-with-AI
2. Install the dependencies
   ```
      pip install -r requirements.txt
3. Download the AI model
   Download GPT4ALL application for windows/linux and install your desired AI model locally. Update the path of your model in the dork_gen_ai.py file
   ```
      model = GPT4All("\\path\\to\\your\\model")
4. Setup Google API Key and Custom Search Engine
   - Visit the website [Google Custom Search Engine](https://developers.google.com/custom-search/v1/overview) and follow the given steps

4. Run the main script
   Simply run
   `python dork_with_ai.py`
   - The AI will generate dorks, extract URLs, and scrape content automatically
   - The dorks and urls are stored in separate files with timestamps

### Future Enhancements
- Machine Learning Filtering - Classify and rank extracted data
- Enhanced Search Scope - Support for other search engines other than google
   
