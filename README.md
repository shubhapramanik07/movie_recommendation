# 🎬 FlickPick - AI-Powered Movie Recommendation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36.0-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Discover your next favorite movie with AI-powered recommendations**

[Live Demo](https://movie-rec-466x.onrender.com) • [Report Bug](https://github.com/shubhapramanik07/movie_recommendation/issues) • [Request Feature](https://github.com/shubhapramanik07/movie_recommendation/issues)

</div>

---

## 📖 Table of Contents

- [About The Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 About The Project

FlickPick is a full-stack movie recommendation system that uses **TF-IDF (Term Frequency-Inverse Document Frequency)** algorithm to suggest similar movies based on content similarity. It features a Netflix-inspired dark theme UI and real-time movie data from TMDB.

### Why FlickPick?

- 🎯 **Smart Recommendations** - Uses TF-IDF algorithm for accurate content-based filtering
- 🎨 **Netflix-Inspired UI** - Beautiful dark theme with smooth animations
- ⚡ **Real-time Data** - Fetches latest movie info from TMDB API
- 🚀 **Fast & Scalable** - Built with FastAPI for high performance
- 📱 **Responsive Design** - Works seamlessly on all devices

---

## ✨ Features

| Feature                       | Description                                          |
| ----------------------------- | ---------------------------------------------------- |
| 🔍 **Smart Search**           | Search movies by title with autocomplete suggestions |
| 🎯 **TF-IDF Recommendations** | Content-based filtering using machine learning       |
| 🎭 **Genre Recommendations**  | Find similar movies by genre                         |
| 🔥 **Trending Movies**        | Browse what's hot right now                          |
| ⭐ **Popular Movies**         | Discover fan favorites                               |
| 🏆 **Top Rated**              | Explore critically acclaimed films                   |
| 🎬 **Now Playing**            | See what's in theaters                               |
| 📅 **Upcoming**               | Preview coming attractions                           |
| 🖼️ **Rich Movie Details**     | View posters, backdrops, overviews, and more         |

---

## 🛠️ Tech Stack

### Backend

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[Uvicorn](https://www.uvicorn.org/)** - Lightning-fast ASGI server
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[Scikit-learn](https://scikit-learn.org/)** - TF-IDF vectorization and similarity computation
- **[HTTPX](https://www.python-httpx.org/)** - Async HTTP client for TMDB API calls

### Frontend

- **[Streamlit](https://streamlit.io/)** - Rapid web app development
- **Custom CSS** - Netflix-inspired dark theme styling

### Data Source

- **[TMDB API](https://www.themoviedb.org/)** - Real-time movie data, posters, and metadata
- **Movies Metadata Dataset** - 45,000+ movies for TF-IDF training

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   Streamlit     │────▶│    FastAPI      │────▶│    TMDB API     │
│   Frontend      │     │    Backend      │     │                 │
│   (app.py)      │◀────│   (main.py)     │◀────│                 │
│                 │     │                 │     │                 │
└─────────────────┘     └────────┬────────┘     └─────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │   TF-IDF Model  │
                        │  (Pickle Files) │
                        │                 │
                        │ • df.pkl        │
                        │ • tfidf.pkl     │
                        │ • indices.pkl   │
                        └─────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- TMDB API Key ([Get one here](https://www.themoviedb.org/settings/api))
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/shubhapramanik07/movie_recommendation.git
   cd movie_recommendation
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "TMDB_API_KEY=your_api_key_here" > .env
   ```

### Environment Variables

Create a `.env` file in the root directory:

| Variable       | Description       | Required |
| -------------- | ----------------- | -------- |
| `TMDB_API_KEY` | Your TMDB API key | ✅ Yes   |

---

## 💻 Usage

### Running the Backend (FastAPI)

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### Running the Frontend (Streamlit)

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Running Both Together

Open two terminals:

```bash
# Terminal 1 - Backend
uvicorn main:app --reload --port 8000

# Terminal 2 - Frontend
streamlit run app.py
```
---

## 📁 Project Structure

```
movie_recommendation/
│
├── 📄 main.py              # FastAPI backend server
├── 📄 app.py               # Streamlit frontend app
├── 📄 requirements.txt     # Python dependencies
├── 📄 .env                 # Environment variables (not in git)
├── 📄 .gitignore           # Git ignore rules
├── 📄 README.md            # Project documentation
│
├── 📊 Data Files
│   ├── movies_metadata.csv # Movie dataset (45K+ movies)
│   ├── df.pkl              # Processed DataFrame
│   ├── tfidf.pkl           # TF-IDF vectorizer
│   ├── tfidf_matrix.pkl    # TF-IDF matrix
│   └── indices.pkl         # Movie title indices
│
└── 📁 .venv/               # Virtual environment
```

---

## 🧠 How It Works

### TF-IDF Recommendation Algorithm

1. **Text Preprocessing**: Movie metadata (overview, genres, keywords) is combined into a single text field
2. **TF-IDF Vectorization**: Convert text to numerical vectors using TF-IDF
3. **Similarity Computation**: Calculate cosine similarity between movie vectors
4. **Recommendation**: Return top N most similar movies

```python
# Simplified algorithm flow
text_data = overview + genres + keywords + cast + director
tfidf_matrix = TfidfVectorizer().fit_transform(text_data)
similarity = cosine_similarity(tfidf_matrix[movie_idx], tfidf_matrix)
recommendations = sorted(similarity, reverse=True)[:10]
```

### Data Flow

```
User Search → FastAPI → TF-IDF Model → TMDB Enrichment → Streamlit Display
```

---

## 📸 Screenshots

### Home Page

![Home Page](https://via.placeholder.com/800x400?text=FlickPick+Home+Page)

### Movie Details

![Movie Details](https://via.placeholder.com/800x400?text=Movie+Details+View)

### Recommendations

![Recommendations](https://via.placeholder.com/800x400?text=AI+Recommendations)

---




## 📧 Contact

**Shubha Pramanik** - [@shubhapramanik07](https://github.com/shubhapramanik07)

Project Link: [https://github.com/shubhapramanik07/movie_recommendation](https://github.com/shubhapramanik07/movie_recommendation)

---

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) - For the amazing movie database API
- [FastAPI](https://fastapi.tiangolo.com/) - For the incredible web framework
- [Streamlit](https://streamlit.io/) - For making web apps easy
- [Netflix](https://www.netflix.com/) - For UI/UX inspiration
- [Kaggle](https://www.kaggle.com/) - For the movies metadata dataset

---

<div align="center">


Made with ❤️ by [Shubha Pramanik](https://github.com/shubhapramanik07)

</div>
