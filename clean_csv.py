import csv
from pathlib import Path


def clean_csv(input_file: str, output_file: str) -> None:
source = Path(input_file)
target = Path(output_file)

if not source.exists():
raise FileNotFoundError(f"Input file not found: {input_file}")

with source.open("r", newline="", encoding="utf-8") as infile, target.open("w", newline="", encoding="utf-8") as outfile:
reader = csv.DictReader(infile)
fieldnames = [name.strip().lower().replace(" ", "_") for name in reader.fieldnames or []]

writer = csv.DictWriter(outfile, fieldnames=fieldnames)
writer.writeheader()

for row in reader:
cleaned = {
key.strip().lower().replace(" ", "_"): (value.strip() if isinstance(value, str) else value)
for key, value in row.items()
}
writer.writerow(cleaned)


if __name__ == "__main__":
input_file = input("Input CSV path: ").strip()
output_file = input("Output CSV path: ").strip()
clean_csv(input_file, output_file)
