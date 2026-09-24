#!/usr/bin/env python3
"""Bygger timetime.work på tre språk: engelska (roten), svenska (/sv/), tyska (/de/).

Varje språk får en fullständig statisk sida — ingen text byts med JavaScript,
så sidan är komplett för sökmotorer, länkförhandsvisningar och den som stängt
av skript. Texterna står här, per språk och nyckel, så att en ändring görs på
ett ställe och ett språk inte kan halka efter: saknas en nyckel stoppar bygget.

Kör:  python3 build.py   (skriver index/privacy/support.html i roten, sv/, de/)

Engelska ligger i roten av samma skäl som i apparna: den som har ett språk vi
saknar ska få engelska, inte svenska. Befintliga länkar till /privacy.html och
/support.html fortsätter att fungera.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://timetime.work"
LANGS = ["en", "sv", "de"]
PREFIX = {"en": "", "sv": "sv/", "de": "de/"}
LABEL = {"en": "English", "sv": "Svenska", "de": "Deutsch"}

# ---------------------------------------------------------------------------
# Texter. Nycklarna måste finnas för alla tre språk.

T = {
"en": {
  "title": "TimeTime — time tracking for teams",
  "meta": "Report time in three taps, against your group's shared activities. One link invites your colleagues. iPhone and Android.",
  "og": "Three taps to fill in a day. One link to invite your colleagues.",
  "hero.eyebrow": "Time tracking for teams · iPhone &amp; Android",
  "hero.h1": 'Time your team <span class="em">actually</span> reports',
  "hero.sub": "Three taps to fill in a day. One link to invite your colleagues. No admin, no accounts to hand out.",
  "hero.t1": "Free for up to 3 people", "hero.t2": "Works offline", "hero.t3": "Nobody sees your time unless you want",
  "badge.soon": "Coming soon to the",
  "stage.title": "Thursday 6 August", "stage.of": "of 8h · 2h 45m left",
  "s.title": "The whole app is four tabs",
  "s.lead": "Report the day, see the week, follow the time — and invite the team.",
  "s.day": "Day", "s.week": "Week", "s.stats": "Statistics", "s.group": "Group",
  "f.title": "Built for low friction",
  "f.lead": "Time tracking is something you have to do, not something you want to do. Every decision in the app shortens the path from impulse to saved entry.",
  "f1.h": "Three taps", "f1.p": "Open, pick an activity, save. Fill in afterwards or start a timer — both are first-class paths, neither an afterthought.",
  "f2.h": "One link invites", "f2.p": "Share the link and your colleague is in. No approval, no invite codes to email around.",
  "f3.h": "Works offline", "f3.p": "Entries queue locally and sync when you are back online. No time lost on the train or in the basement.",
  "f4.h": "Widget and timer", "f4.p": "Add 30 or 60 minutes straight from the home screen. A running timer shows on the lock screen and in the Dynamic Island.",
  "f5.h": "Your country's calendar", "f5.p": "Public holidays for your country — and for German states and the UK's nations — so a day off never shows up as missing time.",
  "p.title": "Privacy that is built in, not promised",
  "p.lead": "The group decides how much is shared — and the rules are enforced by the database, not by the interface.",
  "p1.h": "Open", "p1.p": "Every member sees everyone's entries and names. Good for small teams who sit together anyway.",
  "p2.h": "Summarised", "p2.p": "Totals per activity, without names. You see where the time goes — but nobody sees who did what.",
  "p3.h": "Private", "p3.p": "Everyone only sees their own. The owner can export aggregates for follow-up.",
  "p.note": "Nobody can edit anyone else's time — not even the owner. That is a deliberate rule, not a gap.",
  "pr.title": "Pricing", "pr.lead": "The owner pays for the whole group. No member ever meets a paywall.",
  "pr0.h": "Free", "pr0.p": "Up to 3 people. No time limit.",
  "pr1.h": "Team", "pr1.p": "Up to 10 people.",
  "pr2.h": "Larger team", "pr2.p": "Up to 25 people.",
  "pr3.h": "Unlimited", "pr3.p": "As many as you like.",
  "pr.local": "Monthly, in your local currency — shown in the App Store and Google Play.",
  "pr.note": "Full history and CSV export are included in every tier. A 14-day trial with no seat cap — and if you stop paying nothing is deleted: the group pauses, and everything returns on upgrade.",
  "foot.privacy": "Privacy policy", "foot.support": "Support", "foot.home": "Home", "lang.aria": "Language",
  # Integritetspolicy
  "pv.title": "Privacy policy", "pv.updated": "Last updated 24 September 2026",
  "pv.store.h": "What we store",
  "pv.store.p": "Your email address (for sign-in), your display name, and the time you report yourself: date, activity, minutes, any clock times and notes. We also store which groups you belong to.",
  "pv.store.p2": "To send your daily reminder at the right time and your sign-in codes in your language, we also store your time zone and the language your app is set to. Both are read from your phone; you never enter them.",
  "pv.signin.h": "Sign-in",
  "pv.signin.p": "You can sign in with a one-time code by email, with Apple or with Google. If you choose Apple or Google, we receive your email address and name from them — nothing else.",
  "pv.signin.p2": 'If you choose Apple\'s <strong>Hide My Email</strong>, we only see the relay address, never your real one. That address then becomes your account, which is worth knowing: if you later sign in with another method on your real address, they will not match and become two separate accounts. <a href="{support}">Support</a> explains how to connect several sign-in methods to the same account.',
  "pv.sees.h": "Who sees your time",
  "pv.sees.p": "That depends on the group's visibility mode, which the owner chooses. In open mode members see each other's entries. In summarised mode only totals per activity are shown — nobody sees who did what. In private mode everyone only sees their own. Nobody can edit anyone else's time, not even the owner.",
  "pv.not.h": "What we don't do",
  "pv.not.p": "We don't sell your data, share it with ad networks or track you across apps or websites.",
  "pv.sub.h": "Processors",
  "pv.sub.p": "Data is stored with Supabase in the EU. Email is sent via Resend. Notifications are sent via Apple and Google. Payments are handled by the App Store and Google Play — we never see your card details. Public holiday calendars come from Nager.Date; no personal data is sent there.",
  "pv.rights.h": "Your rights",
  "pv.rights.p": "Both a copy of your data and deletion are available directly in the app, under <strong>Your account</strong> (the button with your initials).",
  "pv.rights.p2": "<strong>Download my data</strong> gives you a JSON file with your account, your memberships and all time you reported yourself. Other people's time is never included, not even in open groups — it is their data, not yours. The file needs no subscription and also works in archived groups.",
  "pv.rights.p3": '<strong>Delete my account</strong> removes your time and your memberships. Groups you own pass to a remaining member, or are deleted if you are alone. If you need help with either, email <a href="mailto:support@timetime.work">support@timetime.work</a>.',
  "pv.contact.h": "Contact",
  # Support
  "sp.intro": 'Email <a href="mailto:support@timetime.work">support@timetime.work</a> and we will reply as soon as we can.',
  "sp.full.h": "I couldn't join the group",
  "sp.full.p": "The free tier has room for three people. If the group is full you can still enter the code in the app and ask the owner for a seat — you are let in automatically when they open one.",
  "sp.acc.h": "I can't get into my account",
  "sp.acc.p": "If you signed in with Apple or Google the first time, you need to use the same method again — we can't merge two accounts afterwards. Under <strong>Your account → Sign-in methods</strong> you can connect several methods to the same account, which is worth doing before you change phones.",
  "sp.acc.p2": "If you chose Apple's <strong>Hide My Email</strong>, the relay address is your account. Signing in with an email code on your real address then creates a new, empty account instead of letting you into the old one — add your real address under Sign-in methods instead.",
  "sp.owner.h": "The owner has left",
  "sp.owner.p": "The owner can transfer the group to anyone in it. If they have already gone, an admin can request to take over after 30 days of inactivity; everyone in the group sees the request, and it takes effect after seven days unless the owner signs in.",
  "sp.pay.h": "What happens if we stop paying",
  "sp.pay.p": "No data is deleted. The group enters a 14-day grace period and is then paused: you can keep reporting and seeing your own time, while the shared part — group statistics, export and new members — is off until someone upgrades.",
  "sp.hol.h": "The wrong days show as days off",
  "sp.hol.p": "Public holidays follow the group's country, set under <strong>Group settings → Working hours → Public holidays</strong>. Germany and the UK can also choose a state or nation. Choose <em>No country</em> if the group follows its own calendar.",
  "sp.off.h": "Does the app work without internet",
  "sp.off.p": "Yes. Entries you make offline are queued locally and synced when you are back online. The timer does need a connection, since it lives on the server and is shared between your devices.",
},
"sv": {
  "title": "TimeTime — tidrapportering för team",
  "meta": "Rapportera tid på tre tapp, mot gruppens gemensamma aktiviteter. En länk bjuder in kollegorna. iPhone och Android.",
  "og": "Tre tapp för att fylla i en dag. En länk för att bjuda in kollegorna.",
  "hero.eyebrow": "Tidrapportering för team · iPhone &amp; Android",
  "hero.h1": 'Tid som teamet <span class="em">faktiskt</span> rapporterar',
  "hero.sub": "Tre tapp för att fylla i en dag. En länk för att bjuda in kollegorna. Ingen administration, inga konton att dela ut.",
  "hero.t1": "Gratis upp till 3 personer", "hero.t2": "Fungerar utan täckning", "hero.t3": "Ingen ser din tid om ni inte vill",
  "badge.soon": "Kommer snart till",
  "stage.title": "Torsdag 6 augusti", "stage.of": "av 8h · 2h 45m kvar",
  "s.title": "Hela appen är fyra flikar",
  "s.lead": "Rapportera dagen, se veckan, följ tiden — och bjud in teamet.",
  "s.day": "Dag", "s.week": "Vecka", "s.stats": "Statistik", "s.group": "Grupp",
  "f.title": "Byggd för låg friktion",
  "f.lead": "Tidrapportering är något man måste göra, inte vill. Därför är varje beslut i appen taget för att korta vägen från impuls till sparad post.",
  "f1.h": "Tre tapp", "f1.p": "Öppna, välj aktivitet, spara. Fyll i efterhand eller starta en timer — båda är förstklassiga vägar, inte den ena en eftertanke.",
  "f2.h": "En länk bjuder in", "f2.p": "Dela länken, kollegan är med direkt. Inget godkännande, inga inbjudningskoder att mejla runt.",
  "f3.h": "Fungerar utan nät", "f3.p": "Poster köas lokalt och synkas när täckningen kommer tillbaka. Ingen tid går förlorad på tåget eller i källaren.",
  "f4.h": "Widget och timer", "f4.p": "Lägg 30 eller 60 minuter direkt från hemskärmen. Pågående timer syns på låsskärmen och i Dynamic Island.",
  "f5.h": "Ert lands kalender", "f5.p": "Röda dagar för ert land — och för tyska förbundsländer och Storbritanniens delar — så att en ledig dag aldrig syns som saknad tid.",
  "p.title": "Integritet som är inbyggd, inte lovad",
  "p.lead": "Gruppen väljer själv hur mycket som delas — och reglerna hålls av databasen, inte av gränssnittet.",
  "p1.h": "Öppen", "p1.p": "Alla medlemmar ser allas poster och namn. Bra för små team som ändå sitter tillsammans.",
  "p2.h": "Summerad", "p2.p": "Totaler per aktivitet, utan avsändare. Ni ser vart tiden går — men ingen ser vem som gjort vad.",
  "p3.h": "Privat", "p3.p": "Var och en ser bara sitt eget. Ägaren kan exportera aggregat för uppföljning.",
  "p.note": "Ingen kan ändra någon annans tid — inte heller ägaren. Det är en medveten regel, inte en lucka.",
  "pr.title": "Pris", "pr.lead": "Ägaren betalar för hela gruppen. Ingen medlem möter någonsin en betalvägg.",
  "pr0.h": "Gratis", "pr0.p": "Upp till 3 personer. Ingen tidsgräns.",
  "pr1.h": "Team", "pr1.p": "Upp till 10 personer.",
  "pr2.h": "Större team", "pr2.p": "Upp till 25 personer.",
  "pr3.h": "Obegränsat", "pr3.p": "Hur många som helst.",
  "pr.local": "Per månad. Utanför Sverige i lokal valuta — priset står i App Store och Google Play.",
  "pr.note": "Full historik och CSV-export ingår i alla nivåer. 14 dagars provperiod utan medlemstak — och slutar ni betala raderas ingenting: gruppen pausas, och allt kommer tillbaka vid uppgradering.",
  "foot.privacy": "Integritetspolicy", "foot.support": "Support", "foot.home": "Till startsidan", "lang.aria": "Språk",
  "pv.title": "Integritetspolicy", "pv.updated": "Senast uppdaterad 24 september 2026",
  "pv.store.h": "Vad vi sparar",
  "pv.store.p": "Din e-postadress (för inloggning), ditt visningsnamn, och den tid du själv rapporterar: datum, aktivitet, antal minuter, eventuella klockslag och noteringar. Vi sparar också vilka grupper du är medlem i.",
  "pv.store.p2": "För att skicka din dagliga påminnelse vid rätt tid och dina inloggningskoder på ditt språk sparar vi också din tidszon och det språk appen visar. Båda läses från telefonen; du anger dem aldrig själv.",
  "pv.signin.h": "Inloggning",
  "pv.signin.p": "Du kan logga in med en engångskod på mejl, med Apple eller med Google. Väljer du Apple eller Google får vi din e-postadress och ditt namn därifrån — inget annat.",
  "pv.signin.p2": 'Väljer du Apples <strong>Dölj min e-postadress</strong> ser vi bara reläadressen, aldrig din riktiga. Den adressen blir då ditt konto, vilket är värt att veta: loggar du senare in med en annan metod på din riktiga adress matchar de inte varandra, utan blir två separata konton. Under <a href="{support}">Support</a> står hur du kopplar flera inloggningssätt till samma konto.',
  "pv.sees.h": "Vem som ser din tid",
  "pv.sees.p": "Det avgörs av gruppens synlighetsläge, som ägaren väljer. I öppet läge ser medlemmarna varandras poster. I summerat läge visas bara totaler per aktivitet — ingen ser vem som gjort vad. I privat läge ser var och en bara sitt eget. Ingen kan ändra någon annans tid, inte heller ägaren.",
  "pv.not.h": "Vad vi inte gör",
  "pv.not.p": "Vi säljer inte dina uppgifter, delar dem inte med annonsnätverk och spårar dig inte mellan appar eller webbplatser.",
  "pv.sub.h": "Underleverantörer",
  "pv.sub.p": "Data lagras hos Supabase inom EU. E-post skickas via Resend. Notiser skickas via Apple respektive Google. Betalningar hanteras av App Store och Google Play — vi ser aldrig dina kortuppgifter. Kalendrarna med röda dagar kommer från Nager.Date; inga personuppgifter skickas dit.",
  "pv.rights.h": "Dina rättigheter",
  "pv.rights.p": "Både utdrag och radering sker direkt i appen, under <strong>Ditt konto</strong> (knappen med dina initialer).",
  "pv.rights.p2": "<strong>Ladda ner mina data</strong> ger dig en JSON-fil med ditt konto, dina medlemskap och all tid du själv rapporterat. Andras tid ingår aldrig, inte ens i öppna grupper — den är deras uppgifter, inte dina. Filen kräver ingen prenumeration och fungerar även i arkiverade grupper.",
  "pv.rights.p3": '<strong>Radera mitt konto</strong> tar bort din tid och dina medlemskap. Grupper du äger går över till en kvarvarande medlem, eller raderas om du är ensam. Behöver du hjälp med något av det, mejla <a href="mailto:support@timetime.work">support@timetime.work</a>.',
  "pv.contact.h": "Kontakt",
  "sp.intro": 'Mejla <a href="mailto:support@timetime.work">support@timetime.work</a> så svarar vi så snart vi kan.',
  "sp.full.h": "Jag kom inte in i gruppen",
  "sp.full.p": "Gratisläget rymmer tre personer. Är gruppen full kan du ändå ange koden i appen och be ägaren om en plats — du släpps in automatiskt när hen öppnar en.",
  "sp.acc.h": "Jag kommer inte in på mitt konto",
  "sp.acc.p": "Loggade du in med Apple eller Google första gången måste du använda samma sätt igen — vi kan inte slå ihop två konton i efterhand. Under <strong>Ditt konto → Inloggningssätt</strong> kopplar du flera sätt till samma konto, vilket är värt att göra innan du byter telefon.",
  "sp.acc.p2": "Valde du Apples <strong>Dölj min e-postadress</strong> blir reläadressen ditt konto. Att då logga in med e-postkod på din riktiga adress skapar ett nytt, tomt konto i stället för att släppa in dig på det gamla — lägg i stället till din riktiga adress under Inloggningssätt.",
  "sp.owner.h": "Ägaren har slutat",
  "sp.owner.p": "Ägaren kan överlåta gruppen till vem som helst i den. Har hen redan försvunnit kan en admin begära övertagande efter 30 dagars inaktivitet; alla i gruppen ser begäran och den träder i kraft efter sju dagar om ägaren inte loggar in.",
  "sp.pay.h": "Vad händer om vi slutar betala",
  "sp.pay.p": "Ingen data raderas. Gruppen går in i respit i fjorton dagar och pausas sedan: din egen tid kan du fortsätta rapportera och se, medan den delade delen — gruppstatistik, export och nya medlemmar — är släckt tills någon uppgraderar.",
  "sp.hol.h": "Fel dagar räknas som lediga",
  "sp.hol.p": "Röda dagar följer gruppens land, som ställs in under <strong>Gruppens inställningar → Arbetstid → Röda dagar</strong>. Tyskland och Storbritannien kan också välja förbundsland respektive del. Välj <em>Inget land</em> om gruppen följer en egen kalender.",
  "sp.off.h": "Fungerar appen utan internet",
  "sp.off.p": "Ja. Poster du skriver offline köas lokalt och synkas när täckningen kommer tillbaka. Timern kräver dock nät, eftersom den ägs av servern och delas mellan dina enheter.",
},
"de": {
  "title": "TimeTime — Zeiterfassung für Teams",
  "meta": "Zeit erfassen mit drei Tipps, auf die gemeinsamen Tätigkeiten deiner Gruppe. Ein Link lädt deine Kolleginnen und Kollegen ein. iPhone und Android.",
  "og": "Drei Tipps für einen ganzen Tag. Ein Link, um das Team einzuladen.",
  "hero.eyebrow": "Zeiterfassung für Teams · iPhone &amp; Android",
  "hero.h1": 'Zeit, die dein Team <span class="em">wirklich</span> erfasst',
  "hero.sub": "Drei Tipps für einen ganzen Tag. Ein Link, um das Team einzuladen. Keine Verwaltung, keine Zugänge zu verteilen.",
  "hero.t1": "Kostenlos für bis zu 3 Personen", "hero.t2": "Funktioniert offline", "hero.t3": "Niemand sieht deine Zeit, wenn ihr es nicht wollt",
  "badge.soon": "Bald verfügbar im",
  "stage.title": "Donnerstag, 6. August", "stage.of": "von 8h · noch 2h 45m",
  "s.title": "Die ganze App in vier Tabs",
  "s.lead": "Den Tag erfassen, die Woche sehen, die Zeit verfolgen — und das Team einladen.",
  "s.day": "Tag", "s.week": "Woche", "s.stats": "Statistik", "s.group": "Gruppe",
  "f.title": "Gebaut für wenig Aufwand",
  "f.lead": "Zeiterfassung muss man machen, nicht wollen. Deshalb verkürzt jede Entscheidung in der App den Weg vom Gedanken zum gespeicherten Eintrag.",
  "f1.h": "Drei Tipps", "f1.p": "Öffnen, Tätigkeit wählen, speichern. Nachträglich eintragen oder einen Timer starten — beides sind vollwertige Wege, keiner ist ein Nachgedanke.",
  "f2.h": "Ein Link lädt ein", "f2.p": "Link teilen, und die Kollegin ist sofort dabei. Keine Freigabe, keine Einladungscodes, die per E-Mail herumgehen.",
  "f3.h": "Funktioniert offline", "f3.p": "Einträge werden lokal gespeichert und synchronisiert, sobald wieder Netz da ist. Keine Zeit geht im Zug oder im Keller verloren.",
  "f4.h": "Widget und Timer", "f4.p": "30 oder 60 Minuten direkt vom Home-Bildschirm eintragen. Ein laufender Timer erscheint auf dem Sperrbildschirm und in der Dynamic Island.",
  "f5.h": "Der Kalender deines Landes", "f5.p": "Feiertage für dein Land — auch für jedes Bundesland — damit ein freier Tag nie als fehlende Zeit erscheint.",
  "p.title": "Datenschutz, der eingebaut ist, nicht versprochen",
  "p.lead": "Die Gruppe entscheidet selbst, wie viel geteilt wird — und die Regeln setzt die Datenbank durch, nicht die Oberfläche.",
  "p1.h": "Offen", "p1.p": "Alle Mitglieder sehen die Einträge und Namen aller. Gut für kleine Teams, die ohnehin zusammensitzen.",
  "p2.h": "Summiert", "p2.p": "Summen pro Tätigkeit, ohne Namen. Ihr seht, wohin die Zeit geht — aber niemand sieht, wer was gemacht hat.",
  "p3.h": "Privat", "p3.p": "Alle sehen nur ihre eigene Zeit. Der Inhaber kann Summen für die Auswertung exportieren.",
  "p.note": "Niemand kann die Zeit anderer ändern — auch nicht der Inhaber. Das ist eine bewusste Regel, keine Lücke.",
  "pr.title": "Preise", "pr.lead": "Der Inhaber bezahlt für die ganze Gruppe. Kein Mitglied stößt je auf eine Bezahlschranke.",
  "pr0.h": "Kostenlos", "pr0.p": "Bis zu 3 Personen. Ohne Zeitlimit.",
  "pr1.h": "Team", "pr1.p": "Bis zu 10 Personen.",
  "pr2.h": "Größeres Team", "pr2.p": "Bis zu 25 Personen.",
  "pr3.h": "Unbegrenzt", "pr3.p": "Beliebig viele.",
  "pr.local": "Monatlich, in deiner Landeswährung — der Preis steht im App Store und bei Google Play.",
  "pr.note": "Der vollständige Verlauf und der CSV-Export sind in jeder Stufe enthalten. 14 Tage Testphase ohne Platzlimit — und wenn ihr nicht mehr zahlt, wird nichts gelöscht: Die Gruppe pausiert, und nach einem Upgrade ist alles wieder da.",
  "foot.privacy": "Datenschutz", "foot.support": "Support", "foot.home": "Zur Startseite", "lang.aria": "Sprache",
  "pv.title": "Datenschutzerklärung", "pv.updated": "Zuletzt aktualisiert am 24. September 2026",
  "pv.store.h": "Was wir speichern",
  "pv.store.p": "Deine E-Mail-Adresse (für die Anmeldung), deinen Anzeigenamen und die Zeit, die du selbst erfasst: Datum, Tätigkeit, Minuten, gegebenenfalls Uhrzeiten und Notizen. Außerdem speichern wir, in welchen Gruppen du Mitglied bist.",
  "pv.store.p2": "Damit deine tägliche Erinnerung zur richtigen Zeit kommt und deine Anmeldecodes in deiner Sprache, speichern wir auch deine Zeitzone und die Sprache der App. Beides wird vom Telefon übernommen; du gibst es nie selbst ein.",
  "pv.signin.h": "Anmeldung",
  "pv.signin.p": "Du kannst dich mit einem Einmalcode per E-Mail, mit Apple oder mit Google anmelden. Wählst du Apple oder Google, erhalten wir von dort deine E-Mail-Adresse und deinen Namen — sonst nichts.",
  "pv.signin.p2": 'Wählst du Apples <strong>E-Mail-Adresse verbergen</strong>, sehen wir nur die Weiterleitungsadresse, nie deine echte. Diese Adresse wird dann dein Konto. Gut zu wissen: Meldest du dich später mit einer anderen Methode über deine echte Adresse an, passen die beiden nicht zusammen und werden zwei getrennte Konten. Unter <a href="{support}">Support</a> steht, wie du mehrere Anmeldemethoden mit demselben Konto verbindest.',
  "pv.sees.h": "Wer deine Zeit sieht",
  "pv.sees.p": "Das hängt vom Sichtbarkeitsmodus der Gruppe ab, den der Inhaber wählt. Im offenen Modus sehen die Mitglieder die Einträge der anderen. Im summierten Modus werden nur Summen pro Tätigkeit angezeigt — niemand sieht, wer was gemacht hat. Im privaten Modus sehen alle nur ihre eigene Zeit. Niemand kann die Zeit anderer ändern, auch nicht der Inhaber.",
  "pv.not.h": "Was wir nicht tun",
  "pv.not.p": "Wir verkaufen deine Daten nicht, geben sie nicht an Werbenetzwerke weiter und verfolgen dich nicht über Apps oder Websites hinweg.",
  "pv.sub.h": "Auftragsverarbeiter",
  "pv.sub.p": "Die Daten liegen bei Supabase in der EU. E-Mails werden über Resend verschickt. Mitteilungen laufen über Apple bzw. Google. Zahlungen wickeln der App Store und Google Play ab — deine Kartendaten sehen wir nie. Die Feiertagskalender stammen von Nager.Date; dorthin werden keine personenbezogenen Daten übermittelt.",
  "pv.rights.h": "Deine Rechte",
  "pv.rights.p": "Auskunft und Löschung erledigst du direkt in der App, unter <strong>Dein Konto</strong> (die Schaltfläche mit deinen Initialen).",
  "pv.rights.p2": "<strong>Meine Daten herunterladen</strong> liefert eine JSON-Datei mit deinem Konto, deinen Mitgliedschaften und aller Zeit, die du selbst erfasst hast. Die Zeit anderer ist nie enthalten, auch nicht in offenen Gruppen — das sind ihre Daten, nicht deine. Die Datei braucht kein Abo und funktioniert auch in archivierten Gruppen.",
  "pv.rights.p3": '<strong>Mein Konto löschen</strong> entfernt deine Zeit und deine Mitgliedschaften. Gruppen, deren Inhaber du bist, gehen an ein verbleibendes Mitglied über oder werden gelöscht, wenn du allein bist. Brauchst du dabei Hilfe, schreib an <a href="mailto:support@timetime.work">support@timetime.work</a>.',
  "pv.contact.h": "Kontakt",
  "sp.intro": 'Schreib an <a href="mailto:support@timetime.work">support@timetime.work</a>, wir antworten so schnell wie möglich.',
  "sp.full.h": "Ich komme nicht in die Gruppe",
  "sp.full.p": "Die kostenlose Stufe bietet Platz für drei Personen. Ist die Gruppe voll, kannst du den Code trotzdem in der App eingeben und den Inhaber um einen Platz bitten — du wirst automatisch hineingelassen, sobald ein Platz frei wird.",
  "sp.acc.h": "Ich komme nicht in mein Konto",
  "sp.acc.p": "Hast du dich beim ersten Mal mit Apple oder Google angemeldet, musst du dieselbe Methode wieder verwenden — zwei Konten lassen sich nachträglich nicht zusammenführen. Unter <strong>Dein Konto → Anmeldemethoden</strong> verbindest du mehrere Methoden mit demselben Konto. Das lohnt sich vor einem Telefonwechsel.",
  "sp.acc.p2": "Hast du Apples <strong>E-Mail-Adresse verbergen</strong> gewählt, ist die Weiterleitungsadresse dein Konto. Eine Anmeldung per E-Mail-Code mit deiner echten Adresse legt dann ein neues, leeres Konto an, statt dich in das alte zu lassen — füge deine echte Adresse lieber unter Anmeldemethoden hinzu.",
  "sp.owner.h": "Der Inhaber ist nicht mehr da",
  "sp.owner.p": "Der Inhaber kann die Gruppe an jedes Mitglied übertragen. Ist er schon weg, kann ein Admin nach 30 Tagen Inaktivität die Übernahme beantragen; alle in der Gruppe sehen den Antrag, und er wird nach sieben Tagen wirksam, wenn sich der Inhaber nicht anmeldet.",
  "sp.pay.h": "Was passiert, wenn wir nicht mehr zahlen",
  "sp.pay.p": "Es werden keine Daten gelöscht. Die Gruppe hat vierzehn Tage Schonfrist und wird dann pausiert: Deine eigene Zeit kannst du weiter erfassen und sehen, während der gemeinsame Teil — Gruppenstatistik, Export und neue Mitglieder — bis zu einem Upgrade ruht.",
  "sp.hol.h": "Die falschen Tage gelten als frei",
  "sp.hol.p": "Feiertage richten sich nach dem Land der Gruppe, einstellbar unter <strong>Gruppeneinstellungen → Arbeitszeit → Feiertage</strong>. In Deutschland lässt sich zusätzlich das Bundesland wählen — ohne Auswahl gelten nur die bundesweiten Feiertage. Wähle <em>Kein Land</em>, wenn die Gruppe einem eigenen Kalender folgt.",
  "sp.off.h": "Funktioniert die App ohne Internet",
  "sp.off.p": "Ja. Einträge, die du offline machst, werden lokal gespeichert und synchronisiert, sobald wieder Netz da ist. Der Timer braucht allerdings eine Verbindung, weil er auf dem Server liegt und zwischen deinen Geräten geteilt wird.",
},
}

# Priserna i kronor bara på svenska: beloppen i andra valutor är inte beslutade
# (brief §11, beslut 13), och kronor för en tysk vore fel valuta.
SEK = {"pr0": "0 kr", "pr1": "149 kr", "pr2": "299 kr", "pr3": "499 kr"}

# ---------------------------------------------------------------------------

CSS = "/assets/site.css"


def url(lang: str, page: str) -> str:
    return f"/{PREFIX[lang]}" + ("" if page == "index" else f"{page}.html")


def head(lang: str, page: str, title: str, description: str | None = None) -> str:
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}{url(l, page)}">' for l in LANGS
    )
    desc = f'<meta name="description" content="{description}">\n' if description else ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{desc}{alternates}
<link rel="alternate" hreflang="x-default" href="{SITE}{url('en', page)}">
<link rel="icon" href="/assets/icon.png">
<link rel="stylesheet" href="{CSS}">
"""


