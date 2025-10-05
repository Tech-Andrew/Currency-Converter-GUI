import json
import tkinter as tk
from typing import Dict, Optional
from tkinter import ttk, messagebox, colorchooser
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://open.er-api.com/v6/latest/{base}"

CURRENCIES = {
    'AED': 'United Arab Emirates Dirham',
    'AFN': 'Afghan Afghani',
    'ALL': 'Albanian Lek',
    'AMD': 'Armenian Dram',
    'ANG': 'Netherlands Antillean Guilder',
    'AOA': 'Angolan Kwanza',
    'ARS': 'Argentine Peso',
    'AUD': 'Australian Dollar',
    'AWG': 'Aruban Florin',
    'AZN': 'Azerbaijani Manat',
    'BAM': 'Bosnia-Herzegovina Convertible Mark',
    'BBD': 'Barbadian Dollar',
    'BDT': 'Bangladeshi Taka',
    'BGN': 'Bulgarian Lev',
    'BHD': 'Bahraini Dinar',
    'BIF': 'Burundian Franc',
    'BMD': 'Bermudan Dollar',
    'BND': 'Brunei Dollar',
    'BOB': 'Bolivian Boliviano',
    'BRL': 'Brazilian Real',
    'BSD': 'Bahamian Dollar',
    'BTC': 'Bitcoin',
    'BTN': 'Bhutanese Ngultrum',
    'BWP': 'Botswanan Pula',
    'BYN': 'Belarusian Ruble',
    'BZD': 'Belize Dollar',
    'CAD': 'Canadian Dollar',
    'CDF': 'Congolese Franc',
    'CHF': 'Swiss Franc',
    'CLF': 'Chilean Unit of Account (UF)',
    'CLP': 'Chilean Peso',
    'CNH': 'Chinese Yuan (Offshore)',
    'CNY': 'Chinese Yuan',
    'COP': 'Colombian Peso',
    'CRC': 'Costa Rican Colon',
    'CUC': 'Cuban Convertible Peso',
    'CUP': 'Cuban Peso',
    'CVE': 'Cape Verdean Escudo',
    'CZK': 'Czech Republic Koruna',
    'DJF': 'Djiboutian Franc',
    'DKK': 'Danish Krone',
    'DOP': 'Dominican Peso',
    'DZD': 'Algerian Dinar',
    'EGP': 'Egyptian Pound',
    'ERN': 'Eritrean Nakfa',
    'ETB': 'Ethiopian Birr',
    'EUR': 'Euro',
    'FJD': 'Fijian Dollar',
    'FKP': 'Falkland Islands Pound',
    'GBP': 'British Pound Sterling',
    'GEL': 'Georgian Lari',
    'GGP': 'Guernsey Pound',
    'GHS': 'Ghanaian Cedi',
    'GIP': 'Gibraltar Pound',
    'GMD': 'Gambian Dalasi',
    'GNF': 'Guinean Franc',
    'GTQ': 'Guatemalan Quetzal',
    'GYD': 'Guyanaese Dollar',
    'HKD': 'Hong Kong Dollar',
    'HNL': 'Honduran Lempira',
    'HRK': 'Croatian Kuna',
    'HTG': 'Haitian Gourde',
    'HUF': 'Hungarian Forint',
    'IDR': 'Indonesian Rupiah',
    'ILS': 'Israeli New Sheqel',
    'IMP': 'Manx pound',
    'INR': 'Indian Rupee',
    'IQD': 'Iraqi Dinar',
    'IRR': 'Iranian Rial',
    'ISK': 'Icelandic Krona',
    'JEP': 'Jersey Pound',
    'JMD': 'Jamaican Dollar',
    'JOD': 'Jordanian Dinar',
    'JPY': 'Japanese Yen',
    'KES': 'Kenyan Shilling',
    'KGS': 'Kyrgystani Som',
    'KHR': 'Cambodian Riel',
    'KMF': 'Comorian Franc',
    'KPW': 'North Korean Won',
    'KRW': 'South Korean Won',
    'KWD': 'Kuwaiti Dinar',
    'KYD': 'Cayman Islands Dollar',
    'KZT': 'Kazakhstani Tenge',
    'LAK': 'Laotian Kip',
    'LBP': 'Lebanese Pound',
    'LKR': 'Sri Lankan Rupee',
    'LRD': 'Liberian Dollar',
    'LSL': 'Lesotho Loti',
    'LYD': 'Libyan Dinar',
    'MAD': 'Moroccan Dirham',
    'MDL': 'Moldovan Leu',
    'MGA': 'Malagasy Ariary',
    'MKD': 'Macedonian Denar',
    'MMK': 'Myanma Kyat',
    'MNT': 'Mongolian Tugrik',
    'MOP': 'Macanese Pataca',
    'MRU': 'Mauritanian Ouguiya',
    'MUR': 'Mauritian Rupee',
    'MVR': 'Maldivian Rufiyaa',
    'MWK': 'Malawian Kwacha',
    'MXN': 'Mexican Peso',
    'MYR': 'Malaysian Ringgit',
    'MZN': 'Mozambican Metical',
    'NAD': 'Namibian Dollar',
    'NGN': 'Nigerian Naira',
    'NIO': 'Nicaraguan Cordoba',
    'NOK': 'Norwegian Krone',
    'NPR': 'Nepalese Rupee',
    'NZD': 'New Zealand Dollar',
    'OMR': 'Omani Rial',
    'PAB': 'Panamanian Balboa',
    'PEN': 'Peruvian Nuevo Sol',
    'PGK': 'Papua New Guinean Kina',
    'PHP': 'Philippine Peso',
    'PKR': 'Pakistani Rupee',
    'PLN': 'Polish Zloty',
    'PYG': 'Paraguayan Guarani',
    'QAR': 'Qatari Rial',
    'RON': 'Romanian Leu',
    'RSD': 'Serbian Dinar',
    'RUB': 'Russian Ruble',
    'RWF': 'Rwandan Franc',
    'SAR': 'Saudi Riyal',
    'SBD': 'Solomon Islands Dollar',
    'SCR': 'Seychellois Rupee',
    'SDG': 'Sudanese Pound',
    'SEK': 'Swedish Krona',
    'SGD': 'Singapore Dollar',
    'SHP': 'Saint Helena Pound',
    'SLE': 'Sierra Leonean Leone',
    'SLL': 'Sierra Leonean Leone (Old)',
    'SOS': 'Somali Shilling',
    'SRD': 'Surinamese Dollar',
    'SSP': 'South Sudanese Pound',
    'STD': 'Sao Tome and Principe Dobra (pre-2018)',
    'STN': 'Sao Tome and Principe Dobra',
    'SVC': 'Salvadoran Colon',
    'SYP': 'Syrian Pound',
    'SZL': 'Swazi Lilangeni',
    'THB': 'Thai Baht',
    'TJS': 'Tajikistani Somoni',
    'TMT': 'Turkmenistani Manat',
    'TND': 'Tunisian Dinar',
    'TOP': 'Tongan Pa\'anga',
    'TRY': 'Turkish Lira',
    'TTD': 'Trinidad and Tobago Dollar',
    'TWD': 'New Taiwan Dollar',
    'TZS': 'Tanzanian Shilling',
    'UAH': 'Ukrainian Hryvnia',
    'UGX': 'Ugandan Shilling',
    'USD': 'United States Dollar',
    'UYU': 'Uruguayan Peso',
    'UZS': 'Uzbekistan Som',
    'VEF': 'Venezuelan Bolivar Fuerte (Old)',
    'VES': 'Venezuelan Bolivar Soberano',
    'VND': 'Vietnamese Dong',
    'VUV': 'Vanuatu Vatu',
    'WST': 'Samoan Tala',
    'XAF': 'CFA Franc BEAC',
    'XAG': 'Silver Ounce',
    'XAU': 'Gold Ounce',
    'XCD': 'East Caribbean Dollar',
    'XCG': 'Caribbean Guilder',
    'XDR': 'Special Drawing Rights',
    'XOF': 'CFA Franc BCEAO',
    'XPD': 'Palladium Ounce',
    'XPF': 'CFP Franc',
    'XPT': 'Platinum Ounce',
    'YER': 'Yemeni Rial',
    'ZAR': 'South African Rand',
    'ZMW': 'Zambian Kwacha',
    'ZWG': 'Zimbabwean ZiG',
    'ZWL': 'Zimbabwean Dollar',
}


class CurrencyConverterApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("560x720")
        self.root.minsize(520, 640)

        self.accent_color = "#4f46e5"
        self.secondary_color = "#1f2937"
        self.muted_color = "#64748b"
        self.surface_color = "#ffffff"
        self.bg_color = "#f3f4f6"

        self.decimal_var = tk.IntVar(value=2)
        self.offline_var = tk.BooleanVar(value=False)
        self.amount_var = tk.StringVar(value="100")
        self.from_display_var = tk.StringVar()
        self.to_display_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Enter an amount to convert")
        self.rate_info_var = tk.StringVar(value="")
        self.status_var = tk.StringVar(value="Ready")

        self.cached_rates: Dict[str, Dict[str, float]] = {}
        self.last_updated: Dict[str, str] = {}

        self.code_to_display = {
            code: f"{code} - {name}"
            for code, name in sorted(CURRENCIES.items())
        }
        self.display_to_code = {
            display: code for code, display in self.code_to_display.items()
        }
        self.currency_choices = list(self.code_to_display.values())

        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except tk.TclError:
            pass
        self.style.configure(
            "Accent.TButton",
            font=("Segoe UI", 11, "bold"),
            padding=8,
        )
        self.style.map(
            "Accent.TButton",
            foreground=[("disabled", "#cbd5f5"), ("!disabled", "white")],
            background=[("active", "#4338ca"), ("pressed", "#3730a3"), ("!disabled", self.accent_color)],
        )
        self.style.configure("Card.TFrame", background=self.surface_color)

        self.settings_window: Optional[tk.Toplevel] = None

        self.build_layout()
        self.apply_theme()

    def build_layout(self) -> None:
        self.container = tk.Frame(self.root, bg=self.bg_color)
        self.container.pack(fill="both", expand=True, padx=24, pady=24)

        self.header = tk.Frame(self.container, bg=self.bg_color)
        self.header.pack(fill="x")
        self.title_label = tk.Label(
            self.header,
            text="Currency Converter",
            font=("Segoe UI", 26, "bold"),
            bg=self.bg_color,
            fg=self.secondary_color,
        )
        self.title_label.pack(anchor="w")
        self.subtitle_label = tk.Label(
            self.header,
            text="Convert between 170+ currencies with live exchange rates",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.muted_color,
        )
        self.subtitle_label.pack(anchor="w", pady=(6, 0))
        self.form_card = tk.Frame(
            self.container,
            bg=self.surface_color,
            highlightbackground="#e2e8f0",
            highlightcolor="#e2e8f0",
            highlightthickness=1,
            bd=0,
        )
        self.form_card.pack(fill="x", pady=(24, 18))
        self.form_card.grid_columnconfigure(0, weight=1)
        self.form_card.grid_columnconfigure(1, weight=1)

        tk.Label(
            self.form_card,
            text="From",
            font=("Segoe UI", 11, "bold"),
            bg=self.surface_color,
            fg=self.secondary_color,
        ).grid(row=0, column=0, sticky="w", padx=18, pady=(18, 4))
        tk.Label(
            self.form_card,
            text="To",
            font=("Segoe UI", 11, "bold"),
            bg=self.surface_color,
            fg=self.secondary_color,
        ).grid(row=0, column=1, sticky="w", padx=18, pady=(18, 4))

        self.from_combo = ttk.Combobox(
            self.form_card,
            values=self.currency_choices,
            state="readonly",
            textvariable=self.from_display_var,
            font=("Segoe UI", 11),
        )
        self.from_combo.grid(row=1, column=0, sticky="ew", padx=(18, 9))
        self.to_combo = ttk.Combobox(
            self.form_card,
            values=self.currency_choices,
            state="readonly",
            textvariable=self.to_display_var,
            font=("Segoe UI", 11),
        )
        self.to_combo.grid(row=1, column=1, sticky="ew", padx=(9, 18))

        swap_button = tk.Button(
            self.form_card,
            text="Swap",
            command=self.swap_currencies,
            bg="#e0e7ff",
            fg=self.secondary_color,
            activebackground="#c7d2fe",
            activeforeground=self.secondary_color,
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )
        swap_button.grid(row=2, column=0, columnspan=2, pady=(12, 4), ipadx=6)

        tk.Label(
            self.form_card,
            text="Amount",
            font=("Segoe UI", 11, "bold"),
            bg=self.surface_color,
            fg=self.secondary_color,
        ).grid(row=3, column=0, columnspan=2, sticky="w", padx=18, pady=(12, 4))

        self.amount_entry = ttk.Entry(
            self.form_card,
            textvariable=self.amount_var,
            font=("Segoe UI", 12),
            justify="center",
        )
        self.amount_entry.grid(row=4, column=0, columnspan=2, sticky="ew", padx=18)

        convert_button = ttk.Button(
            self.form_card,
            text="Convert",
            style="Accent.TButton",
            command=self.convert,
        )
        convert_button.grid(row=5, column=0, columnspan=2, sticky="ew", padx=18, pady=(18, 22))

        self.result_card = tk.Frame(
            self.container,
            bg=self.surface_color,
            highlightbackground="#e2e8f0",
            highlightcolor="#e2e8f0",
            highlightthickness=1,
            bd=0,
        )
        self.result_card.pack(fill="x", pady=(0, 18))

        tk.Label(
            self.result_card,
            text="Converted Amount",
            font=("Segoe UI", 13, "bold"),
            bg=self.surface_color,
            fg=self.secondary_color,
        ).pack(anchor="w", padx=20, pady=(18, 6))
        self.result_value_label = tk.Label(
            self.result_card,
            textvariable=self.result_var,
            font=("Segoe UI", 22, "bold"),
            bg=self.surface_color,
            fg=self.accent_color,
        )
        self.result_value_label.pack(anchor="w", padx=20)
        self.rate_info_label = tk.Label(
            self.result_card,
            textvariable=self.rate_info_var,
            font=("Segoe UI", 11),
            bg=self.surface_color,
            fg=self.muted_color,
        )
        self.rate_info_label.pack(anchor="w", padx=20, pady=(6, 18))

        self.button_bar = tk.Frame(self.container, bg=self.bg_color)
        self.button_bar.pack(fill="x", pady=(12, 18))

        settings_button = tk.Button(
            self.button_bar,
            text="Settings",
            command=self.open_settings,
            bg="#0ea5e9",
            fg="white",
            activebackground="#0284c7",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=16,
            pady=8,
            cursor="hand2",
        )
        settings_button.pack(side="right")

        self.status_label = tk.Label(
            self.container,
            textvariable=self.status_var,
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg=self.muted_color,
        )
        self.status_label.pack(fill="x", side="bottom")

        self.from_display_var.set(self.code_to_display.get("USD", self.currency_choices[0]))
        default_to_index = 1 if len(self.currency_choices) > 1 else 0
        self.to_display_var.set(self.code_to_display.get("INR", self.currency_choices[default_to_index]))

    def apply_theme(self) -> None:
        self.root.configure(bg=self.bg_color)
        self.container.configure(bg=self.bg_color)
        self.header.configure(bg=self.bg_color)
        self.title_label.configure(bg=self.bg_color, fg=self.secondary_color)
        self.subtitle_label.configure(bg=self.bg_color, fg=self.muted_color)
        self.button_bar.configure(bg=self.bg_color)
        self.status_label.configure(bg=self.bg_color, fg=self.muted_color)
        for widget in self.container.winfo_children():
            if isinstance(widget, tk.Frame) and widget not in (self.form_card, self.result_card, self.button_bar):
                widget.configure(bg=self.bg_color)
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label):
                        child.configure(bg=self.bg_color)
        for label in self.form_card.grid_slaves():
            if isinstance(label, tk.Label):
                label.configure(bg=self.surface_color, fg=self.secondary_color)
        self.result_card.configure(bg=self.surface_color)
        self.form_card.configure(bg=self.surface_color)
        self.result_value_label.configure(fg=self.accent_color)

    def update_status(self, message: str) -> None:
        self.status_var.set(message)
        self.status_label.update_idletasks()

    def swap_currencies(self) -> None:
        current_from = self.from_display_var.get()
        current_to = self.to_display_var.get()
        if not current_from or not current_to:
            return
        self.from_display_var.set(current_to)
        self.to_display_var.set(current_from)
        self.update_status("Currencies swapped")

    def convert(self) -> None:
        amount_text = self.amount_var.get().strip()
        if not amount_text:
            messagebox.showinfo("Missing amount", "Please enter an amount to convert.")
            self.amount_entry.focus_set()
            return
        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Invalid amount", "Please enter a numeric amount.")
            self.amount_entry.focus_set()
            return
        if amount < 0:
            messagebox.showerror("Invalid amount", "Amount cannot be negative.")
            self.amount_entry.focus_set()
            return

        from_display = self.from_display_var.get()
        to_display = self.to_display_var.get()
        if not from_display or not to_display:
            messagebox.showinfo("Missing selection", "Please choose both currencies.")
            return

        from_code = self.display_to_code[from_display]
        to_code = self.display_to_code[to_display]

        if from_code == to_code:
            decimals = max(0, min(self.decimal_var.get(), 6))
            self.result_var.set(f"{amount:,.{decimals}f} {to_code}")
            self.rate_info_var.set("Same currency selected")
            self.update_status("No conversion needed")
            return

        rates = self.fetch_rates(from_code)
        if not rates:
            mode = "offline" if self.offline_var.get() else "online"
            messagebox.showwarning(
                "Rates unavailable",
                f"Could not retrieve {mode} exchange rates for {from_code}.",
            )
            self.update_status("Conversion failed")
            return

        rate = rates.get(to_code)
        if rate is None:
            messagebox.showwarning(
                "Unsupported currency",
                f"No rate found for {from_code} to {to_code}.",
            )
            self.update_status("Missing exchange rate")
            return

        decimals = max(0, min(self.decimal_var.get(), 6))
        converted = amount * rate
        self.result_var.set(f"{converted:,.{decimals}f} {to_code}")
        self.rate_info_var.set(f"1 {from_code} = {rate:.6f} {to_code}")

        last_sync = self.last_updated.get(from_code)
        if last_sync:
            self.update_status(f"Rates updated {last_sync}")
        else:
            self.update_status("Using cached rates")

    def fetch_rates(self, base_currency: str) -> Optional[Dict[str, float]]:
        cached = self.cached_rates.get(base_currency)
        if cached is not None:
            return cached
        if self.offline_var.get():
            return None

        self.update_status(f"Fetching live rates for {base_currency}...")
        url = API_URL.format(base=base_currency)
        try:
            request = Request(url, headers={"User-Agent": "CurrencyConverterApp/1.0"})
            with urlopen(request, timeout=10) as response:
                payload = json.load(response)
        except (URLError, HTTPError, TimeoutError) as exc:
            print(f"Failed to fetch rates: {exc}")
            return None

        if payload.get("result") != "success":
            print(f"Unexpected API response: {payload}")
            return None

        rates = payload.get("rates")
        if not rates:
            return None

        self.cached_rates[base_currency] = rates
        self.last_updated[base_currency] = payload.get("time_last_update_utc", "recently")
        return rates

    def open_settings(self) -> None:
        if self.settings_window and tk.Toplevel.winfo_exists(self.settings_window):
            self.settings_window.focus_set()
            return

        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.title("Settings")
        self.settings_window.geometry("320x280")
        self.settings_window.resizable(False, False)
        self.settings_window.configure(bg=self.surface_color)
        self.settings_window.transient(self.root)
        self.settings_window.grab_set()

        tk.Label(
            self.settings_window,
            text="Preferences",
            font=("Segoe UI", 14, "bold"),
            bg=self.surface_color,
            fg=self.secondary_color,
        ).pack(anchor="w", padx=20, pady=(16, 8))

        options_frame = tk.Frame(self.settings_window, bg=self.surface_color)
        options_frame.pack(fill="both", expand=True, padx=20)

        tk.Label(
            options_frame,
            text="Decimal places",
            font=("Segoe UI", 11),
            bg=self.surface_color,
            fg=self.secondary_color,
        ).grid(row=0, column=0, sticky="w")
        decimal_spin = tk.Spinbox(
            options_frame,
            from_=0,
            to=6,
            textvariable=self.decimal_var,
            width=5,
            font=("Segoe UI", 11),
            justify="center",
        )
        decimal_spin.grid(row=0, column=1, sticky="e")

        tk.Label(
            options_frame,
            text="Background color",
            font=("Segoe UI", 11),
            bg=self.surface_color,
            fg=self.secondary_color,
        ).grid(row=1, column=0, sticky="w", pady=(16, 0))

        color_preview = tk.Label(
            options_frame,
            bg=self.bg_color,
            width=12,
            relief="ridge",
            bd=1,
        )
        color_preview.grid(row=1, column=1, sticky="e", pady=(16, 0))

        def choose_color() -> None:
            rgb, hex_value = colorchooser.askcolor(
                initialcolor=self.bg_color,
                title="Select background color",
            )
            if hex_value:
                self.bg_color = hex_value
                color_preview.configure(bg=self.bg_color)
                self.apply_theme()

        tk.Button(
            options_frame,
            text="Pick color",
            command=choose_color,
            bg="#f97316",
            fg="white",
            activebackground="#ea580c",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        offline_check = tk.Checkbutton(
            options_frame,
            text="Offline mode (use cached rates only)",
            variable=self.offline_var,
            onvalue=True,
            offvalue=False,
            bg=self.surface_color,
            fg=self.secondary_color,
            selectcolor=self.surface_color,
            activebackground=self.surface_color,
            anchor="w",
        )
        offline_check.grid(row=3, column=0, columnspan=2, sticky="w", pady=(18, 0))

        options_frame.grid_columnconfigure(0, weight=1)
        options_frame.grid_columnconfigure(1, weight=1)

        def close_settings() -> None:
            self.settings_window.destroy()
            self.settings_window = None

        action_bar = tk.Frame(self.settings_window, bg=self.surface_color)
        action_bar.pack(fill="x", pady=(12, 16), padx=20)
        tk.Button(
            action_bar,
            text="Done",
            command=close_settings,
            bg=self.accent_color,
            fg="white",
            activebackground="#4338ca",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=12,
            pady=6,
            cursor="hand2",
        ).pack(side="right")

        self.settings_window.protocol("WM_DELETE_WINDOW", close_settings)

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    app.run()


if __name__ == "__main__":
    main()
