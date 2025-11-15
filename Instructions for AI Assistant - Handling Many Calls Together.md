# Instructions for AI Assistant - Handling Many Calls Together

These instructions extend the lessons from [[Instructions for AI Assistant - Improved for Next Time]] to handle wikis that synthesize **multiple calls** (typically 10-20) rather than a single call. This adds complexity around temporal relationships, recurring participants, cross-call themes, and personal check-ins.

---

## **Overview**

You will receive artifacts from **multiple calls** (transcripts, chats, visual boards) spanning weeks or months, and create a unified wiki that:
- Documents each call individually
- Shows connections across calls
- Tracks participant journeys over time
- Identifies cross-call themes
- Organizes personal check-ins separately from topical discussions

**Key principle:** This is both a collection of individual call wikis AND a synthesis showing evolution, patterns, and connections across time.

---

## **Phase 0: Multi-Call Mapping (CRITICAL FIRST STEP)**

Before reading any transcripts deeply, create a comprehensive map of the landscape.

### 0.1 Inventory All Calls

Create a spreadsheet or structured document:

```
Call 01 | 2025-10-15 | Curiosity in Education    | 12 participants | Check-ins: Yes
Call 02 | 2025-10-22 | AI and Learning          | 15 participants | Check-ins: Yes
Call 03 | 2025-10-29 | Systems Thinking         | 10 participants | Check-ins: No
...
Call 15 | 2025-12-17 | Year-End Reflection      | 18 participants | Check-ins: Yes
```

For each call note:
- **Date** (establishes chronology)
- **Primary topic(s)** (what was the focus)
- **Participant count**
- **Check-in format** (Yes/No, theme if any)
- **Call type** (topical discussion vs open check-in vs hybrid)
- **Artifacts available** (transcript, chat, board, etc.)

### 0.2 Map Participants Across Calls

Create participant attendance matrix:

```
Participant          | Calls Attended | First | Last  | Type
---------------------|----------------|-------|-------|----------
Jerry Michalski      | 15/15         | 01    | 15    | Regular
Pete Kaminski        | 14/15         | 01    | 15    | Regular
Victoria (Spain)     | 12/15         | 01    | 15    | Regular
Jane Smith           | 1/15          | 07    | 07    | Guest
...
```

Identify:
- **Regulars** (attend >60% of calls)
- **Frequent** (attend 30-60% of calls)
- **Occasional** (attend 10-30%)
- **Guests** (attend 1-2 calls)

### 0.3 Topic Mapping Across Calls

Before deep reading, skim all call topics and create topic clusters:

```
Education cluster:
  - Call 01: Curiosity in Education
  - Call 05: Teaching Methods
  - Call 09: Student Engagement

AI/Technology cluster:
  - Call 02: AI and Learning
  - Call 08: ChatGPT in Education
  - Call 12: Technology Ethics

Meta/Community cluster:
  - Call 06: How We Have Conversations
  - Call 11: Community Building
  - Call 15: Year-End Reflection
```

This creates your initial thematic structure.

### 0.4 Check-In Analysis

For calls with check-ins, note:
- **Check-in theme** (if any) - e.g., "What brought you joy this week?"
- **Structured vs freeform**
- **Approximate time** (first 30 min? entire call?)
- **Relationship to main topic** (related vs separate)

---

## **Phase 1: Per-Call Analysis**

### 1.1 Read Each Call Completely

For each of the 15 calls:
- Read entire transcript
- Read all chat
- Review any visual artifacts
- **Separately track:**
  - Check-in content (personal updates, reflections)
  - Topical discussion content

### 1.2 Per-Call Documentation

As you read each call, document:

**Call-specific notes:**
- Key themes discussed
- Major insights or frameworks introduced
- Stories told
- Decisions made or actions proposed
- Disagreements or tensions
- Unresolved questions

**Participant contributions (per call):**
- What each person contributed to topic
- Their check-in content (if applicable)
- New participants (first time)
- Absent regulars (notable absences)

**Cross-call references:**
- References to previous calls
- "Last time we discussed..."
- Evolution of ideas
- Returning themes

### 1.3 Build Cross-Call Index While Reading

Maintain running lists:

**Topics mentioned across calls:**
```
"Curiosity" - Calls: 01, 03, 05, 07, 12
"AI/ChatGPT" - Calls: 02, 08, 09, 12
"Education reform" - Calls: 01, 05, 09, 14
```

**Participant attendance:**
```
Jerry: All calls
Pete: Missing call 08
Victoria: Missing calls 03, 07, 11
```

**Stories told:**
```
Kevin's cobra story - Call 01
Gil's etymology insight - Call 01, referenced in Call 07
Jane's teaching experience - Call 05
```

---

## **Phase 2: Wiki Structure Design**

