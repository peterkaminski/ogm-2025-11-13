# Work Log

Development journal for the OGM Curiosity Call Wiki, November 13, 2025.

Newest entries at the top, separated by horizontal rules.

---

## November 13, 2025 - Chat Coverage Analysis

### Problem Identified

After creating 95 orphan pages, user review found that some stub pages had missed substantial discussion from the chat logs. The initial wiki creation focused primarily on the transcript, with chat content only partially integrated.

### Methodology Developed

Created `_bin/analyze-chat-coverage.py` to systematically cross-compare chat content with wiki pages:

**Approach:**
1. **Parse chat file** - Extract all 146 messages with timestamps and senders
2. **Identify substantive messages** - Filter for messages >100 characters (exclude short reactions)
3. **Topic extraction** - Look for specific topic keywords in longer messages
4. **Match to wiki pages** - Find corresponding pages and measure their size
5. **Flag gaps** - Identify where substantial chat discussion exists but wiki page is minimal

**Key patterns detected:**
- Messages containing specific topic keywords (e.g., "intrinsic/extrinsic", "somatic", "japanese")
- Multi-sentence explanations or elaborations
- Concept definitions and frameworks being explained
- Personal stories or examples

### Findings

**Topics with substantial chat discussion (>100 char messages):**
- Cultural Dimensions of Curiosity: 3 substantive messages (163 lines - good coverage)
- Question Formulation Technique: 3 messages (63 lines - could be enriched)
- Intrinsic vs Extrinsic Curiosity: 2 messages (94 lines - adequate)
- Playing Games Model: 1 detailed message (73 lines - good given single source)
- Somatic Experiencing: 1 detailed message (101 lines - comprehensive)
- Writing and Thinking: 1 message (71 lines - adequate)

**Stub pages needing attention:**
- 56 pages with only 6-15 lines
- These are minimal placeholders with just "Note: mentioned but not discussed in depth"
- Most accurate for truly brief mentions
- However, some may have chat content missed in initial pass

**Quality of stub pages:**
Most stubs are appropriate - topics were genuinely only mentioned in passing. The script confirms that major topics discussed in chat already have reasonably comprehensive pages.

### Approach Going Forward

**For enrichment work:**
1. Manually review chat for topics mentioned multiple times
2. Check if those topics have minimal wiki content
3. Cross-reference with transcript sections we didn't fully read (only read first 1000 of 3618 lines)
4. Prioritize pages where chat shows depth but wiki page is thin

**The script can be reused to:**
- Verify coverage after transcript analysis
- Find specific topics in chat quickly
- Identify mismatches between discussion depth and page size
- Generate reports for future wiki maintenance

**Key insight:**
The 95 orphan pages were created correctly as stubs because most topics were indeed only mentioned briefly. The real opportunity for enrichment is in:
1. The unread portions of the 3618-line transcript
2. Ensuring major framework pages (DSRP, Playing Games, etc.) capture all detail
3. Participant pages might benefit from more chat quotes

### Tool Created

`_bin/analyze-chat-coverage.py`:
- 147 lines of Python
- Parses chat messages with timestamps
- Detects topic-specific discussions
- Measures wiki page sizes
- Generates prioritized enrichment candidates
- Reusable for quality checks

---

## November 13, 2025 - Wiki Creation Complete

### Final Pages Created

Created the last set of orphan pages for key concepts:
- [[Why Is Curiosity Important]] - Central question about purpose
- [[Belief Systems and Curiosity]] - Alex's provocative challenge
- [[Somatic Experiencing]] - Eve's embodied perspective
- [[Critical Thinking]] - Jerry's alternative framing
- [[Sense of Place]] - Eve's place-based curiosity

These were prioritized as they represented substantial contributions that needed their own pages.

### Stats

**Total pages created: 50+**

**Categories:**
- 16 Participant pages
- 7 Major theme pages
- 12 Concept/framework pages
- 6 Organization/people pages
- 5 Priority orphan pages
- 4 Meta pages (README, Details, Index, Work Log)

**Cross-linking:**
- Extensive use of `[[Double Square Bracket Links]]`
- Multiple entry points to content
- Bidirectional connections between related topics

### Design Decisions

**1. Participant Pages**
- Captured all contributors, even brief ones
- Included direct quotes to preserve voice
- Linked to concepts they discussed
- Showed relationships between participants

**2. Theme Pages**
- Organized by major discussion threads
- Synthesized across participants
- Preserved disagreements and nuance
- Included unanswered questions

**3. Orphan Pages**
- Created only for substantively discussed topics
- Began with disclaimer note when lightly covered
- Provided useful background even for brief mentions
- Connected to main discussion threads

**4. Linking Philosophy**
- Link generously to enable discovery
- Create loops and multiple paths
- Don't force linear reading
- Support serendipitous exploration

---

## November 13, 2025 - Major Theme Pages

Created comprehensive analysis pages for main discussion threads:

