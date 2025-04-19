import tkinter as tk
import webbrowser
import random

# Mood to music mapping
mood_music = {
    "Happy": [
        "https://youtu.be/cBVGlBWQzuc?si=cc2RPd-y77tLo7of",
        "https://youtu.be/ZbZSe6N_BXs?si=7aNTVE8Vmk5cdIw4",
        "https://youtu.be/hT_nvWreIhg?si=zlB4jMTqPX2eDlOd",
        "https://youtu.be/PIh2xe4jnpk?si=T_cmWvVWgjSik5kb",
        "https://youtu.be/jGflUbPQfW8?si=OCXFhf4a9GxNsPqf"
    ],
    "Sad": [
        "https://youtu.be/8ofCZObsnOo?si=5DwrkpTbs75IP2zQ",
        "https://youtu.be/mtf7hC17IBM?si=Lcuh0drSXaYZmfBx",
        "https://youtu.be/Mhj15W23IjA?si=eBx8CqSW-Baay9ZK",
        "https://youtu.be/BiQIc7fG9pA?si=nQLhG8iGQXO6_9iZ",
        "https://youtu.be/ShZ978fBl6Y?si=8OWAooKBArcmOqg-"
    ],
    "Romantic": [
        "https://youtu.be/450p7goxZqg?si=1j4VmcljnIxdvCGP",
        "https://youtu.be/0yW7w8F2TVA?si=jb9EWFEBLK-r8S7w",
        "https://youtu.be/tt2k8PGm-TI?si=0QYhakqyXH_NrvTO",
        "https://youtu.be/GCdwKhTtNNw?si=Mdjq0B9wcfJSPNPA",
        "https://youtu.be/NdYWuo9OFAw?si=JsJDIW3ktNiQFPM_"
    ],
    "Relaxed": [
        "https://youtu.be/63bdUwIjEZQ?si=ONqYYv4qX0paL_pS",
        "https://youtu.be/WI9s4R2fZqg?si=Q7rN0AKuNhnyUlrp",
        "https://youtu.be/P58IumZBGng?si=Zw2WG3Q-zuYz_Ja2",
        "https://youtu.be/08ahRZzDfww?si=w1xW-vPpiGHzHAMT",
        "https://youtu.be/l3mGWr9tQ3w?si=8Ybbp0w-RGPHb7ma"
    ],
    "Energetic": [
        "https://youtu.be/ZcmoBlURJB4?si=OFJ4Cdsydg4n-2U4",
        "https://youtu.be/whwe0KD_rGw?si=FQwtZaHAKNJOP5nM",
        "https://youtu.be/4X4uckVyk9o?si=FgXjTxKUi8HTLo2l",
        "https://youtu.be/dW2MmuA1nI4?si=DKbE5khUSuz8Nt2f",
        "https://youtu.be/bKDdT_nyP54?si=a8gIn8x2gVSLe_RP"
    ]
}

# Function to recommend music
def recommend_music():
    mood = mood_var.get()
    if mood in mood_music:
        song = random.choice(mood_music[mood])
        webbrowser.open(song)
        result_label.config(text=f"Enjoy your {mood.lower()} vibes! 🎵")
    else:
        result_label.config(text="Please select a valid mood.")

# GUI setup
root = tk.Tk()
root.title("Mood-Based Music Recommender")
root.geometry("400x300")
root.configure(bg="#f0f0f0")


tk.Label(root, text="How are you feeling today?", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=20)


mood_var = tk.StringVar()
mood_var.set("Happy")  
dropdown = tk.OptionMenu(root, mood_var, *mood_music.keys())
dropdown.config(width=15, font=("Helvetica", 12))
dropdown.pack(pady=10)


tk.Button(root, text="Play a Song", font=("Helvetica", 12), bg="#4CAF50", fg="white",
          command=recommend_music).pack(pady=20)


result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
result_label.pack()


root.mainloop()
