import os
import pdfkit

class ReportBuilder:
    def build(self, query, summary):
        base = query.replace(" ", "_")[:50]
        path_md = f"data/reports/{base}.md"
        with open(path_md, "w", encoding="utf-8") as f:
            f.write(f"# Research Report: {query}\n\n{summary}")

        pdf_path = path_md.replace(".md", ".pdf")
        pdfkit.from_file(path_md, pdf_path)
        return path_md
