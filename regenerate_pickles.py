"""
Script to regenerate pickle files with NumPy 1.26.4 for Render compatibility.
Run this with: python regenerate_pickles.py
"""
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from ast import literal_eval

print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")

# Load the movies metadata
print("\n📂 Loading movies_metadata.csv...")
df = pd.read_csv('movies_metadata.csv', low_memory=False)
print(f"   Loaded {len(df)} movies")

# Clean and preprocess
print("\n🧹 Cleaning data...")

# Keep only necessary columns
cols_to_keep = ['id', 'title', 'overview', 'genres', 'vote_average', 'vote_count', 
                'popularity', 'release_date', 'runtime', 'original_language']
df = df[[c for c in cols_to_keep if c in df.columns]].copy()

# Remove rows with missing titles
df = df.dropna(subset=['title'])

# Clean ID column - remove non-numeric IDs
df = df[df['id'].apply(lambda x: str(x).isdigit())]
df['id'] = df['id'].astype(int)

# Fill missing overviews
df['overview'] = df['overview'].fillna('')

# Parse genres from string to list
def parse_genres(x):
    try:
        if pd.isna(x) or x == '':
            return ''
        genres = literal_eval(x)
        return ' '.join([g['name'] for g in genres])
    except:
        return ''

df['genres_str'] = df['genres'].apply(parse_genres)

# Create combined text for TF-IDF
df['combined_text'] = df['overview'] + ' ' + df['genres_str']
df['combined_text'] = df['combined_text'].fillna('')

# Remove duplicates based on title
df = df.drop_duplicates(subset=['title'], keep='first')

# Reset index
df = df.reset_index(drop=True)

print(f"   After cleaning: {len(df)} movies")

# Create indices mapping
print("\n📝 Creating indices mapping...")
indices = pd.Series(df.index, index=df['title']).to_dict()

# Create TF-IDF matrix
print("\n🔢 Creating TF-IDF matrix...")
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['combined_text'])
print(f"   TF-IDF matrix shape: {tfidf_matrix.shape}")

# Save pickle files
print("\n💾 Saving pickle files...")

# Save DataFrame
with open('df.pkl', 'wb') as f:
    pickle.dump(df, f, protocol=pickle.HIGHEST_PROTOCOL)
print("   ✅ df.pkl saved")

# Save indices
with open('indices.pkl', 'wb') as f:
    pickle.dump(indices, f, protocol=pickle.HIGHEST_PROTOCOL)
print("   ✅ indices.pkl saved")

# Save TF-IDF vectorizer
with open('tfidf.pkl', 'wb') as f:
    pickle.dump(tfidf, f, protocol=pickle.HIGHEST_PROTOCOL)
print("   ✅ tfidf.pkl saved")

# Save TF-IDF matrix
with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f, protocol=pickle.HIGHEST_PROTOCOL)
print("   ✅ tfidf_matrix.pkl saved")

print("\n✨ All pickle files regenerated successfully!")
print(f"   NumPy version used: {np.__version__}")
