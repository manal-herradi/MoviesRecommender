import pandas as pd

# Load u.data (tab-separated)
ratings = pd.read_csv("../raw_data/u.data", sep="\t", names=["userId", "movieId", "rating", "timestamp"])

# Save as CSV without the timestamp
ratings.drop(columns=["timestamp"], inplace=True)
ratings.to_csv("../data/ratings.csv", index=False)

print("✅ ratings.csv has been created!")
# Load u.item (pipe-separated)
movies = pd.read_csv("../raw_data/u.item", sep="|", encoding="latin-1", header=None, usecols=[0, 1], names=["movieId", "title"])

# Save as CSV
movies.to_csv("../data/movies.csv", index=False)

print("✅ movies.csv has been created!")