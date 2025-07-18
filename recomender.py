import json
import random
import os

# Topics
topics = [
    "Music", "Drama", "Science", "Technology",
    "Sports", "Fashion", "News", "Comedy",
    "Cinema", "Politics"
]

# Simulated users
users = ["user1", "user2", "user3"]
control_user = "control"

# JSON file for storing user interests
DB_FILE = "interests.json"

# Load previous interests
def load_previous_interests():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    else:
        return {user: "" for user in users}

# Save updated interests
def save_interests(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Get topic scores from user
def ask_preferences():
    random.shuffle(topics)
    scores = {}
    for topic in topics:
        while True:
            try:
                value = int(input(f"From 0 to 10, how interested are you in '{topic}'? "))
                if 0 <= value <= 10:
                    scores[topic] = value
                    break
                else:
                    print("Please enter a number between 0 and 10.")
            except ValueError:
                print("Only numbers allowed.")
    return scores

# Get the top interest from the scores
def get_top_interest(scores):
    sorted_topics = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_topics[0][0]

# Display result and compare with previous data
def show_result(username, scores, db):
    top_interest = get_top_interest(scores)
    previous = db.get(username)

    print(f"\nuser: {username} | interest: {top_interest}")

    if previous:
        if previous != top_interest:
            print(f"🔄 Interest changed from '{previous}' to '{top_interest}'")
        else:
            print("✅ Interest remains the same.")
    else:
        print("🆕 No previous data found.")

    db[username] = top_interest
    save_interests(db)

# Main logic
def main():
    db = load_previous_interests()
    username = input("Enter your user key: ")

    if username == control_user:
        print("\n📊 Current interests of all users:\n")
        for user in users:
            interest = db.get(user, "(no data)")
            print(f"user: {user} | interest: {interest}")
    elif username in users:
        print(f"\nWelcome {username}, let's measure your preferences.")
        scores = ask_preferences()
        show_result(username, scores, db)
    else:
        print("❌ Invalid user. Try with user1, user2, user3 or control.")

if __name__ == "__main__":
    main()
