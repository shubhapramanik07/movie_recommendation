import requests
import streamlit as st

# =============================
# CONFIG
# =============================
API_BASE = "https://movie-recommendation-3-hvyy.onrender.com" or "http://127.0.0.1:8000"
TMDB_IMG = "https://image.tmdb.org/t/p/w500"

st.set_page_config(page_title="FlickPick | Movie Recommender", page_icon="🎬", layout="wide")

# =============================
# STYLES (Netflix-inspired Dark Theme)
# =============================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700;800&display=swap');

/* Global */
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.block-container { padding-top: 0.5rem; padding-bottom: 2rem; max-width: 100%; padding-left: 3rem; padding-right: 3rem; }

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Netflix black background */
.stApp {
    background: #141414;
}

/* Sidebar styling - Netflix dark */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #000000 0%, #141414 100%);
    border-right: 1px solid #333;
}
[data-testid="stSidebar"] .stMarkdown { color: #e5e5e5; }
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { 
    color: #e50914;
    font-weight: 700;
}

/* Netflix Logo Style - Clean flat like Netflix */
.netflix-logo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.8rem;
    color: #e50914;
    letter-spacing: 3px;
    font-weight: 400;
}

/* Brand header */
.brand-header {
    text-align: center;
    padding: 1.5rem 0;
    margin-bottom: 1rem;
    border-bottom: 1px solid #333;
}
.brand-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem;
    color: #e50914;
    letter-spacing: 3px;
    font-weight: 400;
}

/* Search box - Netflix style */
[data-testid="stTextInput"] input {
    background: #333 !important;
    border: 1px solid #555 !important;
    border-radius: 4px !important;
    color: white !important;
    padding: 0.75rem 1rem !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: #fff !important;
    box-shadow: none !important;
    background: #454545 !important;
}
[data-testid="stTextInput"] input::placeholder { color: #999 !important; }

/* Movie cards - Netflix hover effect */
.movie-card {
    background: transparent;
    border-radius: 4px;
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
}
.movie-card:hover {
    transform: scale(1.08);
    z-index: 10;
    box-shadow: 0 14px 36px rgba(0,0,0,0.75);
}
.movie-card img {
    border-radius: 4px;
}
.movie-title {
    font-size: 0.85rem;
    font-weight: 500;
    line-height: 1.3;
    height: auto;
    max-height: 2.4rem;
    overflow: hidden;
    color: #e5e5e5;
    padding: 0.5rem 0.25rem;
    opacity: 0;
    transition: opacity 0.3s ease;
}
.movie-card:hover .movie-title {
    opacity: 1;
}

/* Netflix Red Buttons */
.stButton > button {
    background: #e50914 !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.5rem 1.2rem !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: #f40612 !important;
    transform: scale(1.02) !important;
}

/* Section headers - Netflix style */
.section-header {
    font-size: 1.4rem;
    font-weight: 700;
    color: #e5e5e5;
    margin: 2rem 0 1rem;
    padding: 0;
    border: none;
    background: none;
}
.section-header::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 1.2rem;
    background: #e50914;
    margin-right: 0.75rem;
    vertical-align: middle;
}

/* Details card - Netflix dark */
.details-card {
    background: rgba(20, 20, 20, 0.95);
    border-radius: 8px;
    padding: 1.5rem;
    border: 1px solid #333;
}

/* Genre pills - Netflix tags */
.genre-pill {
    display: inline-block;
    background: transparent;
    color: #46d369;
    padding: 0.3rem 0;
    font-size: 0.9rem;
    font-weight: 600;
    margin-right: 0.5rem;
    border: none;
}
.genre-pill::after {
    content: ' •';
    color: #666;
    margin-left: 0.5rem;
}
.genre-pill:last-child::after {
    content: '';
}

/* Info badge - Netflix match style */
.info-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: transparent;
    padding: 0.25rem 0;
    font-size: 0.95rem;
    color: #46d369;
    font-weight: 700;
}

/* Match percentage */
.match-badge {
    color: #46d369;
    font-weight: 700;
    font-size: 1rem;
}

