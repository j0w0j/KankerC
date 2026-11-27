# Logboek Casus C Johanna
Dit markdown bestand fungeert als het praktische logboek van onze module/package. Hierbij ga ik datum bijhouden, wat mijn doel is, waarom dit mijn doel is en hoe ik het doel ga behalen.

Dit logboek is specifiek voor casus C van voor het vak "moduleren van Kanker", bij dit casus werk ik samen met Fleur Luten.

## 27-11-2026
### Doel
Vandaag is mijn doel om me intelezen op opdracht/les 2. 

### Aan de slag
$BagOf Words Classificatie$ doet me denken aan een Bag, vorig kwartaal hebben we het gehad over de datastructuur bag en als ik mij goed herinner is dat vergelijkbaar met een set. Alleen bij een bag maakt de volgorde niet uit en mogen duplicaten voorkomen, dus eigenlijk een verzameling van elementen waarvan de volgorde niet uitmaakt en duplicaten zijn toegestaan. <br><br>

Om de opdracht in stukjes te hakken:
- leesbaar txt bestand gegeven met bestaande reeks documenten. Elk document staat hier op 1 regel
    - document kan uit meerdere zinnen bestaan maar bevat geen regeleinden.
- Schrijf een python script bagofword.py dat kan worden aangeroepen vanaf de commandline
    - elk document word omgezet naar een reeks getallen
    - de gebruiker kan aangeven of een multi-hot,telling fruquentie of TF-IDf encoding wilt gebruiken.
    - het resultaat wordt opgeslagen in een .bow bestand met bag of word representatie
- het is mogelijk om meerdere leesbare .txt tekst bestanden mee te geven. 
    - deze worden gezamelijk omgezet naar hun eigen .bow bestand databestanden.
- Elk bestand gebruikt dezelfde TF-IDF berekening
- Geef korte documentatie van het gebruik weer met een -help functie

Het eerste wat ik hier ga doen is in het nlp.py bestand een doc reader maken specifiek het inlezen van het txt bestand met documenten per line. Deze functie noem ik load_docs_per_line. Om meerdere bestanden op deze manier in te lezen maak ik een functie load_multiple_files die de filepaden pakt en load_docs_per_line aanroept en deze opslaat in een dictionairy.