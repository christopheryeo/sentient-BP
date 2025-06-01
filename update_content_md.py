import subprocess
import sys

def run_converter_and_get_markdown():
    """
    Runs html_to_markdown_converter.py and captures its stdout.
    """
    try:
        # Assuming python3 is the interpreter for html_to_markdown_converter.py
        # and the script is in the current working directory or accessible via PATH.
        process = subprocess.run(
            [sys.executable, 'html_to_markdown_converter.py'],
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        # Check for errors in the converter script's execution itself
        if process.stderr:
            print(f"Error during Markdown generation: {process.stderr}", file=sys.stderr)
            # Decide if this is fatal. For now, proceed if stdout might still be valid.
        return process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running html_to_markdown_converter.py: {e}", file=sys.stderr)
        print(f"Stdout: {e.stdout}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("Error: html_to_markdown_converter.py not found.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred while running converter: {e}", file=sys.stderr)
        return None

def write_markdown_to_file(markdown_content, filepath):
    """
    Writes the given markdown_content to the specified filepath, overwriting it.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully wrote new Markdown content to {filepath}")
    except IOError as e:
        print(f"Error writing to file {filepath}: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred while writing file: {e}", file=sys.stderr)

if __name__ == '__main__':
    target_filepath = 'content/content.md'

    print("Generating new Markdown content...")
    new_markdown = run_converter_and_get_markdown()

    if new_markdown is not None:
        # Before writing, check if the new_markdown actually contains content.
        # The converter script prints error messages to stdout on file not found for json.
        # We need to ensure those are not written into content.md
        if "Error: parsed_html.json not found" in new_markdown or \
           "Error: Could not decode JSON" in new_markdown:
            print(f"Markdown generation script produced an error message instead of content: {new_markdown.strip()}", file=sys.stderr)
            print("Aborting write to content/content.md")
        elif not new_markdown.strip():
             print("Warning: Generated Markdown content is empty. Writing an empty file to content/content.md.", file=sys.stderr)
             write_markdown_to_file(new_markdown, target_filepath)
        else:
            print("Writing new Markdown content to content/content.md...")
            write_markdown_to_file(new_markdown, target_filepath)
    else:
        print("Failed to generate new Markdown content. content/content.md will not be updated.")
