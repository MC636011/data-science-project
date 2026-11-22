# WANG YU MENG — Data Science Portfolio

This repository contains one individual project and two CISC7204 group assignments. Each project is stored in a separate folder so that personal work and group work are clearly identified.

## Repository layout

```text
data-science-project/
├── README.md
├── index.md
├── index.html
├── requirements.txt
├── .gitignore
├── docs/
│   ├── reflection.md
│   ├── peer_feedback.md
│   ├── submission.md
│   └── rubric_checklist.md
└── projects/
    ├── personal-wine-quality/
    ├── assignment01-flight-delay/
    └── assignment02-income-inequality/
```

## Portfolio contents

| Project | Type | Folder | Status |
|---|---|---|---|
| Wine Quality Analysis | Individual work | `projects/personal-wine-quality/` | Completed |
| U.S. Domestic Flight Delay Pattern Analysis | Group Assignment 01 | `projects/assignment01-flight-delay/` | Completed |
| Income Inequality Across UK Local Authorities | Group Assignment 02 | `projects/assignment02-income-inequality/` | Completed |

The two group assignments are separated as requested. The original Wine Quality project is retained as a personal project and clearly labeled as individual work.

## Quick reproduction guide

1. Clone the repository:
   ```bash
   git clone https://github.com/mc636011/data-science-project.git
   cd data-science-project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install shared dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Enter a project folder and follow its `README.md` and `data/README.md`:
   - Wine Quality: `projects/personal-wine-quality/`
   - Assignment 01: `projects/assignment01-flight-delay/`
   - Assignment 02: `projects/assignment02-income-inequality/`
5. Run the relevant script:
   ```bash
   python projects/personal-wine-quality/analysis.py
   python projects/assignment01-flight-delay/analysis.py
   python projects/assignment02-income-inequality/analysis.py
   ```

## Portfolio website

The GitHub Pages entry points are:

- Markdown source: `index.md`
- Static HTML source: `index.html`
- Live URL: https://mc636011.github.io/data-science-project/

If the live URL returns 404, enable GitHub Pages from **Settings → Pages → main → /(root)**.

## Responsible sharing

- Raw CSV and Excel files are not committed when they are large or subject to source terms.
- Download instructions and usage permissions are documented inside each project.
- No passwords, API keys, personal data, or restricted datasets are intentionally exposed.
- Dataset attribution is included in the individual project README files.
