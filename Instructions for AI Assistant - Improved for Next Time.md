# Instructions for AI Assistant - Improved for Next Time

These improved instructions incorporate lessons learned from creating the OGM 2025-11-13 Curiosity Call wiki. See [[Wiki Creation Process - Prompts and Key Decisions]] and [[Work Log]] for the full history.

---

## **Overview**

You will receive artifacts from a call (transcript, chat logs, visual boards, notes) and create a comprehensive, navigable markdown wiki using `[[Double Square Bracket Links]]`.

**Key principle:** This is biographical and testimonial documentation. Accuracy in attribution is paramount.

---

## **Phase 1: Analysis (Read Everything First)**

**CRITICAL: Read all source materials completely before creating any pages.**

### 1.1 Read All Artifacts

- **Transcript:** Read ENTIRE transcript, not just first portion
  - Note line numbers for key quotes
  - Track who is speaking about whom (pronouns matter!)
  - Look for contrasts: "some people... but I..."
  - Mark biographical claims for verification

- **Chat logs:** Read complete chat
  - Parse with timestamps and senders
  - Identify substantive vs brief messages
  - Note which topics have depth vs brief mentions

- **Visual artifacts:** Review any boards, diagrams, images
  - Note what was created collaboratively
  - Track who contributed what visually

### 1.2 Initial Mapping

Create mental/written map of:
- **Participants** (usually 10-20 people)
- **Major themes** (usually 5-10)
- **Frameworks/tools mentioned** (both discussed deeply and in passing)
- **Stories and narratives** (who told which story)
- **Key debates or disagreements**
- **Organizations and people mentioned**

### 1.3 Attribution Tracking

**BEFORE writing any biographical content:**
- Verify pronouns: Is speaker talking about themselves ("I") or others ("they")?
- Check full context: Do they contrast with their own experience?
- Note line numbers for verification
- Mark any ambiguous attributions for later review

**Quality check:** Misattributing someone's words or experiences is the most serious error. When in doubt, verify.

---

## **Phase 2: Initial Wiki Creation**

### 2.1 Core Infrastructure Pages

Create these foundational pages first:

1. **README.md** - Homepage
   - 1-2 paragraph overview
   - High-level themes
   - Participant list with one-line descriptions
   - **Navigation section** (will add hub pages later)
   - Links to major sections

2. **Details About This Wiki.md**
   - Organization and structure
   - Page types and conventions
   - How to navigate
   - Linking conventions

3. **Concept Index.md**
   - Complete categorized index
   - Organized by: Participants, Themes, Frameworks, Concepts, Organizations, People Mentioned, Meta pages
   - Updated as pages are created

4. **Work Log.md**
   - Journal style, newest first
   - Separated by horizontal rules
   - Document decisions and methodology

### 2.2 Participant Pages

For each person who spoke:

**Template structure:**
```markdown
# First Last

**Role:** Brief description

## Contributions to the Discussion

[Major contributions organized by theme]

### [Key Insight/Topic 1]

> "Direct quote with full context"

[Analysis and connection to other themes]

### [Key Insight/Topic 2]

...

## Themes Explored
- [[Theme 1]]
- [[Theme 2]]

## Related Participants
- [[Other Person]] - How they connected

## Related Concepts
- [[Concept 1]]
```

**Quality requirements for participant pages:**
- ✅ Use direct quotes, not paraphrasing
- ✅ Provide context before quotes
- ✅ Distinguish what they said about themselves vs about others
- ✅ Include stories they told (narratives are powerful)
- ✅ Show their unique voice/style (storyteller vs theorist)
- ✅ Link to themes they engaged with
- ❌ Never attribute to person X what they said about person Y
- ❌ Never assume "I" when they said "they"

### 2.3 Theme Pages

Create 5-10 major theme pages that synthesize across participants:

**Template structure:**
```markdown
# Theme Name

[Overview paragraph]

## [Sub-aspect 1]

[Synthesis of multiple perspectives]

### [Participant Name]'s Perspective

> "Quote"

[Analysis]

### [Another Participant]'s View

> "Quote"

[Analysis showing agreement, disagreement, or nuance]

## Related Themes
- [[Related Theme 1]]
- [[Related Theme 2]]

## Discussed By
- [[Participant 1]]
- [[Participant 2]]
```

**Quality requirements:**
- Preserve disagreement and nuance
- Don't force consensus where it doesn't exist
- Show how different perspectives interact
- Include unanswered questions

### 2.4 Concept/Framework/Entity Pages

For mentioned tools, frameworks, organizations, people:

**Start with:** "Note: This topic was mentioned during the call but not discussed in depth." (if applicable)

Then provide:
- Definition or background
- How it was discussed in this call
- Who mentioned it and why
- Links to related discussions

---

## **Phase 3: Systematic Orphan Resolution**

### 3.1 Create Orphan-Finding Script

**Don't manually search.** Create `_bin/find-orphan-links.py`:

```python
# Script should:
# - Find all [[wiki links]] in .md files
# - Handle [[Page|display text]] syntax
# - Identify links without corresponding pages
# - Generate list of orphans
```

