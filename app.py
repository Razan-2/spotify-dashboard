import streamlit as st
import pandas as pd

df = pd.read_csv("clean_data.csv")

st.title("Spotify Songs Dashboard")

# Sidebar
st.sidebar.header("About the Dataset")
st.sidebar.write("The most streamed Spotify songs in 2023 from Kaggle. "
                 "Each row is one song with the artist, release year, "
                 "number of streams and music features.")

st.sidebar.header("Filters")

mode = st.sidebar.selectbox("Mode", ["All", "Major", "Minor"])

min_year, max_year = st.sidebar.slider("Release Year",
                                       int(df["released_year"].min()),
                                       int(df["released_year"].max()),
                                       (2010, int(df["released_year"].max())))

top_artists = df["artist_name"].value_counts().head(20).index.tolist()
artists = st.sidebar.multiselect("Artists (top 20)", top_artists)

# Apply filters
filtered = df[(df["released_year"] >= min_year) & (df["released_year"] <= max_year)]

if mode != "All":
    filtered = filtered[filtered["mode"] == mode]

if artists:
    filtered = filtered[filtered["artist_name"].isin(artists)]

# Data preview
st.header("Data Preview")
st.dataframe(filtered[["track_name", "artist_name", "released_year", "streams",
                       "danceability", "energy", "mode"]].head(20))

# Summary statistics
st.header("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Songs", len(filtered))
col2.metric("Total Streams (billions)", round(filtered["streams"].sum() / 1e9, 1))
col3.metric("Average Danceability", round(filtered["danceability"].mean(), 1))
st.write(filtered[["streams", "danceability", "energy", "valence", "bpm"]].describe())

# Visualizations
st.header("Visualizations")

st.subheader("Top 10 Artists by Number of Songs")
st.bar_chart(filtered["artist_name"].value_counts().head(10))

st.subheader("Top 10 Most Streamed Songs")
top_songs = filtered.sort_values("streams", ascending=False).head(10)
st.bar_chart(top_songs.set_index("track_name")["streams"])

st.subheader("Songs by Release Year")
st.bar_chart(filtered["released_year"].value_counts().sort_index())

st.subheader("Danceability vs Streams")
st.scatter_chart(filtered, x="danceability", y="streams", color="mode")

# Insights
st.header("Insights")
st.write("- Taylor Swift has the most songs in the list (34).")
st.write("- Blinding Lights by The Weeknd is the most streamed song (about 3.7 billion).")
st.write("- About 77% of the songs were released in 2020 or later.")
st.write("- Danceability does not affect the number of streams.")
st.write("- Songs in more Spotify playlists have more streams.")