### 2.1 Multi-Level Structure

```
Root Level - Overview pages
├── README.md (entry point)
├── Start Here.md (navigation guide)
├── About This Wiki.md
└── Work Log.md

Calls Level - Individual call documentation
├── Calls/
│   ├── Calls Hub.md (index of all calls)
│   ├── Call 01 - Curiosity in Education.md
│   ├── Call 02 - AI and Learning.md
│   └── ... (15 call summary pages)

Participants Level
├── Participants/
│   ├── Participants Hub.md
│   ├── Jerry Michalski.md (profile across all calls)
│   ├── Pete Kaminski.md
│   └── ... (participant profile pages)

Topics Level
├── Topics/
│   ├── Topics Hub.md
│   ├── Curiosity.md (synthesis across calls)
│   ├── AI and Education.md
│   └── ... (cross-call topic pages)

Check-Ins Level
├── Check-Ins/
│   ├── Check-Ins Hub.md
│   ├── Personal Updates by Call.md
│   ├── Themes in Check-Ins.md
│   └── ... (check-in collections)

Indexes Level
├── Indexes/
│   ├── By Date.md (chronological)
│   ├── By Topic.md (thematic)
│   ├── By Participant.md (who said what)
│   └── Alphabetical Index.md (A-Z)
```

**Or use flat structure with careful prefixing:**
```
Call 01 - Curiosity in Education.md
Call 02 - AI and Learning.md
...
Jerry Michalski.md
Pete Kaminski.md
...
Topic - Curiosity.md
Topic - AI and Education.md
...
```

Choose based on repo/platform capabilities and user preference.

### 2.2 Page Types and Templates

#### Call Summary Page Template

```markdown
# Call [Number] - [Topic] ([Date])

**Date:** [ISO date]
**Participants:** [List with links to profiles]
**Artifacts:** [Links to transcript, chat, board]
**Type:** [Topical Discussion / Open Check-In / Hybrid]

## Overview

[2-3 paragraph summary of the call]

## Check-Ins

[If applicable - personal updates from participants]

### [Participant Name]

> "[Check-in quote or summary]"

[Repeat for each participant]

## Main Discussion

### [Theme 1]

[Discussion synthesis]

**Key insights:**
- Point 1
- Point 2

**Participants who contributed:**
- [[Person 1]] - [Their perspective]
- [[Person 2]] - [Their perspective]

### [Theme 2]

...

## Stories Told

- [[Kevin Jones]] - [Story title/summary]
- [[Gil Friend]] - [Story title/summary]

## Frameworks & Tools Mentioned

- [[Framework Name]] - Introduced by [[Person]]
- [[Tool Name]] - Discussed by [[Person]]

## Questions Raised

- Unanswered question 1
- Unanswered question 2 (returned in Call [N])

## Connections to Other Calls

- **Previous:** Referenced [[Call 05]] discussion of [topic]
- **Next:** Continued in [[Call 12]] with [development]

## Related Topics

- [[Topic - Curiosity]]
- [[Topic - Education]]

## Participants

- [[Jerry Michalski]]
- [[Pete Kaminski]]
- [etc.]
```

#### Participant Profile Template (Multi-Call)

```markdown
# [Participant Name]

**Role:** [Description]
**Attended:** [X] of [Y] calls ([First] to [Last])
**Calls:** [[Call 01]], [[Call 03]], [[Call 07]], ...

## Overview

[1-2 paragraphs about this person's contributions across all calls]

## Evolution of Thinking

[Track how their ideas developed over time]

### Early Calls (Calls 1-5)

[What they focused on initially]

### Middle Period (Calls 6-10)

[How their thinking evolved]

### Recent Calls (Calls 11-15)

[Current focus and synthesis]

## Major Contributions

### [Topic/Theme]

**Across calls:** [[Call 01]], [[Call 05]], [[Call 09]]

[Synthesis of their perspective on this topic across multiple calls]

> "Quote from Call 01"

> "Evolution in Call 05"

> "Synthesis in Call 09"

### [Another Topic]

...

## Stories Told

- [[Call 01]] - [Story title]
- [[Call 07]] - [Story title]

## Check-Ins

[Collection of their personal check-ins across calls]

### [Call 01] - [Date]

> "[Check-in content]"

### [Call 03] - [Date]

> "[Check-in content]"

## Themes Explored Across Calls

- [[Topic - Curiosity]]
- [[Topic - Education]]
- [[Topic - AI]]

## Related Participants

- [[Person 1]] - Often discussed [topic] together
- [[Person 2]] - Complementary perspectives on [topic]

## Call Attendance

| Call | Date | Topic | Attended |
|------|------|-------|----------|
| 01 | 2025-10-15 | Curiosity | ✓ |
| 02 | 2025-10-22 | AI | ✓ |
| 03 | 2025-10-29 | Systems | ✗ |
...
```

