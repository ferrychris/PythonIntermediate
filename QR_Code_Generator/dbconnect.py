import sqlite3

# ── connection ────────────────────────────────────────────────────────────────

conn = sqlite3.connect('game.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_points (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        points  INTEGER NOT NULL,
        won     INTEGER NOT NULL DEFAULT 0   -- 1 = won, 0 = lost
    )
""")
conn.commit()
print("Database connected ✓")



# ── public helpers ─────────────────────────────────────────────────────────────
def save_result(name: str, points: int, won: bool):
    """Insert one game result into the database."""
    cursor.execute(
        "INSERT INTO user_points (name, points, won) VALUES (?, ?, ?)",
        (name, points, int(won))
    )
    conn.commit()
    print(f"Saved: {name} — {points} pts — {'WON' if won else 'LOST'}")

def get_leaderboard():
    """Return all results ordered by points descending."""
    cursor.execute("select * from user_points order by points desc")
    return cursor.fetchall()

def update_users(id):
    cursor.execute(
        "UPDATE user_points SET name = ?, points = ?, won = ? WHERE id = ?", 
        (name, points, won, id))
    conn.commit()
    print(f"Updated: {name} — {points} pts — {'WON' if won else 'LOST'}")

def delete_users(id):
    cursor.execute(
        "DELETE FROM user_points WHERE id = ?", 
        (id,))
    conn.commit()
    print(f"Deleted: {name} — {points} pts — {'WON' if won else 'LOST'}")

