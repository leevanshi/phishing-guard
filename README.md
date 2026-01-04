# 🔐 Phishing Guard

A Python-based desktop application that detects potentially malicious phishing links using risk-based analysis.  
The tool features a clean GUI and is packaged as a Windows executable for easy use.

---

## 🚀 Features
- Detects phishing links using keyword & heuristic analysis
- Risk scoring system (Low / Medium / High)
- User-friendly GUI built with Tkinter
- Converts Python app into a standalone Windows `.exe`
- Custom application icon and polished UI

---

## 🖥️ Screenshots
![Phishing Guard App](screenshots/app.png)

---

## 🧠 How It Works
The application assigns a risk score based on:
- Presence of suspicious keywords (login, verify, bank, free, etc.)
- Use of unsecured HTTP protocol
- Abnormally long URLs

Based on the score, the link is classified as:
- ✅ Low Risk
- ⚠️ Medium Risk
- 🚨 High Risk (Likely Phishing)

---

## 🛠️ Technologies Used
- Python
- Tkinter (GUI)
- PyInstaller (EXE packaging)

---

## 📦 Installation & Usage

### Option 1: Run as EXE (Recommended)
1. Download `phishing_guard_gui.exe` from the `dist` folder
2. Double-click to launch
3. Enter a URL and click **Check Link**

### Option 2: Run from Source
```bash
python phishing_guard_gui.py


## 👩‍💻 Author
**Leevanshi Sharma**  
Second-year CSE student | Cybersecurity Enthusiast