/* Maturity rating */
.maturity-badge {
    border: 1px solid #999;
    padding: 0 0.4rem;
    font-size: 0.75rem;
    color: #999;
}

/* Footer - Netflix minimal */
.footer {
    text-align: center;
    padding: 3rem 0;
    margin-top: 3rem;
    border-top: 1px solid #333;
    color: #666;
    font-size: 0.85rem;
}
.footer-brand {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.5rem;
    color: #e50914;
    letter-spacing: 2px;
}

/* Selectbox styling */
[data-testid="stSelectbox"] > div > div {
    background: #333 !important;
    border: 1px solid #555 !important;
    border-radius: 4px !important;
    color: white !important;
}

/* Slider - Netflix red */
[data-testid="stSlider"] > div > div > div { background: #e50914 !important; }

/* Top 10 badge */
.top-badge {
    background: #e50914;
    color: white;
    font-weight: 800;
    padding: 0.15rem 0.5rem;
    font-size: 0.7rem;
    border-radius: 2px;
    margin-right: 0.5rem;
}

/* New badge */
.new-badge {
    background: #46d369;
    color: #141414;
    font-weight: 700;
    padding: 0.1rem 0.4rem;
    font-size: 0.65rem;
    border-radius: 2px;
    text-transform: uppercase;
}

/* Row title with see all */
.row-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.75rem;
}
.row-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #e5e5e5;
}
.see-all {
    color: #54b9c5;
    font-size: 0.85rem;
    cursor: pointer;
}
.see-all:hover {
    color: #fff;
}
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING (single-file pages)
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"  # home | details
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except:
        pass


def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()


def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()


# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=30)  # short cache for autocomplete
def api_get_json(path: str, params: dict | None = None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=25)
        if r.status_code >= 400:
            return None, f"HTTP {r.status_code}: {r.text[:300]}"
        return r.json(), None
    except Exception as e:
        return None, f"Request failed: {e}"


def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show.")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    for r in range(rows):
        colset = st.columns(cols)
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                if poster:
                    st.image(poster, use_column_width=True)
                else:
                    st.markdown('<div style="height:200px;background:linear-gradient(135deg,#1a1a2e,#0f0f23);display:flex;align-items:center;justify-content:center;color:#444;font-size:2rem;">🎬</div>', unsafe_allow_html=True)

                if st.button("▶ View", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}"):
                    if tmdb_id:
                        goto_details(tmdb_id)

                st.markdown(
                    f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True
                )
                st.markdown('</div>', unsafe_allow_html=True)


def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append(
                {
                    "tmdb_id": tmdb["tmdb_id"],
                    "title": tmdb.get("title") or x.get("title") or "Untitled",
                    "poster_url": tmdb.get("poster_url"),
                }
            )
    return cards