def lang_links(lang: str, page: str) -> str:
    # Riktiga länkar, inte en JavaScript-knapp: språket ska gå att byta även
    # utan skript, och varje språk har en egen adress som går att dela.
    items = " · ".join(
        f'<a href="{url(l, page)}" hreflang="{l}" lang="{l}"'
        + (' aria-current="page"' if l == lang else "")
        + f">{LABEL[l]}</a>"
        for l in LANGS
    )
    return f'<nav class="langs" aria-label="{T[lang]["lang.aria"]}">{items}</nav>'


# På alla sidor: ett klick på ett språk sparas, så att roten sedan respekterar
# valet — annars skickas den som valt English från /sv/ tillbaka till svenskan.
LANG_SCRIPT = """<script>
document.querySelectorAll(".langs a").forEach(function (a) {
  a.addEventListener("click", function () {
    try { localStorage.setItem("timetime-lang", a.getAttribute("hreflang")); } catch (e) {}
  });
});
</script>"""

# Bara i roten: den som kommer utan språk i adressen och inte valt något skickas
# till sitt språk. Utan JavaScript står språklänkarna där i stället.
ROOT_SCRIPT = """<script>
(function () {
  var saved = null;
  try { saved = localStorage.getItem("timetime-lang"); } catch (e) {}
  var want = saved || (navigator.language || "").slice(0, 2).toLowerCase();
  if (want === "sv" || want === "de") {
    location.replace("/" + want + "/" + location.pathname.replace(/^\\//, "") + location.hash);
  }
})();
</script>"""

