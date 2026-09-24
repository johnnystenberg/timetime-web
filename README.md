# TimeTime — marketing site

Landing page for **TimeTime**, the team time-tracking app for iOS and Android:
report time in three taps against your group's shared activities, and invite
colleagues with a single link.

Static site served via GitHub Pages.

Three languages, each a complete static page (no text is swapped by
JavaScript):

- `/` — English, the fallback (same rule as the apps)
- `/sv/` — Swedish
- `/de/` — German

Each has `index.html`, `privacy.html` (App Store / Play requirement) and
`support.html`. The root sends visitors whose browser is Swedish or German to
their language, unless they picked one; without JavaScript the language links
are there instead.

**Don't edit the HTML.** All text lives in `build.py`, per language and key;
edit there and run `python3 build.py`. A key missing in one language stops
the build — that is how the three stay in step. Shared styles are in
`assets/site.css`.

Prices in SEK appear only on the Swedish page: amounts in other currencies are
not decided yet, and the English and German pages point to the stores.

The join landing and app services live separately at
[app.timetime.work](https://app.timetime.work) (Next.js on Vercel) — a static
site cannot look up a group name, and the invite page needs to say *"You are
invited to <group>"*. This marketing site is served at
[timetime.work](https://timetime.work).

Colours come from the app's design tokens
(`packages/tokens/tokens.json` in the app repo).
