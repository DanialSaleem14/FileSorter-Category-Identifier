import json
import os
from typing import Dict, List, Tuple

from rapidfuzz import fuzz

DEFAULT_CATEGORIES: List[str] = [
	"Rechnungen", "Mahnungen", "Quittungen", "Angebote", "Bestellungen",
	"Verträge allgemein", "Arbeitsvertrag", "Mietvertrag", "Kaufvertrag",
	"Versicherung", "Steuerunterlagen", "Kontoauszüge / Bank",
	# Arbeit & Schule
	"Bewerbungen", "Lebenslauf", "Zeugnisse", "Zertifikate",
	"Schulunterlagen", "Studium / Uni", "Arbeitsprojekte", "Präsentationen",
	# Gesundheit & Familie
	"Arztberichte", "Rezepte", "Krankenhausunterlagen", "Impfungen",
	"Krankenkasse", "Familie", "Kinder / Schule", "Haustiere",
	# Reisen & Freizeit
	"Tickets", "Hotelbuchungen", "Urlaubsplanung", "Ausweis / Reisepass",
	"Führerschein", "Auto / Fahrzeugpapiere", "Fahrkarten / ÖPNV",
	"Events / Konzertkarten",
	# Behörden & Recht
	"Personalausweis", "Steuerbescheide", "Gericht / Anwalt",
	"Bußgeld / Strafe", "Rente / Sozialversicherung", "Meldebescheinigung",
	"Zeugenaussagen / Formulare",
	# Technik & Sonstiges
	"Handbücher / Bedienungsanleitungen", "Garantie / Gewährleistung",
	"Software-Lizenzen", "Screenshots / Notizen", "Fotos & Bilder",
	"Musik & Videos", "Allgemeine Dokumente / Sonstiges",
	"Unknown",
]

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
LEARNING_PATH = os.path.abspath(os.path.join(DATA_DIR, "learning.json"))
CATEGORIES_PATH = os.path.abspath(os.path.join(DATA_DIR, "categories.json"))


def _ensure_data_files() -> None:
	os.makedirs(os.path.dirname(LEARNING_PATH), exist_ok=True)
	if not os.path.exists(LEARNING_PATH):
		with open(LEARNING_PATH, "w", encoding="utf-8") as f:
			json.dump({}, f)
	if not os.path.exists(CATEGORIES_PATH):
		with open(CATEGORIES_PATH, "w", encoding="utf-8") as f:
			json.dump(DEFAULT_CATEGORIES, f, ensure_ascii=False, indent=2)


def _load_learning() -> Dict[str, str]:
	_ensure_data_files()
	with open(LEARNING_PATH, "r", encoding="utf-8") as f:
		return json.load(f)


def _save_learning(store: Dict[str, str]) -> None:
	with open(LEARNING_PATH, "w", encoding="utf-8") as f:
		json.dump(store, f, ensure_ascii=False, indent=2)


def _load_categories() -> List[str]:
	_ensure_data_files()
	with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
		cats: List[str] = json.load(f)
	return cats


def _normalize(text: str) -> str:
	# Lowercase and normalize German umlauts for more robust matching
	t = (text or "").lower()
	t = (
		t.replace("ä", "ae")
		.replace("ö", "oe")
		.replace("ü", "ue")
		.replace("ß", "ss")
	)
	return t


