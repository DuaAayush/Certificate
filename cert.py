from PIL import Image, ImageDraw, ImageFont
import csv
# Load the certificate template image
cert_template = Image.open('certificate_template.png')

# Load the font
font = ImageFont.truetype('arial.ttf', size=32)
def add_name_to_certificate(name, cert_template):
    # Create a draw object
    draw = ImageDraw.Draw(cert_template)
    
    # Get the size of the certificate template
    width, height = cert_template.size
    
    # Calculate the position to place the name
    text_width, text_height = draw.textsize(name, font=font)
    x = (width - text_width) / 2
    y = height - 150
    
    # Add the name to the certificate template
    draw.text((x, y), name, font=font, fill='black')
    
    return cert_template
# Load the names from the CSV file
with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    names = [name[0] for name in reader]

# Add the names to the certificate template and save them
for name in names:
    cert = add_name_to_certificate(name, cert_template)
    cert.save(f'{name}_certificate.png')

