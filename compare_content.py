import json
import re
import difflib

# --- Text Normalization ---
def normalize_text(text):
    if text is None:
        text = ""
    text = str(text) # Ensure text is a string
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace('\u2705', '').replace('\u274c', '').replace('\u26a0\ufe0f', '')
    text = text.replace('\ud83d\udfe0', '').replace('\ud83d\udfe3', '')
    return text

def extract_numerical_data(text):
    if text is None: text = ""
    # Simplified regex for broader matching, includes currency symbols, percentages, and version numbers like x.x
    pattern = re.compile(r'([\$\u20ac\u00a3]?\s*\d+[\d,.]*\d*[\%xmMkK]?\b|\b\d+\-\d+[xmMkK]?\b)')
    # Get unique numbers, sort them for consistent comparison
    return sorted(list(set(match[0] for match in pattern.finditer(normalize_text(text)))))


# --- Content Loading ---
def load_json_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}. Please ensure this file exists.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}. Please check its format.")
        return None

# --- Main Comparison Logic ---
def compare_content_data(markdown_data, html_data):
    differences_report = []

    if not markdown_data:
        differences_report.append({"type": "FatalError", "details": "Markdown data is empty or could not be loaded."})
        return differences_report

    # Assuming the relevant Markdown content is primarily in the first section,
    # or needs to be aggregated if there are multiple sections.
    # For this specific problem, the first MD section contains almost everything.
    # If MD was more granular, this would need adjustment.

    # Let's aggregate all markdown content into one block if it's structured as multiple main sections.
    # Or, if the first section is known to be the "main" one (as per previous observations):
    main_md_content_block = ""
    if isinstance(markdown_data, list) and len(markdown_data) > 0:
        # Option 1: Use only the first section if it's the aggregate
        # main_md_content_block = normalize_text(markdown_data[0].get('title','') + " " + markdown_data[0].get('content',''))

        # Option 2: Aggregate all markdown sections if they are meant to be combined for search
        all_md_texts = []
        for section in markdown_data:
            all_md_texts.append(section.get('title',''))
            all_md_texts.append(section.get('content',''))
        main_md_content_block = normalize_text(" ".join(all_md_texts))
    else:
        differences_report.append({"type": "DataError", "details": "Markdown data is not in the expected list format or is empty."})
        return differences_report

    md_numerics_global = extract_numerical_data(main_md_content_block)

    # Iterate through HTML slides
    for html_slide in html_data:
        slide_id = html_slide.get('slide_id', 'UnknownSlideID')

        slide_action_titles = [item['text'] for item in html_slide.get('content', []) if item['type'] == 'action_title']
        html_title_orig = slide_action_titles[0] if slide_action_titles else "Untitled Slide"
        html_title_norm = normalize_text(html_title_orig)

        html_content_texts = [item.get('text', '') for item in html_slide.get('content', [])]
        html_content_full_norm = normalize_text(" ".join(html_content_texts))
        html_numerics_slide = extract_numerical_data(html_content_full_norm)

        # 1. Check if HTML slide title appears in the main Markdown content
        if html_title_norm and main_md_content_block.find(html_title_norm) == -1:
            # Perform a similarity check if exact match fails, as titles can have minor variations
            # This requires iterating through markdown section titles if they were more granular
            # For now, we check against the combined block. A more advanced check might use difflib.
            # For simplicity, if the exact normalized title isn't found, we flag it.
            # A more robust check would be to see if any of the original MD titles match closely.
            # For this iteration, we'll assume the main_md_content_block should contain it.

            # Let's try to find the original HTML title in original MD titles for a better match
            original_md_titles = [normalize_text(s.get('title','')) for s in markdown_data]
            title_found_somewhere = any(md_t.find(html_title_norm) !=-1 for md_t in original_md_titles)
            if not title_found_somewhere:
                 # Use difflib to check similarity of HTML title against all MD titles
                best_title_match_ratio = 0
                for md_section_title_orig in original_md_titles:
                    ratio = difflib.SequenceMatcher(None, html_title_norm, md_section_title_orig).ratio()
                    if ratio > best_title_match_ratio:
                        best_title_match_ratio = ratio
                if best_title_match_ratio < 0.7: # If no MD title is reasonably similar
                    differences_report.append({
                        "type": "TitleMismatchOrMissing",
                        "html_slide_id": slide_id,
                        "html_slide_title": html_title_orig,
                        "details": f"Normalized HTML title '{html_title_norm}' not closely matched in any Markdown section titles (best similarity: {best_title_match_ratio:.2f})."
                    })

        # 2. Check for HTML numerical data missing in global Markdown numerical data
        missing_html_numerics = [num for num in html_numerics_slide if num not in md_numerics_global]
        if missing_html_numerics:
            differences_report.append({
                "type": "NumericalMismatch_HTMLDataMissingInMD",
                "html_slide_id": slide_id,
                "html_slide_title": html_title_orig,
                "missing_numerics_in_md": missing_html_numerics,
                "details": "Numerical data present in HTML slide is missing from the global Markdown content's numerical data."
            })

        # 3. Check for significant text from HTML slide missing in Markdown content
        # This is a simplified check: if a substantial part of the HTML slide's text isn't in the MD.
        # A more granular check would be sentence by sentence or using advanced text similarity.
        # For now, check if the whole normalized HTML content is roughly findable.
        # Using SequenceMatcher on potentially large blocks can be slow.
        # A simpler heuristic: check for a few key phrases or a sample of the text.

        # Check if non-numeric text from HTML slide is in MD
        html_text_only_norm = normalize_text(re.sub(r'[\$\u20ac\u00a3]?\s*\d+[\d,.]*\d*[\%xmMkK]?\b|\b\d+\-\d+[xmMkK]?\b', '', html_content_full_norm))
        if html_text_only_norm.strip() and main_md_content_block.find(html_text_only_norm) == -1:
            # If exact match of the whole block fails, use difflib ratio
            text_similarity_ratio = difflib.SequenceMatcher(None, html_text_only_norm, main_md_content_block).ratio()
            if text_similarity_ratio < 0.5: # Threshold for "largely missing"
                 # To make snippet more useful, take first few non-empty text items from HTML
                first_few_texts = [t for t in html_content_texts if normalize_text(t)][:3]
                sample_html_text = normalize_text(" ".join(first_few_texts))

                differences_report.append({
                    "type": "TextualMismatch_HTMLContentMissingInMD",
                    "html_slide_id": slide_id,
                    "html_slide_title": html_title_orig,
                    "sample_html_text_not_found_in_md": sample_html_text,
                    "overall_similarity_ratio_to_md_text_block": text_similarity_ratio,
                    "details": "Significant portion of text from HTML slide seems missing or very different in overall Markdown content."
                })

    # Try to find Markdown specific content that is NOT in any HTML slide (harder with current aggregation)
    # This would require iterating MD sections (if granular) and checking against aggregated HTML.
    # For now, this part is omitted due to the "one big MD block" assumption.

    return differences_report

if __name__ == "__main__":
    markdown_data_loaded = load_json_data("parsed_markdown.json")
    html_data_loaded = load_json_data("parsed_html.json")

    if markdown_data_loaded and html_data_loaded:
        # Ensure markdown_data_loaded is a list, as expected by compare_content_data
        if not isinstance(markdown_data_loaded, list):
            print("Error: parsed_markdown.json is not a list as expected.")
            comparison_report = [{"type": "FatalError", "details": "parsed_markdown.json did not load as a list."}]
        else:
            comparison_report = compare_content_data(markdown_data_loaded, html_data_loaded)

        output_json_path = "comparison_report.json"
        with open(output_json_path, 'w', encoding='utf-8') as outfile:
            json.dump(comparison_report, outfile, indent=4)
        print(f"Comparison report generated and saved to {output_json_path}")
    else:
        print("Failed to load one or both JSON data files. Comparison aborted.")