#### Cross-Call Topic Page Template

```markdown
# Topic - [Topic Name]

**Discussed in:** [[Call 01]], [[Call 05]], [[Call 09]], [[Call 12]]
**Primary contributors:** [[Person 1]], [[Person 2]], [[Person 3]]

## Overview

[Synthesis of this topic across all calls where it appeared]

## Evolution Across Calls

### [[Call 01]] - Initial Discussion

[What was first said about this topic]

**Key participants:**
- [[Person 1]]: > "Quote"
- [[Person 2]]: > "Quote"

### [[Call 05]] - Development

[How the discussion evolved]

**New insights:**
- Point 1
- Point 2

### [[Call 09]] - Synthesis

[Further development or integration]

### [[Call 12]] - Current Thinking

[Latest state of discussion]

## Key Themes

### [Sub-theme 1]

[Synthesis across calls]

### [Sub-theme 2]

[Synthesis across calls]

## Frameworks & Tools

- [[Framework Name]] - Introduced in [[Call 01]]
- [[Tool Name]] - Applied in [[Call 05]]

## Stories & Examples

- [[Call 01]] - [[Person]]'s story about [topic]
- [[Call 09]] - [[Person]]'s example of [topic]

## Open Questions

- Question raised in [[Call 01]], still unresolved
- Question from [[Call 09]], partially addressed in [[Call 12]]

## Related Topics

- [[Topic - Related 1]]
- [[Topic - Related 2]]

## Participants Who Engaged

- [[Person 1]] - Calls 01, 05, 09, 12
- [[Person 2]] - Calls 05, 09
- [[Person 3]] - Calls 01, 12
```

---

## **Phase 3: Hub Pages for Multi-Call Wikis**

### 3.1 Calls Hub

```markdown
# Calls Hub

Overview of all [N] calls in this series.

## All Calls by Date

### [Call 01] - [Topic] (October 15, 2025)

[1-2 sentence summary]

**Participants:** [N] - [[Person 1]], [[Person 2]], ...
**Key themes:** [Theme 1], [Theme 2]
**Type:** [Topical / Check-in / Hybrid]

[Link to full call page]

### [Call 02] - [Topic] (October 22, 2025)

...

## Calls by Topic Cluster

### Education Cluster
- [[Call 01]] - Curiosity in Education
- [[Call 05]] - Teaching Methods
- [[Call 09]] - Student Engagement

### AI/Technology Cluster
- [[Call 02]] - AI and Learning
- [[Call 08]] - ChatGPT in Education

### Meta/Community Cluster
- [[Call 06]] - How We Have Conversations
- [[Call 15]] - Year-End Reflection

## Calls by Type

### Topical Discussions (8 calls)
- [[Call 01]], [[Call 02]], [[Call 03]], ...

### Check-In Focused (5 calls)
- [[Call 04]], [[Call 06]], [[Call 11]], ...

### Hybrid (2 calls)
- [[Call 13]], [[Call 15]]

## Timeline View

[Visual representation if possible, otherwise chronological list with key developments]

## Navigation

- [[Participants Hub]] - Who attended which calls
- [[Topics Hub]] - What was discussed across calls
- [[Check-Ins Hub]] - Personal updates from participants
```

### 3.2 Participants Hub (Multi-Call)

```markdown
# Participants Hub

[N] people participated across [M] calls from [Start Date] to [End Date].

## Regulars (Attended >60% of calls)

### [[Jerry Michalski]]
**Attended:** 15/15 calls | **First:** Call 01 | **Last:** Call 15

[1-2 sentence summary of their contributions across all calls]

**Key topics:** Curiosity, Education, Community
**Stories told:** 7 stories across 5 calls
**Notable evolution:** [How their thinking changed]

### [[Pete Kaminski]]
**Attended:** 14/15 calls | **First:** Call 01 | **Last:** Call 15

[Summary]

## Frequent Participants (30-60%)

### [[Victoria (Spain)]]
**Attended:** 12/15 calls | **Absent:** Calls 03, 07, 11

[Summary]

## Occasional Participants (10-30%)

...

## Guest Participants (1-2 calls)

...

## Attendance Matrix

| Participant | 01 | 02 | 03 | 04 | 05 | ... | Total |
|-------------|----|----|----|----|----|----|-------|
| Jerry       | ✓  | ✓  | ✓  | ✓  | ✓  | ✓  | 15    |
| Pete        | ✓  | ✓  | ✓  | ✓  | ✗  | ✓  | 14    |
| Victoria    | ✓  | ✓  | ✗  | ✓  | ✓  | ✗  | 12    |
...

## Navigation

- [[Calls Hub]] - All calls by date and topic
- [[Topics Hub]] - What was discussed
- [[Check-Ins Hub]] - Personal updates
```

