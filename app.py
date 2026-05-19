from flask import Flask, request, jsonify, send_from_directory
import sqlite3, os

app = Flask(__name__, static_folder="../frontend", static_url_path="")
DB = os.path.join(os.path.dirname(__file__), "votes.db")

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

# ── Serve frontend ──────────────────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

# ── GET /items ───────────────────────────────────────────────────────────────
@app.route("/items")
def items():
    conn = get_db()
    rows = conn.execute("SELECT * FROM items ORDER BY id").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

# ── POST /vote ───────────────────────────────────────────────────────────────
@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json(silent=True) or {}
    item_id   = str(data.get("itemId",   "")).strip()
    session_id = str(data.get("sessionId","")).strip()
    choice    = str(data.get("choice",   "")).strip().lower()

    if not item_id or not session_id or choice not in ("yes", "no"):
        return jsonify({"error": "invalid payload"}), 400

    conn = get_db()
    try:
        # UNIQUE(item_id, session_id) prevents double-count
        conn.execute(
            "INSERT OR REPLACE INTO votes (item_id, session_id, choice) VALUES (?,?,?)",
            (item_id, session_id, choice)
        )
        conn.commit()
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# ── GET /results ─────────────────────────────────────────────────────────────
@app.route("/results")
def results():
    conn = get_db()
    rows = conn.execute("""
        SELECT i.id, i.name, i.breed, i.image,
               COALESCE(SUM(CASE WHEN v.choice='yes' THEN 1 ELSE 0 END), 0) AS yes_count,
               COALESCE(SUM(CASE WHEN v.choice='no'  THEN 1 ELSE 0 END), 0) AS no_count
        FROM items i
        LEFT JOIN votes v ON i.id = v.item_id
        GROUP BY i.id
        ORDER BY yes_count DESC
    """).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(port=5000, debug=True)
