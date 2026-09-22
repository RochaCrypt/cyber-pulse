<div align="center">

# Cyber Pulse

An auto-updating cybersecurity news portal — aggregated headlines from leading
security outlets, refreshed every 3 hours by GitHub Actions.

<a href="https://rochacrypt.github.io/cyber-pulse/"><img src="https://img.shields.io/badge/Open_the_live_portal-0d1117?style=for-the-badge&labelColor=ff2e4c" alt="Live portal"/></a>
<a href="https://github.com/RochaCrypt"><img src="https://img.shields.io/badge/Back_to_profile-ff2e4c?style=for-the-badge&logo=github&logoColor=white" alt="Profile"/></a>

<img src="https://img.shields.io/github/last-commit/RochaCrypt/cyber-pulse?style=flat-square&color=ff2e4c&labelColor=0d1117&label=last%20refresh" alt="last refresh"/>

</div>

## What it is

A live, searchable portal that pulls the latest headlines from The Hacker News,
BleepingComputer, Krebs on Security, Dark Reading, SecurityWeek, The Record and
CISA advisories. A scheduled GitHub Action fetches the feeds, writes `news.json`,
and the static page renders it with search and per-source filtering.

Only headlines, sources and links are stored; every item links back to its
original publisher.

## How it works

1. `.github/workflows/update.yml` runs every 3 hours (and on demand).
2. `scripts/fetch_news.py` parses the RSS feeds and writes `news.json`.
3. `index.html` (served by GitHub Pages) loads `news.json` and renders the portal.

## Setup

1. Create a public repo named `cyber-pulse` and upload these files.
2. **Settings → Actions → General → Workflow permissions → Read and write**, save.
3. **Actions → Update Cyber Pulse → Run workflow** to populate real data.
4. **Settings → Pages → Deploy from a branch → main → / (root)** to publish at
   `https://rochacrypt.github.io/cyber-pulse/`.

## Customise

- **Sources:** edit `FEEDS` in `scripts/fetch_news.py`.
- **Frequency:** edit the `cron` in the workflow.
- **Volume:** tune `MAX_PER_FEED` / `MAX_TOTAL`.