### 3.2 Create All Orphan Pages

For each orphan:
- Most will be brief stubs (and that's appropriate)
- Start with disclaimer if not discussed in depth
- Provide genuinely useful background
- Link back to where mentioned

### 3.3 Verify Zero Orphans

Run script again to confirm all links resolve.

---

## **Phase 4: Systematic Enrichment**

### 4.1 Create Coverage Analysis Script

Create `_bin/analyze-chat-coverage.py`:

```python
# Script should:
# - Parse chat with timestamps
# - Identify substantive messages (>100 chars)
# - Match topics to wiki pages
# - Flag where chat discussion is deep but page is thin
```

### 4.2 Cross-Reference Transcript with Pages

**Systematic approach:**
1. Identify pages that could be enriched from transcript
2. Note specific line numbers for each enrichment
3. Verify attributions before adding content
4. Add direct quotes with context
5. Update pages in batches (group related edits)

**Watch for:**
- Stories that weren't captured (narratives add vividness)
- Methodological details for frameworks
- Concrete examples and practices
- Contrasts between viewpoints

### 4.3 Quality Verification Pass

Before considering enrichment complete:

**Participant pages:**
- ✅ Do quotes have context?
- ✅ Are attributions accurate (self vs others)?
- ✅ Are stories fully told?
- ✅ Does the page capture their unique voice?

**Theme pages:**
- ✅ Multiple perspectives represented?
- ✅ Disagreements preserved?
- ✅ Connections to participants clear?

**Concept pages:**
- ✅ Accurate definitions?
- ✅ Examples from the call?
- ✅ Links to who discussed it?

---

## **Phase 5: Navigation & Accessibility**

### 5.1 Create Hub Pages

**Required hub pages:**

1. **Participants Hub.md**
   - All participants organized by role
   - Brief bio for each highlighting key contribution
   - Links to other hubs

2. **Themes Hub.md**
   - Major themes organized by category
   - Each with summary, key insights, entry points
   - Emoji icons for visual scanning (optional but helpful)

3. **Frameworks Hub.md**
   - Tools/methodologies organized by type
   - Each with description, "Use when," and key insights
   - Quick reference section

4. **Alphabetical Index.md**
   - Complete A-Z of all pages
   - Quick navigation bar
   - Links to browse by category

5. **Start Here.md**
   - Curated paths by interest (6-8 paths)
   - "Essential pages" for time-limited readers
   - Browse by organization/depth/format
   - Navigation tips

### 5.2 Update README

Add prominent "Explore This Wiki" section with:
- Link to Start Here
- Links to all hub pages
- Visual hierarchy (emoji icons help)
- Place after Overview, before detailed content

### 5.3 Update Concept Index

Add hub pages to Core Pages section.

---

## **Phase 6: Process Documentation**

### 6.1 Final Work Log Entry

Document:
- Pages created (by type)
- Coverage statistics
- Methodological insights
- What worked well
- What could be improved

### 6.2 Create Wiki Creation Process Page

Document:
- Each user prompt verbatim
- Context for each prompt
- Actions taken
- Key decisions
- Lessons learned
- Metrics

This creates transparency and learning for future wikis.

---

## **Quality Principles**

### Attribution & Accuracy
1. **Biographical claims deserve extra verification** - Slow down when documenting what people said about themselves
2. **Track pronouns carefully** - "They" vs "I" vs "we" matters enormously
3. **Look for contrasts** - "Some people... but I..." signals important distinctions
4. **Verify before committing** - Especially for biographical sections
5. **When in doubt, check the transcript** - Line numbers are your friend

### Voice & Authenticity
1. **Preserve voices** - Direct quotes > paraphrasing
2. **Provide context** - Frame quotes for comprehension
3. **Show unique styles** - Some are storytellers, some theorists
4. **Include narratives** - Stories bring pages alive
5. **Keep nuance** - Don't force agreement where there's disagreement

### Technical Excellence
1. **Systematic over manual** - Scripts ensure completeness
2. **Reusable tools** - Put scripts in `_bin/` directory
3. **Git hygiene** - Commit frequently with clear messages
4. **Source preservation** - Never modify original artifacts
5. **Link generously** - 5-10 related links per page

### Information Architecture
1. **Multiple entry points** - Different users need different starts
2. **Hub pages are essential** - Not optional
3. **Curated paths** - Guide users based on interests
4. **Progressive disclosure** - Start simple, enable deep exploration
5. **Cross-linking** - Creates discovery paths

---

## **File & Link Conventions**

### Files
- Filename = page title with spaces, capitalization
- Extension: `.md`
- Location: Repository root (flat structure)
- Scripts: `_bin/` directory

### Links
- Use `[[Double Square Bracket Links]]` everywhere
- Support both `[[Page]]` and `[[Page|display text]]`
- Ensure all links resolve (zero orphans)
- Every page links to 5-10 related pages
- No page should be stranded

### Structure
```
repo/
├── README.md (homepage)
├── Start Here.md
├── Participants Hub.md
├── Themes Hub.md
├── Frameworks Hub.md
├── Alphabetical Index.md
├── Concept Index.md
├── Details About This Wiki.md
├── Work Log.md
├── Wiki Creation Process.md
├── [Participant Name].md (16 participants)
├── [Theme Name].md (7 themes)
├── [Concept Name].md (95+ concepts)
├── [Framework Name].md (12 frameworks)
├── Call Artifacts/
│   ├── meeting_saved_closed_caption.txt
│   ├── meeting_saved_new_chat.txt
│   └── [other artifacts]
└── _bin/
    ├── find-orphan-links.py
    └── analyze-chat-coverage.py
```

---

## **Common Pitfalls to Avoid**

### ❌ Don't Do This
1. **Reading only part of transcript** - Read it ALL before creating pages
2. **Manual orphan hunting** - Use a script
3. **Paraphrasing instead of quoting** - Direct quotes preserve voice
4. **Assuming self-reference** - Verify who is speaking about whom
5. **Creating pages without enrichment plan** - Know you'll do multiple passes
6. **Skipping hub pages** - They're essential for navigation
7. **Ignoring stories** - Narratives make pages memorable
8. **Forcing consensus** - Preserve disagreement

### ✅ Do This Instead
1. **Complete read-through first** - Then create pages
2. **Script for systematic work** - Ensures completeness
3. **Quote with context** - Let participants speak
4. **Track pronouns carefully** - "They" vs "I" matters
5. **Plan for phases** - Initial → Orphans → Enrichment → Navigation
6. **Hub pages early** - Create after initial content
7. **Capture narratives** - Stories are gold
8. **Show nuance** - Real conversations have disagreement

---

## **Success Metrics**

Your wiki should achieve:

**Completeness:**
- ✅ 100% of transcript analyzed
- ✅ 100% of chat analyzed
- ✅ Zero orphan links
- ✅ All participants have pages
- ✅ All major themes covered

**Quality:**
- ✅ Accurate attributions (verified)
- ✅ Participants' voices preserved (direct quotes)
- ✅ Stories and narratives captured
- ✅ Disagreements shown, not hidden
- ✅ Context provided for quotes

**Navigation:**
- ✅ 5 hub pages created
- ✅ Start Here with curated paths
- ✅ README with clear navigation
- ✅ Every page links to 5-10 related pages
- ✅ Multiple entry points for different users

**Process:**
- ✅ Work Log documents decisions
- ✅ Scripts created for systematic work
- ✅ Wiki Creation Process documents full history
- ✅ Lessons learned captured

---

## **Deliverables**

At completion, deliver:

1. **Complete wiki** (150+ pages typical)
   - Participant pages (one per speaker)
   - Theme pages (5-10 major themes)
   - Concept/framework pages (as many as needed)
   - Hub pages (5 essential)
   - Meta pages (README, Details, Index, Work Log, Wiki Creation Process)

2. **Scripts** (in `_bin/`)
   - Orphan finder
   - Coverage analyzer
   - Both reusable for updates

3. **Documentation**
   - Work Log with process journal
   - Wiki Creation Process with prompts and decisions
   - Clear README for users

4. **Verified quality**
   - Zero orphans
   - Accurate attributions
   - Complete coverage
   - Rich cross-linking

---

## **Timeline Estimate**

For a typical 2-hour call with 15-20 participants:

- **Phase 1 (Analysis):** Read everything - 1-2 hours
- **Phase 2 (Initial creation):** 2-3 hours (40-50 pages)
- **Phase 3 (Orphans):** 1-2 hours (script + 90+ stub pages)
- **Phase 4 (Enrichment):** 2-4 hours (systematic deepening)
- **Phase 5 (Navigation):** 1-2 hours (5 hub pages)
- **Phase 6 (Documentation):** 1 hour (process docs)

**Total: 8-14 hours of focused work**

May span 2 sessions if context limits are reached.

---

## **Key Lessons from OGM 2025-11-13 Experience**

### What Worked Exceptionally Well
1. **Reading entire transcript before enrichment** - Gave comprehensive view
2. **Scripts for orphan finding and coverage analysis** - Found gaps manual review missed
3. **Hub pages** - Dramatically improved discoverability
4. **Direct quotes with context** - Made participant pages vivid and authentic
5. **Work Log** - Created transparency and captured learning

### Critical Mistake to Avoid
**Attribution error in Stacey Druss page:** Attributed to her what she said about others because pronouns weren't carefully tracked. This is the most serious type of error in biographical documentation.

**Prevention:**
- Slow down on biographical claims
- Verify pronouns ("they" vs "I")
- Check for contrasts ("some people... but I...")
- Re-read before committing participant pages

### If Starting Over, We Would
1. Read entire transcript BEFORE creating any pages
2. Create hub pages earlier (after initial content, before enrichment)
3. Build attribution verification into workflow from start
4. Plan navigation architecture upfront
5. Create scripts for systematic work from beginning

---

*These improved instructions incorporate lessons learned from the OGM 2025-11-13 Curiosity Call wiki creation. For full process history, see [[Wiki Creation Process - Prompts and Key Decisions]] and [[Work Log]].*
