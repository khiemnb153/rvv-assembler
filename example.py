from src.parser import sectionify, parse_data, parse_text
from src.translator import translate_data, translate_text
import os

INPUT_FILE = 'test_0.S'
OUTPUT_DIR = 'output'

# Read assembly file
f = open(INPUT_FILE, 'r', encoding="utf-8")
assembly = f.read()
f.close()

# Split into text section and data section
text_section, data_section = sectionify(assembly)

# Parse
data = parse_data(data_section)
text= parse_text(text_section, data)

# Translate
dmem = translate_data(data)
imem = translate_text(text)

# Output
os.makedirs(OUTPUT_DIR, exist_ok=True)

f = open(f'{OUTPUT_DIR}/dmem.mem', 'w')
f.write(dmem)
f.close

f = open(f'{OUTPUT_DIR}/imem.mem', 'w')
f.write(imem)
f.close