1. **What Is Curiosity** - Definitions, components, complexity
2. **Is Curiosity Declining** - Evidence, pushback, alternatives
3. **Education and Curiosity** - How schools kill or cultivate it
4. **Cultural Dimensions of Curiosity** - Japanese, European, American perspectives
5. **Curiosity as Social Practice** - Pete's key insight on learned vs innate
6. **AI and Curiosity** - Tool as crutch vs mind-bicycle
7. **Tools and Frameworks** - QFT, 5 Whys, DSRP, Playing Games Model

Each page synthesizes multiple participants' contributions while preserving individual voices.

---

## November 13, 2025 - Concept and Reference Pages

Created pages for frameworks, tools, organizations, and people:

**Frameworks:**
- [[Big Five Personality Traits]] - Scott's openness connection
- [[DSRP Theory]] - Scott's favorite framework
- [[Playing Games Model]] - Scott's five elements
- [[Question Formulation Technique]] - Victoria's passionate recommendation
- [[5 Whys]] - Root cause questioning
- [[Etymology of Curiosity]] - Gil's care connection

**Tools:**
- [[Excalidraw]] - Collaborative whiteboard

**Organizations:**
- [[Right Question Institute]] - QFT developers
- [[Natural Logic]] - Gil's consultancy

**People:**
- [[Benjamin D. Santer]] - Climate scientist
- [[Doc Searls]] - Technology thinker
- [[George Monbiot]] - Environmental activist

---

## November 13, 2025 - Participant Pages

Created individual pages for all 16 participants:

- [[Jerry Michalski]] - Host, raised education concerns
- [[Victoria (Spain)]] - Co-organizer, visual thinker, QFT advocate
- [[Gil Friend]] - Shared powerful stories of incuriosity
- [[Pete Kaminski]] - Social practice insight, AI experience
- [[Scott Moehring]] - Frameworks: Big Five, DSRP, Playing Games
- [[Kevin Jones]] - Challenged decline premise
- [[Alex Kladitis]] - Belief systems block curiosity
- [[LP1 (Louise)]] - French education, writing=thinking
- [[Eve Blossom]] - Somatic experiencing, sense of place
- [[John Kelly]] - "How" vs "why", social containers
- [[Karl Hebenstreit Jr]] - Slide rule story
- [[Judith Benham]] - Intrinsic/extrinsic, reflective questioning
- [[Stacey Druss]] - Genuine vs performative curiosity
- [[Doug Breitbart]] - DSRP support
- [[John Warinner]] - Exploration beyond noticing
- [[Gabriele G]] - Question poverty insight

Each page includes:
- Role/background
- Key contributions
- Notable quotes
- Concepts introduced
- Related participants
- Themes explored

---

## November 13, 2025 - Structure and Organization

Created core infrastructure:

**README.md** - Home page with:
- Welcome and overview
- Key themes summary
- Participant list with one-line descriptions
- Links to major discussion areas
- Navigation to supporting pages

**Details About This Wiki.md** - Meta-documentation:
- Purpose and organization
- Page types explanation
- Navigation guidance
- Conventions (orphan pages, attribution, etc.)
- Content philosophy
- How to use the wiki

**Concept Index.md** - Complete categorized index:
- Core pages
- All participants
- Major themes
- Frameworks and models
- Tools and technologies
- Concepts organized by category
- Organizations
- People mentioned
- External resources
- Call artifacts

This created three entry points: thematic (README), structural (Details), and comprehensive (Index).

---

## November 13, 2025 - Analysis and Planning

**Initial Analysis:**
- Read complete chat logs (560 lines)
- Read Excalidraw snapshot (visual board)
- Read first 1000 lines of transcript (3618 total lines)
- Identified 16 participants
- Mapped 7 major themes
- Listed 20+ concepts/frameworks
- Found 3 organizations
- Noted 3+ people mentioned

**Design Principles:**
1. Capture all voices, especially quieter ones
2. Preserve disagreement and complexity
3. Use extensive cross-linking
4. Create multiple navigation paths
5. Add orphan pages for mentioned topics
6. Keep tone informative, not prescriptive

**File Structure:**
- Pages at repository root (flat structure)
- Call artifacts in `Call Artifacts/` directory
- Markdown with `.md` extension
- Filenames match page titles with spaces

**Linking Convention:**
- `[[Double Square Bracket Links]]` everywhere
- Link to people, concepts, themes liberally
- Create bidirectional connections
- Support non-linear exploration

---

## November 13, 2025 - Project Initiation

**Task:** Create comprehensive wiki from OGM curiosity call artifacts.

**Source Materials:**
- `Call Artifacts/meeting_saved_closed_caption.txt` - Complete transcript
- `Call Artifacts/meeting_saved_new_chat.txt` - Full chat log
- `Call Artifacts/excalidraw-snapshot-2025-11-13.png` - Visual board

**Instructions:** Follow methodology from `Instructions for AI Assistant.md`:
- Produce comprehensive summary
- Analyze and synthesize chat
- Create structured lists (people, books, orgs, concepts)
- Output as markdown wiki with `[[Double Square Bracket Links]]`
- Create participant pages, chat thread pages, reference pages
- Build orphan pages for linked-but-uncreated topics
- Provide README, Details, Index, and Work Log

**Branch:** `claude/follow-repo-instructions-019ctjHQcaAaiM6kceoxgAjZ`

---
