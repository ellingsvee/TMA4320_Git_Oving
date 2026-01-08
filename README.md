# TMA4320: Git-øvelse før prosjekt

Denne øvingen er ment som en intro til Git og GitHub. Du lærer grunnleggende kommandoer ved å gjøre enkle endringer i dette repoet.

## Del 1: Sette opp repoet lokalt

### Fork dette repoet
1. Pass på at du er logget inn på GitHub
2. Trykk på "Fork"-knappen øverst til høyre på GitHub
3. Du får nå din egen kopi av repoet
4. Velg om du vil gjøre repoet privat eller offentlig (valgfritt). Dersom det er et offentlig repo, kan alle se koden din.

### Naviger til passende sted maskinen din
Åpne terminalen og gå til mappen der du vil ha repoet. Bruk kommandoene
```bash
ls                      # List filer og mapper
mkdir ny_mappe          # Lag en ny mappe (valgfritt)
cd /sti/til/mappen      # Naviger til ønsket mappe
```

### Klon repoet til maskinen din
```bash
git clone https://github.com/DITT-BRUKERNAVN/TMA4320_Git_Oving.git  # Bytt ut DITT-BRUKERNAVN med ditt GitHub-brukernavn
cd TMA4320_Git_Oving                                                # Beveg deg inn i mappen
```

### Sjekk statusen
```bash
git status 
```
Dette viser hvilken branch du er på og om det er noen endringer.

### Generer en ssh nøkkel for å kommunisere mellom Git og Github (OBS: Kan være krevende):

[Følg denne guiden for å lage en ssh nøkkel og koble den til GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)


## Del 2: Gjør din første endring

### Oppgave: Legg til navnet ditt i `studenter.txt`

1. Åpne filen `studenter.txt` i en teksteditor
2. Legg til navnet ditt på en ny linje
3. Lagre filen

### Sjekk hva som er endret
```bash
git status
git diff
```

### Legg til endringen og commit
```bash
git add studenter.txt
git commit -m "La til mitt navn i studentlisten"
```

### Push til GitHub
```bash
git push
```

Gå til GitHub og sjekk at endringen dukket opp!

## Del 3: Jobbe med branches

Branches lar deg jobbe på nye features uten å ødelegge hovedkoden.

### Lag en ny branch
```bash
git branch min-feature      # Lag en ny branch kalt "min-feature"
git switch min-feature      # Bytt fra "main" branch til den nye branchen "min-feature"
```

### Oppgave: Gjør noen endringer i `kalkulator.py`

For eksempel, legg til en ny funksjon:
```python
def multipliser(a, b):
    return a * b
```

### Sjekk hva som er endret
```bash
git status 
git diff
```

### Commit endringene
```bash
git add kalkulator.py
git commit -m "La til multiplikasjonsfunksjon"
git push -u origin min-feature
```

## Del 4: Merge og pull requests

### På GitHub:
1. Gå til repoet ditt på GitHub
2. Du vil se en notifikasjon om den nye branchen
3. Trykk "Compare & pull request"
4. Skriv en kort beskrivelse og trykk "Create pull request"
5. Merge pull requesten

### Tilbake i terminalen:
```bash
git switch main     # Bytt tilbake til main-branchen
git pull            # Hent de nyeste endringene fra GitHub
```

Nå er endringene dine i main-branchen!

## Del 5: Håndtere merge conflicts (dette er noe mange sliter med)

Merge conflicts oppstår når to branches endrer samme linje i en fil. Vi skal nå lage en konflikt lokalt på din egen PC for å lære hvordan man håndterer dem.

### Lag en merge conflict:

1. Sjekk at du er på main-branchen:
```bash
git switch main
```

2. Lag to nye branches fra main:
```bash
git branch feature-1
git branch feature-2
```

3. Gjør en endring på feature-1:
```bash
git switch feature-1
```
Åpne `studenter.txt` og endre den **første linjen** til:
```
Dette er endring fra feature-1
```
Commit endringen:
```bash
git add studenter.txt
git commit -m "Endring fra feature-1"
```

4. Bytt til feature-2 og gjør en **annen** endring på **samme linje**:
```bash
git switch feature-2
```
Åpne `studenter.txt` og endre den **første linjen** til:
```
Dette er endring fra feature-2
```
Commit endringen:
```bash
git add studenter.txt
git commit -m "Endring fra feature-2"
```

5. Merge feature-1 inn i main (dette går fint):
```bash
git switch main
git merge feature-1
```

6. Nå prøver vi å merge feature-2 (dette gir konflikt!):
```bash
git merge feature-2
```

Du får nå en feilmelding om merge conflict!

### Løs konflikten:

7. Åpne `studenter.txt`. Git har markert konflikten slik:
```
<<<<<<< HEAD
Dette er endring fra feature-1
=======
Dette er endring fra feature-2
>>>>>>> feature-2
```

