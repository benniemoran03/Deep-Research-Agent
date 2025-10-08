from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

class WebSearcher:
    def __init__(self, max_results=5):
        self.max_results = max_results

    def search(self, query: str):
        results = []
        for r in DDGS().text(query, max_results=self.max_results):
            url = r["href"]
            content = self._fetch_page(url)
            if content:
                results.append({"url": url, "content": content})
        return results

    def _fetch_page(self, url: str):
        try:
            html = requests.get(url, timeout=10).text
            soup = BeautifulSoup(html, "html.parser")
            text = " ".join(p.text for p in soup.find_all("p"))
            return text[:8000]
        except Exception:
            return None