### 3.3 Topics Hub (Multi-Call)

```markdown
# Topics Hub

Major themes and topics discussed across [N] calls.

## Core Recurring Topics

### [[Topic - Curiosity]]
**Calls:** 01, 03, 05, 07, 12
**Contributors:** Jerry, Pete, Victoria, Kevin, Stacey

[2-3 sentence summary of how this topic evolved]

### [[Topic - AI and Education]]
**Calls:** 02, 08, 09, 12
**Contributors:** Pete, Alex, Louise

[Summary]

## Topic Clusters

### Education & Learning
- [[Topic - Curiosity in Education]]
- [[Topic - Teaching Methods]]
- [[Topic - Student Engagement]]
- [[Topic - Assessment]]

### Technology & AI
- [[Topic - AI and Learning]]
- [[Topic - ChatGPT Uses]]
- [[Topic - Technology Ethics]]

### Systems & Thinking
- [[Topic - Systems Thinking]]
- [[Topic - Complexity]]
- [[Topic - Frameworks]]

### Community & Practice
- [[Topic - Conversation Design]]
- [[Topic - Community Building]]
- [[Topic - Collective Sense-Making]]

## Topic Evolution Map

[Showing how topics emerged, merged, split over time]

```
Call 01: Curiosity introduced
         ↓
Call 03: Curiosity + Education (merged)
         ↓
Call 05: Curiosity (cont.) + Teaching Methods (new)
         ↓
Call 07: Curiosity synthesis + Systems Thinking (new)
```

## One-Time Topics

[Topics discussed in only one call - with links to that call]

## Navigation

- [[Calls Hub]] - Find topics by call
- [[Participants Hub]] - Find topics by person
- [[Alphabetical Index]] - A-Z of all topics
```

### 3.4 Check-Ins Hub

```markdown
# Check-Ins Hub

Personal updates and check-ins from participants across calls.

## About Check-Ins

[Explanation of the check-in practice in this community]

## Check-Ins by Call

### [[Call 01]] Check-Ins - "What brings you here?"

- [[Jerry Michalski]]: > "[Check-in quote]"
- [[Pete Kaminski]]: > "[Check-in quote]"
- [[Victoria]]: > "[Check-in quote]"
...

### [[Call 02]] Check-Ins - "What brought you joy this week?"

...

## Check-Ins by Participant

### [[Jerry Michalski]]'s Check-Ins

- **Call 01:** "[Check-in summary]"
- **Call 02:** "[Check-in summary]"
- **Call 03:** "[Check-in summary]"
...

[Pattern or evolution in Jerry's check-ins over time]

### [[Pete Kaminski]]'s Check-Ins

...

## Themes in Check-Ins

### Personal Growth & Learning
- Participants who focused on growth: Jerry, Victoria, Louise
- Evolution over calls: [Pattern]

### Work & Projects
- Participants sharing professional updates: Pete, Kevin, Gil
- Common themes: [Themes]

### Health & Wellbeing
- Calls where health was prominent: 04, 08, 11
- Participants: Stacey, Eve, John

### Joy & Gratitude
- Calls with gratitude theme: 02, 06, 10
- Patterns: [Patterns]

## Check-In Practices

### Structured Check-Ins
- **Call 02:** "What brought you joy?"
- **Call 06:** "What are you learning?"
- **Call 10:** "What are you grateful for?"

### Freeform Check-Ins
- Calls: 01, 04, 08, 11, 15

## Navigation

- [[Calls Hub]] - Check-ins by call
- [[Participants Hub]] - Personal journeys
```

### 3.5 Start Here (Multi-Call)

