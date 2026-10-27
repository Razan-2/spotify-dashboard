# Spotify Songs Analysis

Final Project – Unit 3: Individual Data Exploration & Dashboard Development
**Name:** Razan Alqobti

## Overview
This project analyzes the most streamed Spotify songs in 2023. The data has text values in numeric columns, missing values and duplicate songs, so it was cleaned first. Then it was explored with charts, and an interactive dashboard was built with Streamlit.

## Dataset
- **Title:** Most Streamed Spotify Songs 2023
- **Source:** [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023)
- **Size:** 953 songs and 24 columns (948 songs after cleaning)

## Live Dashboard
[Add the Streamlit link here]

## Questions
1. Which artist has the most songs in the list?
2. What are the most streamed songs?
3. Are danceable songs streamed more?
4. Are newer songs more common in the list?
5. Are there more Major or Minor songs?

## Files
| File | Description |
|---|---|
| `spotify_eda.ipynb` | Jupyter Notebook: data loading, cleaning and EDA |
| `spotify-2023.csv` | Original dataset |
| `clean_data.csv` | Cleaned dataset |
| `app.py` | Streamlit dashboard |
| `requirements.txt` | Libraries needed to run the dashboard |
| `Spotify_Report.pdf` | Project report |

## How to Run

### Notebook
1. Open `spotify_eda.ipynb` in Google Colab or Jupyter.
2. Upload `spotify-2023.csv` to the same folder.
3. Run all cells. The notebook creates `clean_data.csv`.

### Dashboard
```
pip install -r requirements.txt
streamlit run app.py
```

## Main Insights
- Taylor Swift has the most songs in the list (34).
- Blinding Lights by The Weeknd is the most streamed song (about 3.7 billion streams).
- About 77% of the songs were released in 2020 or later.
- Danceability, energy and mood have almost no effect on streams.
- Songs in more Spotify playlists have more streams (correlation 0.79).

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, Streamlit
