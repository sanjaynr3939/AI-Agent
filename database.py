import sqlite3

# Connect to the database
conn = sqlite3.connect("memory.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    memory TEXT
)
""")

conn.commit()


# Save a message
def save_message(role, message):
    cursor.execute(
        "INSERT INTO chat_history(role, message) VALUES(?, ?)",
        (role, message)
    )
    conn.commit()

# Save an important memory
def save_memory(memory):

    # Check if memory already exists
    cursor.execute(
        "SELECT * FROM memories WHERE memory = ?",
        (memory,)
    )

    existing_memory = cursor.fetchone()

    if existing_memory is None:
        cursor.execute(
            "INSERT INTO memories(memory) VALUES(?)",
            (memory,)
        )
        conn.commit()

# Load conversation history in Gemini format
def get_history():
    cursor.execute("SELECT role, message FROM chat_history ORDER BY id")
    rows = cursor.fetchall()

    history = []

    for role, message in rows:

        if role.lower() == "user":
            gemini_role = "user"
        else:
            gemini_role = "model"

        history.append({
            "role": gemini_role,
            "parts": [
                {
                    "text": message
                }
            ]
        })

    return history

# Load all saved memories
def get_memories():
    cursor.execute("SELECT memory FROM memories")
    rows = cursor.fetchall()

    memories = []

    for row in rows:
        memories.append(row[0])

    return memories


# Clear all conversation history
def clear_history():
    cursor.execute("DELETE FROM chat_history")
    conn.commit()