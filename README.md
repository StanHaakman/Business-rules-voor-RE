# Business-rules-voor-RE
Dit word een rule-based systeem ten behoeve van het aankomende recommendation engine.

Ik ga 2 business rules maken.

De eerste business rule is om producten op te halen voor aanbevelingen voor verschillende doelgroepen. Ik heb 5 doelgroepen verwerkt maar deze zijn indentiek aan elkaar qua de code en ik heb er voor gekozen om alleen target_kinderen te laten zien.

De aangemaakte tabellen:

![Target tabellen](https://github.com/StanHaakman/Business-rules-voor-RE/blob/main/images/target_tabellen.png)

Het resultaat van select query:

![Resultaat select query target kinderen](https://github.com/StanHaakman/Business-rules-voor-RE/blob/main/images/Resultaat_select_query_target_kinderen.png)

De tweede business rule in om 4 productsn op te halen per sessie op basis van een preference. Ik heb 2 preferences verwerkt namelijk categorie en brand maar het resultaat is indentiek en ik laat daarom dus alleen preference_brand zien.

De aangemaakte tabellen:

![Preference tabellen](https://github.com/StanHaakman/Business-rules-voor-RE/blob/main/images/preference_tabellen.png)

Het resultaat van select query:

![Resultaat select join query preference brand](https://github.com/StanHaakman/Business-rules-voor-RE/blob/main/images/Resultaat_selectjoin_query_preference_brand.png)

## Installatie instructies
Hier volgt een visuele en textuele uitleg over een nieuwe gebruiker dit project werkend krijgt.

### Prerequirements
Voordat dit project werkt zijn er een aantal onderdelen nodig die zijn hier te vinden.

<ul>
  <li>MongoDB moet geinstalleerd zijn</li>
  <ul>
    <li>Met MongoImport moet de goede database aanwezig zijn. Deze bevat gevoelige gegevens dus hier gaan we verder niet op in in dit document.</li>
  </ul>
  <li>Python Libraries: Deze kan je vooraf globaal installeren of met het opstellen van het project local geinstalleren.
    <ul>
      <li>pymongo library</li>
      <li>psycopg2</li>
      <li>csv</li>
    </ul>
  </li>
  <li>Postgress</li>
  <li>Python</li>
</ul>

### Setup

Download een zip bestand van de data of kies ervoor om de git te Forken naar je eigen account en dan clonen.

Zorg dat alle benodigde libraries gedownload anders kan installeren met:
```
python3 install pymongo

&&

python3 install psycopg2

&&

python3 install csv
```

Voordat het programma werkt moet er een file aangemaakt worden genaamd: dbsecret.py

Geef in deze file de volgende onderdelen aan en verander de inhoud naar jou eigen postgress gegevens:
```
user = 'user'
database = 'dbname'
password = 'password'
```

Open het project folder in de terminal en run dit commando:

```
python3 main.py
```

Hiermee vul je de relationele postgres database met de data van mongoDB. Om nu het onderdeel van de code te runnen waarin deze opdracht uitgevoert word voer run je dit commando:

```
python3 business_rules.py
```
