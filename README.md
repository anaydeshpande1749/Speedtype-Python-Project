# ⌨️ Typo.in — Typing Speed Tester (Python + Tkinter)

A clean, desktop typing-speed tester built with **Python Tkinter**. Choose a difficulty, type the given prompt, and get **real-time WPM** plus **accuracy** with green/red character highlights. Results are shown in a dialog and appended to a simple **Leaderboard**—great for quick practice sessions or friendly competitions.

---

## ✨ Features
- **Three difficulty levels**: Low / Medium / Hard
- **Real-time WPM** calculation while you type
- **Live accuracy feedback**: green (correct) & red (wrong) character highlights
- **Result dialog** with **WPM** and **Accuracy %**
- **In-app Leaderboard** (session-only)
- **Restart** button to reset and try again
- Dark theme UI

---

## 🧩 How it works (quick overview)
1. Enter your **name**, select a **difficulty**, and start typing the shown sentence.
2. WPM updates live as you type; characters turn **green/red** for correct/incorrect.
3. When you finish the sentence **including the final period (`.`)**, a result dialog pops up with your **WPM** and **Accuracy**, and your score is added to the **Leaderboard**.
4. Click **Restart** to reset the test and try again.

> _Tip:_ Make sure you type the full prompt including the last `.` to trigger the results.

---

## 🖥️ Tech Stack
- **Language:** Python (3.8+ recommended)
- **GUI:** Tkinter (standard library)

---

## 🚀 Run Locally

### 1) Clone
```bash
git clone https://github.com/<your-username>/typing-speed-tester.git
cd typing-speed-tester
