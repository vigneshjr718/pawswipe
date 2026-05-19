# PawSwipe 🐾 — Swipe-to-Vote for Adoptable Pets

Swipe right to adopt, left to pass. See how the community votes on 100 unique dogs.

## How to Run

### Requirements
- Python 3.9+
- Flask (`pip install flask`)

### Steps
```bash
# 1. Clone / unzip the project
cd swipe-app

# 2. Seed the database (only needed once)
cd backend
python3 seed.py

# 3. Start the server
python3 app.py

# 4. Open in browser
# Go to: http://localhost:5000
```
Open on your phone by visiting `http://<your-laptop-ip>:5000` on the same Wi-Fi.

---

## Architecture

**Frontend:** Single-file vanilla JS + HTML/CSS (`frontend/index.html`), served statically by Flask. No framework — keeps it fast and simple on mobile. Touch and mouse drag events are handled natively. Session identity is a random UUID stored in `localStorage` (used only to deduplicate votes on the server).

**Backend:** Python/Flask with SQLite (stdlib `sqlite3`). Three endpoints: `GET /items`, `POST /vote`, `GET /results`. Votes are deduplicated via a `UNIQUE(item_id, session_id)` constraint with `INSERT OR REPLACE` — so a user flipping their vote updates the record rather than double-counting. SQLite was chosen because it requires zero setup, is file-based, and is perfectly adequate for a single-server demo with low concurrency.

---

## Requirements Checklist

### Core ✅
- [x] 100 distinct pets with image + name + breed + description
- [x] Swipe right = yes, swipe left = no
- [x] Visual feedback: card tilt, yes/no color stamp, glow shadow
- [x] Smooth card transition after each vote
- [x] Results view with aggregate yes/no counts across all users
- [x] Sortable: Most Loved, Most Divisive, Least Loved, A–Z
- [x] Votes persisted to backend SQLite database
- [x] End-of-deck state with CTA to results

### Stretch ✅
- [x] Anonymous session ID — votes remembered across reloads
- [x] Undo last swipe (↩ button + `z` key)
- [ ] Matches view — not implemented
- [ ] Real-time updates — not implemented (would add polling)
- [ ] Admin seed script — seed.py covers this

---

## Known Issues
- Images are from Picsum.photos (random stock photos, not actual dogs)
- No real-time vote refresh — results are fetched fresh each time you open the tab
- No HTTPS — for local demo only

---

## AI Notes
See `AI_NOTES.md`
