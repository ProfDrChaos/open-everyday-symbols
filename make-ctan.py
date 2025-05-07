import os
from pathlib import Path
import shutil

root = Path.cwd()
ctan = root / "open-everyday-symbols"
ctan.mkdir(exist_ok=True)

# Paths
documentation_tex = root / "open-everyday-symbols-doc.tex"
documentation_pdf = root / "open-everyday-symbols-doc.pdf"
sty_file = root / "open-everyday-symbols.sty"
readme_file = root / "README.md"

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
            new_lines.append("")
            new_lines.append(included)
            new_lines.append("")
            new_lines.append(f"% --- END {relative_path}.tex ---")
        else:
            print(f"WARNING: File not found: {input_file}")
    else:
        new_lines.append(line)

# Save modified .sty
(ctan / sty_file.name).write_text("\n".join(new_lines), encoding="utf-8")

# Copy documentation
(ctan / documentation_tex.name).write_text(documentation_tex.read_text(encoding="utf-8"), encoding="utf-8")
(ctan / documentation_pdf.name).write_bytes(documentation_pdf.read_bytes())

# Copy README
if readme_file.exists():
    (ctan / readme_file.name).write_text(readme_file.read_text(encoding="utf-8"), encoding="utf-8")

# Create zip archive
zip_path = shutil.make_archive("open-everyday-symbols", 'zip', root_dir=ctan.parent, base_dir=ctan.name)

# Delete the directory
shutil.rmtree(ctan)

print("✅ Zipped package created at:", zip_path)
print("📦 Folder deleted:", ctan)