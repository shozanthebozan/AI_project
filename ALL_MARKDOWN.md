# NEON CORE AI

> One-file local AI with saved chats, a smarter brain, live web research, and a full settings panel.

```
███╗   ██╗███████╗ ██████╗ ███╗   ██╗
████╗  ██║██╔════╝██╔═══██╗████╗  ██║
██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
██║ ╚████║███████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
```

## Run

```bash
python3 ai.py
```

## Main Features

| Feature | What It Does |
|---|---|
| Smarter OmniBrain | Handles local facts, math, code, memory recap, explanations, and web research |
| Saved chats | Chat history is embedded directly inside `ai.py` |
| New Chat | Creates a fresh named session |
| Clear History | Wipes all saved chats after confirmation |
| Settings panel | Controls theme, intelligence, speed, web behavior, result count, font size, and answer style |
| Web research | Uses DuckDuckGo HTML and optional Wikipedia context |
| Cleanup | Strips HTML, decodes entities, removes leaked tags like `#27`, and normalizes spacing |
| Image preview | Shows PNG/JPG/JPEG/WEBP images when Pillow is installed |
| Neon UI | Dark Tkinter interface with Consolas font and theme options |

## Brain Powers

| Skill | Example |
|---|---|
| Local facts | `what is a banana` |
| Math | `12 * 8 + 4` |
| Code generation | `write python code for hello world` |
| Memory recap | `recap history` |
| Explanation mode | `explain gravity` |
| Web fallback | `search current AI news` |
| Help | `help` |

## Settings

Open **Settings** from the sidebar.

| Setting | Options |
|---|---|
| Theme | Neon, Cyber Blue, Matrix, Light, Midnight |
| Intelligence | Fast, Balanced, Deep, Local Only |
| Speed | Fast, Normal, Deep |
| Response Style | Short, Balanced, Detailed |
| Web Result Count | 1 to 10 |
| Font Size | 9 to 18 |
| Web Search | On/off |
| Wikipedia Context | On/off |
| Ad/Shopping Filter | On/off |

Settings are saved inside `ai.py`:

```python
# NEON_SETTINGS_START
NEON_SETTINGS = json.loads('...')
# NEON_SETTINGS_END
```

### What The Settings Actually Change

| Control | Real Effect |
|---|---|
| Theme | Recolors the app background, panels, input box, user text, and bot text |
| Intelligence | Changes whether NEON answers locally, searches selectively, or uses deeper context |
| Speed | Changes web request timeout: faster answers or deeper waiting |
| Response Style | Changes memory/explanation length |
| Result Count | Limits how many web snippets appear |
| Font Size | Resizes chat and input text |
| Web Search | Disables/enables all web fallback |
| Wikipedia | Disables/enables Wikipedia summaries |
| Ad Filter | Removes shopping/ad-like result noise unless you ask for buying/prices |

## Intelligence Modes

| Mode | Behavior |
|---|---|
| Fast | Uses local abilities first and avoids broad research unless the prompt clearly asks for search/current info |
| Balanced | Good default mix of local answers and web research fallback |
| Deep | Uses more context and slower web timeouts for broader research |
| Local Only | No web research; math, code, memory, built-in facts, and explanations only |

## Chat Storage

Chat history is embedded into the source file:

```python
# NEON_HISTORY_START
NEON_HISTORY = json.loads('...')
# NEON_HISTORY_END
```

Every message updates that block so chats survive restarts without a database.

## Controls

| Control | Action |
|---|---|
| `+ New Chat` | Create a new saved chat |
| `Settings` | Open behavior and theme controls |
| `× Clear History` | Delete all saved chats |
| `+` | Load a file or preview an image |
| `➜` | Send message |
| `Enter` | Send message |

## Example Prompts

```text
what is a banana
12 * 8 + 4
write python code for hello world
recap history
explain gravity
latest AI news
help
```

## Example Answers

```text
YOU
12 * 8 + 4

NEON
🧮 12 * 8 + 4 = 100
```

```text
YOU
recap history

NEON
Recent chat history:
• You: ...
• NEON: ...
```

## Architecture

```text
ai.py
├── NEON_HISTORY       Embedded chat history
├── NEON_SETTINGS      Embedded app/brain settings
├── MemoryDatabase     Saved chats and clear-history behavior
├── SettingsStore      Saves Settings into ai.py
├── OmniBrain          Local-first intelligence and web fallback
└── NeonUI             Tkinter interface, themes, settings, files, chat
```

## Optional Image Support

```bash
pip install pillow
```

Supported preview formats:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

## Privacy

- No LLM API keys
- No cloud chat storage
- History and settings stay in `ai.py`
- Web requests happen only when web search is enabled and needed

## Current Files

| File | Purpose |
|---|---|
| `ai.py` | Complete NEON app, brain, UI, settings, and embedded storage |
| `ALL_MARKDOWN.md` | Current documentation |

## Status

```text
App: NEON CORE AI
Brain: OmniBrain
Storage: Embedded NEON_HISTORY
Settings: Embedded NEON_SETTINGS
UI: Tkinter
Font: Consolas
Themes: Neon, Cyber Blue, Matrix, Light, Midnight
```

---

**NEON CORE AI** is now a configurable local assistant: smart brain, saved sessions, theme controls, speed/intelligence settings, and cleaned web research in one Python file.
