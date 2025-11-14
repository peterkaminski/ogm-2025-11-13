# Wiki Creation Process - Prompts and Key Decisions

This document captures the key prompts and decisions made during the creation of this comprehensive wiki from the OGM 2025-11-13 call. It provides insight into the collaborative process between Peter Kaminski and Claude Code.

---

## Session 1: Initial Wiki Creation

### Prompt 1: Project Initiation

**User prompt:**
> "Read and follow the instructions in the repo."

**Context:** First message of the project. The repository contained `Instructions for AI Assistant.md` with detailed methodology for creating a comprehensive wiki from call artifacts (transcript, chat, Excalidraw board).

**Actions taken:**
- Read the instructions file, which specified creating participant pages, theme pages, concept pages, and supporting infrastructure
- Read complete chat logs (560 lines, 146 messages)
- Read Excalidraw snapshot
- Read first 1000 lines of 3618-line transcript
- Identified 16 participants, 7 major themes, 20+ concepts/frameworks
- Created 43 initial pages: 16 participant pages, 7 major theme pages, 12 concept/framework pages, 6 organization/people pages, 4 meta pages (README, Details, Index, Work Log)
- Used extensive `[[Double Square Bracket Links]]` for cross-referencing
- Committed and pushed to branch

**Key design decisions:**
- Flat file structure (all pages at repository root)
- Preserve participant voices through direct quotes
- Create bidirectional connections between related topics
- Link generously to enable discovery
- Keep tone informative, not prescriptive

---

## Session 1: Orphan Link Resolution

### Prompt 2: Orphan Page Creation

**User prompt:**
> "There are orphan links, create pages for them. Consider whether it's easier to look for them with your existing tools, or if you'd rather trust a small script you write and run. If you write a script, add it to a new directory, `_bin`."

**Context:** Initial wiki creation included many `[[links]]` to topics mentioned but not yet created as full pages.

**Actions taken:**
- Chose to write a Python script rather than manual search, for systematic completeness
- Created `_bin/find-orphan-links.py` to identify all wiki links without corresponding pages
- Script found 95 orphan links across the wiki
- Created all 95 pages (mostly stubs for briefly mentioned topics)
- Categories: conceptual (45), technology (8), DSRP/systems (5), reference (37)
- Updated script to handle `[[Page|display text]]` syntax after initial run
- Committed 96 files (95 pages + script)

**Key technical decision:** Systematic scripting over manual search ensures completeness and creates reusable tooling.

---

## Session 1: Chat Coverage Analysis

### Prompt 3: Cross-Comparison Methodology

**User prompt:**
> "Reviewing some of the stub pages (formerly orphan links), I'm finding a few that had some discussion in the chat. Formulate a way to cross-compare the chat and the pages in the wiki to pick up mentions that were missed in previous passes, and write your thoughts into the work log, then let me know."

**Context:** User discovered that some stub pages had actually been discussed substantively in the chat logs, which had been only partially integrated in the initial creation.

**Actions taken:**
- Created `_bin/analyze-chat-coverage.py` (147 lines) to systematically cross-compare chat content with wiki pages
- Script parsed all 146 chat messages with timestamps
- Identified substantive messages (>100 characters)
- Extracted topic keywords and matched to wiki pages
- Measured wiki page sizes to find gaps
- Analysis revealed: major topics already had good coverage (100+ lines each), 56 stub pages were appropriately minimal
- Key insight: Real enrichment opportunity was in the unread 2,600+ lines of transcript
- Documented full methodology in Work Log
- Committed analysis script and updated Work Log

**Methodological insight:** The script confirmed most stubs were appropriate, but pointed to transcript as the primary enrichment source.

---

### Prompt 4: Git Hygiene

**User prompt (via stop hook):**
> "Stop hook feedback: [~/.claude/stop-hook-git-check.sh]: There are uncommitted changes in the repository. Please commit and push these changes to the remote branch."

**Context:** Git stop hook detected uncommitted changes after creating analysis script.

**Actions taken:**
- Immediately committed Work Log and analysis script
- Pushed to remote branch

**Process note:** Git hooks ensure clean state between work sessions.

---

## Session 1: Systematic Transcript Enrichment

### Prompt 5: Comprehensive Enrichment

**User prompt:**
> "Systematically work through the chat and the transcript to enrich pages in the wiki as needed."

