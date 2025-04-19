import os
from pathlib import Path

root = Path.cwd()  # or manually set your root path
ctan = root / "CTAN"
ctan.mkdir(exist_ok=True)

# Paths
catalog_tex = root / "CATALOG.tex"
catalog_pdf = root / "CATALOG.pdf"
sty_file = root / "open-everyday-tikz-symbols.sty"

# Read sty file
with sty_file.open(encoding="utf-8") as f:
    sty_content = f.read()

# Replace all \input{...} with actual content
lines = sty_content.splitlines()
new_lines = []
for line in lines:
    if "\\input{" in line:
        start = line.find(r"\input{") + len(r"\input{")
        end = line.find("}", start)
        relative_path = line[start:end]
        input_file = root / (relative_path + ".tex")
        if input_file.exists():
            with input_file.open(encoding="utf-8") as f:
                included = f.read()
            new_lines.append(f"% --- BEGIN {relative_path}.tex ---")
            new_lines.append(included)
            new_lines.append(f"% --- END {relative_path}.tex ---")
        else:
            print(f"WARNING: File not found: {input_file}")
    else:
        new_lines.append(line)

# Save modified .sty
(ctan / sty_file.name).write_text("\n".join(new_lines), encoding="utf-8")

# Copy CATALOG.tex and .pdf
(ctan / catalog_tex.name).write_text(catalog_tex.read_text(encoding="utf-8"), encoding="utf-8")
(ctan / catalog_pdf.name).write_bytes(catalog_pdf.read_bytes())

print("✅ CTAN package assembled in:", ctan)