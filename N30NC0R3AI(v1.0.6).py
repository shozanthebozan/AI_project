import base64
import datetime
import html
import json
import math
import os
import random
import re
import threading
import tkinter as tk
import urllib.parse
import urllib.request
from tkinter import filedialog, scrolledtext, messagebox, simpledialog

# ============================================================================
# PERSISTENT STORAGE (Safe Base64 Encoding)
# ============================================================================
# NEON_HISTORY_START
NEON_HISTORY_B64 = 'eyJjaGF0cyI6IHsiMSI6IHsibmFtZSI6ICJOZXcgU2Vzc2lvbiIsICJ0aW1lIjogIjIwMjYtMDYtMjdUMTI6MTU6MTYuNTMxOTIwIn19LCAibWVzc2FnZXMiOiB7IjEiOiBbeyJyb2xlIjogInVzZXIiLCAidGV4dCI6ICJoaSJ9LCB7InJvbGUiOiAiYm90IiwgInRleHQiOiAiWC1DMFIzIE9NTklTIFBSRVBBUkVEOiBHbG9iYWwgU3ludGhlc2lzIEVuZ2luZSBBY3RpdmUuIn0sIHsicm9sZSI6ICJ1c2VyIiwgInRleHQiOiAiaGVsbG8gbXkgbmFtZSBpcyBhbnNoIn0sIHsicm9sZSI6ICJib3QiLCAidGV4dCI6ICJJJ20gbm90IHF1aXRlIHN1cmUgYWJvdXQgdGhhdCBvbmUuIENvdWxkIHlvdSBnaXZlIG1lIG1vcmUgZGV0YWlscyBvciBjaGVjayB0aGUgc3BlbGxpbmc/In0sIHsicm9sZSI6ICJ1c2VyIiwgInRleHQiOiAiaGVsbG8ifSwgeyJyb2xlIjogImJvdCIsICJ0ZXh0IjogIkhleSEgSSdtIE5FT04uIEknbSBvbmxpbmUgYW5kIHJlYWR5IHRvIGhlbHAuIFdoYXQncyBvbiB5b3VyIG1pbmQ/In0sIHsicm9sZSI6ICJ1c2VyIiwgInRleHQiOiAibXkgbmFtZSBpcyBhbnNoIn0sIHsicm9sZSI6ICJib3QiLCAidGV4dCI6ICJJJ20gbm90IHF1aXRlIHN1cmUgYWJvdXQgdGhhdCBvbmUuIENvdWxkIHlvdSBnaXZlIG1lIG1vcmUgZGV0YWlscyBvciBjaGVjayB0aGUgc3BlbGxpbmc/In0sIHsicm9sZSI6ICJ1c2VyIiwgInRleHQiOiAiaGkgbXkgbmFtZSBpcyBhbnNoIn0sIHsicm9sZSI6ICJib3QiLCAidGV4dCI6ICJOaWNlIHRvIG1lZXQgeW91LCBBbnNoISBJJ20gTkVPTiwgYnkgdGhlIHdheS4gSG93IGNhbiBJIGhlbHAgeW91IHRvZGF5PyJ9LCB7InJvbGUiOiAidXNlciIsICJ0ZXh0IjogImNhbiB5b3UgZmluZCBpbmZvIG9uIHRoZSBtaSAxMSB1bHRyYT8ifSwgeyJyb2xlIjogImJvdCIsICJ0ZXh0IjogIkknbSBub3QgcXVpdGUgc3VyZSBhYm91dCB0aGF0IG9uZS4gQ291bGQgeW91IGdpdmUgbWUgbW9yZSBkZXRhaWxzIG9yIGNoZWNrIHRoZSBzcGVsbGluZz8ifSwgeyJyb2xlIjogInVzZXIiLCAidGV4dCI6ICJoaSBteSBuYW1lIGlzIGFuc2gifSwgeyJyb2xlIjogImJvdCIsICJ0ZXh0IjogIk5pY2UgdG8gbWVldCB5b3UsIEFuc2ghIEknbSBORU9OLCBieSB0aGUgd2F5LiBIb3cgY2FuIEkgaGVscCB5b3UgdG9kYXk/In0sIHsicm9sZSI6ICJ1c2VyIiwgInRleHQiOiAiZ2l2ZSBtZSBpbmZvIG9uIHRoZSBtaSAxMSJ9LCB7InJvbGUiOiAiYm90IiwgInRleHQiOiAiSSdtIG5vdCBxdWl0ZSBzdXJlIGFib3V0IHRoYXQgb25lLiBDb3VsZCB5b3UgZ2l2ZSBtZSBtb3JlIGRldGFpbHMgb3IgY2hlY2sgdGhlIHNwZWxsaW5nPyJ9LCB7InJvbGUiOiAidXNlciIsICJ0ZXh0IjogIm1pIDExIn0sIHsicm9sZSI6ICJib3QiLCAidGV4dCI6ICJIZXJlIGlzIHRoZSBmYWN0dWFsIHN1bW1hcnkgZm9yIE1JIDExOlxuXG5UaGUgWGlhb21pIDExIGlzIGFuIEFuZHJvaWQtYmFzZWQgaGlnaC1lbmQgc21hcnRwaG9uZSBkZXZlbG9wZWQgYnkgWGlhb21pIEluYy4gSXQgd2FzIGludHJvZHVjZWQgYXMgdGhlIHN1Y2Nlc3NvciB0byB0aGUgWGlhb21pIDEwIHNlcmllcyBhbmQgc2VydmVzIGFzIHRoZSBmbGFnc2hpcCBtb2RlbCBpbiB0aGUgWGlhb21pIDExIGxpbmV1cC4gVGhlIGRldmljZSBmZWF0dXJlcyB1cGdyYWRlZCBoYXJkd2FyZSBzcGVjaWZpY2F0aW9ucywgaW5jbHVkaW5nIGEgaGlnaC1yZXNvbHV0aW9uIGRpc3BsYXkgYW5kIGltcHJvdmVkIGNhbWVyYSBzeXN0ZW0sIGFpbWVkIGF0IGNvbXBldGluZyB3aXRoIG90aGVyIHByZW1pdW0gc21hcnRwaG9uZXMuIFRoZSBYaWFvbWkgMTEgd2FzIGZpcnN0IHVudmVpbGVkIGluIENoaW5hIGluIERlY2VtYmVyIDIwMjAgYW5kIGxhdW5jaGVkIGdsb2JhbGx5IG9uIDggRmVicnVhcnkgMjAyMS4ifV19LCAibmV4dF9pZCI6IDJ9'
# NEON_HISTORY_END

