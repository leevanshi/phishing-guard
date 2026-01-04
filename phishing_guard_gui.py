import tkinter as tk
from tkinter import messagebox

def calculate_risk(link):
    suspicious_words = [
        "login", "verify", "secure", "account",
        "update", "bank", "free", "click"
    ]

    score = 0

    for word in suspicious_words:
        if word in link.lower():
            score += 15

    if link.startswith("http://"):
        score += 20

    if len(link) > 75:
        score += 10

    return score


def check_link():
    link = entry.get().strip()

    if not link:
        messagebox.showwarning("Input Error", "Please enter a link")
        return

    risk = calculate_risk(link)

    if risk >= 50:
        result_label.config(
            text=f"🚨 HIGH RISK ({risk}%)\nLikely PHISHING",
            fg="#c0392b",   # strong red
            bg="#fdecea"
        )
    elif risk >= 30:
        result_label.config(
            text=f"⚠️ MEDIUM RISK ({risk}%)\nBe cautious",
            fg="#e67e22",   # orange
            bg="#fff4e6"
        )
    else:
        result_label.config(
            text=f"✅ LOW RISK ({risk}%)\nLooks safe",
            fg="#27ae60",   # green
            bg="#eafaf1"
        )

    entry.delete(0, tk.END)


# GUI Window
root = tk.Tk()
root.title("Phishing Guard")
root.geometry("420x300")
root.resizable(False, False)
root.configure(bg="white")   # IMPORTANT

tk.Label(
    root,
    text="🔐 Phishing Guard",
    font=("Segoe UI", 18, "bold"),
    bg="white"
).pack(pady=12)

tk.Label(
    root,
    text="Check suspicious links before clicking",
    font=("Segoe UI", 10),
    fg="gray",
    bg="white"
).pack()

tk.Label(
    root,
    text="Enter a link to check:",
    font=("Segoe UI", 11),
    bg="white"
).pack(pady=(15, 5))

entry = tk.Entry(root, width=48, font=("Segoe UI", 10))
entry.pack()

tk.Button(
    root,
    text="Check Link",
    font=("Segoe UI", 10, "bold"),
    width=15,
    command=check_link
).pack(pady=15)

result_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 11, "bold"),
    wraplength=380,
    justify="center",
    bg="white"      # IMPORTANT
)
result_label.pack(pady=10)

root.mainloop()
