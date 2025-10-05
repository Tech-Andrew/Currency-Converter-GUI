# ***💱 Currency Converter App***

A modern, real-time ***Python currency converter*** built with ***Tkinter***.  
Convert between ***170+ world currencies*** with live exchange rates powered by the **Open Exchange Rate API** — all wrapped in a clean, adaptive ***16:9 GUI interface.***

---

### **✨ Overview**

This app provides a fast, interactive way to convert currencies using live data.  
It features a polished Tkinter interface, smart caching for offline use, and dynamic styling that lets you change themes and background colors.

Designed to be lightweight yet full-featured, it’s ideal for finance learners, travelers, or anyone needing quick conversions on desktop 💻.

---

### **🧩 Features**

_🌍 Global Coverage_ — Supports over ***170 currencies*** (including crypto options like BTC).  
_⚙️ Adjustable Precision_ — Choose your preferred number of decimal places (0–6).  
_🎨 Customizable Theme_ — Pick your background color and adjust UI elements live.  
_📴 Offline Mode_ — Automatically uses cached exchange rates when offline.  
_💡 Real-Time Updates_ — Fetches fresh data from **Open Exchange Rate API**.  
_🪟 Modern GUI_ — A polished, responsive interface designed for 16:9 layouts.  
_🔁 Swap Button_ — Instantly flip between “From” and “To” currencies.  
_📊 Rate Info_ — Displays live rate and last updated time for transparency.  

---

### **🪄 How It Works**

1. Launch the app:
   ```bash
   python main.py
   ```
2. Choose the source and target currencies.  
3. Enter the amount to convert.  
4. Click **Convert** — and watch results appear instantly.  
5. Use **Settings** to change:
   - Decimal precision
   - Background color
   - Offline mode toggle  

🧠 Tip: Use the ***Swap*** button to reverse conversion direction with one click.

---

### **⚙️ Requirements**

- ***Python 3.9+***
- Internet connection (for live mode)

Install dependencies:
```bash
pip install pillow
```

(`tkinter`, `urllib`, and `json` are built into most Python installations.)

---

### **🧠 Tech Stack**

- ***Python*** – Core application logic  
- ***Tkinter + ttk*** – GUI rendering and widgets  
- ***urllib*** – Handles API requests  
- ***JSON*** – Parses live exchange rate data  
- ***Open Exchange Rate API*** – Provides reliable global rates  

---

### **📐 GUI Highlights**

- Clean 16:9 layout optimized for desktop
- “Accent.TButton” theme with custom hover effects
- Soft card-based panels for conversion and result sections
- Context-aware status bar showing current state (e.g. *Fetching rates…*)

---

### **📦 Code Structure**

```
main.py
│
├── CurrencyConverterApp (class)
│   ├── build_layout()       → Builds UI components
│   ├── convert()            → Performs conversion
│   ├── fetch_rates()        → Fetches/caches API rates
│   ├── apply_theme()        → Updates GUI colors dynamically
│   ├── open_settings()      → Handles settings menu logic
│   └── run()                → Starts Tkinter main loop
│
└── main()                   → App entry point
```

---

### **💾 Offline Mode**

When offline mode is enabled:
- Cached rates are used for conversions.
- No live API calls are made.
- App indicates “Using cached rates” in status bar.

---

### **🧑‍💻 Author**

Built with ❤️ by ***Tech-Andrew*** — merging aesthetics, usability, and performance to make currency conversion elegant and fun.

---

### **📸 Example Screenshot (optional)**

_(Add a screenshot of your GUI here for visual appeal)_

---

### **📜 License**

This project is open-source and free to modify for personal or educational use.
