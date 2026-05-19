# 🐾 PawSwipe — Swipe to Adopt

> A mobile-first swipe-to-vote app for adoptable dogs. Swipe right to adopt ❤️, left to pass 👋. See how the community votes in real time.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=flat&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Mobile](https://img.shields.io/badge/Mobile-First-orange?style=flat)

## 🖥️Screenshots
<img width="1600" height="807" alt="WhatsApp Image 2026-05-18 at 18 08 16" src="https://github.com/user-attachments/assets/134e15c1-79bd-460c-8bc8-6dde37b15201" />
<img width="1600" height="809" alt="WhatsApp Image 2026-05-18 at 18 08 31" src="https://github.com/user-attachments/assets/f68a3239-2162-415f-b71c-9ea01938eb78" />
<img width="1600" height="809" alt="WhatsApp Image 2026-05-18 at 18 08 31" src="https://github.com/user-attachments/assets/d2b6beb9-0ded-46e4-bfcd-dfbd008983f1" />


---

## 📹 Demo Video

[![Watch the Demo](https://www.youtube.com/watch?v=6qQaHP8HUIw)

---

## ✨ Features

- 🐶 **100 unique dog profiles** — each with name, breed, description, and image
- 👆 **Swipe gestures** — drag right to vote yes, left to vote no (touch + mouse)
- 💚 **Visual feedback** — card tilt, YES/NOPE stamp overlay, color glow as you drag
- 📊 **Results view** — aggregate votes across all users with 4 sort modes
- 🔄 **Sort by** — Most Loved · Most Divisive · Least Loved · A–Z
- ↩️ **Undo** — bring back your last card anytime
- 💾 **Session memory** — your progress is saved across page reloads
- 🖥️ **Real backend** — Flask + SQLite, votes persist server-side

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vanilla HTML / CSS / JavaScript |
| Backend | Python + Flask |
| Database | SQLite (stdlib) |
| Gestures | Native Touch & Mouse Events |
| Persistence | SQLite + localStorage (session cache) |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/pawswipe.git
cd pawswipe

# 2. Install Flask
pip install flask

# 3. Seed the database (run once)
cd backend
python seed.py

# 4. Start the server
python app.py
```

Then open **http://localhost:5000** in your browser.

> 📱 To test on your phone: run `ipconfig` (Windows) or `ifconfig` (Mac) to get your laptop IP, then visit `http://<your-ip>:5000` on the same Wi-Fi.

---

## 📁 Project Structure
## pawswipe/
├── backend/
│   ├── app.py          # Flask server — API endpoints
│   ├── seed.py         # Seeds 100 dogs into the database
│   └── votes.db        # SQLite database (auto-created)
├── frontend/
│   └── index.html      # Full frontend (HTML + CSS + JS)
├── README.md
└── AI_NOTES.md

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/items` | Returns all 100 pet profiles |
| POST | `/vote` | Records a vote `{ itemId, choice, sessionId }` |
| GET | `/results` | Returns aggregate yes/no counts per pet |

### Vote Deduplication
Votes use a `UNIQUE(item_id, session_id)` constraint with `INSERT OR REPLACE` — so a user can change their vote but never double-count it.

---

## ✅ Requirements Checklist

### Core
- [x] 100 distinct items with image, label, and description
- [x] Swipe right = yes, swipe left = no
- [x] Visual feedback during gesture (tilt, stamp, glow)
- [x] Smooth card transition after each vote
- [x] Results view with aggregate counts across all users
- [x] Sortable results (4 modes)
- [x] Votes persisted to backend database
- [x] End-of-deck state with link to results

### Stretch
- [x] Anonymous session ID — progress remembered across reloads
- [x] Undo last swipe
- [ ] Real-time updates (polling / websockets)
- [ ] Matches view

---

## 🤖 AI Usage

See [`AI_NOTES.md`](./AI_NOTES.md) for a full reflection on how Claude was used, where I pushed back on its output, and what it did well vs. poorly.

---

## 📌 Known Issues

- Images are placeholder photos from [picsum.photos](https://picsum.photos) — not real dogs
- No HTTPS — local demo only
- Results refresh on tab open, not in real time

---

## 📄 License

For educational use — CMPE 285 Final Project, San Jose State University.