STORE_BADGE = """<span class="store soon">
  <svg viewBox="0 0 180 54" role="img" aria-label="{name}" xmlns="http://www.w3.org/2000/svg">
    <rect width="180" height="54" rx="12" fill="#161616"/>
    <g fill="#fff">
      <path d="{icon}"/>
      <text x="54" y="24" font-family="Helvetica,Arial,sans-serif" font-size="9" fill="#a1a1a1">{soon}</text>
      <text x="54" y="41" font-family="Helvetica,Arial,sans-serif" font-size="17" font-weight="700" fill="#fff">{name}</text>
    </g>
  </svg>
</span>"""
APPLE_ICON = "M37 26.9c0-3 2.4-4.4 2.5-4.5-1.4-2-3.5-2.3-4.2-2.3-1.8-.2-3.5 1-4.4 1-.9 0-2.3-1-3.8-1-1.9 0-3.7 1.1-4.7 2.9-2 3.5-.5 8.7 1.4 11.5.9 1.4 2 2.9 3.5 2.9 1.4-.1 1.9-.9 3.6-.9s2.2.9 3.7.9c1.5 0 2.5-1.4 3.4-2.8 1.1-1.6 1.5-3.1 1.6-3.2-.1 0-3-1.2-3-4.4zM34.2 18.2c.8-1 1.3-2.3 1.2-3.7-1.1 0-2.5.8-3.3 1.7-.7.8-1.4 2.2-1.2 3.5 1.3.1 2.5-.6 3.3-1.5z"
PLAY_ICON = "M24 15.6c-.5.5-.8 1.3-.8 2.3v18.2c0 1 .3 1.8.8 2.3l.1.1 10.2-10.2v-2.4L24.1 15.5l-.1.1zm13.7 13.1-3.4-3.4 3.4-3.4 4.1 2.3c1.2.7 1.2 1.8 0 2.5l-4.1 2.3v-.3zm-1.1.6L33.1 26l-7.9 7.9c.4.4 1 .5 1.8.1l9.6-5.4v.7zm0-8.6-9.6-5.4c-.8-.4-1.4-.3-1.8.1l7.9 7.9 3.5-3.5v.9z"


