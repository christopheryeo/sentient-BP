import json
import re

def parse_markdown_to_json(markdown_content):
    """
    Parses Markdown text to extract sections based on headings and outputs JSON.
    A section includes all content under a heading, including sub-headings,
    until the next heading of the same or higher level.
    """
    sections = []
    current_section_data = None # Stores {level, title, content_lines}

    heading_pattern = re.compile(r"^(#+)\s+(.*)")

    for line in markdown_content.splitlines():
        heading_match = heading_pattern.match(line)

        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()

            if current_section_data is not None and level <= current_section_data["level"]:
                sections.append({
                    "title": current_section_data["title"],
                    "content": "\n".join(current_section_data["content_lines"]).strip()
                })
                current_section_data = None

            if current_section_data is None:
                 current_section_data = {"level": level, "title": title, "content_lines": []}
            elif level > current_section_data["level"]:
                current_section_data["content_lines"].append(line)

            if current_section_data is None:
                 current_section_data = {"level": level, "title": title, "content_lines": []}
            elif current_section_data["title"] != title and level <= current_section_data["level"]:
                # This case should be covered by the first conditional block that closes sections.
                # If it's a new title at the same or higher level, the previous section is closed,
                # and current_section_data is reset and then re-initialized.
                # This specific 'elif' might be redundant if the logic flow is correct.
                # Re-initializing if title is different but level is same/higher:
                current_section_data = {"level": level, "title": title, "content_lines": []}


        elif current_section_data is not None:
            current_section_data["content_lines"].append(line)

    if current_section_data is not None:
        sections.append({
            "title": current_section_data["title"],
            "content": "\n".join(current_section_data["content_lines"]).strip()
        })

    return sections # Return the list of dicts, not JSON string yet

if __name__ == "__main__":
    markdown_file_path = "content/content.md"
    output_json_path = "parsed_markdown.json"
    try:
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        processed_content = "\n".join(line for line in content.splitlines() if line.strip() != "---")

        sections_data = parse_markdown_to_json(processed_content)

        with open(output_json_path, 'w', encoding='utf-8') as outfile:
            json.dump(sections_data, outfile, indent=4)
        print(f"Successfully parsed Markdown and saved to {output_json_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {markdown_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
