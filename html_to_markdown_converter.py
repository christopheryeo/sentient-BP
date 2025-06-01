import json
import textwrap
import sys # Ensure sys is imported

def escape_table_cell(text):
    if text is None:
        return ""
    return str(text).replace("|", "\\|").rstrip() # MD009

def format_table(headers, rows):
    if not headers:
        if not rows or not rows[0]:
            return ""
        num_cols = len(rows[0])
        headers = [""] * num_cols

    num_cols = len(headers)
    if num_cols == 0:
        return ""

    markdown_table_parts = []
    markdown_table_parts.append(("| " + " | ".join(escape_table_cell(h) for h in headers) + " |").rstrip())
    markdown_table_parts.append(("| " + " | ".join(["---"] * num_cols) + " |").rstrip())
    for row in rows:
        processed_row = list(row)
        if len(processed_row) < num_cols:
            processed_row.extend([""] * (num_cols - len(processed_row)))
        elif len(processed_row) > num_cols:
            processed_row = processed_row[:num_cols]
        markdown_table_parts.append(("| " + " | ".join(escape_table_cell(c) for c in processed_row) + " |").rstrip())

    return "\n".join(markdown_table_parts) + "\n"

def process_blockquote_text(text_content):
    """Helper to format multiline text inside blockquotes for MD028 and MD009."""
    lines = text_content.strip().splitlines()
    processed_lines = []
    for line in lines:
        stripped_line = line.strip() # Remove leading/trailing whitespace from the original line
        if stripped_line: # Only add non-empty lines
            processed_lines.append(f"> {stripped_line.rstrip()}") # MD009
        # else: # Avoids creating ">" lines for blank lines within the source text
            # If we wanted to preserve internal blank lines but ensure they have "> ",
            # it would be: processed_lines.append(f"> {stripped_line.rstrip()}")
            # but MD028 wants no blank lines within blockquotes, so skipping empty lines is better.
    return "\n".join(processed_lines)