```markdown
# Start Here

Welcome to the wiki for [Series Name] - [N] calls from [Start] to [End].

## Choose Your Path

### "I want to understand the series"

1. [[README]] - Overview of the entire series
2. [[Calls Hub]] - Browse all calls chronologically
3. [[Major Themes Across Calls]] - Synthesis of key ideas

**Next:** Pick a topic cluster that interests you

### "I'm interested in a specific topic"

1. [[Topics Hub]] - All topics across all calls
2. Find your topic (e.g., [[Topic - Curiosity]])
3. Follow the evolution across calls

**Next:** See which participants engaged deeply

### "I want to follow specific people"

1. [[Participants Hub]] - All participants
2. Choose a participant (e.g., [[Jerry Michalski]])
3. See their journey across calls

**Next:** Explore topics they engaged with

### "I'm looking for personal stories"

1. [[Check-Ins Hub]] - Personal updates from participants
2. Browse by person or by call
3. See patterns and evolution over time

**Next:** Connect personal to topical discussions

### "I attended some calls and want to revisit"

1. [[Calls Hub]] - Find your calls by date
2. Read the synthesis
3. Follow cross-references to related calls

**Next:** See how topics evolved after your calls

### "I want to see the big picture"

1. [[README]] - Start with overview
2. [[Major Themes Across Calls]] - Synthesis
3. [[Evolution and Patterns]] - How ideas developed
4. [[Participants Hub]] - Who shaped the conversation

## Browse By

- 📅 **[[By Date]]** - Chronological view of all calls
- 💡 **[[By Topic]]** - Thematic organization
- 👥 **[[By Participant]]** - Who said what
- 🔤 **[[Alphabetical Index]]** - A-Z of everything

## Quick Stats

- **Calls:** [N]
- **Participants:** [M] total ([P] regulars, [Q] occasional, [R] guests)
- **Topics:** [T] major themes discussed
- **Pages:** [X] total
- **Time period:** [Start date] to [End date]

## Navigation Tips

- **Call pages** have full summaries with check-ins, discussion, and cross-references
- **Participant pages** show evolution across all their calls
- **Topic pages** synthesize discussion across multiple calls
- **Check-in pages** collect personal updates separately from topical content
```

---

## **Phase 4: Enhanced Processing Passes**

Multi-call wikis require additional passes beyond single-call wikis.

### Pass 1: Individual Call Processing

For each call:
- Create call summary page
- Extract participant contributions
- Identify topics discussed
- Document check-ins separately

**Output:** 15 call summary pages + raw lists of participants, topics

### Pass 2: Participant Synthesis

For each participant:
- Aggregate their contributions across all calls they attended
- Track evolution of their thinking
- Collect their check-ins
- Identify their key topics
- Note their stories across calls

**Output:** Participant profile pages (one per person)

### Pass 3: Topic Synthesis

For each recurring topic:
- Find all calls where discussed
- Synthesize evolution across calls
- Note who contributed when
- Track unresolved questions
- Show development of ideas

**Output:** Cross-call topic pages

### Pass 4: Pattern Recognition

Look across all calls for:
- **Recurring debates** (same question across multiple calls)
- **Evolution of thinking** (how ideas developed)
- **Topic relationships** (how topics connected)
- **Participant relationships** (who engaged with whom)
- **Check-in patterns** (themes in personal updates)
- **Seasonal variations** (changes over time)

**Output:**
- Evolution and Patterns page
- Topic relationship maps
- Participant collaboration networks

### Pass 5: Cross-Linking Enhancement

Now that all pages exist:
- Add "Discussed in these calls" to topic pages
- Add "Related topics across calls" to call pages
- Add "Also discussed by" to participant pages
- Create bidirectional "See also" sections
- Build navigation paths

**Output:** Enriched linking throughout wiki

### Pass 6: Meta-Synthesis

Create synthesis pages:
- **Major Themes Across All Calls** - Top 10 themes synthesized
- **Evolution of Ideas** - How thinking developed over series
- **Participant Journeys** - Notable personal/intellectual growth
- **Unresolved Questions** - What remains open
- **Community Patterns** - How the group itself evolved

**Output:** 5-10 synthesis pages providing high-level perspective

---

## **Phase 5: Navigation for Scale**

With 15 calls, potentially 50+ participants, 100+ topics, you need robust navigation.

### 5.1 Multiple Index Pages

**By Date (Chronological):**
- Call 01 (Oct 15) → Call 02 (Oct 22) → etc.

**By Topic (Thematic):**
- Education cluster (Calls 01, 05, 09)
- AI cluster (Calls 02, 08, 12)
- Meta cluster (Calls 06, 11, 15)

**By Participant:**
- Jerry's calls (all 15)
- Pete's calls (14 of 15, missing 08)
- Jane's calls (only 07)

**By Type:**
- Topical discussions (8 calls)
- Check-in focused (5 calls)
- Hybrid (2 calls)

### 5.2 Timeline/Evolution Pages

**Evolution of Key Ideas:**

```markdown
# Evolution of [Topic]

## Phase 1: Introduction (Calls 1-5)

[Topic] was first introduced in [[Call 01]] by [[Person]]...

## Phase 2: Development (Calls 6-10)

The discussion deepened in [[Call 07]] when [[Person]] connected it to [[Other Topic]]...

## Phase 3: Synthesis (Calls 11-15)

By [[Call 12]], the group had reached consensus that...

## Timeline

Oct 15 (Call 01): [Topic] introduced
Oct 29 (Call 03): [Development]
Nov 12 (Call 07): Connected to [Other Topic]
Dec 03 (Call 12): Synthesis reached
Dec 17 (Call 15): Applied to [New Context]
```

### 5.3 Relationship Maps

**Topic Relationship Map:**

