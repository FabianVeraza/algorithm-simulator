# # 🎯 Interest Learning System (Console Simulation)

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
   git clone https://github.com/your-user/your-repo.git
   cd your-repo
