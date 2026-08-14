# CUNY Python

Python coursework and projects from teaching at CUNY Queensborough, plus personal
practice following the 100 Days of Code curriculum.

## Structure

- **[fundamentals/](fundamentals/)** — Barebones intro-to-Python basics (JetBrains
  Academy course). Numbered `01`–`10`, covering variables, strings, data
  structures, conditionals, loops, functions, OOP, modules, and file I/O.
- **`day-01-…` … `day-79-…`** — 100 Days of Code, in order. Each folder covers a
  topic or mini-project (e.g. `day-05-for-loops`, `day-15-coffee-machine-oop`,
  `day-39-flight-deal-finder`).
- **[extra-practice/](extra-practice/)** — Standalone practice scripts and small
  projects (Hangman, Rock Paper Scissors, Trivia Quiz, etc.) not tied to a
  specific day.

## Getting started

```bash
git clone https://github.com/yigitisik/CUNY-Python.git
cd CUNY-Python
pip install -r fundamentals/requirements.txt  # only needed for fundamentals/
```

Most `day-XX` and `extra-practice` projects are self-contained scripts — open
the folder and run the `main.py` (or similarly named file) directly. A few
require API keys, read via `os.environ.get(...)`; create a `.env` file in
that project's folder with the needed keys (`.env` is gitignored).

## License

See [fundamentals/LICENSE](fundamentals/LICENSE).