```markdown
# Topic Relationships

## Clusters

### Education Cluster
- Curiosity in Education
  - Connected to: Teaching Methods, Student Engagement
  - Tension with: Assessment, Standardization
- Teaching Methods
  - Connected to: Curiosity, Technology
  - Builds on: Pedagogy

### AI Cluster
- AI and Learning
  - Connected to: ChatGPT, Ethics
  - Tension with: Critical Thinking, Authenticity
...
```

**Participant Collaboration Network:**

```markdown
# Who Worked With Whom

## Frequent Co-Contributors

### Jerry + Pete
**Co-appeared:** 14 calls
**Co-discussed:** Curiosity (5 times), Education (4 times), Community (3 times)
**Dynamic:** [Description of their interaction pattern]

### Victoria + Klaus
**Co-appeared:** 8 calls
**Co-discussed:** Visual Thinking (4 times), Culture (3 times)
**Dynamic:** [Description]
```

---

## **Phase 6: Quality Verification for Multi-Call Wikis**

Additional quality checks beyond single-call wikis:

### 6.1 Cross-Call Consistency

**Verify:**
- ✅ Same participant described consistently across calls
- ✅ Topic definitions don't contradict across calls
- ✅ Dates and chronology are accurate
- ✅ Call numbers referenced correctly
- ✅ "Previous call" and "next call" links work

**Watch for:**
- ❌ Participant name variations (ensure consistency)
- ❌ Topic name variations (pick canonical names)
- ❌ Conflicting summaries of same discussion
- ❌ Broken temporal references

### 6.2 Completeness Checks

**Per call:**
- ✅ Every call has summary page
- ✅ Every call's participants are documented
- ✅ Every call's topics are extracted
- ✅ Check-ins captured if applicable

**Per participant:**
- ✅ Profile exists for each person
- ✅ All their calls are listed
- ✅ Major contributions are documented
- ✅ Check-ins are collected

**Per topic:**
- ✅ Cross-call synthesis exists for recurring topics
- ✅ All calls where discussed are linked
- ✅ Evolution is tracked
- ✅ Key contributors are noted

### 6.3 Attribution Verification (Critical)

For multi-call wikis, attribution is even more complex:

**Verify:**
- When participant profile says "Person X believed Y," is this true across all calls or just one?
- When topic page says "Person X introduced this in Call 3," is that accurate?
- When check-in is attributed to Person X in Call 5, is it really theirs?
- When evolution is described, is the chronology correct?

**Process:**
- Verify each biographical claim against specific call transcript
- Note which call/line number supports each claim
- Distinguish "said once in Call 3" from "consistently said across Calls 3, 7, 11"
- Track if person's view evolved vs stayed constant

---

## **Special Considerations for Check-In Calls**

### 7.1 Separating Personal from Topical

Many calls start with check-ins before topical discussion. Keep these separate:

**In Call Summary Page:**
```markdown
## Check-Ins (First 30 minutes)

[Check-in summaries]

## Main Discussion (Remaining time)

[Topical content]
```

**In Participant Profile:**
```markdown
## Check-Ins

[Collection of their personal updates]

## Topical Contributions

[Their contributions to discussions]
```

**In Check-Ins Hub:**
```markdown
# Check-Ins Hub

[All check-ins collected here, separate from topics]
```

### 7.2 When Check-Ins ARE the Call

Some calls are purely check-in focused. For these:

**Call summary emphasizes:**
- Themes in check-ins
- Patterns across participants
- Emergent topics from check-ins
- Community building aspects

**Don't force topical structure** if it doesn't exist.

### 7.3 Personal vs Public

Some check-ins may be sensitive. Consider:
- Summarizing rather than quoting verbatim if personal
- Noting themes without attributing specifics
- Checking if transcript is public or restricted

---

## **File Organization Options**

### Option A: Flat with Prefixes

```
Call 01 - Curiosity in Education.md
Call 02 - AI and Learning.md
...
Jerry Michalski.md
Pete Kaminski.md
...
Topic - Curiosity.md
Topic - AI and Education.md
...
CheckIns - Call 01.md
CheckIns - Call 02.md
...
Index - By Date.md
Index - By Topic.md
Hub - Calls.md
Hub - Participants.md
README.md
Start Here.md
```

**Pros:** Simple, works with any platform, easy file management
**Cons:** Gets cluttered with 500+ files

### Option B: Directory Structure

