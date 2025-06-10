import feedparser
from datetime import datetime, timedelta
import re

# --- Configs ---
search_query = '(ti:RLVR OR abs:RLVR OR (ti:"reinforcement learning" AND ti:"verifiable reward") OR (abs:"reinforcement learning" AND abs:"verifiable reward"))'
days_back = 30
max_results = 50
section_marker = "### 🔄 Auto-Fetched Recent Papers"


# --- Get Papers ---
def fetch_arxiv_results():
    base_url = "http://export.arxiv.org/api/query?"
    query = f"search_query={search_query}&sortBy=lastUpdatedDate&sortOrder=descending&max_results={max_results}"
    feed = feedparser.parse(base_url + query)
    return feed.entries


def filter_recent(entries):
    cutoff_date = datetime.utcnow() - timedelta(days=days_back)
    return [e for e in entries if datetime.strptime(e.updated, "%Y-%m-%dT%H:%M:%SZ") > cutoff_date]


# --- Format Markdown Entries ---
def format_paper(entry):
    title = entry.title.strip().replace('\n', ' ')
    authors = ', '.join(a.name for a in entry.authors)
    date = entry.updated.split("T")[0]
    return f"- **{title}** <{date}>  \n  *{authors}*. [[Paper]]({entry.link})"


# --- Inject into README ---
def update_readme(new_papers):
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    try:
        idx = lines.index(f"{section_marker}\n")
    except ValueError:
        idx = len(lines)
        lines.append(f"\n{section_marker}\n")

    # Insert papers
    papers_md = [format_paper(p) + "\n" for p in new_papers]
    updated_lines = lines[:idx + 1] + papers_md + lines[idx + 1:]

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(updated_lines)


# --- Run ---
if __name__ == "__main__":
    entries = fetch_arxiv_results()
    recent = filter_recent(entries)
    update_readme(recent)
    print(f"Inserted {len(recent)} recent papers.")
