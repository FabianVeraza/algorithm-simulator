# 🎯 Interest Learning System (Console Simulation)

This project is a **console-based simulation** of a basic interest learning system — perfect for anyone who wants to **understand how recommendation algorithms work** without diving into advanced machine learning.

---

## 🧠 What Is This?

It's a Python application that simulates how platforms like TikTok or YouTube learn your interests based on your interactions. In this case:

- There are **three simulated users**: `usuario1`, `usuario2`, `usuario3`.
- A **fourth user called "control"** can view the detected interests of the others.
- Each user answers a series of questions from 0 to 10, rating how interested they are in specific topics.
- The system identifies their **strongest interest** and saves it to a local file (`intereses.json`).
- When run again, it compares if the user’s interest has changed or remained the same.

---

## 🧩 What Algorithms Are Used?

- **Maximum scoring selection:** Detects the topic with the highest score after one round.
- **JSON persistence:** Simulates a basic database that stores the last known interest per user.
- **Simple comparison:** Compares the current top interest to the previous one.
- **Basic learning:** If the interest changed, it updates. If it stayed the same, it confirms.

This model is a basic example of **behavior-based learning**, a technique used in real-world recommendation systems.

---

## 🚀 How to Use It

1. **Clone this repository**
   ```bash
   git clone https://github.com/FabianVeraza/algorithm-simulator.git
   cd algorithm-simulator

2. **Install python (if you don't have it)**
3. **Run the script**
   ```bash
   python recommender.py
 4. **Use the folowing keys:**
    - user1, user2, user3: To answer the interest questions
    - control: to view all users' interests

## 📁 Important Files

- recommender.py
- interests.json

## Example Output
   Enter your user key: usuario1
   From 0 to 10, how interested are you in 'Music'? 9
   From 0 to 10, how interested are you in 'Drama'? 8
   ...
   ✅ Your strongest interest: Music
   🔄 Your interest has changed from 'Drama' to 'Music'

   Enter your user key: control
   user: user1 | interest: Music
   user: user3 | interest: Science
   user: user3 | interest: (no data yet)

## Who Is This For?
   •  Students learning programming or AI.
	•	Curious minds who want to understand how apps “learn” about users.
	•	Educators who need a classroom example of behavior-based logic.
	•	Beginner developers looking for Python practice.

 ## Possible Improvements
   •  Store full interest history per user.
	•	Turn into a web app using Flask or Streamlit.
	•	Add multiple rounds to improve accuracy.
	•	Explore more complex models like multi-armed bandits.