def convert_to_markdown(slides_data):
    markdown_slide_outputs = [] # Stores the full markdown for each slide

    for slide_idx, slide in enumerate(slides_data):
        slide_content_blocks = [] # Store markdown for each block within a slide

        items = slide.get('content', [])
        i = 0
        while i < len(items):
            item = items[i]
            item_type = item.get('type')
            item_text = item.get('text', "")
            block_md = ""

            # MD041: First line should be H1.
            # We'll make the first slide's action_title H1, others H2.
            if item_type == 'action_title':
                if slide_idx == 0:
                    block_md = f"# {item_text.rstrip()}\n"
                else:
                    block_md = f"## {item_text.rstrip()}\n"
            elif item_type == 'subtitle':
                # MD001: Adjust subtitle based on preceding title level
                # If previous was H1, this is H2 (or H3). If previous was H2, this is H3 (or H4).
                # For simplicity, making it H4 consistently after H2, or H3 after H1.
                if slide_idx == 0: # Subtitle for the H1 slide title
                    block_md = f"### {item_text.rstrip()}\n" # H3
                else: # Subtitle for H2 slide titles
                    block_md = f"#### {item_text.rstrip()}\n" # H4

            elif item_type == 'paragraph':
                if item_text.strip():
                    # replace_whitespace=False and drop_whitespace=False are important
                    # to prevent textwrap from altering intentional spacing too much.
                    wrapped_text = textwrap.fill(item_text, width=80, replace_whitespace=False, drop_whitespace=False)
                    block_md = f"{wrapped_text.rstrip()}\n"
                # else: # If paragraph is empty, don't add anything, let inter-block spacing handle it
                    # block_md = "\n" # This would create an extra blank line if not careful

            elif item_type == 'list_item':
                current_list_items_text = []
                while i < len(items) and items[i].get('type') == 'list_item':
                    list_item_content = items[i].get('text', '')
                    # Simple rstrip for list items, full wrapping can be complex with indentation
                    current_list_items_text.append(f"- {list_item_content.rstrip()}")
                    i += 1
                block_md = "\n".join(current_list_items_text) + "\n"
                i -= 1

            elif item_type == 'table_header' or item_type == 'table_cell':
                headers = []
                rows = []
                current_row = []

                while i < len(items) and items[i].get('type') == 'table_header':
                    headers.append(items[i].get('text', ''))
                    i += 1

                num_cols = len(headers) if headers else 0

                while i < len(items) and items[i].get('type') == 'table_cell':
                    current_row.append(items[i].get('text', ''))
                    if num_cols > 0 and len(current_row) == num_cols:
                        rows.append(list(current_row))
                        current_row = []
                    elif num_cols == 0 and (i + 1 == len(items) or items[i+1].get('type') != 'table_cell'):
                        if not num_cols and not headers and current_row:
                            num_cols = len(current_row)
                        if current_row:
                           rows.append(list(current_row))
                           current_row = []
                    i += 1

                if current_row:
                    rows.append(list(current_row))

                if headers or rows:
                    block_md = format_table(headers, rows)
                i -= 1

            elif item_type == 'stat_value':
                stat_value_text = item_text.rstrip()
                stat_label_text = ""
                if (i + 1) < len(items) and items[i+1].get('type') == 'stat_label':
                    stat_label_text = items[i+1].get('text', '').rstrip()
                    i += 1
                if stat_label_text:
                    block_md = f"**{stat_value_text}:** {stat_label_text}\n"
                else:
                    block_md = f"**{stat_value_text}**\n"

            elif item_type == 'callout_box' or item_type == 'framework_item':
                blockquote_lines = []
                if ' | ' in item_text:
                    title, content = item_text.split(' | ', 1)
                    title = title.strip().rstrip()
                    content = content.strip() # Content will be split by lines by process_blockquote_text
                    if title:
                        blockquote_lines.append(f"> **{title}**")
                    if content: # Only add content if it's not empty
                        # If there was a title, and content exists, add a ">" line for spacing ONLY if content is multi-line or to separate from title
                        # MD028 fix: process_blockquote_text handles multi-line content correctly.
                        # No explicit ">" line needed here if title exists.
                        processed_content_blockquote = process_blockquote_text(content)
                        if processed_content_blockquote : # if content results in valid blockquote lines
                             blockquote_lines.append(processed_content_blockquote)
                else: # No title separator
                    processed_item_text_blockquote = process_blockquote_text(item_text)
                    if processed_item_text_blockquote:
                        blockquote_lines.append(processed_item_text_blockquote)

                if blockquote_lines:
                    block_md = "\n".join(blockquote_lines) + "\n"

            if block_md.strip(): # Add block if it's not just whitespace
                 slide_content_blocks.append(block_md.rstrip()) # Add rstrip() here too for safety
            i += 1

        # Join all markdown blocks for the current slide with ONE blank line (two newlines)
        processed_slide_content = "\n\n".join(filter(None, slide_content_blocks)) # filter(None,...) removes empty strings
        markdown_slide_outputs.append(processed_slide_content)

    # Join slides with a thematic break, ensuring one blank line before and after "---"
    final_markdown = ""
    for idx, part in enumerate(markdown_slide_outputs):
        if part: # Only add if part is not empty
            final_markdown += part
            if idx < len(markdown_slide_outputs) - 1:
                # Check if the next part is also non-empty before adding separator
                if markdown_slide_outputs[idx+1]:
                     final_markdown += "\n\n---\n\n"

    return final_markdown.strip() + "\n" # Ensure final document ends with a newline for POSIX compliance


if __name__ == '__main__':
    try:
        with open('parsed_html.json', 'r', encoding='utf-8') as f:
            html_data = json.load(f)

        markdown_output = convert_to_markdown(html_data)
        print(markdown_output)

    except FileNotFoundError:
        sys.stderr.write("Error: parsed_html.json not found. Please ensure it's in the same directory.\n")
    except json.JSONDecodeError:
        sys.stderr.write("Error: Could not decode JSON from parsed_html.json.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")
