from argostranslate import translate
from pathlib import Path

input_path = Path(input("Podaj nazwę pliku .srt do tłumaczenia: ").strip())
if not input_path.exists():
    print(f"❌ Plik '{input_path}' nie istnieje.")
    exit(1)

output_path = input_path.with_name(f"{input_path.stem}_EN{input_path.suffix}")

def is_timestamp(line: str) -> bool:
    return "-->" in line

def is_numbered_line(line: str) -> bool:
    return line.strip().isdigit()

translated_lines = []
with input_path.open("r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()
        if not stripped:
            translated_lines.append("\n")
        elif is_numbered_line(stripped) or is_timestamp(stripped):
            translated_lines.append(line)
        else:
            translated = translate.translate(stripped, "pl", "en")
            translated_lines.append(translated + "\n")

with output_path.open("w", encoding="utf-8") as f:
    f.writelines(translated_lines)

print(f"✔ Tłumaczenie zakończone. Zapisano do: {output_path}")

