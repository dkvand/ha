# Din egen AI-hjælper til Home Assistant — gratis

En AI (Claude-appen eller Google Antigravity) på din egen computer, med fuld adgang til din Home
Assistant: SSH, token og MCP. Plus daglig backup til Google Drive og (valgfrit) automatisk git-sync
til GitHub.

**Hvorfor:** Der dukker betalte guides og kurser op til præcis det her. Det er ikke svært nok til at
koste penge, og det burde være frit tilgængeligt. Så her er det.

## Sådan bruger du det

**Hent begge filer på én gang:** [ZIP under Releases](https://github.com/dkvand/ha/releases/latest)
→ `ha-guide.zip` → pak den ud.

Du skal have **Home Assistant OS** (det almindelige: Green/Yellow, Raspberry Pi eller en virtuel
maskine). Kører du HA i Docker (*Container*), virker guiden ikke.

| Fil | Til hvem |
|---|---|
| [`Vejledning-AI-hjaelper-Home-Assistant.pdf`](Vejledning-AI-hjaelper-Home-Assistant.pdf) | Dig. Læs den og følg Del 1 (~20 min). |
| [`GUIDE.md`](GUIDE.md) | Din AI. Kopiér den ind i mappen `ha-config`, og bed AI'en om at læse den. AI'en laver resten og siger til, når du skal klikke. |

Du behøver ikke kunne programmere. AI'en laver terminal-arbejdet; du klikker i Home Assistant og
indsætter et token i en fil (aldrig i chatten).

## Før du går i gang

- Giver du en AI fuld adgang, kan den også ødelægge noget. Guiden tager en fuld backup og en
  git-kopi, før AI'en ændrer noget, så alt kan rulles tilbage — men læs afsnittet **"Godt at vide"**.
- Åbn aldrig Home Assistant mod internettet for at få det her til at virke.
- Guiden er testet i dele, ikke fra ende til anden på en helt ny installation. Finder du en fejl,
  så opret et [issue](https://github.com/dkvand/ha/issues) eller send en rettelse.

## Byg PDF'en selv

`tools/build_pdf.py` laver HTML ud af `GUIDE.md` (uden Del 2, som kun er til AI'en); print den til
PDF med Chrome/Chromium:

```bash
uvx --with markdown python tools/build_pdf.py GUIDE.md guide.html
chromium --headless --no-pdf-header-footer --print-to-pdf=guide.pdf guide.html
```

## Licens

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.da) — brug, kopiér, ret og del frit,
også kommercielt. Bare nævn, hvor det kommer fra. Sælg det gerne videre, men folk kan finde det gratis her.
