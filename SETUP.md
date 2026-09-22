# Cyber News Feed — setup

Turns your GitHub profile into an auto-updating cybersecurity news portal.
It refreshes a section of your profile README every 6 hours with the latest
headlines from leading security outlets, using the maintained
`blog-post-workflow` action (no custom code to maintain).

## 1. Add the news section to your profile README

In `RochaCrypt/RochaCrypt` → `README.md`, paste the block from
`README-news-section.md` where you want the feed to appear (a good spot is a
new "News" section, or right under the summary so it's the first fresh thing
visitors see). Keep the two comment markers exactly as they are — the action
replaces everything between them:

    <!-- CYBER-NEWS:START -->
    <!-- CYBER-NEWS:END -->

Optionally add a nav button:

    [![News](https://img.shields.io/badge/›-News-0d1117?style=for-the-badge&labelColor=ff2e4c)](#latest-in-cybersecurity)

## 2. Add the workflow

Create `.github/workflows/cyber-news.yml` in `RochaCrypt/RochaCrypt` with the
contents of the file in this folder.

## 3. Allow the workflow to write

Repository **Settings → Actions → General → Workflow permissions** →
**Read and write permissions** → **Save**.

## 4. Run it

**Actions** tab → **Cyber News Feed** → **Run workflow**. Wait ~1 minute; the
section between the markers fills with the latest headlines and refreshes every
6 hours from then on.

## Customising

- **More / fewer headlines:** change `max_post_count`.
- **Frequency:** change the `cron`. `0 */6 * * *` = every 6 hours; `0 */3 * * *`
  = every 3 hours. More frequent = fresher profile, but avoid < 1 hour.
- **Sources:** edit `feed_list` (comma-separated RSS URLs). Add or remove outlets
  to match your niche (e.g. cloud security, threat intel, AppSec).
- **Layout:** the `template` controls each row. Current template renders a table;
  for a simple bullet list use `template: "- [$title]($url)"` and drop the table
  header from the README section.

## Feeds used

| Source | Focus |
| :--- | :--- |
| The Hacker News | Breaking security news |
| BleepingComputer | Malware, breaches, how-tos |
| Krebs on Security | Investigative security journalism |
| Dark Reading | Enterprise security |
| SecurityWeek | Industry news |
| The Record | Threat intel & nation-state |
| CISA Advisories | Official US gov advisories |

> Only headlines and links are published, pointing back to each source — a
> standard, fair-use aggregation, like any RSS reader.
