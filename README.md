# shodaninfo
Verkrijg informatie over een IP-adres van de website Shodan.io

## Gebruik
Het script heeft op dit moment de mogelijkheid om één of meerdere IP-adressen te controleren op Shodan.io.

**IP-adres**
Voor het testen van één of meer IP-adressen gebruik het onderstaande commando. Wanneer je meer IP-adressen toe wilt voegen zet deze dan achter elkaar, gescheiden door een spatie.

```python
python main.py --ip 192.168.0.1

python main.py --ip 192.168.0.1 88.54.56.21
```

Voor het weergeven van alle opties van het programma gebruik het onderstaande commando:

```python
python main.py -h
```


## Bijdragen
Als je wilt bijdragen aan deze repository volg dan de onderstaande stappen

1. Clone de repository

```terminal
git clone https://github.com/jebr/shodaninfo.git
```

2. Maak een eigen branch

```terminal
git checkout [naam van de branch]
```

3. Maak een `pull-request` om wijzigingen door te voeren in de `main` repository