# NEON_SETTINGS_START
NEON_SETTINGS_B64 = 'eyJ0aGVtZSI6ICJOZW9uIE9yYW5nZSIsICJpbnRlbGxpZ2VuY2UiOiAiRGVlcCIsICJyZXNwb25zZV9zdHlsZSI6ICJEZXRhaWxlZCIsICJzcGVlZCI6ICJEZWVwIiwgInJlc3VsdF9jb3VudCI6IDIwLCAiZm9udF9zaXplIjogMTIsICJ3ZWJfc2VhcmNoIjogdHJ1ZSwgIndpa2lwZWRpYSI6IHRydWUsICJsaXZlX3NlYXJjaCI6IHRydWUsICJnaXRodWJfc2VhcmNoIjogZmFsc2UsICJyZWRkaXRfc2VhcmNoIjogZmFsc2UsICJuZXdzX3NlYXJjaCI6IGZhbHNlLCAiYWRfZmlsdGVyIjogdHJ1ZSwgInNhdmVfbWVtb3J5IjogdHJ1ZSwgInNhdmVfbG9jYWxseIjogZmFsc2UsICJzYXZlX3BhdGgiOiAiIn0='
# NEON_SETTINGS_END

def _decode_store(b64_str):
    try: return json.loads(base64.b64decode(b64_str).decode('utf-8'))
    except: return {}

NEON_HISTORY = _decode_store(NEON_HISTORY_B64)
NEON_SETTINGS = _decode_store(NEON_SETTINGS_B64)

try:
    from PIL import Image, ImageTk
    HAS_PIL = True
except:
    HAS_PIL = False

# ============================================================================
# LIVE DATA COLLECTOR
# ============================================================================
class LiveDataCollector:
    def __init__(self, settings=None):
        self.settings = settings or {}
        self.user_agents = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36']
    
    def _fetch(self, url, timeout=10):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': random.choice(self.user_agents)})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read().decode('utf-8', errors='ignore')
        except: return ""

    def get_weather(self, city):
        key = self.settings.get("weather_api_key")
        if not key: return "No weather API key found."
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&appid={key}&units=metric"
            data = json.loads(self._fetch(url))
            return f"🌡️ {city.title()}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
        except: return "Couldn't fetch weather."

