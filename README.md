# GTM Data Pipeline

A Python pipeline that identifies, scores, and enriches law firm leads for outbound sales — built for companies like August that target mid-size law firms.

## What It Does

1. **Ingests** a CSV of law firms
2. **Scores** each firm using an ICP (Ideal Customer Profile) model
3. **Labels** firms as High / Medium / Low Priority
4. **Enriches** each firm with live email data from Hunter.io
5. **Exports** a ranked, enriched CSV ready for a sales team

## Why This Matters

Sales teams waste time on bad leads. This pipeline surfaces the best prospects automatically — so reps spend time selling, not researching.

## Quick Start

### 1. Install dependencies
```
pip install pandas requests
```

### 2. Add your firms to `firms_input.csv`
Required columns: `firm_name`, `city`, `size`, `practice_area`, `website`

### 3. Add your Hunter.io API key
Sign up free at hunter.io and paste your key into `pipeline.py`

### 4. Run the pipeline
```
py pipeline.py
```

### 5. Check your output
Open `enriched_firms.csv` — firms ranked by ICP score with email enrichment data

## ICP Scoring Model

| Signal | Points |
|--------|--------|
| Mid-size firm | +50 |
| High-value practice area (Corporate, IP, Employment) | +30 |
| Major metro city | +20 |
| **Max score** | **100** |

## Output Fields

| Column | Description |
|--------|-------------|
| firm_name | Law firm name |
| icp_score | Score out of 100 |
| priority | High / Medium / Low |
| emails_found | Number of emails found via Hunter.io |
| email_pattern | Email format e.g. {first}.{last} |

## Tech Stack

- Python 3.14
- pandas — data processing
- requests — API calls
- Hunter.io API — email enrichment

## Error Handling

The pipeline handles: API timeouts, connection errors, missing CSV columns, and malformed responses — logging each issue without crashing.
```
```
git push
