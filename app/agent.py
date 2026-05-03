



















































import os
from app.search import WebSearcher
from app.summarizer import Summarizer
from app.report import ReportBuilder
from app.utils import ensure_dirs

class ResearchAgent:
    def __init__(self):
        ensure_dirs()
        self.searcher = WebSearcher()
        self.summarizer = Summarizer()
        self.reporter = ReportBuilder()

    def run(self, query: str):
        print(f"[1/3] Searching for '{query}'...")
        docs = self.searcher.search(query)

        print("[2/3] Summarizing sources...")
        summary = self.summarizer.summarize(docs, query)

        print("[3/3] Generating report...")
        path = self.reporter.build(query, summary)
        print(f"✅ Done! Report saved to {path}")
