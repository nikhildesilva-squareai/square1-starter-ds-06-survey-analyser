# Survey Data Analyser — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · Data Science · Project 6.**

✅ **Data included.** The dataset is committed in [`dataset/`](dataset/) and is the **same standardized dataset every learner uses** — so results are comparable. It is 100% synthetic and Square 1-owned (no third-party or personal data). You can also download it as a single file from the project page on Square 1.

To run the commands below, copy the files into `data/` (`mkdir -p data && cp -r dataset/* data/`) or point the commands straight at `dataset/`.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# Survey Data Analyser — starter

Starter for Square 1 AI **Data Science · Project 6**. Turn open-ended survey comments into sentiment + themes, and check them against the star ratings.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Get the data
Download `survey_responses.csv` from your project page (Resources → Dataset) into `data/`.

## Your task
Three tests define the contract — they fail until you implement the stubs in `survey/survey.py`:
```bash
pytest -q
python -m survey.cli data/survey_responses.csv
```
Pipeline: `load_responses` (parse dates, treat blank comments as missing) → `score_sentiment` (positive text must score above negative) → `top_themes` (recurring keywords by sentiment) → `summarize` (overall split, top themes each way, sentiment-vs-rating agreement, worst department). Clean the dirt first — ~8% blank comments, plus ALL-CAPS and typos. Full brief, rubric, and references are on your Square 1 project page. MIT licensed.