def _keyword_rules() -> List[Tuple[str, List[str]]]:
	return [
		("Rechnungen", ["rechnung", "rechnungsnummer", "betrag", "steuer", "ust", "mwst", "fälligkeit"]),
		("Mahnungen", ["mahnung", "zahlungserinnerung", "letzte mahnung"]),
		("Quittungen", ["quittung", "kassenbon", "zahlung erhalten", "beleg"]),
		("Angebote", ["angebot", "offerte", "preisangebot", "quote"]),
		("Bestellungen", ["bestellung", "auftragsbestätigung", "order", "auftrag"]),
		("Verträge allgemein", ["vertrag", "vertragsnummer", "vereinbarung"]),
		("Arbeitsvertrag", ["arbeitsvertrag", "arbeitgeber", "arbeitnehmer"]),
		("Mietvertrag", ["mietvertrag", "vermieter", "mieter", "kaution"]),
		("Kaufvertrag", ["kaufvertrag", "käufer", "verkäufer", "kaufpreis"]),
		("Versicherung", ["versicherung", "police", "versicherungsnummer", "beitrag"]),
		("Steuerunterlagen", ["steuer", "elster", "einkommensteuer", "steuerbescheid"]),
		("Kontoauszüge / Bank", ["kontoauszug", "kontobewegung", "iban", "bank"]),
		("Bewerbungen", ["bewerbung", "anschreiben", "bewerber"]),
		("Lebenslauf", ["lebenslauf", "cv", "curriculum vitae"]),
		("Zeugnisse", ["zeugnis", "arbeitszeugnis", "zwischenzeugnis"]),
		("Zertifikate", ["zertifikat", "bescheinigung", "urkunde", "certificate", "diplom", "abschluss", "qualifikation", "ausbildung", "kurs", "schulung"]),
		("Schulunterlagen", ["schule", "noten", "zeugnisse", "unterricht"]),
		("Studium / Uni", ["universität", "hochschule", "studium", "matrikel"]),
		("Arbeitsprojekte", ["projekt", "projektplan", "task", "sprint"]),
		("Präsentationen", ["präsentation", "folien", "agenda", "slide", "deck"]),
		("Arztberichte", ["arzt", "befund", "diagnose"]),
		("Rezepte", ["rezept", "verschreibung", "apotheke"]),
		("Krankenhausunterlagen", ["krankenhaus", "entlassbrief", "stationär"]),
		("Impfungen", ["impfung", "impfpass", "impfzertifikat"]),
		("Krankenkasse", ["krankenkasse", "versicherungskarte", "mitgliedsnummer"]),
		("Familie", ["familie", "heirat", "geburt"]),
		("Kinder / Schule", ["kind", "schule", "kita"]),
		("Haustiere", ["hund", "katze", "tierarzt"]),
		("Tickets", ["ticket", "flug", "bahn", "eintrittskarte"]),
		("Hotelbuchungen", ["hotel", "buchung", "reservierung"]),
		("Urlaubsplanung", ["urlaub", "reiseplan", "itinerary"]),
		("Ausweis / Reisepass", ["reisepass", "passnummer", "ausweis"]),
		("Führerschein", ["führerschein", "fahrerlaubnis"]),
		("Auto / Fahrzeugpapiere", ["fahrzeugschein", "fahrzeugbrief", "zulassung", "tüv"]),
		("Fahrkarten / ÖPNV", ["fahrkarte", "abo", "monatskarte", "öpnv"]),
		("Events / Konzertkarten", ["konzert", "event", "ticketmaster"]),
		("Personalausweis", ["personalausweis", "id-karte"]),
		("Steuerbescheide", ["steuerbescheid", "bescheid", "festsetzung"]),
		("Gericht / Anwalt", ["gericht", "anwalt", "klage", "urteil"]),
		("Bußgeld / Strafe", ["bußgeld", "strafe", "verwarnung"]),
		("Rente / Sozialversicherung", ["rente", "sozialversicherung", "rentenkasse"]),
		("Meldebescheinigung", ["meldebescheinigung", "einwohnermeldeamt"]),
		("Zeugenaussagen / Formulare", ["formular", "zeugenaussage", "antrag"]),
		("Handbücher / Bedienungsanleitungen", ["handbuch", "bedienungsanleitung", "manual"]),
		("Garantie / Gewährleistung", ["garantie", "gewährleistung", "hersteller"]),
		("Software-Lizenzen", ["lizenz", "license key", "product key"]),
		("Screenshots / Notizen", ["screenshot", "notiz", "memo"]),
		("Fotos & Bilder", ["foto", "bild", "jpeg", "png"]),
		("Musik & Videos", ["musik", "audio", "video", "mp3", "mp4"]),
		("Allgemeine Dokumente / Sonstiges", ["dokument", "unterlage", "sonstiges"]),
	]


def classify_text(text: str) -> str:
	text_norm = _normalize(text)
	if not text_norm.strip():
		return "Unknown"

	# Rule-based keywords
	for category, keywords in _keyword_rules():
		for kw in keywords:
			if kw in text_norm:
				return category

	# Fuzzy match against learned exemplars
	learning = _load_learning()
	best_category = "Unknown"
	best_score = 0
	for exemplar, category in learning.items():
		score = fuzz.partial_ratio(_normalize(exemplar), text_norm)
		if score > best_score:
			best_score = score
			best_category = category

	# Threshold to avoid random matches
	if best_score >= 70:
		return best_category
	return "Unknown"


def learn(text: str, category: str) -> None:
	if not text.strip():
		return
	store = _load_learning()
	snippet = _normalize(text).strip()[:500]
	store[snippet] = category
	_save_learning(store)