# =============================
# IMPORTANT: Robust TMDB search parsing
# Supports BOTH API shapes:
# 1) raw TMDB: {"results":[{id,title,poster_path,...}]}
# 2) list cards: [{tmdb_id,title,poster_url,...}]
# =============================
def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    """
    Returns:
      suggestions: list[(label, tmdb_id)]
      cards: list[{tmdb_id,title,poster_url}]
    """
    keyword_l = keyword.strip().lower()

    # A) If API returns dict with 'results'
    if isinstance(data, dict) and "results" in data:
        raw = data.get("results") or []
        raw_items = []
        for m in raw:
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                }
            )

    # B) If API returns already as list
    elif isinstance(data, list):
        raw_items = []
        for m in data:
            # might be {tmdb_id,title,poster_url}
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            poster_url = m.get("poster_url")
            if not title or not tmdb_id:
                continue
            raw_items.append(
                {
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": poster_url,
                    "release_date": m.get("release_date", ""),
                }
            )
    else:
        return [], []

    # Word-match filtering (contains)
    matched = [x for x in raw_items if keyword_l in x["title"].lower()]

    # If nothing matched, fallback to raw list (so never blank)
    final_list = matched if matched else raw_items

    # Suggestions = top 10 labels
    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    # Cards = top N
    cards = [
        {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
        for x in final_list[:limit]
    ]
    return suggestions, cards


# =============================
# SIDEBAR (Netflix Style)
# =============================
with st.sidebar:
    st.markdown("""
    <div class="brand-header">
        <div class="brand-title">FLICKPICK</div>
        <div style="color:#808080;font-size:0.8rem;margin-top:0.5rem;">Unlimited movies, endless discovery</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("▶ Home"):
        goto_home()

    st.markdown("")
    st.markdown('<p style="color:#e50914;font-weight:700;margin-bottom:0.5rem;">Browse</p>', unsafe_allow_html=True)
    
    category_labels = {
        "trending": "Trending Now",
        "popular": "Popular on FlickPick",
        "top_rated": "Top 10 Today",
        "now_playing": "New Releases",
        "upcoming": "Coming This Week"
    }
    home_category = st.selectbox(
        "Category",
        list(category_labels.keys()),
        format_func=lambda x: category_labels[x],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("")
    st.markdown('<p style="color:#808080;font-size:0.85rem;">Grid Size</p>', unsafe_allow_html=True)
    grid_cols = st.slider("Grid columns", 4, 8, 6, label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("""
    <div style="padding:1rem 0;">
        <div style="color:#808080;font-size:0.7rem;text-transform:uppercase;letter-spacing:1px;">Powered by</div>
        <div style="color:#e5e5e5;font-size:0.85rem;margin-top:0.25rem;">TMDB • TF-IDF AI</div>
    </div>
    """, unsafe_allow_html=True)

# =============================
# HEADER (Netflix Style)
# =============================
st.markdown("""
<div style="padding:0.5rem 0 1.5rem;">
    <span class="netflix-logo">FLICKPICK</span>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":
    typed = st.text_input(
        "Search", placeholder="Titles, genres, people", label_visibility="collapsed"
    )

    st.markdown("")

    # SEARCH MODE (Autocomplete + word-match results)
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Type at least 2 characters for suggestions.")
        else:
            data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(
                    data, typed.strip(), limit=24
                )

                # Dropdown
                if suggestions:
                    labels = ["-- Select a movie --"] + [s[0] for s in suggestions]
                    selected = st.selectbox("Suggestions", labels, index=0)

                    if selected != "-- Select a movie --":
                        # map label -> id
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                else:
                    st.info("No suggestions found. Try another keyword.")

                st.markdown('<div class="section-header">Search Results</div>', unsafe_allow_html=True)
                poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        st.stop()

    # HOME FEED MODE
    category_titles = {
        "trending": "Trending Now",
        "popular": "Popular on FlickPick", 
        "top_rated": "Top 10 in Your Country",
        "now_playing": "New Releases",
        "upcoming": "Coming This Week"
    }
    section_title = category_titles.get(home_category, home_category.replace("_", " ").title())
    
    # Add Top 10 badge for top rated
    if home_category == "top_rated":
        st.markdown(f'<div class="section-header"><span class="top-badge">TOP 10</span>{section_title}</div>', unsafe_allow_html=True)
    elif home_category == "now_playing":
        st.markdown(f'<div class="section-header"><span class="new-badge">NEW</span> {section_title}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="section-header">{section_title}</div>', unsafe_allow_html=True)

    home_cards, err = api_get_json(
        "/home", params={"category": home_category, "limit": 24}
    )
    if err or not home_cards:
        st.error(f"Home feed failed: {err or 'Unknown error'}")
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")
    
    # Footer
    st.markdown("""
    <div class="footer">
        <div class="footer-brand">FLICKPICK</div>
        <div style="margin-top:0.5rem;">Questions? Contact us.</div>
        <div style="margin-top:1rem;display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;font-size:0.8rem;">
            <span>FAQ</span><span>Help Center</span><span>Terms of Use</span><span>Privacy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("🏠 Back to Home"):
            goto_home()
        st.stop()

    # Back button
    if st.button("← Back to Browse"):
        goto_home()
    
    st.markdown("")

    # Details (your FastAPI safe route)
    data, err = api_get_json(f"/movie/id/{tmdb_id}")
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        st.stop()

    # Hero backdrop - Netflix style
    if data.get("backdrop_url"):
        st.markdown(f"""
        <div style="position:relative;border-radius:8px;overflow:hidden;margin-bottom:2rem;">
            <img src="{data['backdrop_url']}" style="width:100%;height:450px;object-fit:cover;filter:brightness(0.35);">
            <div style="position:absolute;inset:0;background:linear-gradient(90deg,#141414 0%,transparent 50%),linear-gradient(to top,#141414 0%,transparent 50%);"></div>
            <div style="position:absolute;bottom:3rem;left:3rem;right:40%;">
                <h1 style="color:white;font-size:3rem;margin:0;font-weight:800;line-height:1.1;">{data.get('title','')}</h1>
                <div style="margin-top:1.5rem;display:flex;align-items:center;gap:1rem;flex-wrap:wrap;">
                    <span class="match-badge">98% Match</span>
                    <span style="color:#999;">{(data.get("release_date") or "N/A")[:4]}</span>
                    <span class="maturity-badge">PG-13</span>
                </div>
                <p style="color:#e5e5e5;margin-top:1rem;font-size:1rem;line-height:1.6;max-width:600px;">{(data.get("overview") or "")[:200]}...</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Layout: Poster LEFT, Details RIGHT
    left, right = st.columns([1, 2.4], gap="large")

    with left:
        if data.get("poster_url"):
            st.image(data["poster_url"], use_column_width=True)
        else:
            st.markdown('<div style="height:300px;background:#222;display:flex;align-items:center;justify-content:center;color:#444;font-size:3rem;border-radius:4px;">🎬</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="details-card">', unsafe_allow_html=True)
        
        if not data.get("backdrop_url"):
            st.markdown(f"""
            <h2 style="margin:0 0 1rem;font-weight:800;color:#e5e5e5;">{data.get('title','')}</h2>
            <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;">
                <span class="match-badge">98% Match</span>
                <span style="color:#999;">{(data.get("release_date") or "N/A")[:4]}</span>
            </div>
            """, unsafe_allow_html=True)
        
        # Genres - Netflix inline style
        genres = data.get("genres", [])
        if genres:
            genre_html = "".join([f'<span class="genre-pill">{g["name"]}</span>' for g in genres])
            st.markdown(f'<div style="margin:1rem 0;">{genre_html}</div>', unsafe_allow_html=True)
        
        # Overview
        if not data.get("backdrop_url"):
            overview = data.get("overview") or "No overview available."
            st.markdown(f'<div style="color:#d2d2d2;line-height:1.7;font-size:1rem;">{overview}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("")
    
    # Recommendations - Netflix style
    st.markdown('<div class="section-header">More Like This</div>', unsafe_allow_html=True)

    title = (data.get("title") or "").strip()
    if title:
        bundle, err2 = api_get_json(
            "/movie/search",
            params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
        )

        if not err2 and bundle:
            tfidf_cards = to_cards_from_tfidf_items(bundle.get("tfidf_recommendations"))
            if tfidf_cards:
                st.markdown('<div class="section-header" style="font-size:1.1rem;">Because You Watched This</div>', unsafe_allow_html=True)
                poster_grid(tfidf_cards, cols=grid_cols, key_prefix="details_tfidf")

            genre_cards = bundle.get("genre_recommendations", [])
            if genre_cards:
                st.markdown('<div class="section-header" style="font-size:1.1rem;">Similar Titles</div>', unsafe_allow_html=True)
                poster_grid(genre_cards, cols=grid_cols, key_prefix="details_genre")
        else:
            genre_only, err3 = api_get_json(
                "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
            )
            if not err3 and genre_only:
                poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
            else:
                st.info("No recommendations available right now.")
    else:
        st.info("No recommendations available.")
    
    # Footer
    st.markdown("""
    <div class="footer">
        <div class="footer-brand">FLICKPICK</div>
        <div style="margin-top:0.5rem;">Questions? Contact us.</div>
        <div style="margin-top:1rem;display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;font-size:0.8rem;">
            <span>FAQ</span><span>Help Center</span><span>Terms of Use</span><span>Privacy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)