def footer(lang: str, page: str) -> str:
    t = T[lang]
    return f"""<footer><div class="wrap">
  <p><a href="{url(lang, 'privacy')}">{t['foot.privacy']}</a> ·
     <a href="{url(lang, 'support')}">{t['foot.support']}</a> ·
     <a href="mailto:support@timetime.work">support@timetime.work</a></p>
  <p class="langline">{lang_links(lang, page)}</p>
  <p>© 2026 JMS Software</p>
</div></footer>"""


def index(lang: str) -> str:
    t = T[lang]
    price = (lambda k: f'<div class="amount">{SEK[k]}' + ("" if k == "pr0" else '<span class="unit">/mån</span>') + "</div>") \
        if lang == "sv" else (lambda k: "")
    cards = "".join(
        f'<div class="card"><span class="dot" style="background:{c}"></span><h3>{t[k + ".h"]}</h3><p>{t[k + ".p"]}</p></div>'
        for k, c in [("f1", "#B03A22"), ("f2", "#4E7C7F"), ("f3", "#7A6A9C"), ("f4", "#C9A94A"), ("f5", "#5A6066")]
    )
    privacy_cards = "".join(
        f'<div class="card"><h3>{t[k + ".h"]}</h3><p>{t[k + ".p"]}</p></div>' for k in ["p1", "p2", "p3"]
    )
    price_cards = "".join(
        f'<div class="price-card{" hi" if k == "pr1" else ""}"><h3>{t[k + ".h"]}</h3>{price(k)}<p>{t[k + ".p"]}</p></div>'
        for k in ["pr0", "pr1", "pr2", "pr3"]
    )
    # Riktiga skärmdumpar, på sidans eget språk (samma bilder som i butikerna,
    # nedskalade till WebP i assets/screens/<språk>/).
    shot_dir = {"en": "en", "sv": "sv", "de": "de"}[lang]
    shots = "".join(
        f'<figure><img src="/assets/screens/{shot_dir}/{k}.webp" width="600" height="1304" '
        f'loading="lazy" alt="{t["s." + k]}"><figcaption>{t["s." + k]}</figcaption></figure>'
        for k in ["day", "week", "stats", "group"]
    )
    badges = STORE_BADGE.format(name="App Store", icon=APPLE_ICON, soon=t["badge.soon"]) + \
        STORE_BADGE.format(name="Google Play", icon=PLAY_ICON, soon=t["badge.soon"])
    return head(lang, "index", t["title"], t["meta"]) + f"""<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['og']}">
<meta property="og:image" content="{SITE}/assets/icon.png">
<meta property="og:type" content="website">
</head>
<body>
<div class="wrap">
  <header class="site">
    <a class="brand" href="{url(lang, 'index')}"><img src="/assets/icon.png" alt="">timetime</a>
    {lang_links(lang, 'index')}
  </header>
  <section class="hero" style="border:0">
    <div>
      <p class="eyebrow">{t['hero.eyebrow']}</p>
      <h1>{t['hero.h1']}</h1>
      <p class="sub">{t['hero.sub']}</p>
      <div class="cta">{badges}</div>
      <div class="trust"><span>{t['hero.t1']}</span><span>{t['hero.t2']}</span><span>{t['hero.t3']}</span></div>
    </div>
    <div class="stage" aria-hidden="true">
      <div class="stage-group">Nordvind AB</div>
      <div class="stage-title">{t['stage.title']}</div>
      <div class="daytotal"><span class="big">5h 15m</span><span class="of">{t['stage.of']}</span></div>
      <div class="bar"><i></i></div>
      <div class="rowline"><span class="tab" style="background:#B03A22"></span><span class="name">R&amp;D</span><span class="val">2h 30m</span></div>
      <div class="rowline"><span class="tab" style="background:#4E7C7F"></span><span class="name">Projekt Alva</span><span class="val">1h 45m</span></div>
      <div class="rowline"><span class="tab" style="background:#7A6A9C"></span><span class="name">Support</span><span class="val">1h 00m</span></div>
    </div>
  </section>
</div>
<section><div class="wrap">
  <h2>{t['s.title']}</h2><p class="lead">{t['s.lead']}</p>
  <div class="screens">{shots}</div>
</div></section>
<section><div class="wrap">
  <h2>{t['f.title']}</h2><p class="lead">{t['f.lead']}</p>
  <div class="grid">{cards}</div>
</div></section>
<section><div class="wrap">
  <h2>{t['p.title']}</h2><p class="lead">{t['p.lead']}</p>
  <div class="grid">{privacy_cards}</div>
  <p class="note">{t['p.note']}</p>
</div></section>
<section><div class="wrap">
  <h2>{t['pr.title']}</h2><p class="lead">{t['pr.lead']}</p>
  <div class="grid">{price_cards}</div>
  <p class="note">{t['pr.local']}</p>
  <p class="note">{t['pr.note']}</p>
</div></section>
{footer(lang, 'index')}
{LANG_SCRIPT}{ROOT_SCRIPT if lang == 'en' else ''}
</body>
</html>
"""


