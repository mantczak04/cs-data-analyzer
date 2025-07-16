# [Counter Strike AI Data Analyzer - csanalyzer.pl](https://csanalyzer.pl/)
This project is a web application that allows user to prompt natural language questions to get answers from database of Counter-Strike match statistics. It leverages on a Large Language Model (Gemini) to translate user prompts into SQL queries, which are then executed and displayed in frontend.
It's based on data collected with usage of my another project, ETL pipeline `wall-e`.

### Tech stack:
- Data ETL (wall-e): `python`, `polars`, `pandas`, `awpy`, `demoparser2`, `duckDB`
- Backend: `python`, `fastApi`
- Database: `PostgreSQL`
- AI/LLM: `Gemini 2.5 pro`
- Frontend: `python`, `streamlit`
- Hosting: `Docker` container hosted on Ubuntu VPS Server.

### How to use it?
Additional info and example prompts can be found at [About subpage](https://csanalyzer.pl/About).
