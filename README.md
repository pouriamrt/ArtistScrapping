# 🎨 ArtistScrapping – Social Media Scraper

**Purpose**: Automates the process of collecting social media and metadata information for musical artists using scraping tools and APIs. This project combines web scraping, browser automation, and API requests to gather and consolidate data into Excel files.

---

## 🔍 Features

- Scrapes social media data (Instagram, Facebook, Genius) for musicians
- Automates browser tasks using Selenium + ChromeDriver
- Uses RapidAPI to enrich results
- Parses HTML with BeautifulSoup (for applicable endpoints)
- Stores results in structured Excel sheets via `pandas`

---

## 🧠 Technologies Used

| Tool          | Purpose                                |
|---------------|----------------------------------------|
| Selenium      | Browser automation (headless Chrome)   |
| chromedriver  | WebDriver backend for Chrome           |
| RapidAPI      | API integration (Instagram scraping)   |
| Requests      | RESTful API communication              |
| BeautifulSoup | HTML content parsing                   |
| Pandas        | Excel file read/write operations       |
| OpenPyXL      | (Optional) Enhanced Excel manipulation |

---

## 📁 Project Structure

```bash
ArtistScrapping/
├── Book1.xlsx                   # Sample or output data
├── Social Media Accounts.xlsx  # Source list of artists
├── chromedriver.exe            # Chrome WebDriver
├── facebook_scrap.py           # Facebook scraping script (Selenium)
├── genius_scrap.py             # Genius.com scraper (API or HTML-based)
├── instagram_rapidapi.py       # Instagram data via RapidAPI
├── final.py                    # Final integration and orchestration script
├── final.spec                  # PyInstaller build spec
├── README.md                   # Project overview
```

---

## ⚙️ How to Run

1. **Install dependencies**:
```bash
pip install selenium requests pandas beautifulsoup4 openpyxl
```

2. **Download `chromedriver.exe`** compatible with your Chrome version  
   Place it in the root folder or update your PATH.

3. **Run individual scripts** as needed:
```bash
python facebook_scrap.py
python genius_scrap.py
python instagram_rapidapi.py
python final.py
```

Each script reads artist names from Excel and writes enriched results to a new or updated Excel file.

---

## 📌 Notes

- Requires valid Internet connection to access public pages and APIs.
- Consider rate limiting and ethical scraping practices (Genius, FB, IG).
- You can customize `final.py` to batch or sequence different scrapers.

---

## ✅ Example Use Case

You have a list of musicians and want to gather:
- Their Facebook page likes/followers
- Verified Instagram profiles
- Genius profiles with biography or top songs

The tool fetches and aggregates this into an Excel dataset for reporting or analysis.

---

## 📄 License

MIT License © 2025 Pouria Mortezaagha

---

## 🤝 Acknowledgments

- [SeleniumHQ](https://www.selenium.dev/)
- [RapidAPI](https://rapidapi.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
