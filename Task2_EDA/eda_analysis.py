import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"E:/Task1_Web_Scraping/quotes_data.csv")

# Basic info
print(df.head())
print(df.info())
print(df.isnull().sum())

# Add quote length
df["Quote_Length"] = df["Quote"].apply(len)

# Top authors
top_authors = df["Author"].value_counts().head(5)
print(top_authors)

# Plot
top_authors.plot(kind="bar")
plt.title("Top 5 Authors")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.show()
