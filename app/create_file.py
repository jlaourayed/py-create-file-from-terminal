import sys
from datetime import datetime
from pathlib import Path

# 1. Lecture de sys.argv
args = sys.argv[1:]

directories = []
filename = ""

if "-d" in args:
    idx_d = args.index("-d")
    for item in args[idx_d + 1:]:
        if item in ("-d", "-f"):
            break
        directories.append(item)

if "-f" in args:
    idx_f = args.index("-f")
    if idx_f + 1 < len(args):
        filename = args[idx_f + 1]

# 2. Gestion des dossiers
dir_path = Path(*directories) if directories else None

if dir_path:
    dir_path.mkdir(parents=True, exist_ok=True)

# 3. Écriture dans le fichier
if filename:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    # L'horodatage est isolé sur sa première ligne
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_block = f"{timestamp}\n"

    # Ajout des lignes de contenu indexées (avec un \n normal en fin de ligne)
    for idx, content in enumerate(lines, start=1):
        if idx == len(lines):
            formatted_block += f"{idx} {content}"
        else:
            formatted_block += f"{idx} {content}\n"

    full_file_path = dir_path / filename if dir_path else Path(filename)

    if full_file_path.exists() and full_file_path.stat().st_size > 0:
        with full_file_path.open("a", encoding="utf-8") as file:
            file.write("\n\n" + formatted_block)
    else:
        with full_file_path.open("a", encoding="utf-8") as file:
            file.write(formatted_block)
