# AccuTester

AccuTester is een desktopapplicatie voor het monitoren van temperatuurmetingen via een Arduino en het genereren van grafieken uit meetgegevens.

## Functionaliteit

- Realtime temperatuurmetingen van vier sensoren via een seriële COM-poort
- Realtime weergave van plots met een gedeelde y-as
- CSV-logging van metingen naar `metingen.csv`
- Vastleggen van testcondities en omgevingstemperatuur in `testcondities.csv`
- Genereren van gecombineerde grafieken op basis van temperatuur- en elektriciteitsdata

## Installatie

1. Zorg dat Python 3.11 of hoger geïnstalleerd is.
2. Maak een virtuele omgeving aan:

```bash
python -m venv venv
```

3. Activeer de virtuele omgeving:

Windows:
```powershell
venv\Scripts\Activate.ps1
```

4. Installeer de dependencies:

```bash
pip install -r requirements.txt
```

## Gebruik

Start de applicatie met:

```bash
python main.py
```

## GitHub / versiebeheer

Deze map is nu voorbereid als git-repository. Volg deze stappen om een GitHub-opslagplaats te koppelen:

1. Maak een nieuwe repository aan op GitHub.
2. Voeg de remote toe op jouw machine:

```bash
git remote add origin https://github.com/<gebruikersnaam>/<repositorynaam>.git
```

3. Stuur de eerste commit naar GitHub:

```bash
git push -u origin main
```

## Bestanden om te negeren

`README.md` en `.gitignore` zijn toegevoegd, zodat tijdelijke bestanden, virtuele omgevingen en build-artifacts niet naar GitHub worden gestuurd.
