# **Notizen** (German)
Beginn der Aufzeichnungen ab dem 16.11.2021, da davor nichts notiert werden musste.

## <span style="color:#9ACD32"><u>16.11.2021</u></span>
- ### <span style="color:#A52A2A">**Meeting (online)**</span>
  - <span style="color:#40a6a3">***Notizen:***</span>
    Datenpipeline verstehen. Was wird gebraucht
  - <span style="color:#40a6a3">***Abgeleitete Aufgaben:***</span>
    - [x] ESP32 nachricht an RPI senden, mit MQTT Protokoll
    - [x] Recherche IOT Protokolle
    - [x] Recherche Datenbanken
    - [x] Recherche CRISP DM und Alternativen
    - [x] Recherche Machine Learning (ML-Arten, oberflächlich)


## <span style="color:#9ACD32"><u>19.11.2021</u></span>
- ESP32 nachricht an RPI gesendet


## <span style="color:#9ACD32"><u>20.11.2021</u></span>
- Recherche IOT Protokolle
- Recherche Datenbanken


## <span style="color:#9ACD32"><u>21.11.2021</u></span>
- Recherche CRISP DM und Alternativen


## <span style="color:#9ACD32"><u>22.11.2021</u></span>
- Recherche Machine Learning (ML-Arten, oberflächlich)


## <span style="color:#9ACD32"><u>23.11.2021</u></span>
- ### <span style="color:#A52A2A">**Meeting (am Fraunhofer Vaihingen)**</span>
  - <span style="color:#40a6a3">***Notizen:***</span>
    - Prüfungsamt, Abtretungserklärung, Informatik Seite Prüfer, Bfs, Lean Startup (weitere Variante)
  - <span style="color:#40a6a3">***Abgeleitete Aufgaben:***</span>
    - [x] Datenpipeline aufbauen
    - [x] Verstehen des Aufbaus
    - [x] Monitoring mit Grafana


## <span style="color:#9ACD32"><u>25.11.2021</u></span>
- Durchlesen von Dev-Tutorials über MQTT auf dem ESP32 und RPI
- Email Impuls: Welche Versionierung für Software und Datenvarianz erhöhen.


## <span style="color:#9ACD32"><u>26.11.2021</u></span>
- Anschließen vom BME680 Sensor an den ESP32 [mit Tutorial](https://randomnerdtutorials.com/esp32-bme680-sensor-arduino/) (SPI Anschluss)
  

## <span style="color:#9ACD32"><u>27.11.2021</u></span>
- Schreiben des ESP32 Programms. Hilfreiche Quellen: 
  [Sensoren/Library Setup](https://randomnerdtutorials.com/esp32-bme680-sensor-arduino/), 
  [Bosch Github](https://github.com/BoschSensortec/BSEC-Arduino-library), 
  [Wifi und MQTT publisher](https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/)
- Nutze die Arduino Library von Bosch. Setup der Library hat sehr lange gebraucht, da es sich um eine static-Library handelt und in den esp32 Arduino files, bestimmte Konfigurationen angepasst werden mussten. Steht ungefähr im Bosch Github.


## <span style="color:#9ACD32"><u>28.11.2021</u></span>
- Aufspielen von Raspbian OS Lite auf SD-Karte (Headless OS)
- SSH und WIFI aktivieren.  Beispiel: [Hier](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)
- Steuern von RPI über PC
- Installieren von Mosquitto, InfluxDB und Grafana
- InfluxDB Tabelle über Cmd erstellen
- Mosquitto autostart einstellen
- Python Script schreiben, das die Daten vom ESP32 empfängt und in die Datenbank schreibt.
- Grafana profil anlegen und server starten
- **Problem:** Das Python-Script soll zum Systemstart direkt laufen, aber das funktioniert überhaupt nicht.
- Manuelles ausführen des Scripts funktioniert aber.


## <span style="color:#9ACD32"><u>29.11.2021</u></span>
- **Bug Fixing:** Das Python Script startet nun automatisch, nachdem der rpi an geht. Dafür habe ich einen Service geschrieben, der nach erfolgreichem Systemstart ausgeführt wird. Nämlich erst nachdem alle Systemprozesse laufen. [Guide](https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/)
- Der Vollständigkeitshalber wird Grafana Server nun auch voll automatisch ausgefürt.


## <span style="color:#9ACD32"><u>30.11.2021</u></span>
- ### <span style="color:#A52A2A">**Meeting (online)**</span>
  - <span style="color:#40a6a3">***Notizen:***</span>
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
  - <span style="color:#40a6a3">***Abgeleitete Aufgaben:***</span>
    - [x] UML-Diagramm über Datenpipeline erstellen
    - [x] GitHub anlegen
    - [x] Recherche Deskriptive Statistik
    - [ ] Recherche Jupiter Notebook
    - [ ] Recherche Zeitreihendatenanalyse
    - [ ] \(Optional) Json anstatt Strings zum übermitteln


## <span style="color:#9ACD32"><u>2.12.2021</u></span>
- Recherche Deskriptive Statistik
  

## <span style="color:#9ACD32"><u>3.12.2021</u></span>
- Anlegen von Github Repo und digitalisierung der Notes
