# TimeTime — marketing site

Landing page for **TimeTime**, the team time-tracking app for iOS and Android:
report time in three taps against your group's shared activities, and invite
colleagues with a single link.

Static site served via GitHub Pages.

- `index.html` — landing page (SV/EN)
- `privacy.html` — privacy policy (App Store / Play requirement)
- `support.html` — support / FAQ (App Store / Play requirement)
- `assets/` — app icon

The join landing and app services live separately at
[app.timetime.work](https://app.timetime.work) (Next.js on Vercel) — a static
site cannot look up a group name, and the invite page needs to say *"You are
invited to <group>"*. This marketing site is served at
[timetime.work](https://timetime.work).

Colours come from the app's design tokens
(`packages/tokens/tokens.json` in the app repo).