# ============================================================================
# APEX-OMNIS BRAIN V16: HYPER-LOGIC & KNOWLEDGE
# ============================================================================

class ThinkingBrain:
    """
    V16 APEX-OMNIS: The ultimate logic engine.
    Combines common knowledge, deep research, and intuitive reasoning.
    """
    def __init__(self, settings=None):
        self.settings = settings or {}
        self.live = LiveDataCollector(settings)
        self.last_subject = ""
        self.name = "NEON"
        self.stop_words = {"a","an","the","what","where","who","is","are","how","to","best","good","find","get","nearby","in","of","at","for","some","any"}
        
        # INSTANT KNOWLEDGE BASE
        self.common_kb = {
            "gravity": "Gravity pulls everything toward the center of the Earth. It's why things fall and why we stay on the ground.",
            "sky blue": "Sunlight scatters through the atmosphere, and blue light waves scatter more, making the sky look blue.",
            "honey": "Honey is amazing—it's the only food that basically never expires. Edible honey was found in 3,000-year-old Egyptian tombs!",
            "banana": "Fun fact: Bananas are technically berries, and they grow on huge herbs, not trees.",
            "duck": "Ducks are water birds. Males are 'drakes' and females are 'hens'.",
            "capital of france": "Paris is the capital of France.",
            "capital of australia": "Canberra is the capital of Australia.",
            "boiling water": "Water boils at 100°C or 212°F.",
            "photosynthesis": "That's how plants turn sunlight and water into energy and oxygen."
        }

    def update_settings(self, settings):
        self.settings = settings
        self.live.settings = settings

    @staticmethod
    def _clean(text):
        text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
        return re.sub(r'\s+', ' ', text).strip()

    def _fuzzy_subject(self, q):
        tokens = [w for w in re.findall(r'\b\w+\b', q.lower()) if w not in self.stop_words]
        return " ".join(tokens) if tokens else q

    def _deep_harvest(self, html_content):
        results = []
        blocks = re.findall(r'<div class="(?:result__body|links_main|web-result|nr-n-result|result)">.*?</div>\s*</div>', html_content, re.DOTALL)
        if not blocks: blocks = re.findall(r'<(?:div|li|p)[^>]*>(.*?)</(?:div|li|p)>', html_content, re.DOTALL)
        
        for b in blocks:
            t_m = re.search(r'<a[^>]+class="[^"]*(?:title|result__a|links_main__ad)[^"]*"[^>]*>(.*?)</a>', b, re.DOTALL)
            s_m = re.search(r'class="[^"]*(?:snippet|result__snippet|links_main__snippet)[^"]*"[^>]*>(.*?)</a>|</div>', b, re.DOTALL)
            if t_m and s_m:
                t, s = self._clean(t_m.group(1)), self._clean(s_m.group(1))
                if len(s) < 12: continue
                ph = re.search(r'(\+?[0-9][0-9\-\(\)\. ]{8,15})', s)
                ad = re.search(r'(\d+ [A-Za-z0-9\. ]+ (?:St|Rd|Ave|Way|Pde|Cct|Lane|Dr|Pl|Ct|Cl|Gr|Sq|Hwy|Highway|Road|Street|Avenue|Boulevard|Blvd))', s, re.IGNORECASE)
                results.append({"title": t, "snippet": s, "phone": ph.group(0) if ph else None, "address": ad.group(0) if ad else None})
        return results

    def respond(self, query):
        q_low = query.lower().strip()
        
        # 1. CONVERSATIONAL LOGIC (Common Sense & Identity)
        # Handle Name Introductions & "What's yours?"
        name_pattern = re.search(r"\b(?:my name is|i'm|i am|call me)\s+([a-zA-Z]+)", q_low)
        asking_name = any(x in q_low for x in ["your name", "who are you", "whats yours", "what is yours"])
        
        if name_pattern or asking_name:
            greeting = ""
            if name_pattern:
                user_name = name_pattern.group(1).title()
                greeting = f"Nice to meet you, {user_name}! "
            
            if asking_name:
                return greeting + f"I'm {self.name}. What's up?"
            elif name_pattern:
                return greeting + f"I'm {self.name}, by the way. How can I help you today?"

        # Standard Greetings
        if q_low in ["hi", "hello", "hey", "yo", "sup"]:
            return f"Hey! I'm {self.name}. What's on your mind?"

        # Small Talk
        if any(x in q_low for x in ["how are you", "hows it going", "how you doing"]):
            return "I'm doing great! Just sitting here in the cloud, ready to help. How are things with you?"

        # Fact Trigger
        if any(x in q_low for x in ["tell me a fact", "give me a fact", "random fact"]):
            fact_key = random.choice(list(self.common_kb.keys()))
            return f"Did you know? {self.common_kb[fact_key]}"

        if q_low in ["time", "date"]: 
            return f"It's {datetime.datetime.now().strftime('%I:%M %p on %A, %B %d')}."
        
        # 2. COMMON KNOWLEDGE
        for key, val in self.common_kb.items():
            # Check for specific mention or "what is [key]"
            if key in q_low and (len(q_low.split()) < 5 or any(x in q_low for x in ["what is", "tell me about"])):
                return f"I know about that! {val}"

        is_fact_query = any(x in q_low for x in ["what is", "who is", "who was", "where is", "define", "history of", "how does"])

        # 3. BRAIN SYNTHESIS
        subject = self._fuzzy_subject(query)
        if len(subject) > 2: self.last_subject = subject
        
        # Logic: Location/Commerce expansion
        search_list = [query, subject]
        if any(k in q_low for k in ["shop", "grocer", "buy", "eat", "restaurant", "store", "cafe", "location"]):
            search_list.append(f"{subject} location address contact hours")
        
        aggregated = []
        seen = set()
        for term in search_list[:2]:
            raw = self.live._fetch(f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(term)}")
            scraped = self._deep_harvest(raw)
            for item in scraped:
                if item["title"].lower() not in seen:
                    aggregated.append(item); seen.add(item["title"].lower())

        # Scoring
        keywords = set(re.findall(r'\b\w{3,}\b', query.lower()))
        for item in aggregated:
            score = 0
            text = (item["title"] + " " + item["snippet"]).lower()
            for kw in keywords:
                if kw in text: score += 30
            
            if is_fact_query:
                # Prioritize longer explanations for facts
                score += min(len(item["snippet"]) // 10, 40)
            else:
                if item["address"]: score += 50
                if item["phone"]: score += 30
            item["_score"] = score

        aggregated.sort(key=lambda x: x["_score"], reverse=True)
        top = [x for x in aggregated if x["_score"] > 0]

        # 4. FINAL HUMAN RESPONSE
        if not top:
            # More aggressive Wikipedia fallback for factual queries
            if len(self.last_subject) > 2:
                wiki = self.live._fetch(f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(self.last_subject.replace(' ', '_'))}")
                try:
                    js = json.loads(wiki)
                    if js.get("extract"): return f"Here is the factual summary for {self.last_subject.upper()}:\n\n{js['extract']}"
                except: pass
            return "I'm not quite sure about that one. Could you give me more details or check the spelling?"

        report = f"Alright, here's what I synthesized for {self.last_subject.upper()}:\n"
        entities = [i for i in top if i["address"] or i["phone"] or any(k in i["title"].lower() for k in ["shop","store","market","grocer","restaurant"])]
        general = [i for i in top if i not in entities]

        if entities:
            report += "\n📍 Best spots and contact info found:\n"
            for e in entities[:12]:
                ad = f" | 🏠 {e['address']}" if e["address"] else ""
                ph = f" | 📞 {e['phone']}" if e["phone"] else ""
                report += f"• **{e['title']}**{ad}{ph}\n  {e['snippet']}\n"
            report += f"\n🗺️ View on **[Google Maps](https://www.google.com/maps/search/{urllib.parse.quote(query)})**\n"

        if general:
            report += "\n🔍 Other useful info:\n"
            for g in general[:8]: report += f"• {g['snippet']}\n"

        # Math Logic
        if re.search(r'[\d\+\-\*\/\(\)\^]', query) and any(c in query for c in "+-*/"):
            try:
                math_val = eval(re.sub(r'[^0-9\+\-\*\/\(\)\.\%\s\^a-zA-Z]', '', query.replace("^", "**")), {'__builtins__': None}, {k: getattr(math, k) for k in dir(math) if not k.startswith('_')})
                report = f"Calculated result: **{math_val}**\n\n" + report
            except: pass

        return report.strip()

# ============================================================================
# INFRASTRUCTURE (Persistent Memory & UI)
# ============================================================================

class MemoryDatabase:
    _storage = None
    def __init__(self, settings=None):
        self.settings = settings or {}
        if MemoryDatabase._storage is None:
            if self.settings.get("save_locally") and self.settings.get("save_path") and os.path.exists(self.settings["save_path"]):
                try:
                    with open(self.settings["save_path"], "r") as f: MemoryDatabase._storage = json.load(f)
                except: pass
            if MemoryDatabase._storage is None:
                MemoryDatabase._storage = {"chats": {int(k): v for k, v in NEON_HISTORY.get("chats", {}).items()}, "messages": {int(k): v for k, v in NEON_HISTORY.get("messages", {}).items()}, "next_id": NEON_HISTORY.get("next_id", 1)}

    def create_chat(self, name):
        cid = self._storage["next_id"]; self._storage["next_id"] += 1
        self._storage["chats"][cid] = {"name": name, "time": datetime.datetime.now().isoformat()}
        self._storage["messages"][cid] = []; self._save(); return cid

    def get_or_create_chat(self):
        if self._storage["chats"]: return sorted(self._storage["chats"].keys())[0]
        return self.create_chat("New Session")

    def add_msg(self, cid, role, text):
        if cid in self._storage["messages"]: 
            self._storage["messages"][cid].append({"role": role, "text": text})
            if self.settings.get("save_memory", True): self._save()

    def get_history(self, cid): return self._storage["messages"].get(cid, [])
    def get_chats(self): return sorted(self._storage["chats"].items())
    def clear_all(self): self._storage = {"chats": {}, "messages": {}, "next_id": 1}; return self.create_chat("New Session")

    def _save(self):
        if self.settings.get("save_locally") and self.settings.get("save_path"):
            try:
                with open(self.settings["save_path"], "w") as f: json.dump(self._storage, f, indent=4)
                return
            except: pass
        try:
            path = os.path.abspath(__file__)
            with open(path, "r") as f: source = f.read()
            b64 = base64.b64encode(json.dumps(self._storage).encode('utf-8')).decode('utf-8')
            source = re.sub(r"# NEON_HISTORY_START\nNEON_HISTORY_B64 = .*?\n# NEON_HISTORY_END", f"# NEON_HISTORY_START\nNEON_HISTORY_B64 = '{b64}'\n# NEON_HISTORY_END", source, flags=re.DOTALL)
            with open(path, "w") as f: f.write(source)
        except: pass

class SettingsStore:
    def __init__(self): self.data = NEON_SETTINGS
    def save(self):
        try:
            path = os.path.abspath(__file__)
            with open(path, "r") as f: source = f.read()
            b64 = base64.b64encode(json.dumps(self.data).encode('utf-8')).decode('utf-8')
            source = re.sub(r"# NEON_SETTINGS_START\nNEON_SETTINGS_B64 = .*?\n# NEON_SETTINGS_END", f"# NEON_SETTINGS_START\nNEON_SETTINGS_B64 = '{b64}'\n# NEON_SETTINGS_END", source, flags=re.DOTALL)
            with open(path, "w") as f: f.write(source)
        except: pass

class NeonUI:
    themes = {
        "Neon Orange": {"bg": "#000000", "panel": "#0A0A0A", "field": "#111111", "accent": "#FF5F00", "bot": "#00F0FF", "text": "#FFFFFF", "muted": "#444444"},
        "Neon Pink": {"bg": "#000000", "panel": "#0A0A0A", "field": "#111111", "accent": "#FF007F", "bot": "#BC13FE", "text": "#FFFFFF", "muted": "#444444"},
        "Neon Green": {"bg": "#000000", "panel": "#030803", "field": "#061206", "accent": "#39FF14", "bot": "#00FFCC", "text": "#E8FFE8", "muted": "#1A4D1A"},
        "Neon Blue": {"bg": "#000000", "panel": "#00050f", "field": "#000c1f", "accent": "#00BFFF", "bot": "#00FFFF", "text": "#E0F7FF", "muted": "#003366"},
        "Neon Red": {"bg": "#000000", "panel": "#0f0000", "field": "#1f0000", "accent": "#FF003F", "bot": "#FF6600", "text": "#FFE0E0", "muted": "#660000"},
        "Soft Night (Green)": {"bg": "#121212", "panel": "#1E1E1E", "field": "#252525", "accent": "#81C784", "bot": "#64B5F6", "text": "#E0E0E0", "muted": "#424242"},
        "Soft Night (Blue)": {"bg": "#0D1117", "panel": "#161B22", "field": "#21262D", "accent": "#58A6FF", "bot": "#A5D6FF", "text": "#C9D1D9", "muted": "#484F58"}
    }

    def __init__(self, root):
        self.root = root; self.root.title("N30N C0R3 AI"); self.root.geometry("1100x900")
        self.settings_store = SettingsStore(); self.settings = self.settings_store.data
        self.memory = MemoryDatabase(self.settings); self.chat_id = self.memory.get_or_create_chat()
        self.brain = ThinkingBrain(self.settings); self.img_cache = []
        self._build_layout(); self.apply_theme(); self.load_history()

    def _build_layout(self):
        self.header = tk.Frame(self.root, height=60); self.header.pack(side=tk.TOP, fill=tk.X)
        self.logo = tk.Label(self.header, text="N30N C0R3 AI", font=("Consolas", 16, "bold")); self.logo.pack(side=tk.LEFT, padx=30)
        self.paned = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, bd=0, sashwidth=2); self.paned.pack(fill=tk.BOTH, expand=True)
        self.side = tk.Frame(self.paned, width=220); self.side.pack_propagate(False); self.paned.add(self.side)
        self.side_label = tk.Label(self.side, text="SESSIONS", font=("Consolas", 11, "bold")); self.side_label.pack(pady=20)
        self.chat_list = tk.Listbox(self.side, bd=0, font=("Consolas", 10)); self.chat_list.pack(fill=tk.BOTH, expand=True, padx=15)
        self.chat_list.bind("<<ListboxSelect>>", self._switch_chat)
        self.btn_f = tk.Frame(self.side); self.btn_f.pack(fill=tk.X, padx=15, pady=15)
        self.b_new = tk.Button(self.btn_f, text="+", bd=0, font=("Consolas", 14), command=self.new_chat, width=3); self.b_new.pack(side=tk.LEFT, padx=2)
        self.b_set = tk.Button(self.btn_f, text="⚙", bd=0, font=("Consolas", 14), command=self.open_settings, width=3); self.b_set.pack(side=tk.LEFT, padx=2)
        self.b_clr = tk.Button(self.btn_f, text="×", bd=0, font=("Consolas", 14), command=self.clear_history, width=3); self.b_clr.pack(side=tk.LEFT, padx=2)
        self.chat_main = tk.Frame(self.paned); self.paned.add(self.chat_main)
        self.display = scrolledtext.ScrolledText(self.chat_main, bd=0, wrap=tk.WORD, state='disabled', padx=25, pady=25); self.display.pack(fill=tk.BOTH, expand=True)
        self.footer = tk.Frame(self.chat_main, height=100); self.footer.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=15); self.footer.pack_propagate(False)
        self.wrap = tk.Frame(self.footer, highlightthickness=1); self.wrap.pack(fill=tk.BOTH, expand=True)
        self.b_file = tk.Button(self.wrap, text="+", bd=0, font=("Arial", 22), command=self.load_file); self.b_file.pack(side=tk.LEFT, padx=15)
        self.entry = tk.Entry(self.wrap, bd=0, font=("Consolas", 13)); self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True); self.entry.bind("<Return>", lambda e: self.send())
        self.b_send = tk.Button(self.wrap, text="➜", bd=0, font=("Arial", 22), command=self.send); self.b_send.pack(side=tk.RIGHT, padx=15)

    def apply_theme(self):
        theme_name = self.settings.get("theme", "Neon Orange")
        theme = self.themes.get(theme_name, self.themes["Neon Orange"])
        self.root.configure(bg=theme["bg"]); self.paned.configure(bg=theme["bg"]); self.header.configure(bg=theme["panel"]); self.logo.configure(bg=theme["panel"], fg=theme["accent"])
        self.side.configure(bg=theme["panel"]); self.side_label.configure(bg=theme["panel"], fg=theme["accent"]); self.chat_list.configure(bg=theme["panel"], fg=theme["text"], selectbackground=theme["field"])
        self.btn_f.configure(bg=theme["panel"])
        for b in [self.b_new, self.b_set, self.b_clr, self.b_file, self.b_send]: b.configure(bg=theme["field"], fg=theme["accent"], activebackground=theme["panel"], activeforeground=theme["accent"])
        self.chat_main.configure(bg=theme["bg"]); self.display.configure(bg=theme["bg"], fg=theme["text"], font=("Consolas", int(self.settings.get("font_size", 12))), insertbackground=theme["accent"])
        self.display.tag_config("user", foreground=theme["accent"], font=("Consolas", int(self.settings.get("font_size", 12)), "bold")); self.display.tag_config("bot", foreground=theme["bot"]); self.display.tag_config("code", foreground=theme["text"], background=theme["field"])
        self.footer.configure(bg=theme["bg"]); self.wrap.configure(bg=theme["field"], highlightbackground=theme["muted"]); self.entry.configure(bg=theme["field"], fg=theme["text"], font=("Consolas", 13), insertbackground=theme["accent"])
        self._refresh_chats()

    def open_settings(self):
        win = tk.Toplevel(self.root); win.title("All Settings"); win.geometry("600x850")
        theme_name = self.settings.get("theme", "Neon Orange")
        theme = self.themes.get(theme_name, self.themes["Neon Orange"])
        win.configure(bg=theme["bg"])
        def _get_val(k, default=False):
            v = self.settings.get(k); return v if v is not None else default
        v = {
            "theme": tk.StringVar(value=str(self.settings.get("theme", "Neon Orange"))),
            "intelligence": tk.StringVar(value=str(self.settings.get("intelligence", "Balanced"))),
            "response_style": tk.StringVar(value=str(self.settings.get("response_style", "Balanced"))),
            "speed": tk.StringVar(value=str(self.settings.get("speed", "Normal"))),
            "result_count": tk.StringVar(value=str(self.settings.get("result_count", 15))),
            "font_size": tk.StringVar(value=str(self.settings.get("font_size", 12))),
            "web_search": tk.BooleanVar(value=_get_val("web_search", True)),
            "wikipedia": tk.BooleanVar(value=_get_val("wikipedia", True)),
            "live_search": tk.BooleanVar(value=_get_val("live_search", True)),
            "weather_api_key": tk.StringVar(value=str(self.settings.get("weather_api_key", ""))),
            "ad_filter": tk.BooleanVar(value=_get_val("ad_filter", True)),
            "save_memory": tk.BooleanVar(value=_get_val("save_memory", True)),
            "save_locally": tk.BooleanVar(value=_get_val("save_locally", False)),
            "save_path": tk.StringVar(value=str(self.settings.get("save_path", "")))
        }
        container = tk.Frame(win, bg=theme["bg"]); container.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        def _l(t): tk.Label(container, text=t, bg=theme["bg"], fg=theme["accent"], font=("Consolas", 10, "bold")).pack(anchor="w", pady=(15, 2))
        _l("UI THEME"); tk.OptionMenu(container, v["theme"], *self.themes.keys()).pack(fill=tk.X)
        _l("INTELLIGENCE MODE"); tk.OptionMenu(container, v["intelligence"], "Fast", "Balanced", "Deep", "Local Only").pack(fill=tk.X)
        _l("SEARCH SPEED"); tk.OptionMenu(container, v["speed"], "Fast", "Normal", "Deep").pack(fill=tk.X)
        _l("ACTIVE DATA SOURCES")
        tk.Checkbutton(container, text="Web Search (General)", variable=v["web_search"], bg=theme["bg"], fg=theme["text"], selectcolor=theme["field"], activebackground=theme["bg"]).pack(anchor="w")
        tk.Checkbutton(container, text="Live Search (Real-time)", variable=v["live_search"], bg=theme["bg"], fg=theme["text"], selectcolor=theme["field"], activebackground=theme["bg"]).pack(anchor="w")
        _l("LIVE API KEYS (Optional)")
        tk.Label(container, text="OpenWeatherMap API Key", bg=theme["bg"], fg=theme["text"], font=("Consolas", 9)).pack(anchor="w")
        tk.Entry(container, textvariable=v["weather_api_key"], bg=theme["field"], fg=theme["text"], bd=0, show="*").pack(fill=tk.X, ipady=5)
        _l("STORAGE")
        tk.Checkbutton(container, text="Save Chat Memory", variable=v["save_memory"], bg=theme["bg"], fg=theme["text"], selectcolor=theme["field"], activebackground=theme["bg"]).pack(anchor="w")
        tk.Checkbutton(container, text="External JSON Database", variable=v["save_locally"], bg=theme["bg"], fg=theme["text"], selectcolor=theme["field"], activebackground=theme["bg"]).pack(anchor="w")
        p_f = tk.Frame(container, bg=theme["bg"]); p_f.pack(fill=tk.X, pady=5)
        tk.Entry(p_f, textvariable=v["save_path"], bg=theme["field"], fg=theme["text"], bd=0).pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        tk.Button(p_f, text="...", command=lambda: v["save_path"].set(filedialog.asksaveasfilename(defaultextension=".json")), bg=theme["field"], fg=theme["bot"], bd=0).pack(side=tk.RIGHT, padx=5)

        def _apply():
            for k in v:
                val = v[k].get()
                if k in ["result_count", "font_size"]:
                    try: self.settings[k] = int(val)
                    except: pass
                else: self.settings[k] = val
            self.settings_store.save(); self.brain.update_settings(self.settings); self.apply_theme()
            new_theme = self.themes.get(self.settings["theme"], self.themes["Neon Orange"])
            win.configure(bg=new_theme["bg"]); container.configure(bg=new_theme["bg"])
            for widget in container.winfo_children():
                try: widget.configure(bg=new_theme["bg"], fg=new_theme["text"])
                except: pass
                if isinstance(widget, tk.Label): widget.configure(fg=new_theme["accent"])
                if isinstance(widget, tk.Button): widget.configure(bg=new_theme["field"], fg=new_theme["accent"])
            btn_apply.configure(bg=new_theme["accent"], fg=new_theme["bg"])
            btn_save.configure(bg=new_theme["field"], fg=new_theme["accent"])

        btn_apply = tk.Button(win, text="APPLY", command=_apply, bg=theme["accent"], fg=theme["bg"], font=("Consolas", 11, "bold"), bd=0)
        btn_apply.pack(pady=(20, 5), fill=tk.X, padx=40)
        btn_save = tk.Button(win, text="SAVE & CLOSE", command=lambda: [_apply(), win.destroy()], bg=theme["field"], fg=theme["accent"], font=("Consolas", 11, "bold"), bd=0)
        btn_save.pack(pady=5, fill=tk.X, padx=40)

    def _refresh_chats(self):
        self.chat_list.delete(0, tk.END)
        for cid, chat in self.memory.get_chats(): self.chat_list.insert(tk.END, chat["name"])

    def _switch_chat(self):
        idx = self.chat_list.curselection()
        if idx:
            chats = self.memory.get_chats()
            self.chat_id = chats[idx[0]][0]; self.load_history()

    def new_chat(self):
        name = simpledialog.askstring("New", "Session name:")
        if name: self.chat_id = self.memory.create_chat(name); self._refresh_chats(); self.load_history()

    def clear_history(self):
        if messagebox.askyesno("Clear", "Wipe chat history?"): self.chat_id = self.memory.clear_all(); self._refresh_chats(); self.load_history()

    def load_history(self):
        self.display.config(state='normal'); self.display.delete("1.0", tk.END); self.display.config(state='disabled')
        for m in self.memory.get_history(self.chat_id):
            tag = "user" if m.get("role") == "user" else "bot"
            self.add_msg("YOU" if tag=="user" else "NEON", m.get("text", ""), tag)

    def load_file(self):
        path = filedialog.askopenfilename()
        if path:
            filename = os.path.basename(path)
            if any(path.lower().endswith(e) for e in ['.png','.jpg','.jpeg','.webp']) and HAS_PIL:
                img = Image.open(path); img.thumbnail((400, 400)); photo = ImageTk.PhotoImage(img); self.img_cache = [photo]
                self.display.config(state='normal'); self.display.image_create(tk.END, image=photo); self.display.insert(tk.END, "\n"); self.display.config(state='disabled')
                self.add_msg("SYSTEM", f"Captured {filename}.", "bot")
            else: self.add_msg("SYSTEM", f"Document {filename} loaded.", "bot")

    def send(self):
        text = self.entry.get().strip()
        if text: self.add_msg("YOU", text, "user"); self.memory.add_msg(self.chat_id, "user", text); self.entry.delete(0, tk.END); threading.Thread(target=self._process, args=(text,)).start()

    def _process(self, text):
        resp = self.brain.respond(text)
        self.root.after(0, lambda: self.add_msg("NEON", resp, "bot")); self.memory.add_msg(self.chat_id, "bot", resp)

    def add_msg(self, sender, msg, tag):
        self.display.config(state='normal'); self.display.insert(tk.END, f"\n{sender}\n", tag)
        if "```" in msg:
            parts = msg.split("```")
            for i, p in enumerate(parts): self.display.insert(tk.END, p, "code" if i % 2 == 1 else None)
        else: self.display.insert(tk.END, msg + "\n")
        self.display.config(state='disabled'); self.display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk(); NeonUI(root); root.mainloop()

