# NEON CORE AI

> A neon-dark local chat assistant in one Python file.

```
███╗   ██╗███████╗ ██████╗ ███╗   ██╗
████╗  ██║██╔════╝██╔═══██╗████╗  ██║
██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
██║ ╚████║███████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
```

## Run It

```bash
python3 ai.py
```

NEON opens a black Tkinter chat window with orange/cyan styling, a sessions sidebar, a message area, and a bottom input bar.

## Feature Snapshot

| Feature | Status | Details |
|---|---:|---|
| Local GUI | Ready | Tkinter desktop UI with dark neon styling |
| Saved history | Ready | Chat history is embedded directly inside `ai.py` |
| New Chat | Ready | Sidebar button creates a fresh saved chat |
| Clear History | Ready | Sidebar button wipes all embedded history after confirmation |
| Web findings | Ready | DuckDuckGo HTML snippets with cleanup |
| Wikipedia context | Ready | Adds summary context when available |
| Latest mode | Ready | `latest`, `news`, `update`, `current`, `today`, and `2024` trigger update-style searching |
| Context follow-ups | Ready | Short searches can include the previous message as context |
| Image preview | Optional | PNG/JPG/JPEG/WEBP preview when Pillow is installed |
| Code-style display | Ready | Code-like snippets are rendered in dark code blocks |
| Time/date | Ready | Ask `time` or `date` |
| Font | Restored | Uses the original Consolas-based UI fonts |

## Controls

| Control | What Happens |
|---|---|
| `New Chat` | Creates a new named session and clears the visible chat window |
| `Clear History` | Deletes all saved chats from the embedded `NEON_HISTORY` block |
| `+` | Opens a file picker; image files can be previewed |
| `➜` | Sends the current message |
| `Enter` | Sends the current message |

## Chat History

History lives inside `ai.py`, not in a database:

```python
# NEON_HISTORY_START
NEON_HISTORY = json.loads('...')
# NEON_HISTORY_END
```

When you send a message, NEON rewrites that block so chats survive app restarts. The save format is JSON-loaded Python, so multiline bot replies stay safe and do not break the script.

## Sessions

The sidebar lists saved sessions from the embedded history.

- Startup loads the first saved chat.
- `New Chat` creates a separate saved conversation.
- Old chats remain stored in `ai.py`.
- `Clear History` resets everything back to one fresh session.

## Web Answer Flow

```text
User message
  ↓
SmartBrain checks casual chat and local tools
  ↓
DynamicEngine searches DuckDuckGo HTML
  ↓
Wikipedia summary is fetched when available
  ↓
Result text is cleaned
  ↓
NEON displays web findings or latest updates
```

## Cleanup Built In

Search snippets are cleaned before display:

- HTML tags are stripped
- Entities like `&amp;` are decoded
- Standalone leaked tags like `#27` are removed
- Extra whitespace is normalized

## Example Prompts

```text
hello
how are you
who are you
thanks
time
date
what is Python
latest AI news
current tech update
find information about quantum computing
```

## Example Output

### Casual

```text
YOU
hello

NEON
Hey! Need some info?
```

### Time

```text
YOU
time

NEON
It is 05:41 PM, June 24.
```

### Latest Search

```text
YOU
latest AI news

NEON
⚡ **LATEST UPDATES:**

Real-time findings:
• Cleaned result snippet...
• Another useful update...
```

### Regular Web Search

```text
YOU
what is machine learning

NEON
Wikipedia summary...

Web findings:
• Cleaned result snippet...
• Another useful result...
```

## Image Loading

The `+` button can load files.

Image preview works for:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`

Install Pillow for image display:

```bash
pip install pillow
```

## Requirements

```text
Python 3
Tkinter
Internet connection for web search
```

Optional:

```text
Pillow for image preview
```

## Architecture

```text
ai.py
├── NEON_HISTORY       Saved chats embedded in the source file
├── MemoryDatabase     Creates chats, saves messages, clears history
├── DynamicEngine      Fetches web/Wikipedia data and cleans text
├── SmartBrain         Routes casual chat, time/date, and web answers
└── NeonUI             Tkinter interface, sidebar, buttons, display, input
```

## Privacy

- No LLM API keys
- No cloud chat storage
- Chat history stays in `ai.py`
- Web requests only happen for search-style answers

## Current Files

| File | Purpose |
|---|---|
| `ai.py` | The full app |
| `ALL_MARKDOWN.md` | This documentation |

## Status

```text
App: NEON CORE AI
UI: Tkinter neon dark mode
Font: Consolas
Storage: Embedded in ai.py
Sessions: New Chat + saved history
Clear: Clear History button
```

---

**NEON CORE AI** is a compact local assistant: flashy interface, saved sessions, live web findings, cleaned output, and everything packed into one Python file.