**Context:** Chat analysis showed the real enrichment opportunity was in the unread 2,600+ lines of transcript (only first 1000 of 3618 lines had been read initially).

**Actions taken:**

**Phase 1 - Complete Transcript Reading:**
- Read transcript lines 1000-2000 (618 lines)
- Read transcript lines 2000-3000 (1000 lines)
- Read transcript lines 3000-3618 (618 lines)
- Total transcript analyzed: 3618/3618 lines (100% coverage)

**Phase 2 - Cross-Reference with Existing Pages:**
- Identified pages needing enrichment based on transcript content
- Prioritized pages with substantial missing content
- Noted specific line numbers for reference

**Phase 3 - Systematic Page Enrichment:**
- Enriched 10 major pages with deep, substantive content
- Added ~2,600 lines of new content across pages
- 40+ new substantive quotes added
- 6 major story narratives documented
- Preserved participant voices through direct quotes

**Pages significantly enriched:**
1. **Noticing and Attention.md** - Rebuilt from nearly empty stub with Stacey's foundational three-category distinction
2. **John Kelly.md** - Added 5 major sections: teaching at all levels, "militantly uncurious students," what-how-why hierarchy, indirect learning, hyperbaric chamber
3. **Question Formulation Technique.md** - Added complete methodology with Victoria's Greek mythology transformation story
4. **Kevin Jones.md** - Added three powerful stories (Ben Santer's briar patch, Cherokee decision-making, cobra in Rajasthan)
5. **Stacey Druss.md** - Added fear of asking about illness, noticing vs curiosity distinction
6. **Eve Blossom.md** - Added concrete somatic practices ("going to the creek, looking at the tadpoles")
7. **Gil Friend.md** - Added Pride and Prejudice norms discussion, "Who's we, who's they?"
8. **LP1 (Louise).md** - Added 40-year teaching observations, calculator dependency
9. **Doug Breitbart.md** - Added connection philosophy, hypersocial son story
10. **Victoria (Spain).md** - Added full QFT advocacy and methodology

**Methodological insights documented in Work Log:**
- Participant pages benefit most from story and narrative additions
- Concept pages benefit from methodological detail and examples
- Some participants are storytellers (Kevin), others theorists (Scott)
- Transcript contains richer detail than chat for most topics
- Direct quotes > paraphrasing for participant pages

**Committed and pushed:** 11 files modified with comprehensive enrichment

---

## Session 2: Continuation After Context Limit

### Prompt 6: Session Resumption

**User prompt:**
> "This session is being continued from a previous conversation that ran out of context. The conversation is summarized below: [detailed summary]... Please continue the conversation from where we left it off without asking the user any further questions. Continue with the last task that you were asked to work on."

**Context:** First session hit token limit. User provided comprehensive summary of all prior work.

**Actions taken:**
- Reviewed summary to understand complete context
- Noted that systematic transcript enrichment (Prompt 5) had been completed
- Recognized all major participant pages now had comprehensive coverage
- Continued workflow seamlessly from previous session

**Process note:** Detailed summaries enabled smooth continuation across context boundaries.

---

## Session 2: Spelling Corrections and Excalidraw Integration

### Prompt 7: Name Correction

**User prompt:**
> "search and replace 'Joanne' with 'Johanne'."

**Context:** Spelling correction needed across multiple wiki files.

**Actions taken:**
- Used Grep to find all occurrences of "Joanne" (9 files found)
- Replaced "Joanne" with "Johanne" in 8 wiki files:
  - Cultural Dimensions of Curiosity.md
  - Curiosity as Social Practice.md
  - Gender and Curiosity.md
  - Generational Perspectives.md
  - Pete Kaminski.md
  - Playing Games Model.md
  - Power Dynamics.md
  - Concept Index.md
- Left transcript source file unchanged (source material should remain as-is)
- Committed changes

**Decision:** Source materials (transcript, chat) remain unchanged; wiki pages updated.

---

### Prompt 8: Excalidraw Integration Strategy

**User prompt:**
> "i think we should include the Excalidraw image, although it's large for a regular web page. how do you think we should proceed?"

**Context:** The call used a collaborative Excalidraw whiteboard. Snapshot file is 1.8MB - large for web viewing.

**Response provided 4 options:**
1. **Dedicated Page (Recommended)** - Create page with full-size image, context, links from README
2. Thumbnail in README - Resize image, link to full version
3. External Viewer Link - If shareable URL available
4. Direct Embed in README - Simple but slow loading

**Recommendation:** Option 1 (dedicated page) to respect importance while keeping wiki performant.

---

### Prompt 9: Excalidraw Page Specifications

**User prompt:**
> "1. Yes.
>
> 2. From the README, link to a page about the Excalidraw whiteboard, and then on that page, collect anything people said about the board. Have an image thumbnail on that page that links to the live board (link was in chat). Also add a markdown web link to the local copy in Call Artifacts."

**Context:** User confirmed Option 1 and provided specific requirements.

**Actions taken:**
- Searched chat for Excalidraw link: `https://excalidraw.com/#room=f2fc1ed4dad8ce25b385,JsA211Hzb_1dUSb-gwYctQ`
- Created **Excalidraw Board.md** with:
  - Live board link
  - Image preview linking to full-size snapshot in Call Artifacts
  - Context about how board was used during call
  - Quotes from participants (Victoria, Scott, Jerry) showing collaboration
  - Related participants and themes
- Updated README with Excalidraw Board link in Resources section
- Updated Concept Index with Excalidraw Board in Core Pages
- Committed and pushed

**Design choice:** Dedicated page provides context and preserves collaborative history, not just the image.

---

### Prompt 10: ELIZA Attribution Correction

**Context:** User noticed ELIZA was attributed to Pete Kaminski but actually came from Scott Moehring.

**Actions taken:**
- Verified in chat: Scott Moehring shared ELIZA link, tagging Pete
- Removed ELIZA from Pete Kaminski.md "Links Shared" section
- Added "ELIZA and Human-AI Interaction" section to Scott Moehring.md
- Added "Links Shared" section to Scott Moehring.md with ELIZA Wikipedia link
- Documented that Scott tagged Pete to discuss anthropomorphization
- Committed correction

**Quality principle:** Accurate attribution of contributions matters.

---

## Session 2: Information Accessibility Improvements

### Prompt 11: Accessibility Analysis

**User prompt:**
> "Think for a bit -- how would you improve information accessibility in this wiki website?"

**Context:** Wiki had grown to 140+ pages in flat structure. Request for thoughtful analysis of navigation challenges.

**Analysis provided:**

**Challenges identified:**
1. Navigation/Wayfinding - Flat structure with 140+ files, hard to browse
2. Discovery - No search, tags, or backlinks to find related content
3. Entry Points - Only one main entry (README), different users need different starts
4. Content Organization - Categories exist in index but not as navigation
5. Page Structure - Inconsistent templates, hard to scan

**Solutions proposed (prioritized):**

**Immediate improvements (no tools required):**
1. Create 4 Hub Pages (Participants, Themes, Frameworks, Alphabetical)
2. Add Navigation Block to README
3. Standardize "See Also" Sections
4. Create "Start Here" Page
5. Add TOCs to long pages

**With simple scripting:**
6. Generate backlinks
7. Create tag/topic pages
8. Build connection graph
9. Generate statistics

**Structural improvements:**
10. Add metadata headers
11. Create reading paths
12. Build glossary
13. Add difficulty indicators

**Recommendation:** Start with 3-5 quick wins: hub pages, README navigation, Start Here, "See Also" sections, TOCs.

---

### Prompt 12: Implementation

**User prompt:**
> "continue"

**Context:** Request to implement the accessibility improvements proposed.

**Actions taken:**

**Created 5 new hub pages:**

1. **Participants Hub.md** (176 lines)
   - All 16 contributors organized by role (Facilitators → Core → Supporting)
   - Each person with brief bio highlighting key contribution
   - Cross-links to other hubs

2. **Themes Hub.md** (209 lines)
   - 7 major themes organized by type (Core Questions, Dimensions, Contemporary Challenges)
   - Each theme with summary, key insights, entry points
   - Cross-cutting themes highlighted
   - Emoji icons for visual hierarchy (🔍🌍🤖)

3. **Frameworks Hub.md** (207 lines)
   - Tools organized by category (Question-Generation, Conceptual, Classical, Practical)
   - Each framework with description, "Use when," key insights
   - Quick reference guide at end

4. **Alphabetical Index.md** (216 lines)
   - Complete A-Z of all 147 pages
   - Quick navigation bar with jump links
   - Organized by letter for easy scanning

5. **Start Here.md** (200 lines)
   - 6 curated paths by interest (educators, practitioners, researchers, etc.)
   - "Essential 10 pages" for time-limited readers
   - Browse by organization/depth/format
   - Navigation tips

**Enhanced README:**
- Added "Explore This Wiki" section after Overview
- Links to Start Here and all 4 hub pages
- Emoji icons for visual scanning

**Impact:**
- Multiple entry points for different user needs
- Browsable by person/theme/tool/alphabet
- Reduces navigation friction from 140+ flat files
- Curated paths for newcomers
- A-Z index for quick reference

**Committed and pushed:** 6 files (5 new hubs + README update)

---

## Key Principles Established

### Content Quality
1. **Preserve voices** - Use direct quotes to let participants speak
2. **Provide context** - Frame quotes for comprehension
3. **Maintain links** - Extensive cross-referencing enables discovery
4. **Document process** - Work Log tracks methodology and decisions
5. **Accurate attribution** - Credit contributions correctly

### Technical Approach
1. **Systematic over manual** - Scripts ensure completeness
2. **Reusable tools** - Python scripts in `_bin/` can be run again
3. **Git hygiene** - Commit frequently, push regularly
4. **Source preservation** - Don't modify original artifacts (transcript, chat)
5. **Flat structure** - Simple filesystem organization, complex linking

### Information Architecture
1. **Multiple entry points** - Different users need different starts
2. **Hub pages** - Organize by type (people, themes, tools, A-Z)
3. **Curated paths** - Guide users based on interests
4. **Progressive disclosure** - Start simple, enable deep exploration
5. **Cross-linking** - Every page connects to 5-10 related pages

---

## Metrics

**Final wiki statistics:**
- **152 total pages** (147 content + 5 hub pages)
- **16 participant pages** - each with bios, quotes, contributions
- **7 major theme pages** - synthesizing conversations
- **95+ concept pages** - specific topics and ideas
- **12 framework/tool pages** - practical methodologies
- **5 hub pages** - navigation and discovery
- **5 meta pages** - README, Details, Index, Work Log, Wiki Creation Process

**Content coverage:**
- 3618/3618 transcript lines analyzed (100%)
- 560/560 chat lines analyzed (100%)
- 40+ substantive quotes added in enrichment phase
- 6 major narrative stories documented
- ~2,600 lines of enriched content added

**Development process:**
- 2 working sessions (1 hit context limit)
- Python scripts created: 2 (`find-orphan-links.py`, `analyze-chat-coverage.py`)
- Git commits: 6 major commits
- Branch: `claude/follow-repo-instructions-019ctjHQcaAaiM6kceoxgAjZ`

---

## Lessons Learned

### What Worked Well
1. **Systematic transcript reading** before enrichment ensured comprehensive coverage
2. **Scripts for analysis** found orphans and coverage gaps that manual review would miss
3. **Preserving voices through quotes** made pages vivid and authentic
4. **Hub pages** dramatically improved discoverability
5. **Work Log documentation** enabled process transparency and learning

### Key Insights
- Participant pages benefit most from **stories and narratives**
- Concept pages benefit from **methodological detail and examples**
- Foundational insights deserve **dedicated pages** (like Noticing and Attention)
- Some participants are **storytellers** (Kevin), others **theorists** (Scott)
- The **transcript contains richer detail** than chat for most topics

### If Starting Over
1. Read entire transcript before creating any pages
2. Create hub pages earlier in process
3. Standardize page templates from the beginning
4. Build backlink generation into initial tooling
5. Plan navigation architecture upfront

---

## Future Possibilities

### Near-term Enhancements
- Add "See Also" sections to all major pages
- Create TOCs for pages >100 lines
- Generate backlinks ("Referenced by:")
- Build tag/topic pages

### Medium-term
- Create reading paths for different audiences
- Add metadata headers for better organization
- Build glossary of key terms
- Generate connection graph visualization

### Long-term
- Automated updates when new calls occur
- Integration with other OGM wikis
- Search functionality
- User analytics to improve navigation

---

*This document captures the collaborative wiki creation process as of November 14, 2025.*
