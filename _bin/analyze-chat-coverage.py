#!/usr/bin/env python3
"""
Analyze chat content to find topics with substantial discussion that may need
enrichment in corresponding wiki pages.
"""

import re
from pathlib import Path
from collections import defaultdict, Counter

def parse_chat_file(filepath):
    """Parse chat file and extract messages with metadata."""
    messages = []
    current_msg = None

    with open(filepath, 'r') as f:
        for line in f:
            # Check if this is a new message (has timestamp)
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) From (.+?) to Everyone:', line)
            if match:
                if current_msg:
                    messages.append(current_msg)
                timestamp, sender = match.groups()
                current_msg = {
                    'timestamp': timestamp,
                    'sender': sender,
                    'content': ''
                }
            elif current_msg:
                current_msg['content'] += line

    if current_msg:
        messages.append(current_msg)

    return messages

def extract_topics_from_content(content):
    """Extract potential topics from message content."""
    topics = []

    # Look for explicit topic mentions (capitalized phrases)
    capitalized = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', content)
    topics.extend(capitalized)

    # Look for key phrases
    key_phrases = [
        'curiosity', 'curious', 'question', 'asking', 'learning',
        'education', 'culture', 'intrinsic', 'extrinsic', 'AI',
        'attention', 'noticing', 'etiquette', 'social', 'belief',
        'polarization', 'critical thinking', 'listening', 'writing',
        'thinking', 'somatic', 'embodied', 'fear', 'safety'
    ]

    content_lower = content.lower()
    for phrase in key_phrases:
        if phrase in content_lower:
            topics.append(phrase)

    return topics

def find_wiki_page(topic, existing_pages):
    """Try to find corresponding wiki page for a topic."""
    topic_lower = topic.lower()

    # Direct match
    for page in existing_pages:
        if page.lower() == topic_lower:
            return page

    # Partial match
    for page in existing_pages:
        if topic_lower in page.lower() or page.lower() in topic_lower:
            return page

    return None

def get_page_size(page_path):
    """Get size of wiki page in lines."""
    try:
        return len(page_path.read_text().split('\n'))
    except:
        return 0

def main():
    repo_root = Path('/home/user/ogm-2025-11-13')
    chat_file = repo_root / 'Call Artifacts' / 'meeting_saved_new_chat.txt'

    # Parse chat
    messages = parse_chat_file(chat_file)
    print(f"Parsed {len(messages)} chat messages\n")

    # Get existing wiki pages
    md_files = list(repo_root.glob('*.md'))
    existing_pages = {f.stem: f for f in md_files}

    # Analyze topic mentions in chat
    topic_mentions = defaultdict(list)
    topic_details = defaultdict(list)

    for msg in messages:
        sender = msg['sender']
        content = msg['content'].strip()

        if len(content) < 20:  # Skip very short messages
            continue

        # Track longer, more substantive messages
        if len(content) > 100:
            # Look for specific topics being discussed
            if 'intrinsic' in content.lower() or 'extrinsic' in content.lower():
                topic_details['Intrinsic vs Extrinsic Curiosity'].append({
                    'sender': sender,
                    'content': content[:200]
                })

            if 'somatic' in content.lower():
                topic_details['Somatic Experiencing'].append({
                    'sender': sender,
                    'content': content[:200]
                })

            if 'game' in content.lower() and 'element' in content.lower():
                topic_details['Playing Games Model'].append({
                    'sender': sender,
                    'content': content[:200]
                })

            if 'writing' in content.lower() and 'thinking' in content.lower():
                topic_details['Writing and Thinking'].append({
                    'sender': sender,
                    'content': content[:200]
                })

            if 'japanese' in content.lower() or '探求心' in content:
                topic_details['Cultural Dimensions of Curiosity'].append({
                    'sender': sender,
                    'content': content[:200]
                })

            if 'question' in content.lower() and ('formulation' in content.lower() or 'anxiety' in content.lower()):
                topic_details['Question Formulation Technique'].append({
                    'sender': sender,
                    'content': content[:200]
                })

    # Find stub pages (very short pages)
    stub_pages = []
    for page_name, page_path in existing_pages.items():
        size = get_page_size(page_path)
        if 5 < size < 20:  # Likely a stub
            stub_pages.append((page_name, size))

    # Output analysis
    print("=" * 80)
    print("TOPICS WITH SUBSTANTIAL CHAT DISCUSSION")
    print("=" * 80)

    for topic, details in sorted(topic_details.items()):
        print(f"\n{topic}:")
        print(f"  Mentioned by {len(details)} messages")

        if topic in existing_pages:
            page_size = get_page_size(existing_pages[topic])
            print(f"  Current page size: {page_size} lines")
            if page_size < 30:
                print(f"  ⚠️  Page may need enrichment")
        else:
            print(f"  ⚠️  No page found!")

        print(f"  Sample content:")
        for detail in details[:2]:
            print(f"    - {detail['sender']}: {detail['content'][:100]}...")

    print("\n" + "=" * 80)
    print(f"STUB PAGES (potential candidates for enrichment)")
    print("=" * 80)

    for page_name, size in sorted(stub_pages, key=lambda x: x[1]):
        print(f"  {page_name}: {size} lines")

    print(f"\n  Total stub pages: {len(stub_pages)}")

if __name__ == '__main__':
    main()
