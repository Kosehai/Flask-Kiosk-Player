README.md in Norwegian

# Oppsett av programvare
## Pakket executable
Pakket versjon av ligger i "./dist/app". Bare ta å kopier hele denne mappen til klient. Denne er pakket med alt den trenger og bør kjøre uten noe oppsett på ny maskin. Kan ta litt tid første kjøring.

Om edge ikke starter automatisk ligger webserver på localhost:5000

## Med Python
Er testet og utviklet med python 3.10. Kan hentest tilsvarende versjon fra Windows Store. Anbefaler å bruke denne siden den kommer med pip package manageren.

Når denne er installert er det bare å kjøre i mappen med powershell/cmd:
``` bash
pip install -r requirements.txt
```

For å store webserver/client kjører du
``` bash
python app.py
```

Det er alt! Må ligge en kopi av ffmpeg i samme directory som du kjører programet i fra. Skal ligge med "ffmpeg.exe" men om den mangler kan det ordnest ny fra ffmpeg.org.

Om edge ikke starter automatisk ligger webserver på localhost:5000

## Modifisering av media/web gui
Programet henter alt av media fra ./media mappen. Det genererer også thumbnails for alle videoer i ./media/thumb mappen. 

Så lenge videoer som blir lagt til er av format MPEG eller h264 (.mp4) blir det lagt til automatisk så lenge de ligger i media mappen. Er litt begrenset på format pga av nettleser grensesnitt.

Alt av web gui ligger i ./template mappen, kan gjøres noen endringer her på tekst osv om kunde vil ha det.

**Titler på videoene blir hentet fra MetaData**. Så for å få inn riktig titel må du: Høgereklikk -> Properties -> Details -> Rediger tittel feltet

## Automatisk sync mot OneDrive/Dropbox/Gdrive
Programet er veldig enkelt av design og har ingen API mot noen spesifik cloud løsning. Enkleste måten å få til dette på er bare en SymLink. Bare innstaler klient for skytjeneste og lag en symbolsk link med denne commanden (må tilpasse path osv):

```
mklink /J media "C:\Users\mw\OneDrive - Agnitio as\media"
(Må muligens kjøre cmd som admin)
```
Hugs å slett media mappe før du kjører denne. Når dette er gjort vil den bare bruke cloud mappen som media mappe og automatisk synce.

## Pakke ny executeable
Legger raskt til command som er brukt til å pakke python programet. Må installere pyinstaller modulen for å gjøre dette.
```
pip install pyinstaller
```

Der etter kan du bare bruke pyinstaller til å pakke programet:
```
python -m PyInstaller --add-data 'templates;templates' --add-data 'media;media' --add-data 'static;static' app.py
```

**Hugs å legge med en ffmpeg.exe i dist mappen!**

## Autorun på boot i windows
1. Lag en lokal windows bruker som skal kjøre kiosken
2. Lag en shortcut til programmet
   1. Om du bruker den pakket versionen blir dette app.exe
   2. Om du bare kjører python programet må du lage en .bat script som kjører python app.py å lage en shortcut til denne
3. Win+R - Skriv in shell:startup
4. Kopier shortcut til denne mappen

Er lurt å endre noen windows instillinger, skru av power saving og touch gestures om det er touch skjerm.

## Screenshots
![Homepage](/rm_img/homepage.png)
![Video Player](/rm_img/player.png)
