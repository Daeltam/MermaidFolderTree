import os


def build_mindmap(path, indent=2):
    lines = []
    prefix = "  " * indent
    entries = sorted(os.scandir(path), key=lambda e: (not e.is_dir(follow_symlinks=False), e.name))
    for entry in entries:
        if entry.is_symlink():
            continue
        if entry.is_dir():
            lines.append(f"{prefix}{entry.name}")
            lines.extend(build_mindmap(entry.path, indent + 1))
        else:
            lines.append(f"{prefix}{entry.name}")
    return lines


def main():
    path = input("Enter the path to the folder: ").strip()

    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a valid directory.")
        return

    folder_name = os.path.basename(os.path.abspath(path))
    output_file = f"{folder_name}_mindmap.md"

    lines = ["```mermaid", "mindmap", f"  root(({folder_name}))"]
    lines.extend(build_mindmap(path))
    lines.append("```")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Mindmap saved to '{output_file}'")


if __name__ == "__main__":
    main()
