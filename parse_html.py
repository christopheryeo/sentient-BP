import json
from bs4 import BeautifulSoup, NavigableString, Tag
import re

def get_element_text(element):
    """Extracts text from an element, handling various structures."""
    if element is None:
        return ""
    return element.get_text(separator=' ', strip=True)

def extract_slide_content_ordered(slide_element):
    """
    Extracts various content types from a slide element, attempting to preserve order.
    """
    content_items = []

    for element in slide_element.find_all(recursive=True):
        item = None
        if not isinstance(element, NavigableString) and element.name:
            classes = element.get('class', [])

            if 'action-title' in classes:
                item = {"type": "action_title", "text": get_element_text(element)}
            elif 'subtitle' in classes:
                item = {"type": "subtitle", "text": get_element_text(element)}
            elif element.name == 'p':
                if not (element.find_parent(class_='callout-box') or element.find_parent(class_='framework-item')):
                    item = {"type": "paragraph", "text": get_element_text(element)}
            elif element.name == 'li':
                item = {"type": "list_item", "text": get_element_text(element)}
            elif element.name == 'th':
                item = {"type": "table_header", "text": get_element_text(element)}
            elif element.name == 'td':
                item = {"type": "table_cell", "text": get_element_text(element)}
            elif 'stat-value' in classes:
                item = {"type": "stat_value", "text": get_element_text(element)}
            elif 'stat-label' in classes:
                item = {"type": "stat_label", "text": get_element_text(element)}
            elif 'callout-box' in classes:
                title = element.find('h4')
                para = element.find('p')
                callout_texts = []
                if title:
                    callout_texts.append(get_element_text(title))
                if para and get_element_text(para):
                    callout_texts.append(get_element_text(para))
                if callout_texts:
                     item = {"type": "callout_box", "text": " | ".join(callout_texts)}
                elif not title and not para and get_element_text(element): # Fallback for other content
                    item = {"type": "callout_box", "text": get_element_text(element)}

            elif 'framework-item' in classes:
                title = element.find('h4')
                para = element.find('p')
                framework_texts = []
                if title:
                    framework_texts.append(get_element_text(title))
                if para and get_element_text(para):
                    framework_texts.append(get_element_text(para))
                if framework_texts:
                    item = {"type": "framework_item", "text": " | ".join(framework_texts)}

            if item:
                # Removed the aggressive de-duplication logic that was here:
                # if content_items and content_items[-1]["type"] == item["type"] and content_items[-1]["text"] == item["text"]:
                #    is_duplicate = True
                # This was causing issues with tables having identical consecutive cell values.
                content_items.append(item)

    return content_items

def parse_html_to_json(html_content):
    """
    Parses HTML content to extract slide data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    slides_data = []
    slide_elements = soup.find_all('div', class_='slide', id=re.compile(r'^slide\d+'))

    for slide_el in slide_elements:
        slide_id = slide_el.get('id')
        extracted_content = extract_slide_content_ordered(slide_el)

        slides_data.append({
            "slide_id": slide_id,
            "content": extracted_content
        })
    return slides_data

if __name__ == "__main__":
    html_file_path = "index.html"
    output_json_path = "parsed_html.json"
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        slide_data_list = parse_html_to_json(content)

        with open(output_json_path, 'w', encoding='utf-8') as outfile:
            json.dump(slide_data_list, outfile, indent=4)
        print(f"Successfully parsed HTML and saved to {output_json_path}")

    except FileNotFoundError:
        print(f"Error: File not found at {html_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
