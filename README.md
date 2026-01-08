# TMA4320: Git-øvelse

Denne øvingen er ment som en intro til Git og GitHub. Du lærer grunnleggende kommandoer ved å gjøre enkle endringer i dette repoet.

## Del 1: Sette opp repoet lokalt

**Fork dette repoet**
1. Pass på at du er logget inn på GitHub
2. Trykk på "Fork"-knappen øverst til høyre på GitHub
3. Du får nå din egen kopi av repoet

**Naviger til passende sted maskinen din**
Åpne terminalen og gå til mappen der du vil ha repoet. Bruk kommandoene
```bash
ls                      # List filer og mapper
mkdir ny_mappe          # Lag en ny mappe (valgfritt)
cd /sti/til/mappen      # Naviger til ønsket mappe
```

**Klon repoet til maskinen din**
```bash
git clone https://github.com/DITT-BRUKERNAVN/TMA4320_Git_Oving.git  # Bytt ut DITT-BRUKERNAVN med ditt GitHub-brukernavn
cd TMA4320_Git_Oving                                                # Beveg deg inn i mappen
```

**Sjekk statusen**
```bash
git status 
```
Dette viser hvilken branch du er på og om det er noen endringer.

## Del 2: Gjør din første endring

**Oppgave:** Legg til navnet ditt i `studenter.txt`

1. Åpne filen `studenter.txt` i en teksteditor
2. Legg til navnet ditt på en ny linje
3. Lagre filen

**Sjekk hva som er endret**
```bash
git status
git diff
```

**Legg til endringen og commit**
```bash
git add studenter.txt
git commit -m "La til mitt navn i studentlisten"
```

**Push til GitHub**
```bash
git push
```

Gå til GitHub og sjekk at endringen dukket opp!

## Del 3: Jobbe med branches

Branches lar deg jobbe på nye features uten å ødelegge hovedkoden.

**Lag en ny branch**
```bash
git branch min-feature      # Lag en ny branch kalt "min-feature"
git switch min-feature      # Bytt fra "main" branch til den nye branchen "min-feature"
```

**Oppgave:** Gjør noen endringer i `kalkulator.py`

For eksempel, legg til en ny funksjon:
```python
def multipliser(a, b):
    return a * b
```

**Sjekk hva som er endret**
```bash
git status 
git diff
```

**Commit endringene**
```bash
git add kalkulator.py
git commit -m "La til multiplikasjonsfunksjon"
git push -u origin min-feature
```

## Del 4: Merge og pull requests

**På GitHub:**
1. Gå til repoet ditt på GitHub
2. Du vil se en notifikasjon om den nye branchen
3. Trykk "Compare & pull request"
4. Skriv en kort beskrivelse og trykk "Create pull request"
5. Merge pull requesten

**Tilbake i terminalen:**
```bash
git checkout main
git pull
```

Nå er endringene dine i main-branchen!

## Del 5: Håndtere merge conflicts (valgfri)

Dette skjer når to personer endrer samme linje i en fil.

1. Be en medstudent endre samme linje i `studenter.txt` som deg
2. Dere vil begge pushe til hver deres fork
3. Når dere prøver å merge, får dere en konflikt
4. Git markerer konflikten i filen slik:
```
<<<<<<< HEAD
Din endring
=======
Medstudentens endring
>>>>>>> main
```
5. Rediger filen manuelt, fjern markeringene, og behold det du vil ha
6. `git add`, `git commit`, og `git push`

## Nyttige kommandoer

```bash
git status              # Se hva som er endret
git log                 # Se commit-historikk
git diff                # Se hva som er endret i filer
git branch              # Se alle branches
git switch <branch>     # Bytt til en annen branch
git pull                # Hent nyeste endringer fra GitHub
```

## Tips

- Pull før du begynner å jobbe (for å få andres endringer)
- Test koden din før du pusher
- Bruk branches for nye features
- "Atomic commits": Gjør små, meningsfulle commits. Ikke commit store endringer på en gang.

Andre nyttige ressurser:
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Pro Git Book](ps://git-scm.com/learn)


## Frivillig: GUIs for Git
Mange foretrekker å bruke grafiske brukergrensesnitt (GUIs) for å håndtere Git i stedet for kommandolinjen. Her er noen populære alternativer.

### LazyGit (min personlige favoritt)
LazyGit er et terminal-basert GUI for Git som gjør det enklere å håndtere commits, branches og merges uten å måtte skrive lange kommandoer. Personlig er det dette jeg bruker mest. Koden er åpen kildekode og kan lastes ned fra [LazyGit GitHub repository]("https://github.com/jesseduffield/lazygit").

<img src="figures/lazygit.png" width="50%" height="50%">

### GitHub Desktop
GitHub Desktop er et brukervennlig GUI for Git som er utviklet av Microsoft. Det kan lastes ned gratis fra [Download GitHub Desktop]("https://desktop.github.com/download/").
<img src="figures/github_desktop.webp" width="50%" height="50%">

### Source Control i VSCode
VSCode har innebygd støtte for Git gjennom Source Control-panelet. Finn mer informasion på [Source Control in VS Code]("https://code.visualstudio.com/docs/sourcecontrol/overview").
<img src="figures/vscode_source_control.png" width="50%" height="50%">



Lykke til!
