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
CUSTOM_KEYWORDS_PATH = os.path.abspath(os.path.join(DATA_DIR, "custom_keywords.json"))


def _ensure_data_files() -> None:
	os.makedirs(os.path.dirname(LEARNING_PATH), exist_ok=True)
	if not os.path.exists(LEARNING_PATH):
		with open(LEARNING_PATH, "w", encoding="utf-8") as f:
			json.dump({}, f)
	if not os.path.exists(CATEGORIES_PATH):
		with open(CATEGORIES_PATH, "w", encoding="utf-8") as f:
			json.dump(DEFAULT_CATEGORIES, f, ensure_ascii=False, indent=2)
	if not os.path.exists(CUSTOM_KEYWORDS_PATH):
		with open(CUSTOM_KEYWORDS_PATH, "w", encoding="utf-8") as f:
			json.dump({}, f, ensure_ascii=False, indent=2)


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


def _save_categories(categories: List[str]) -> None:
	_ensure_data_files()
	with open(CATEGORIES_PATH, "w", encoding="utf-8") as f:
		json.dump(categories, f, ensure_ascii=False, indent=2)


def _load_custom_keywords() -> Dict[str, List[str]]:
	_ensure_data_files()
	with open(CUSTOM_KEYWORDS_PATH, "r", encoding="utf-8") as f:
		return json.load(f)


def _save_custom_keywords(keywords: Dict[str, List[str]]) -> None:
	_ensure_data_files()
	with open(CUSTOM_KEYWORDS_PATH, "w", encoding="utf-8") as f:
		json.dump(keywords, f, ensure_ascii=False, indent=2)


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
	# Load custom keywords from file
	custom_keywords = _load_custom_keywords()
	
	# Base keyword rules
	base_rules = [
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
		("Zertifikate", ["zertifikat", "bescheinigung", "urkunde", "certificate", "diplom", "abschluss", "qualifikation", "ausbildung", "kurs", "schulung", "teilnahme", "participation", "seminare", "workshop", "fortbildung", "weiterbildung", "lernziele", "veranstaltung"]),
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
	
	# Add custom keywords to the rules (at the beginning for priority)
	custom_rules = []
	for category, keywords in custom_keywords.items():
		custom_rules.append((category, keywords))
	
	# Return custom rules first, then base rules
	return custom_rules + base_rules


def classify_text(text: str) -> str:
	text_norm = _normalize(text)
	if not text_norm.strip():
		return "Unknown"

	# Rule-based keywords - prioritize longer, more specific matches
	rules = _keyword_rules()
	
	# Sort rules by keyword length (longer keywords first) for better specificity
	sorted_rules = []
	for category, keywords in rules:
		for kw in keywords:
			sorted_rules.append((len(kw), category, kw))
	
	# Sort by length descending, then by category name
	sorted_rules.sort(key=lambda x: (-x[0], x[1]))
	
	for _, category, kw in sorted_rules:
		if kw in text_norm:
			return category
	
	# Try fuzzy matching for OCR errors
	from rapidfuzz import fuzz
	best_fuzzy_match = None
	best_fuzzy_score = 0
	
	for _, category, kw in sorted_rules:
		# Check if keyword is similar to any word in the text
		words = text_norm.split()
		for word in words:
			score = fuzz.ratio(kw, word)
			if score > 80 and score > best_fuzzy_score:  # 80% similarity threshold
				best_fuzzy_match = category
				best_fuzzy_score = score
	
	if best_fuzzy_match:
		return best_fuzzy_match

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


def add_custom_keywords(category: str, keywords: List[str]) -> None:
	"""Add custom keywords for a category"""
	custom_keywords = _load_custom_keywords()
	custom_keywords[category] = keywords
	_save_custom_keywords(custom_keywords)
