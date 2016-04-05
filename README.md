Omgevings analyse tool - rapporteertool voor milieuvergunningen
====

Ontwikkelen van een vereenvoudigd QGIS project met specifieke functionaliteit
----

De bedoeling is om 1 toolbar te maken specifiek voor dit project: Functionaliteiten van de toolbar:

- zoeken op perceel of adres worden --> zoeken op adres is vrij eenvoudig
- een select perceel knop waarbij één of meerdere percelen geselecteerd worden uit de CADMAP (ter beschikking als WFS service binnen MercatorNet) --> voor identify of ???
- of de GRB ADP percelenkaart (die zou dan lokaal moeten geïnstalleerd worden. (percelenkaart pas zichtbaar op 1/2500) --> Lokale data s af te raden, GRB is te groot --> Werken met GRB-WMS indien mogelijk
- zoom in/uit , pan --> standaard
- meet afstand knop --> standaard
- genereer rapport knop --> in html, met opslaan knop
- kies basiskaart dropdown --> of radiobutton

Functionaliteit genereer rapport knop
----

Ten opzichte van de verschillende vector lagen (groot aantal) die ingeladen zijn in het project (WFS of vectorlaag) 
een soort rapport venster gegenereerd wordt met volgende informatie:

- Welke afstand de geselcteerde perce(e)l(en)de tot de dichtsbijgelegen polygonen/punten/of lijnen van de verschillende vectorlagen gelegen zijn: 
- Afstand dichtbijgelegen object
- Bekijk op kaart toon attrubten dichstbijgelegen feature Ven gebieden —— 1500m knop: bekijk op kaart toon attributen Vogelrichtlijngebieden —— 750m
- knop: bekijk op kaart toon attributen Seveso terreinen —— 3500m knop: bekijk op kaart toon attributen 
- Voor rasterlagen:
    - de knop 'toon op kaart' zou dan het kaartvenster aanpassen naar:
    - achtergrondkaart: bv GRB of Orthofoto's
    - geselecteerde percelen
    - enkel laag zichtbaar maken waarin men geïnteresseerd is
    - de toon attribuutwaarde geeft de attributen van de dichtsbijgelegen punt/lijn/polygoon van de kaart --> Rasterlagen als WMS ?
    
Het zou goed zijn moest het project generiek kunnen geconfigureerd worden worden. 
Je kan dan als beheerder de vector (bv vector of WFS, raster of WMS WMTS en de percelen of dossierskaart inladen, 
alle panelen en toolbars verwijderen en de configuratie maken. In een configuratievenster voor een soort beheerder kan je dan :

- de verschillende basiskaarten aanduiden
- de laag in de percelen geselecteerd worden
- de vectorlagen waartegen de afstand moet berekend worden
- de rasterlagen die enkel getoond worden

Uitwerking
----
De rapporteertool kan ontwikkelt als een QGIS plugin, de configuratie kan een gewoon QGIS-project zijn. 