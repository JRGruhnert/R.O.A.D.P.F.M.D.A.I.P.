# **Notizen** (German)
Beginn der Aufzeichnungen ab dem 16.11.2021, da davor nichts notiert werden musste.

## <u>16.11.2021</u>
- ### **Meeting (online)**
  - ***Notizen:***
    Datenpipeline verstehen. Was wird gebraucht
  - ***Abgeleitete Aufgaben:***
    - [x] ESP32 nachricht an RPI senden, mit MQTT Protokoll
    - [x] Recherche IOT Protokolle
    - [x] Recherche Datenbanken
    - [x] Recherche CRISP DM und Alternativen
    - [x] Recherche Machine Learning (ML-Arten, oberflächlich)


## <u>19.11.2021</u>
- ESP32 nachricht an RPI gesendet


## <u>20.11.2021</u>
- Recherche IOT Protokolle
- Recherche Datenbanken


## <u>21.11.2021</u>
- Recherche CRISP DM und Alternativen


## <u>22.11.2021</u>
- Recherche Machine Learning (ML-Arten, oberflächlich)


## <u>23.11.2021</u>
- ### **Meeting (am Fraunhofer Vaihingen)**
  - ***Notizen:***
    - Prüfungsamt, Abtretungserklärung, Informatik Seite Prüfer, Bfs, Lean Startup (weitere Variante)
  - ***Abgeleitete Aufgaben:***
    - [x] Datenpipeline aufbauen
    - [x] Verstehen des Aufbaus
    - [x] Monitoring mit Grafana


## <u>25.11.2021</u>
- Durchlesen von Dev-Tutorials über MQTT auf dem ESP32 und RPI
- Email Impuls: Welche Versionierung für Software und Datenvarianz erhöhen.


## <u>26.11.2021</u>
- Anschließen vom BME680 Sensor an den ESP32 [mit Tutorial](https://randomnerdtutorials.com/esp32-bme680-sensor-arduino/) (SPI Anschluss)
  

## <u>27.11.2021</u>
- Schreiben des ESP32 Programms. Hilfreiche Quellen: 
  [Sensoren/Library Setup](https://randomnerdtutorials.com/esp32-bme680-sensor-arduino/), 
  [Bosch Github](https://github.com/BoschSensortec/BSEC-Arduino-library), 
  [Wifi und MQTT publisher](https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/)
- Nutze die Arduino Library von Bosch. Setup der Library hat sehr lange gebraucht, da es sich um eine static-Library handelt und in den esp32 Arduino files, bestimmte Konfigurationen angepasst werden mussten. Steht ungefähr im Bosch Github.


## <u>28.11.2021</u>
- Aufspielen von Raspbian OS Lite auf SD-Karte (Headless OS)
- SSH und WIFI aktivieren.  Beispiel: [Hier](https://desertbot.io/blog/headless-raspberry-pi-4-ssh-wifi-setup)
- Steuern von RPI über PC
- Installieren von Mosquitto, InfluxDB und Grafana
- InfluxDB Tabelle über Cmd erstellen
- Mosquitto autostart einstellen
- Python Script schreiben, das die Daten vom ESP32 empfängt und in die Datenbank schreibt.
- Grafana profil anlegen und server starten
- **Problem:** Das Python-Script soll zum Systemstart direkt laufen, aber das funktioniert überhaupt nicht.
- Manuelles ausführen des Scripts funktioniert aber.


## <u>29.11.2021</u>
- **Bug Fixing:** Das Python Script startet nun automatisch, nachdem der rpi an geht. Dafür habe ich einen Service geschrieben, der nach erfolgreichem Systemstart ausgeführt wird. Nämlich erst nachdem alle Systemprozesse laufen. [Guide](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)
- Der Vollständigkeitshalber wird Grafana Server nun auch voll automatisch ausgefürt.


## <u>30.11.2021</u>
- ### **Meeting (online)**
  - ***Notizen:***
    - UML-Dokument für Visualisierung
    - GitHub
    - Deskriptive Statistik
    - exponentiell gewichteter Mittelwert
    - Gradienten
    - Json File(MQTT Datenübermittlung)
    - Programmiersprache für ML?
    - Zeitreihendatenanalyse
    - Jupiter Notebook
    - Wie zieht man die Daten aus der Datenbank?
  - ***Abgeleitete Aufgaben:***
    - [x] UML-Diagramm über Datenpipeline erstellen
    - [x] GitHub anlegen
    - [x] Recherche Deskriptive Statistik
    - [ ] Recherche Jupiter Notebook
    - [x] Recherche Zeitreihendatenanalyse
    - [ ] \(Optional) Json anstatt Strings zum übermitteln


## <u>2.12.2021</u>
- Recherche Deskriptive Statistik
- UML-Diagramm erstellt
  

## <u>3.12.2021</u>
- Anlegen von Github Repo und digitalisierung der Notes


## <u>4.12.2021</u>
- JSON Format ausprobieren
- läuft nicht, da Probleme mit der Datenbank und dem abspeichern
- Das genaue Abspeichern von Daten und die Struktur der Daten muss ich nochmal genau nachholen.


## <u>5.12.2021</u>
- Recherche zu Zeitreihendatenanalyse. 


## <u>7.12.2021</u>
- ### **Meeting (online)**
  - ***Notizen:***
    - Prüfer finden, der mit dem Thema zutun hat.
    - Anderer Prüfe ist Professor Ridel.
    - Mehrere Prüfer, nur Unterschrift.
    - Frau Dr. Katrin Schneider.
    - Was braucht sie von uns?
    - Jupyter Notebook Visualisierungen mit InfluxDB.
    - Wie visualisiert man eine Zeitreihe?
    - TIG-Stack.
    - Active Noisecancelling Prinzip.
    - Abweichung ist Label.
    - Vergleichen von Messungen mit gleicher Vorraussetzung.
    - [Conceptboard](https://app.conceptboard.com/board/gto3-21dt-n0mk-k9sa-xukq)


  - ***Abgeleitete Aufgaben:***
    - [ ] Visualisierung von Sensordaten in Jupyter Notebook.
    - [x] Bacheloranmeldung abklären.
    - [ ] TIG angucken. Was ist das genau?


## <u>8.12.2021</u>
- Jupiter Notebook oberflächlich angeguckt. Soll angeblich sehr verbreitet für ML-Programmierung sein.

## <u>10.12.2021</u>
- Studiengangsorganisation telefonisch erreicht -> Es darf offiziell nur einen Prüfer geben und dieser muss ein Informatik-Prof sein.
- BFS erreicht. Vom IAT geht es in Ordnung, wenn es nur einen Prüfer gibt und dieser aus Fakultät 5 kommt.
- -> Übers Wochenende Prüfer raussuchen und am Montag kontaktieren.

## <u>11.12.2021</u>
- Anaconda und Tensorflow runtergeladen.
- Jupiter Notebook gestartet und mit Funktionen vertraut gemacht und eingerichtet.
  
## <u>12.12.2021</u>
- TIG Stack eingerichtet

## <u>13.12.2021</u>
- Jupiter Notebook Daten visualisiert

