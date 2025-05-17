# 🕷️ Smart Web Crawler with Summarization & Graph Visualization

This is a multithreaded web crawler built using Python. It crawls web pages from a given starting URL, summarizes the content using a Large Language Model (LLM) like **Gemini API**, stores the results in a local SQLite database and JSON file, and visualizes the crawl structure using a graph.

---

## 🚀 Features

- 🔗 Crawl internal links starting from a given URL (domain-restricted)
- 🧠 Summarize content using Gemini API (LLM-based)
- 🧵 Multi-threaded crawling for faster processing
- 💾 Save crawl data to SQLite and JSON
- 🌐 Normalize URLs to avoid duplicate visits
- 📈 Visualize crawl graph (pages as nodes, links as edges)
- 🖥️ CLI dashboard to track progress

---

## 📂 Project Structure

```

web-crawler/
│
├── main.py                     # Entry point to run crawler
├── cli/
│   └── dashboard.py            # Prints crawl progress
├── crawler/
│   ├── fetcher.py              # Fetches HTML content
│   ├── parser.py               # Extracts title, text, and links
│   ├── summarizer.py           # Summarizes content using Gemini or other LLM
│   ├── utils.py                # URL normalization and validation
│   ├── database.py             # SQLite database operations
│   └── graph\_builder.py        # Builds and saves crawl graph
└── data/
└── results.json            # Summarized data output

````

---

## 📥 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/web-crawler.git
cd web-crawler
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your Gemini API Key**
   Set this as an environment variable or place in a `.env` file:

```
GEMINI_API_KEY=your_key_here
```

---

## 🧪 Usage

```bash
python main.py
```

Or update `main.py` to directly call:

```python
crawl("https://example.com", max_pages=10, num_threads=5)
```

---

## 🧠 Summary Example (output)

```json
[
  {
    "url": "https://example.com/about",
    "title": "About Us - Example",
    "summary": "This page describes the mission and team behind Example..."
  }
]
```

---

## 📊 Crawl Graph Output

* A graph image or HTML will be saved as `crawl_graph.html` or `crawl_graph.png` (depending on implementation).
* Pages are nodes, and hyperlinks between them are edges.

---


## 📚 Dependencies

* `requests`, `beautifulsoup4`
* `tqdm` (progress bar)
* `networkx`, `matplotlib`, or `pyvis`
* `openai`, `google-generativeai`, or any LLM API
* `sqlite3` (built-in)
* `concurrent.futures` for multithreading

---