def doc(lang: str, page: str, title: str, body: str) -> str:
    t = T[lang]
    return head(lang, page, f"{title} — TimeTime") + f"""</head>
<body class="doc"><div class="wrap narrow">
<header class="site">
  <a class="brand" href="{url(lang, 'index')}"><img src="/assets/icon.png" alt="">timetime</a>
  {lang_links(lang, page)}
</header>
<h1>{title}</h1>
{body}
</div>
{footer(lang, page)}
{LANG_SCRIPT}{ROOT_SCRIPT if lang == 'en' else ''}
</body></html>
"""


def privacy(lang: str) -> str:
    t = T[lang]
    s = lambda k: t[k].replace("{support}", url(lang, "support"))
    body = f"""<p class="muted">{t['pv.updated']}</p>
<h2>{t['pv.store.h']}</h2><p>{s('pv.store.p')}</p><p>{s('pv.store.p2')}</p>
<h2>{t['pv.signin.h']}</h2><p>{s('pv.signin.p')}</p><p>{s('pv.signin.p2')}</p>
<h2>{t['pv.sees.h']}</h2><p>{s('pv.sees.p')}</p>
<h2>{t['pv.not.h']}</h2><p>{s('pv.not.p')}</p>
<h2>{t['pv.sub.h']}</h2><p>{s('pv.sub.p')}</p>
<h2>{t['pv.rights.h']}</h2><p>{s('pv.rights.p')}</p><p>{s('pv.rights.p2')}</p><p>{s('pv.rights.p3')}</p>
<h2>{t['pv.contact.h']}</h2><p>JMS Software · <a href="mailto:support@timetime.work">support@timetime.work</a></p>"""
    return doc(lang, "privacy", t["pv.title"], body)


def support(lang: str) -> str:
    t = T[lang]
    qa = "".join(f"<h2>{t[k + '.h']}</h2><p>{t[k + '.p']}</p>" + (f"<p>{t[k + '.p2']}</p>" if k + ".p2" in t else "")
                 for k in ["sp.full", "sp.acc", "sp.owner", "sp.pay", "sp.hol", "sp.off"])
    return doc(lang, "support", "Support", f"<p>{t['sp.intro']}</p>{qa}")


def main():
    keys = set(T["en"])
    for lang in LANGS:
        missing, extra = keys - set(T[lang]), set(T[lang]) - keys
        if missing or extra:
            raise SystemExit(f"{lang}: saknas {sorted(missing)}, extra {sorted(extra)}")
    for lang in LANGS:
        out = ROOT / PREFIX[lang]
        out.mkdir(exist_ok=True)
        for name, render in [("index", index), ("privacy", privacy), ("support", support)]:
            (out / f"{name}.html").write_text(render(lang))
    print("byggt:", ", ".join(f"/{PREFIX[l]}" or "/" for l in LANGS))


if __name__ == "__main__":
    main()