8. Rediger filen manuelt. Fjern `<<<<<<<`, `=======`, og `>>>>>>>` markeringene, og behold det du vil ha. For eksempel:
```
Dette er endring fra feature-1 og feature-2
```

9. Fullfør merge:
```bash
git add studenter.txt
git commit -m "Løst merge conflict mellom feature-1 og feature-2"
```

Gratulerer! Du har nå håndtert din første merge conflict.

## Del 6: Bruk av .gitignore

Noen filer skal ikke være med i Git, for eksempel store datafiler, midlertidige filer, eller autogenererte filer. Filen `.gitignore` forteller Git hvilke filer og mapper som skal ignoreres.

### Oppgave: Lag en `.gitignore` fil

1. Lag noen testfiler:
```bash
touch rapport.pdf       # touch kommandoen lager en tom fil med det valgte filnavnet
touch data.csv
touch notater.pdf
```

2. Sjekk status:
```bash
git status
```
Du vil se at alle de nye filene er "untracked".

3. Lag en `.gitignore` fil i rotmappen av repoet:
```bash
touch .gitignore
```

4. Åpne `.gitignore` i en teksteditor og legg til:
```bash
# Ignorer alle PDF-filer. På "dataspråk" betyr "*" alle filer. Ved å legge ved ".pdf" betyr det alle filer som slutter på .pdf
*.pdf

# Ignorer spesifikke filer
data.csv

# Ignorer hele mapper
temp/
```

5. Sjekk status igjen:
```bash
git status
```
Nå vil du se at `rapport.pdf` og `notater.pdf` ikke lenger vises som untracked filer!

### Nyttige .gitignore patterns:
- `*.pdf` - ignorerer alle PDF-filer
- `__pycache__/` - ignorerer Python cache-mappen
- `.DS_Store` - ignorerer macOS systemfiler

6. Commit .gitignore filen:
```bash
git add .gitignore
git commit -m "La til .gitignore"
```

**Tips:** GitHub har en samling av nyttige .gitignore-templates for ulike språk: [github.com/github/gitignore](https://github.com/github/gitignore) 

**Obs:** .gitignore påvirker kun filer som ikke allerede er tracket av Git. Hvis du allerede har commitet en fil, må du fjerne den fra Git-historikken for at .gitignore skal fungere på den filen.

## Oppsummering av brukte kommandoer

```bash
# Sjekke status og endringer
git status                      # Se hva som er endret
git log                         # Se commit-historikk
git diff                        # Se hva som er endret i filer

# Legge til og committe endringer
git add <filnavn>               # Legg til en fil for commit. Evt. bruk "git add ." for å legge til alle endrede filer.
git commit -m "Commit melding"  # Lag en commit med en melding


# Jobbe med branches
git branch                      # Se alle branches
git branch <branch-navn>        # Lag en ny branch
git switch <branch-navn>        # Bytt til en annen branch
git merge <branch-navn>         # Merge en branch inn i den nåværende branchen

# Sende endringer til og fra GitHub
git push                        # Send endringer til GitHub
git pull                        # Hent nyeste endringer fra GitHub
```
**Merk:** Dette er bare et utvalg av de mest brukte kommandoene. Git har mange flere funksjoner og kommandoer som kan være nyttige i forskjellige situasjoner.

## Tips

- Pull før du begynner å jobbe (for å få andres endringer)
- Test koden din før du pusher
- Bruk branches for nye features
- "Atomic commits": Gjør små, meningsfulle commits. Ikke commit store endringer på en gang.

Andre nyttige ressurser:
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Pro Git Book](ps://git-scm.com/learn)
- [Philomatics Youtube kanal](https://www.youtube.com/@philomatics)


## Bonus: GUIs for Git
Mange foretrekker å bruke grafiske brukergrensesnitt (GUIs) for å håndtere Git i stedet for kommandolinjen. Dette kan gjøre det enklere å visualisere endringer og raskere å utføre visse operasjoner. Her er noen populære alternativer.

### LazyGit (min personlige favoritt)
LazyGit er en terminal-basert GUI. Personlig bruker jeg LazyGit for 90% av mine Git-operasjoner, og kun kommandolinen for avanserte ting. Koden er åpen kildekode og programmet kan lastes ned fra [LazyGit GitHub repository]("https://github.com/jesseduffield/lazygit").

<img src="figures/lazygit.png" width="50%" height="50%">

### GitHub Desktop
GitHub Desktop er et brukervennlig GUI for Git som er utviklet av Microsoft. Det kan lastes ned gratis fra [Download GitHub Desktop]("https://desktop.github.com/download/").

<img src="figures/github_desktop.webp" width="50%" height="50%">

### Source Control i VSCode
VSCode har innebygd støtte for Git gjennom Source Control-panelet. Finn mer informasion på [Source Control in VS Code]("https://code.visualstudio.com/docs/sourcecontrol/overview").

<img src="figures/vscode_source_control.png" width="50%" height="50%">



### Lykke til! Det kan kreve litt øvelse, men Git er et utrolig kraftig verktøy som er verdt å mestre.
