from pathlib import Path

ROOT = Path("plots")


def build_tree(path, indent=0):
    html = ""

    entries = sorted(path.iterdir())

    folders = [e for e in entries if e.is_dir()]
    files = [e for e in entries if e.suffix == ".html"]

    for folder in folders:
        html += " " * indent + f"<details><summary>{folder.name}</summary>\n"

        html += build_tree(folder, indent + 4)

        html += " " * indent + "</details>\n"

    for file in files:
        rel = file.as_posix()

        name = file.stem.replace("_", " ")

        html += (
            " " * indent
            + f'<div><a target="viewer" href="#/{rel[:-5]}">{name}</a></div>\n'
        )

    return html


sidebar = build_tree(ROOT)

with open("sidebar.js", "w") as f:
    f.write(f'document.getElementById("sidebar").innerHTML = `{sidebar}`;')
# %%
