# Create a Wiki from This Call + Artifacts

## **Instructions**

I’m going to give you a transcript, chat logs, notes, and any other artifacts from a call.
Your job is to **analyze everything** and produce a **complete markdown wiki**, following the rules below.

---

## **1. Core Output Requirements**

* Produce a **comprehensive summary** of the call.
* Fully **analyze and synthesize the chat**, organizing the threads and summarizing the important conversations.
* Create structured lists of:

  * **People**
  * **Books**
  * **Organizations**
  * **Referenced concepts or tools**
* Output everything as a **markdown wiki**, with:

  * filenames matching page titles (capitalize, use spaces, no forbidden FS chars)
  * file extension `.md`
  * rich linking using `[[Double Square Bracket Links]]`.

---

## **2. Pages You Must Create**

### **2.1 Participant Pages**

For each participant named in the transcript or chat:

* create a page named `First Last.md`
* include their contributions, references, themes, and any notable statements
* link them where relevant.

### **2.2 Chat Thread Pages**

* Group chat into major threads
* Summarize each in its own page
* Link participant messages to the participants’ pages.

### **2.3 Reference/Entity Pages**

Whenever people, books, organizations, or concepts are mentioned:

* create a dedicated page
* include definitions or explanations
* link back to individuals and discussion where relevant.

---

## **3. Orphan Page Rule**

After building the first pass of the wiki:

* find all **linked-but-uncreated** (orphan) pages
* create each one
* begin each with a disclaimer:

  > **Note:** This topic was mentioned during the call but not discussed in depth.
* provide a short but genuinely useful explanation/background for each topic.

---

## **4. Organizational Structure**

### **4.1 Homepage (`README.md`)**

* This is the **home page of the wiki**.
* It must be **short, welcoming, not overwhelming**.
* It should contain:

  * a 1–2 paragraph overview of the call
  * a high-level summary of the themes
  * links to major sections
  * a list of participants with one-line summaries.

### **4.2 “Details About This Wiki.md”**

* A deeper documentation page describing how the wiki is organized.
* Include navigation tips, page types, conventions, etc.

### **4.3 Concept Index (`Concept Index.md`)**

* A complete index of **all pages in the wiki**, organized into categories/clusters such as:

  * Participants
  * Chat Threads
  * Technology & Tools
  * Systems & Society
  * People Mentioned
  * Organizations
  * Concepts
  * Meta/Supporting Pages

(Adjust categories to fit the content.)

---

## **5. File + Link Conventions**

* Use page-title-as-filename with `.md`.
* Use `[[Double Square Bracket Links]]` everywhere.
* Make sure all links resolve after file reorganization.
* No file should be stranded or unlinked.

---

## **6. Work Log**

Create a `Work Log.md` page:

* journal style
* newest entries at the top
* separate entries with a horizontal rule.

---

## **7. Deliverables**

At the end, deliver:

1. The complete set of markdown pages
2. A fully linked wiki with:

   * participant pages
   * chat analyses
   * concept/entity pages
   * orphan pages filled
   * hierarchical navigation
   * clear, concise README
3. A stable file structure that can be copied directly into a repo.

---
