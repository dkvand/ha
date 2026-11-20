# Din egen AI-hjælper til Home Assistant

Når du er færdig, kan du skrive til en AI på din computer, fx *"tænd lyset i køkkenet ved
solnedgang"*, og den laver automationen i Home Assistant for dig. Den kan også finde fejl,
rydde op og tage backup.

## Sådan bruger du guiden

| Del | Hvem | Tid |
|---|---|---|
| **Del 1: Kom i gang** | **Dig.** Installér AI'en, og giv den filen `GUIDE.md`. | ca. 20 min |
| **Del 2: Agentens opgaver** | **AI'en.** Står kun i `GUIDE.md`, og du behøver ikke læse den. | ca. 45 min |
| **Del 3: Klik-vejledninger** | **Dig**, når AI'en beder om det | et par min hver |

Du skal aldrig selv skrive kommandoer. AI'en skriver dem, og du klikker og kopierer.

> 🆘 **Sidder du fast?** Tag et skærmbillede, og spørg i en Home Assistant-gruppe, eller opret et issue på github.com/dkvand/ha.

**Du skal bruge:**

- Home Assistant, som du kan åbne i browseren
- En computer (Mac, Windows eller Linux) på **samme netværk** som Home Assistant
- En Google-konto

---

# Del 1: Kom i gang (dig)

## 1. Vælg din AI

Begge virker. Vælg den, du har lyst til.

