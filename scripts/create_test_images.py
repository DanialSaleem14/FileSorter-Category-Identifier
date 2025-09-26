import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UNSORTED = os.path.join(BASE, "UnsortedDemo")

def create_certificate_image(text: str, filename: str) -> None:
	# Create a certificate-like image
	img = Image.new('RGB', (800, 600), color='white')
	draw = ImageDraw.Draw(img)
	
	# Try to use a nice font, fallback to default
	try:
		font_large = ImageFont.truetype("arial.ttf", 24)
		font_medium = ImageFont.truetype("arial.ttf", 18)
		font_small = ImageFont.truetype("arial.ttf", 14)
	except:
		font_large = ImageFont.load_default()
		font_medium = ImageFont.load_default()
		font_small = ImageFont.load_default()
	
	# Draw border
	draw.rectangle([50, 50, 750, 550], outline='black', width=3)
	
	# Draw title
	draw.text((400, 100), "ZERTIFIKAT", fill='black', font=font_large, anchor='mm')
	
	# Draw content
	lines = textwrap.wrap(text, width=40)
	y_pos = 200
	for line in lines:
		draw.text((400, y_pos), line, fill='black', font=font_medium, anchor='mm')
		y_pos += 30
	
	# Draw signature line
	draw.text((400, 500), "Unterschrift: _________________", fill='black', font=font_small, anchor='mm')
	
	img.save(os.path.join(UNSORTED, filename))

def create_invoice_image(text: str, filename: str) -> None:
	# Create an invoice-like image
	img = Image.new('RGB', (600, 400), color='white')
	draw = ImageDraw.Draw(img)
	
	try:
		font_large = ImageFont.truetype("arial.ttf", 20)
		font_medium = ImageFont.truetype("arial.ttf", 16)
	except:
		font_large = ImageFont.load_default()
		font_medium = ImageFont.load_default()
	
	# Draw header
	draw.text((50, 50), "RECHNUNG", fill='black', font=font_large)
	draw.text((50, 80), "Rechnungsnummer: 2024-001", fill='black', font=font_medium)
	draw.text((50, 110), "Datum: 25.09.2024", fill='black', font=font_medium)
	
	# Draw content
	lines = textwrap.wrap(text, width=50)
	y_pos = 150
	for line in lines:
		draw.text((50, y_pos), line, fill='black', font=font_medium)
		y_pos += 25
	
	# Draw total
	draw.text((50, 350), "Gesamtbetrag: 199,00 EUR", fill='black', font=font_large)
	
	img.save(os.path.join(UNSORTED, filename))

def main() -> None:
	os.makedirs(UNSORTED, exist_ok=True)
	
	# Create certificate images
	create_certificate_image("Dieses Zertifikat bestätigt die erfolgreiche Teilnahme am Python-Programmierkurs. Der Teilnehmer hat alle Module erfolgreich abgeschlossen.", "Python_Zertifikat.png")
	create_certificate_image("Bescheinigung über den erfolgreichen Abschluss der Ausbildung zum Fachinformatiker. Qualifikation: Anwendungsentwicklung.", "Ausbildungszeugnis.jpg")
	create_certificate_image("Certificate of Completion - Microsoft Office Specialist. The candidate has demonstrated proficiency in Microsoft Excel.", "Excel_Zertifikat.tiff")
	
	# Create invoice images
	create_invoice_image("Rechnung für IT-Dienstleistungen. Beratung und Entwicklung einer Dokumentenorganisations-Software. Stundensatz: 85 EUR", "IT_Rechnung.png")
	create_invoice_image("Mahnung - Zahlungserinnerung. Rechnungsnummer 2024-001 ist seit 30 Tagen überfällig. Bitte begleichen Sie den Betrag umgehend.", "Mahnung_Bild.jpg")
	
	print(f"Test images created in: {UNSORTED}")

if __name__ == "__main__":
	main()
