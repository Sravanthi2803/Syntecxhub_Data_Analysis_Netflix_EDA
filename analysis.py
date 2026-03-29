import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create graphs folder
if not os.path.exists("graphs"):
    os.makedirs("graphs")

# Load dataset
df = pd.read_csv("netflix_titles.csv",encoding='latin1')

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# Movies vs TV Shows
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows")
plt.savefig("graphs/type_count.png")
plt.clf()

# Release year trend
df['release_year'].value_counts().sort_index().plot()
plt.title("Content Release Over Years")
plt.savefig("graphs/release_year.png")
plt.clf()

# Top genres
df['listed_in'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Genres")
plt.savefig("graphs/top_genres.png")
plt.clf()

print("Netflix Analysis Completed!")