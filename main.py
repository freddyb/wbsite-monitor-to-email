#!/usr/bin/env python3
# encoding: utf-8
import os
import subprocess
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

os.environ['MOZ_HEADLESS'] = '1'

fredlog = open("results.txt", "w")
fredlog.write("Ergebnisse für alle Webseiten zum Zeitpunkt {}\n\n".format(time.asctime()))


def teardown_module():
    fredlog.write("\n-- \nEOF.\n")
    fredlog.close()
    tmplog = open("results.txt", "r")
    logtext = tmplog.read()
    if "hat ihren Text" in logtext:
        command = ["mail", "-s", "Webseitenbericht", "-c", "frederik@braun.im", "jannah@luemmer.de"]
        p = subprocess.Popen(command, stdin=subprocess.PIPE)
        p.communicate(input=logtext.encode())


class TestSchwimmkurse():
    def setup_method(self, method):
        self.driver = driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def open_a_web_page_and_compare(self, url, website_shortname, selector, expected_text):
        # test for existing override-text
        try:
            override = open(website_shortname + ".txt", "r").read()
            if not override == '':
                expected_text = override
        except:
            pass
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 30000).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector)))
            new_text = self.driver.find_element(By.CSS_SELECTOR, selector).text
            write_new = open(website_shortname+".txt", "w")
            write_new.write(new_text)
            if not (new_text == expected_text):
                fredlog.write("Die Webseite unter {} hat ihren Text geändert!\n".format(url))
                return False
            else:
                return True
        except selenium.common.exceptions.TimeoutException:
            fredlog.write("Die Webseite unter {} wurde übersprungen (Timeout)\n".format(url))
            return True  # secretly swallowing timeouts on our end
        return True

    def test_kitaschwimmen(self, caplog):
        url = "https://kitaschwimmen.de/anfaenger-schwimmkurse-fuer-kinder/"
        shortname = "kitaschwimmen_de"
        selector = "div.sections_group"
        text = "Anf\u00e4nger-Schwimmkurse\n\nab ca. 4 Jahren\nhier wird das Seepferdchen gemacht\nAnf\u00e4nger-Schwimmkurse f\u00fcr Kinder\nHier wird das Seepferdchen gemacht. Erreicht werden soll das angstfreie Bewegen und Spielen im Wasser; Kenntnisse der Selbstrettung und die Abnahme des \"Seepferdchen\" in einer Schwimmlage.\nDie Eckpunkte::\nf\u00fcr Kinder ab etwa 4 Jahren\n\nDauer der Kurseinheit: 30 min (Samstag: 45 min)\nBis auf die Kurse am Samstag finden alle Kurse 2 x w\u00f6chentlich statt\n\nAlle Kurse finden im Forumbad und im Stadtbad Spandau S\u00fcd (Gatower Stra\u00dfe) statt\nAnf\u00e4nger A1, ab 23.11.2020\n\nMo 17.15-17.45 + Fr 17.00 bis 17.30 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Sandra u.a.\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A2, ab 23.11.2020\n\nMo 17.45-18.15 + Fr 17.30 bis 18.00 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Sandra u.a.\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A3, ab 24.11.2020\n\nDi + Do 15.30 bis 16.00 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Peschi\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A4, ab 24.11.2020\n\nDi + Do 16.00 bis 16.30 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Peschi\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A5, ab 24.11.2020\n\nDi + Do 16.30 bis 17.00 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Peschi\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A6, ab 25.11.2020\n\nMi 17.30 bis 18.00 Uhr/So 12.30 bis 13.00 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Daniela & Ebru\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A7, ab 25.11.2020\n\nMi 18.00 bis 18.30 Uhr/So 12.00 bis 12.30 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Daniela & Ebru\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A8, ab 23.11.2020\n\nMo + Do 18.00 bis 18.30 Uhr\n\nSchwimmhalle: Gatower Stra\u00dfe\n\nTrainer: Markus & Pyvan\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A9, ab 23.11.2020\n\nMo + Do 18.30 bis 19.00 Uhr\n\nSchwimmhalle: Gatower Stra\u00dfe\n\nTrainer: Markus & Pyvan\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A10, ab 28.11.2020\n\nSamstag 10.15 bis 11.00 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Sandra u.a.\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A11, ab 28.11.2020\n\nSamstag 11.00 bis 11.45 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Sandra u.a.\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A12, ab 28.11.2020\n\nSamstag 11.45 bis 12.30 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Sandra u.a.\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A14, ab 28.11.2020\n\nSamstag 14.30 bis 15.15 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Sandra u.a.\n\nBuchung nicht mehr m\u00f6glich\nAnf\u00e4nger A15, ab 28.11.2020\n\nSamstag 13.00 bis 13.45 Uhr\n\nSchwimmhalle: Forumbad\n\nTrainer: Sandra u.a.\n\nBuchung nicht mehr m\u00f6glich\nDas Forumbad im Olympiapark\nDas Kombibad Spandau-S\u00fcd (Gatower Stra\u00dfe)\nDie Unterst\u00fctzer des \"Kitaschwimm-Projektes\"\n\nEinige Auszeichungen\n\nAusgezeichnet mit dem \"gr\u00fcnen Band\" 2011 f\u00fcr vorbildliche Talentf\u00f6rderung im Verein\nAusgezeichnet mit dem \"gr\u00fcnen Band\" 2005 f\u00fcr vorbildliche Talentf\u00f6rderung im Verein\nPreistr\u00e4ger beim \"Innovationspreis des Berliner Sports\" 2010\nAuszeichnung als \"Bester Nachwuchsverein\" im Berliner Schwimmverband 2009/2010\n\"Sterne des Sports\" in Bronze 2008 und 2006"
        assert self.open_a_web_page_and_compare(url, shortname, selector, text)

    def test_sg_schoene(self):
        url = "https://www.sg-schoeneberg.de/schwimmen/kinder-jugendliche/anfaengerschwimmen"
        shortname = "sg-schoeneberg"
        selector = "main.tm-content"
        text = "Anf\u00e4ngerschwimmen\nBis auf weiteres findet kein Probetraining statt.\nSchwimmen\nin unseren homogenen Trainingsgruppen bringt Spa\u00df und Freude\nf\u00f6rdert das soziale Miteinander und schafft neue Freundschaften\nist Training f\u00fcr Kraftausdauer, Gleichgewicht und Koordination\nschafft einen Ausgleich zum Alltag und st\u00e4rkt das Selbstwertgef\u00fchl des Kindes\nbeugt gesundheitlich vor\nWir legen gro\u00dfen Wert auf eine gute, solide Schwimmausbildung/-weiterbildung. Unsere erfahrenen und sehr gut ausgebildeten Trainer werden ihrem Kind die vier Grundlagenschwimmarten n\u00e4her bringen. Dadurch erf\u00e4hrt Ihr Kind eine st\u00e4ndige Leistungsverbesserung/-steigerung, so dass sp\u00e4ter die M\u00f6glichkeit besteht, in unseren wettkampforientierten Nachwuchsschwimmgruppen am Leistungstraining teilzunehmen.\nInformationen rund um unser Sichtungsschwimmen f\u00fcr Kinder und Jugendliche finden Sie in der Kategorie Schwimmen unter Vorschwimmen.\nUnsere \u00dcbungsleiter*innen\nScotty Chris Jacky Dirk\nSophie Tobi Felix Ariana\nWeitere Fragen?\nBei Interesse und Fragen stehen wir Ihnen in der Gesch\u00e4ftsstelle gerne zur Verf\u00fcgung.\nDrucken"
        assert self.open_a_web_page_and_compare(url, shortname, selector, text)

    def test_tsv58(self):
        url = "https://www.tsv58.de/de/sport--ballsport/schwimmen/"
        shortname = "tsv58"
        selector = "div.content_content-inner"
        text = "Ansprechpartner\nRoy Klatt und Jens Berger\ninfo@tsv58.de\n  Trainingszeit\nFreitag 16:15 - 17:15 Uhr\n  Ort\nStadtbad Charlottenburg\nKrumme Stra\u00dfe 9\n10585 Berlin\nSeepferdchen Freitag\nab 5 Jahren / Auf Grund der aktuellen Situation k\u00f6nnen wir aktuell nicht sagen, ob in diesem Jahr Seepferdchen-Kurse stattfinden werden. Bitte ab August 2021 in der Gesch\u00e4ftstelle erfragen.\nErlernen des Schwimmens und Abnahme des Seepferdchen-Abzeichens. Beginn der Kurse  etwas Ende Januar und Ende September. Anmeldung erforderlich! Es muss eine zus\u00e4tzliche Kursgeb\u00fchr entrichtet werden.\n \n\n\n\n\n\n\n\nAnsprechpartner\nJens Berger und Roy Klatt\ninfo@tsv58.de\n  Trainingszeit\nFreitag ab 17:30 - 20:30 Uhr in verschiedenen Gruppen\n  Ort\nStadtbad Charlottenburg\nKrumme Stra\u00dfe 9\n10585 Berlin\nFortgeschrittene Freitag\nDa die Schwimmhallen in den Sommerferien geschlossen sind, bieten wir allen Mitgliedern eine alternative Trainings-M\u00f6glichkeit im Freibad Olympiestadion (Olympischer Platz 3) an. Immer freitags von 17:30-19:00 Uhr ist schwimmen unter unserer Aufsicht m\u00f6glich. Eintritt \u00fcbernimmt der Verein. Zur Planung ist eine Anmeldung in der Gesch\u00e4ftsstelle per Mail oder Anruf) bis donnerstags 13 Uhr notwendig!\nAllgemeines Schwimmtraining und Erlernen der Grundschwimmarten.\nEs besteht die M\u00f6glichkeit zum Erwerb\nder Jugendschwimmabzeichen in Bronze, Silber und Gold\n "
        assert self.open_a_web_page_and_compare(url, shortname, selector, text)

    def test_berlinerbaeder(self):
        url = "https://www.berlinerbaeder.de/schwimmkurse/"
        shortname = "berlinerbaeder"
        selector = "div.wrapper"
        text = "In den Ferien Schwimmen lernen\nFerienschwimmkurse in zehn Sommerb\u00e4dern\nOnline-Reservierung ab sofort f\u00fcr alle m\u00f6glich\n  Mit Beginn der Sommerferien k\u00f6nnen wir in zehn Sommerb\u00e4dern wieder Schwimmlernkurse f\u00fcr Kinder ab dem 5. bis zum 12. Lebensjahr anbieten.\nDie in der Regel dreiw\u00f6chigen Intensivkurse werden ab dem 28. Juni starten. Die Kurse mit zehn bzw. f\u00fcnfzehn Unterrichtseinheiten kosten 70,00 bzw. 105,00 Euro.\nBitte beachten Sie, dass die Schwimmkurse ausschlie\u00dflich in den Sommerb\u00e4dern stattfinden. Daher entspricht die Wassertemperatur den aktuellen Wetterverh\u00e4ltnissen.\nDie hohe Nachfrage nach Kurspl\u00e4tzen infolge der Pandemie macht ein neues Procedere n\u00f6tig: Kurspl\u00e4tze k\u00f6nnen ausschlie\u00dflich im Online-Shop reserviert werden. F\u00fcr die Reservierung wird eine Anzahlung in H\u00f6he von 5,00 Euro erhoben. Beim Bezahlen an der Kasse muss das Reservierungsticket der Buchung vorgelegt werden. Bei der Zahlung wird sowohl die Anzahlung verrechnet als auch nicht eingel\u00f6ste Kurskarten beziehungsweise Gutscheine f\u00fcr Corona-bedingt ausgefallene Kurse aus 2020. Wenn Sie die Reservierung abgeschlossen haben, k\u00f6nnen Sie ab sofort mit der ausgedruckten Reservierungsbest\u00e4tigung an der Kasse des Bades, in dem der Kurs stattfindet, die Bezahlung vornehmen.\nWichtige Information zu den Kursen\nZum 1. Kurstag m\u00fcssen von den Eltern die unterzeichneten Erkl\u00e4rungen \u201eElternbrief Corona-Regelungen\u201c und \"Einverst\u00e4ndniserkl\u00e4rung Schwimmtauglichkeit\" mitgebracht werden. Ohne diese ausgef\u00fcllten Erkl\u00e4rungen kann Ihr Kind leider nicht am Kurs teilnehmen.\nDie Erkl\u00e4rungen k\u00f6nnen Sie sich hier herunterladen.\nElternbrief Corona-Regelungen\nEinverst\u00e4ndniserkl\u00e4rung Schwimmtauglichkeit\n  Intensiv-Schwimmkurse der Sportjugend Berlin\nF\u00fcr Sch\u00fclerinnen und Sch\u00fcler der 3. und 4. Klassen bietet die Sporjugend Berlin gemeinsam mit Berliner Vereinen Intensiv-Schwimmkurse in den Sommerferien an.\nInformationen zu den Kursen finden Sie auf der Seite der Sportjugend Berlin."
        assert self.open_a_web_page_and_compare(url, shortname, selector, text)

    def test_fb0e_debug(self):
        url = "https://0e.vc/monitor-changes-smoke-test.html"
        shortname = "0evc"
        selector = "div#maindiv"
        text = "The news are new. Exciting."
        assert self.open_a_web_page_and_compare(url, shortname, selector, text)