```
/
├── README.md
├── Start Here.md
├── About This Wiki.md
├── Work Log.md
├── Calls/
│   ├── Calls Hub.md
│   ├── Call 01 - Curiosity in Education.md
│   ├── Call 02 - AI and Learning.md
│   └── ...
├── Participants/
│   ├── Participants Hub.md
│   ├── Jerry Michalski.md
│   ├── Pete Kaminski.md
│   └── ...
├── Topics/
│   ├── Topics Hub.md
│   ├── Curiosity.md
│   ├── AI and Education.md
│   └── ...
├── CheckIns/
│   ├── CheckIns Hub.md
│   ├── By Call.md
│   ├── By Participant.md
│   └── Themes.md
├── Indexes/
│   ├── By Date.md
│   ├── By Topic.md
│   ├── By Participant.md
│   └── Alphabetical.md
└── Synthesis/
    ├── Major Themes.md
    ├── Evolution of Ideas.md
    └── Community Patterns.md
```

**Pros:** Organized, scalable, clear categories
**Cons:** Requires platform supporting subdirectories, more complex linking

**Recommendation:** Use Option B (directories) for multi-call wikis to manage scale.

---

## **Workflow Summary for 15-Call Wiki**

### Week 1: Mapping (Phase 0)
- Inventory all 15 calls
- Map participants across calls
- Identify topic clusters
- Analyze check-in patterns

### Week 2-3: Per-Call Processing (Phases 1-2)
- Read all 15 transcripts and chats
- Create 15 call summary pages
- Build initial participant profiles
- Extract all topics

### Week 4: Synthesis (Pass 3-4)
- Create cross-call topic pages
- Enrich participant profiles with evolution
- Build check-ins hub and collections
- Identify patterns and relationships

### Week 5: Navigation (Pass 5-6)
- Create all hub pages
- Build indexes (by date, topic, participant)
- Create synthesis pages
- Add cross-links throughout

### Week 6: Quality & Documentation (Phase 6)
- Verify attributions across calls
- Check completeness
- Verify cross-call consistency
- Write process documentation
- Update work log

**Total estimated time: 40-60 hours for 15 calls with 50 participants and 100+ topics**

---

## **Metrics for Success**

### Completeness
- ✅ All calls documented with summary pages
- ✅ All participants have profile pages
- ✅ All recurring topics have synthesis pages
- ✅ All check-ins collected and organized
- ✅ Zero orphan links

### Cross-Call Integration
- ✅ Topic evolution tracked across calls
- ✅ Participant journeys documented
- ✅ Cross-references between related calls
- ✅ Patterns and relationships identified
- ✅ Synthesis pages provide high-level view

### Navigation
- ✅ 5+ hub pages (Calls, Participants, Topics, Check-Ins, Index)
- ✅ 4+ index pages (by date, topic, participant, A-Z)
- ✅ Start Here with 5+ curated paths
- ✅ README with clear overview
- ✅ Timeline or evolution pages

### Quality
- ✅ Accurate attributions (verified against transcripts)
- ✅ Consistent naming across calls
- ✅ Correct chronology
- ✅ Personal check-ins separated from topical content
- ✅ Evolution tracked accurately

---

## **Key Lessons Applied from "Improved for Next Time"**

All quality principles from single-call wikis apply, plus:

### 1. Read Everything First (Even More Critical)

With 15 calls, the temptation is to process incrementally. **Don't.**

- Read all 15 transcripts before creating pages
- Map the entire landscape first
- Identify patterns that only appear across multiple calls
- See the arc of the series before documenting individual moments

### 2. Attribution Across Time

Single-call: "Person X said Y"
Multi-call: "Person X said Y in Call 3, evolved to Z in Call 7, synthesized as W in Call 12"

**Verify:**
- Which call a claim comes from
- Whether it's consistent across calls
- How it evolved over time
- What the current state is

### 3. Participant Consistency

Same person may:
- Evolve their thinking (track evolution)
- Contradict themselves (note it)
- Try different ideas (show exploration)
- Reach synthesis (document journey)

**Don't:**
- Assume consistency across calls
- Hide evolution or contradiction
- Present final view as always-held

### 4. Topic Evolution is the Story

Single-call: "What was said about X"
Multi-call: "How understanding of X developed"

The **evolution** is often more valuable than any single snapshot.

### 5. Systematic Passes at Scale

With 15 calls, you can't keep it all in mind. Use scripts and systematic passes:
- Pass 1: Individual calls
- Pass 2: Participant aggregation
- Pass 3: Topic synthesis
- Pass 4: Pattern recognition
- Pass 5: Cross-linking
- Pass 6: Meta-synthesis

### 6. Hub Pages Are Essential, Not Optional

Single-call: Hub pages improve navigation
Multi-call: Hub pages are mandatory for usability

Without them, users drown in 500+ pages.

### 7. Check-Ins Need Separate Treatment

Personal check-ins are:
- Valuable for understanding participants
- Different from topical contributions
- Worth collecting and analyzing
- Potentially sensitive

Give them dedicated space and respect their personal nature.

---