| | **Google Antigravity** | **Claude (appen)** |
|---|---|---|
| Ser ud som | Et program med vinduer og knapper | Et program med en chat (fanen **Code**) |
| Login | Din Google-konto (gratis at starte) | Kræver Claude Pro eller højere (gratis-kontoen kan ikke bruge **Code**) |
| Pris | Se [Googles prisside](https://one.google.com/about/google-ai-plans/) | Se [Anthropics prisside](https://claude.com/pricing) |
| Anbefalet hvis | Du bruger Google til alt | Du allerede betaler for Claude |

## 2. Installér git

Git er et lille program, der husker alle ændringer, så AI'en kan fortryde sine fejl.

- **Windows:** Hent [Git for Windows](https://git-scm.com/download/win). Klik **Next** hele vejen
  igennem, og til sidst **Install**.
- **Mac:** Tryk `Cmd + Mellemrum`, skriv `Terminal`, og tryk Enter. Skriv `git --version`, og tryk
  Enter. Kommer der et vindue, så tryk **Installér**, og vent.
- **Linux:** Det er der som regel allerede.

## 3. Installér AI'en

### Hvis du valgte Antigravity

1. Hent den på [antigravity.google/download](https://antigravity.google/download), og installér som
   ethvert andet program
2. Åbn den, og log ind med din Google-konto

### Hvis du valgte Claude

1. Hent Claude-appen på [claude.ai/download](https://claude.ai/download) (Mac og Windows; Linux
   er beta), og installér som ethvert andet program
2. Åbn den, og log ind med din Claude-konto

## 4. Lav en mappe, og læg `GUIDE.md` i den

1. Lav en mappe, der hedder **`ha-config`**, i din hjemmemappe (der hvor *Dokumenter* og *Overførsler* ligger)
2. Kopiér filen **`GUIDE.md`**, som du fik sammen med denne vejledning, ind i mappen. Navnet skal
   være præcis `GUIDE.md`.

## 5. Start AI'en i mappen

- **Antigravity:** **File → Open Folder** → vælg `ha-config`. Åbn chatten/agent-panelet.
- **Claude:** Åbn appen → fanen **Code** → under beskedfeltet: vælg **Local** → tryk på
  mappe-knappen ved siden af → **Open folder…** → vælg `ha-config`.
  Claude spørger om lov, før den kører en kommando. Læs, hvad den vil, og tryk **Tillad**.

## 6. Kopiér denne besked ind til AI'en

```text
Læs GUIDE.md og udfør "Del 2: Agentens opgaver", én opgave ad gangen.
Jeg er ikke teknisk. Forklar kort på dansk, hvad du gør, og sig præcis,
hvad jeg skal klikke på, når du har brug for mig (henvis til Del 3).
Bed mig aldrig skrive et password eller en kode i chatten.
```

Herfra fører AI'en dig igennem resten. Den spørger, før den kører noget. Tryk **ja/tillad**, når
den beder om det. Er du i tvivl, så spørg den: *"Hvad gør det?"*

> Lukker du AI'en undervejs, så start den igen i samme mappe, og skriv: **"Fortsæt med guiden."**
> Den husker, hvor I kom til.

---

# Del 2: Agentens opgaver (AI'en)

> **Til agenten.** Brugeren er ikke teknisk. Regler for hele Del 2:
> 1. Én opgave ad gangen. Tjek, at den virker, før du går videre.
> 2. Efter hver opgave: skriv én linje i `FREMSKRIDT.md` (`✅ 2.3 SSH virker`). Ved start: læs den,
>    og fortsæt, hvor I slap.
> 3. Når du skal bruge brugeren: sig hvilken klik-vejledning i Del 3, giv brugeren det, der skal
>    kopieres, og vent på "færdig".
> 4. **Hemmeligheder** (tokens, passwords) skal aldrig stå i chatten. Brugeren indsætter dem i
>    `~/.profile`, som du åbner for brugeren i en editor. Du må aldrig udskrive en værdi fra den.
>    Test om en variabel er sat med `echo ${HA_TOKEN:+sat}`.
> 5. Find selv ud af, om det er Mac, Windows (Git Bash) eller Linux, og tilpas kommandoerne.
> 6. Rør aldrig `.storage/` i Home Assistant. Genstart aldrig HA uden at spørge.

## 2.1 Find Home Assistant på netværket

Prøv `curl -s -o /dev/null -w '%{http_code}' http://homeassistant.local:8123/` (forvent `200`).
Virker navnet ikke, så bed brugeren om HA's IP-adresse (**Klik A**), og brug den i stedet for
`homeassistant.local` i resten af guiden.

## 2.2 Lav nøglefilen `~/.profile`

Tilføj nederst i `~/.profile` (opret den, hvis den ikke findes). Kun én gang, og tjek først, at
blokken ikke allerede står der:

```bash

# ===== Adgang til huset — HEMMELIG: aldrig i git, aldrig i en chat =====

# Home Assistant
export HA_URL="http://homeassistant.local:8123"
export HA_TOKEN="INDSÆT_TOKEN_HER"
ha_ssh() { ssh -i "$HOME/.ssh/ha" -o StrictHostKeyChecking=accept-new root@homeassistant.local "$@"; }

# Andre adgange — én linje pr. tjeneste, efterhånden som de kommer
# export MQTT_USER=""
# export MQTT_PASSWORD=""
```

Kør `chmod 600 ~/.profile`. Åbn så filen i en editor, som brugeren kan bruge (Mac:
`open -e ~/.profile`, Windows: `notepad "$(cygpath -w ~/.profile)"`, Linux: `xdg-open ~/.profile`),
og bed brugeren følge **Klik B** (lav token og indsæt det).

Test:
```bash
source ~/.profile
curl -s -H "Authorization: Bearer $HA_TOKEN" "$HA_URL/api/"   # forvent {"message":"API running."}
```

**Husk:** start hver kommando, der skal bruge adgangene, med `source ~/.profile`. Den bliver ikke
læst automatisk i din shell.

## 2.3 SSH-adgang

```bash
mkdir -p ~/.ssh && ssh-keygen -t ed25519 -f ~/.ssh/ha -N "" -C ai-laptop
```

Byg den **komplette** YAML herunder med indholdet af `~/.ssh/ha.pub` indsat, og giv den til
brugeren med **Klik C**:

```yaml
ssh:
  username: root
  password: ""
  authorized_keys:
    - INDHOLDET_AF_HA.PUB
  sftp: true
  compatibility_mode: false
  allow_agent_forwarding: false
  allow_remote_port_forwarding: false
  allow_tcp_forwarding: false
zsh: false
share_sessions: false
packages: []
init_commands: []
```

Test: `source ~/.profile && ha_ssh "ha core info"` skal vise version og status.

## 2.4 Hent konfigurationen ned, og sæt git op

```bash
cd ~/ha-config
source ~/.profile
ha_ssh "tar czf - -C /config --exclude=.storage --exclude='*.db*' --exclude='*.log*' \
  --exclude=deps --exclude=tts --exclude=backups ." | tar xzf -
```

Opret `.gitignore`:
```text
.storage/
.ssh/
secrets.yaml
*.db*
*.log*
deps/
tts/
backups/
.cloud/
zigbee2mqtt/log/
```

Sæt git op. Brug brugerens navn, og spørg brugeren om e-mailen, hvis `git config --global user.email`
er tom:
```bash
git init -b main && git add -A && git commit -m "Udgangspunkt fra Home Assistant"
```

## 2.5 Husreglerne

Opret `AGENTS.md` i `~/ha-config` med dette indhold (tilpas værtsnavnet, hvis du brugte en IP i 2.1):

````markdown
# Home Assistant — husregler for AI-agenten

Denne mappe er en kopi af `/config` på Home Assistant. **Ændringer her gør intet**, før de er
kopieret over til HA. Brugeren er ikke teknisk: forklar kort på dansk, og spørg før store skridt.

## Adgang
- Alle adgange ligger i `~/.profile`. Start kommandoer med `source ~/.profile`.
- Den giver `HA_URL`, `HA_TOKEN` m.fl. og funktionen `ha_ssh` (SSH til HA).
- 🚨 Udskriv aldrig en værdi fra `~/.profile`. Test med `echo ${HA_TOKEN:+sat}`.
- Mangler der en adgang: tilføj en tom linje i `~/.profile`, åbn filen for brugeren, og lad brugeren
  indsætte værdien.
- MCP-serveren `homeassistant` kan styre de eksponerede enheder direkte.

## Sådan gennemfører du en ændring
```bash
source ~/.profile
ha_ssh "ha backups new --name før-<ændring>"     # ved større ændringer
tar czf - <de ændrede filer> | ha_ssh "tar xzf - -C /config"
ha_ssh "ha core check"                            # SKAL bestå
ha_ssh "ha core restart"                          # spørg brugeren først
ha_ssh "ha core logs | tail -50"                  # se efter ERROR
```

## Regler
1. Tjek, at entity_id'er findes, før du bruger dem: `curl -s -H "Authorization: Bearer $HA_TOKEN" "$HA_URL/api/states"`
2. Brug `entity_id`, aldrig `device_id`.
3. Rør aldrig `.storage/`.
4. HA omskriver `automations.yaml`, når man retter i UI'et. Hent den nyeste fra HA, før du retter i den.
5. Navne på automationer og dashboards skrives på dansk.
6. Commit i git efter hver ændring, der virker.
7. Spørg, før du genstarter HA eller sletter noget.
````

Bruges **Claude**, så opret også `CLAUDE.md` med den ene linje `@AGENTS.md`.
Antigravity læser selv `AGENTS.md`. Commit begge.

## 2.6 Forbind MCP (AI'en styrer huset direkte)

Bed først brugeren om **Klik D** (MCP i HA). Derefter:

- **Claude (appen):** Tilføj serveren under `mcpServers` i `~/.claude.json` (bevar alt andet i
  filen). Skriv den med et lille script, der læser `HA_TOKEN` fra miljøet:
  ```json
  { "mcpServers": { "homeassistant": { "type": "http",
      "url": "http://homeassistant.local:8123/api/mcp",
      "headers": { "Authorization": "Bearer <HA_TOKEN>" } } } }
  ```
  Bed brugeren om at lukke appen **helt** (Mac: `Cmd + Q`; Windows: højreklik på ikonet ved uret →
  Quit) og åbne den igen. Test: skriv `/mcp` i beskedfeltet, og se, om **homeassistant** står
  på listen. Gør den ikke, så spring MCP over: REST og SSH kan det samme.
- **Antigravity:** Tilføj serveren i `~/.gemini/config/mcp_config.json` (bevar eksisterende servere).
  Skriv filen med et lille script, der læser `HA_TOKEN` fra miljøet, så tokenet aldrig står i chatten:
  ```json
  { "mcpServers": { "homeassistant": {
      "serverUrl": "http://homeassistant.local:8123/api/mcp",
      "headers": { "Authorization": "Bearer <HA_TOKEN>" } } } }
  ```

Bed brugeren om at genstarte AI'en og skrive *"Fortsæt med guiden"*. Test bagefter ved at spørge
MCP: *hvilke lys er tændt?*

## 2.7 Backup til Google Drive

Bed brugeren om **Klik E** (Google-nøgler) og bagefter **Klik F** (backup i HA). Tjek bagefter
med brugeren, at der ligger en backup i mappen `Home Assistant` i brugerens Drive.

## 2.8 (Valgfri) HA gemmer selv sin config på GitHub hver nat

Spørg brugeren, om det ønskes. Forklar: *"Så gemmes alle ændringer, også dem du laver i
HA's skærmbilleder, hver nat på GitHub, og man kan altid se og fortryde dem."* Er svaret nej, så
spring over.

1. **Klik G** (GitHub-konto og login). Tjek med `gh auth status`.
2. Repo og nøgle (HA's nøgle kan kun skrive til dette ene repo). 🚨 Repoet skal være **privat**:
   `/config` indeholder adresser, passwords og hvornår folk er hjemme. Står der ikke `PRIVATE`,
   så stop og sig det til brugeren.
   ```bash
   source ~/.profile
   gh repo create ha-config --private
   gh repo view ha-config --json visibility --jq .visibility   # skal give PRIVATE
   ha_ssh 'mkdir -p /config/.ssh /config/scripts &&
     ssh-keygen -t ed25519 -f /config/.ssh/github -N "" -C ha-git-sync &&
     ssh-keyscan github.com > /config/.ssh/known_hosts'
   ha_ssh 'cat /config/.ssh/github.pub' > /tmp/ha-github.pub
   gh repo deploy-key add /tmp/ha-github.pub --allow-write --title ha-git-sync -R "$(gh api user --jq .login)/ha-config"
   rm /tmp/ha-github.pub
   ```
3. Kopiér `.gitignore`, `AGENTS.md`, `CLAUDE.md` (hvis den findes), `GUIDE.md` og `FREMSKRIDT.md`
   til `/config` med `tar … | ha_ssh "tar xzf - -C /config"`.
4. Git på HA. 🚨 Tjek, at intet hemmeligt kommer med, **før** du pusher:
   ```bash
   U=$(gh api user --jq .login)
   ha_ssh "cd /config && git init -b main &&
     git config user.name 'Home Assistant' && git config user.email ha@localhost &&
     git config core.sshCommand 'ssh -i /config/.ssh/github -o UserKnownHostsFile=/config/.ssh/known_hosts' &&
     git remote add origin git@github.com:$U/ha-config.git && git add -A &&
     git status --short | grep -E '\.ssh/|\.storage/|secrets\.yaml' && echo STOP || echo ok"
   ```
   Kun hvis der står `ok`: `ha_ssh "cd /config && git commit -qm 'Første snapshot' && git push -u origin main"`.
   Fejler push på en fil over 100 MB: læg den i `.gitignore`, `git rm --cached` den, og commit igen.
5. Sync-scriptet, `/config/scripts/git-sync.sh`:
   ```sh
   #!/bin/sh
   # Commit and push /config if anything changed.
   cd /config || exit 1
   git add -A
   git diff --cached --quiet && exit 0
   git commit -q -m "Auto: $(date '+%Y-%m-%d %H:%M')"
   git push -q origin main
   ```
6. Tilføj i `/config/configuration.yaml` (under en eksisterende `shell_command:`, hvis den findes):
   ```yaml
   shell_command:
     git_sync: "sh /config/scripts/git-sync.sh"
   ```
   Kør `ha core check`. **Spørg brugeren**, og kør så `ha core restart` (en ny `shell_command`
   kræver en rigtig genstart).
7. Automation. Læg den i `automations.yaml`, eller giv den til brugeren til **Klik H**:
   ```yaml
   - id: git_sync_nat
     alias: "Git: gem konfigurationen"
     description: "Committer og pusher /config til GitHub hver nat"
     triggers:
       - trigger: time
         at: "03:30:00"
     actions:
       - action: shell_command.git_sync
         response_variable: svar
         continue_on_error: true
       - if:
           - condition: template
             value_template: "{{ svar is not defined or svar.returncode != 0 }}"
         then:
           - action: persistent_notification.create
             data:
               title: "Git-sync fejlede"
               message: "{{ svar.stderr if svar is defined else 'Intet svar fra scriptet' }}"
   ```
8. Test: kald `shell_command.git_sync` via API'et, og tjek, at GitHub har fået en ny commit.
9. Lad laptop-mappen følge GitHub uden at flytte den:
   ```bash
   cd ~/ha-config
   git remote add origin "https://github.com/$(gh api user --jq .login)/ha-config.git"
   git fetch origin && git reset --mixed origin/main && git branch -u origin/main
   git status --short     # bør være tom eller næsten tom; forklar brugeren resten
   ```
10. Erstat regel 6 i `AGENTS.md` med nedenstående, og deploy `AGENTS.md` til `/config`:
    ```markdown
    6. Laptoppen committer og pusher aldrig. HA gemmer selv i git.
       - Før arbejde: `git pull --ff-only`
       - Efter en deploy: `ha_ssh "sh /config/scripts/git-sync.sh"` og så `git add -A && git pull --ff-only`
       - Fejler den sidste pull, er noget på laptoppen ikke deployet. Stop, og forklar brugeren det.
    ```

## 2.9 Færdig

Skriv `✅ Færdig` i `FREMSKRIDT.md`. Vis brugeren, hvad der nu virker, og giv tre ting, brugeren kan
prøve at bede om. Fx: *"Find automationer, der ikke virker"*, *"Tænd lyset i entréen ved
solnedgang, hvis nogen er hjemme"*, *"Hvorfor kørte min automation i går ikke?"*

---

# Del 3: Klik-vejledninger (dig, når AI'en beder om det)

## Klik A: Find Home Assistants IP-adresse

1. Åbn Home Assistant i browseren
2. **Indstillinger → System → Netværk**
3. Under **IPv4** står et tal som `192.168.1.50`. Giv det til AI'en.

## Klik B: Lav et token, og indsæt det

AI'en har åbnet en fil for dig, hvor der står `INDSÆT_TOKEN_HER`.

1. Home Assistant → klik på **dit navn** nederst til venstre → fanen **Sikkerhed**
2. Rul helt ned til **Langtidsadgangstokens** → **Opret token** → navn: `ai` → **OK**
3. Tryk **kopiér**-ikonet. Tokenet vises kun denne ene gang.
4. I filen: markér `INDSÆT_TOKEN_HER` (lad anførselstegnene `"` stå), og sæt ind (`Ctrl+V` / `Cmd+V`)
5. Gem (`Ctrl+S` / `Cmd+S`), luk filen, og skriv **"færdig"** til AI'en

> Indsæt **aldrig** tokenet i chatten. Det er nøglen til hele dit hus.

## Klik C: SSH-adgang i Home Assistant

AI'en har givet dig en tekstblok, der starter med `ssh:`.

1. Klik på **dit navn** nederst til venstre → slå **Avanceret tilstand** til
2. **Indstillinger → Apps** (hedder *Tilføjelsesprogrammer* i ældre versioner) → knappen nederst
   til højre (**Butik** / **Installér app**)
3. Søg **Advanced SSH & Web Terminal** → klik på den → **Installér**. Vent.
4. Fanen **Konfiguration** → **⋮** øverst til højre → **Rediger i YAML** → slet alt i feltet →
   indsæt AI'ens tekstblok → **Gem**
5. Rul ned til **Netværk**: skriv `22` i feltet → **Gem**
6. Fanen **Info**: slå **Start ved opstart** og **Watchdog** til → **Start**. Skriv "færdig" til AI'en.

## Klik D: Slå MCP til i Home Assistant

1. **Indstillinger → Enheder og tjenester** → **Tilføj integration** (nederst til højre)
2. Søg **Model Context Protocol Server** → vælg den → **Send/OK**
3. **Indstillinger → Stemmeassistenter** → fanen **Eksponér**
4. Vælg det, AI'en må styre, fx lys. 🚨 **Ikke** stikkontakter til fryser, køleskab eller computer.
   Det, der står her, kan AI'en slukke.
5. Skriv "færdig" til AI'en

## Klik E: Lav Google-nøgler til backup (15 min, den kedeligste del)

Home Assistant skal have lov til at lægge filer i dit Google Drive. Det kræver to "nøgler" fra
Google, som du laver selv. Det er gratis og kræver intet betalingskort.

1. Gå til [console.cloud.google.com](https://console.cloud.google.com/), og log ind med din
   Google-konto. Godkend betingelserne, hvis den spørger.
2. Øverst: **Select a project → New project** → navn `Home Assistant` → **Create**. Vent, og
   vælg projektet øverst, hvis det ikke allerede er valgt.
3. Gå til [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com) → **Enable**
4. Gå til [Google Auth Platform](https://console.cloud.google.com/auth/branding) → **Get started**:
   - App name: `Home Assistant`, User support email: din e-mail → **Next**
   - Audience: **External** → **Next**
   - Contact information: din e-mail → **Next** → sæt flueben → **Continue** → **Create**
5. Til venstre: **Branding**:
   - De tre felter under **App domain**: skriv `https://home-assistant.io` i alle tre
   - **Authorized domains** → **Add domain** → `home-assistant.io` → **Save**
6. Til venstre: **Audience** → **Publish app** → **Confirm**. Ellers holder det op med at virke
   efter 7 dage.
7. Til venstre: **Clients** → **Create client**:
   - Application type: **Web application**, Name: `Home Assistant`
   - **Authorized redirect URIs** → **Add URI** → `https://my.home-assistant.io/redirect/oauth`
   - **Create**
8. Et vindue viser nu **Client ID** og **Client Secret**. Kopiér begge ind i din password manager
   (eller en note) **nu**, for de vises kun én gang.

> Mistede du dem? Lav bare en ny under **Clients**. Nye nøgler kan være et par timer om at virke.

## Klik F: Automatisk backup til Google Drive

**Forbind Drive:**

1. **Indstillinger → Enheder og tjenester → Tilføj integration** → søg **Google Drive**
2. Indsæt **Client ID** og **Client Secret** fra Klik E → log ind med Google
3. Google siger *"Google hasn't verified this app"*. Det er din egen app, så klik **Fortsæt**
   (evt. under *Avanceret*) → **Continue** → **Link Account**

**Slå backup til:**

1. **Indstillinger → System → Sikkerhedskopier** → **Set up backups**
2. HA viser en **nødpakke**: tryk **Download**, gem filen i din Drive → **Next**
3. Vælg **Custom**: **Daily**, behold **7**, placeringer: denne enhed **og** Google Drive → **Save**
4. **Configure backup settings** → under **Locations**: tryk **tandhjulet** ved hver placering →
   **Encryption** → **Turn off**. Så kan backupen åbnes uden kode.
5. Tilbage på **Sikkerhedskopier** → **Opret backup nu**. Tjek efter et par minutter, at den ligger
   i mappen **Home Assistant** i dit Drive.

> 🚨 Google gemmer selv alt i Drive krypteret, så en stjålet harddisk hos Google er ikke et
> problem. Men **den, der kan logge ind på din Google-konto, kan åbne backupen**, og den indeholder
> alle Home Assistants passwords. Slå derfor **2-trinsbekræftelse** til:
> [myaccount.google.com/security](https://myaccount.google.com/security).

**Valgfrit, senere: kryptér backupen**

1. **Sikkerhedskopier** → kortet **Encryption key** → **Download emergency kit**
2. Gem den i din **password manager**, ikke kun i Drive ved siden af backupen
3. Tandhjulet ved **Google Drive** → **Encryption** → **Turn on**

Uden den nøgle kan en krypteret backup **ikke** gendannes. Heller ikke af Google.

## Klik G: GitHub-konto og login

1. Opret en gratis konto på [github.com/signup](https://github.com/signup)
2. AI'en installerer GitHub-programmet `gh`. Kan den ikke (den mangler dit password), så kør den
   linje, den giver dig, i en terminal.
3. I en terminal (**Antigravity:** menuen **Terminal → New Terminal**; **Claude:** åbn programmet **Terminal** på Mac eller **Git Bash** på Windows): skriv `gh auth login`, og tryk Enter
4. Vælg med piletasterne og Enter: **GitHub.com** → **HTTPS** → **Yes** → **Login with a web browser**
5. Kopiér den kode, den viser → Enter → indsæt koden i browseren → **Authorize**. Skriv "færdig" til AI'en.

> 🚨 Repoet `ha-config`, som AI'en opretter, er **privat**: kun du kan se det. Skift det aldrig til
> **Public**. Det indeholder din HA-opsætning med adresser, passwords og hvornår I er hjemme.

## Klik H: Indsæt en automation

1. **Indstillinger → Automationer og scener** → **Opret automation** → **Opret ny automation**
2. **⋮** øverst til højre → **Rediger i YAML** → slet alt → indsæt AI'ens tekst → **Gem**

---

## Godt at vide

- **AI'en laver fejl.** Derfor tager den backup og bruger git. Bed den om at *"fortryde den sidste
  ændring"*, hvis noget går galt.
- **`~/.profile` er nøglen til hele huset.** Send den aldrig til nogen, og læg den aldrig på nettet.
- **Mister du computeren:** slet tokenet i Home Assistant (Klik B, trin 1–2: skraldespanden ved
  tokenet), og skift de passwords, der står i `~/.profile`.
- **Åbn aldrig Home Assistant mod internettet** for at få det her til at virke hjemmefra. Brug i stedet en VPN (fx WireGuard) eller Home Assistant Cloud (Nabu Casa).
- **Lad ikke AI'en arbejde alene**, mens du er væk. Det er familiens hus.

> 🆘 **Sidder du fast?** Tag et skærmbillede, og spørg i en Home Assistant-gruppe, eller opret et issue på github.com/dkvand/ha.