## **Common Pitfalls in Multi-Call Wikis**

### ❌ Don't Do This

1. **Processing calls sequentially without reading all first**
   - You'll miss cross-call patterns
   - You'll create inconsistent structure
   - You'll duplicate effort

2. **Treating it as 15 separate wikis**
   - Misses the synthesis opportunity
   - Creates redundancy
   - Loses the evolution story

3. **Forgetting which call a quote came from**
   - Always note [Call XX, lines YYY-ZZZ]
   - Track sources meticulously
   - Verify before claiming "Person X believed Y"

4. **Mixing check-ins with topical content**
   - Keep personal separate from intellectual
   - Respect the different modes
   - Create dedicated check-in spaces

5. **Not tracking participant attendance**
   - "Person X said Y" when they weren't in that call
   - Assuming regulars attended everything
   - Missing notable absences

6. **Skipping the synthesis passes**
   - Just documenting individual calls isn't enough
   - The value is in cross-call synthesis
   - Patterns only emerge with analysis

7. **Creating flat structure at this scale**
   - 500+ files in one directory is unmanageable
   - Use subdirectories or careful prefixing
   - Think about navigation from the start

8. **Not documenting evolution**
   - Multi-call wikis should show growth over time
   - Static snapshots miss the point
   - Track how ideas developed

### ✅ Do This Instead

1. **Complete read-through of all calls first**
2. **Design for synthesis from the start**
3. **Meticulous source attribution with call numbers**
4. **Separate check-ins space**
5. **Attendance matrix for participants**
6. **Dedicated synthesis passes**
7. **Directory structure or clear prefixing**
8. **Evolution and timeline pages**

---

## **Templates for Scripts**

### Multi-Call Orphan Finder

```python
# _bin/find-orphan-links-multicall.py

# Should handle:
# - Links to calls: [[Call 01]]
# - Links to participants: [[Jerry Michalski]]
# - Links to topics: [[Topic - Curiosity]]
# - Links across directories if using directory structure
# - Both [[Page]] and [[Page|display]] syntax
```

### Cross-Call Topic Tracker

```python
# _bin/track-topics-across-calls.py

# Outputs:
# - Which topics appear in which calls
# - Who discussed each topic in each call
# - Evolution of topic across calls
# - Gaps where topic wasn't discussed
```

### Participant Attendance Matrix

```python
# _bin/participant-attendance.py

# Outputs:
# - Matrix of who attended which calls
# - Statistics (regulars, occasional, guests)
# - First and last call for each person
# - Percentage attendance
```

---

## **Deliverables for Multi-Call Wiki**

1. **Call Pages** (15 pages)
   - Full summary for each call
   - Check-ins section
   - Main discussion synthesis
   - Cross-references

2. **Participant Profiles** (50+ pages)
   - Evolution across calls
   - All contributions aggregated
   - Check-ins collected
   - Attendance tracked

3. **Topic Synthesis Pages** (100+ pages)
   - Cross-call synthesis
   - Evolution tracking
   - Key contributors
   - Related topics

4. **Hub Pages** (5+ pages)
   - Calls Hub
   - Participants Hub
   - Topics Hub
   - Check-Ins Hub
   - Start Here

5. **Index Pages** (4+ pages)
   - By Date
   - By Topic
   - By Participant
   - Alphabetical

6. **Synthesis Pages** (5+ pages)
   - Major Themes Across Calls
   - Evolution of Ideas
   - Participant Journeys
   - Community Patterns
   - Unresolved Questions

7. **Meta Pages**
   - README
   - About This Wiki
   - Work Log
   - Wiki Creation Process
   - Scripts in _bin/

**Total:** 600-800 pages typical for 15 calls with 50 participants

---

## **Final Checklist**

Before considering multi-call wiki complete:

- [ ] All 15 calls have summary pages
- [ ] All participants have profile pages
- [ ] All recurring topics have synthesis pages
- [ ] All check-ins are collected
- [ ] 5+ hub pages created
- [ ] 4+ index pages created
- [ ] 5+ synthesis pages created
- [ ] Evolution is tracked for key topics
- [ ] Participant journeys are documented
- [ ] Cross-call patterns are identified
- [ ] Attendance matrix is accurate
- [ ] All attributions verified with call numbers
- [ ] Zero orphan links
- [ ] Timeline/chronology is correct
- [ ] Personal check-ins separated from topical
- [ ] Scripts created for reusability
- [ ] Work log documents process
- [ ] Wiki Creation Process documents decisions
- [ ] README provides clear entry point
- [ ] Start Here guides different user types

---

*These instructions extend [[Instructions for AI Assistant - Improved for Next Time]] to handle the complexity of multi-call wikis while preserving all the quality principles and lessons learned from single-call wiki creation.*
