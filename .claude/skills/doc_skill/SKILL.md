---
Name: DocSkill
Description: Preserve and manage .doc files with backup and metadata extraction capabilities
---

### Document Preservation Skill

A skill to help preserve, manage, and extract data from Microsoft Word (.doc/.docx) files with automated backups and metadata tracking.

### Features:

1. **File Preservation**: Automatically backup .doc and .docx files with timestamp versioning
2. **Metadata Extraction**: Extract document metadata (author, creation date, modification date, etc.)
3. **Content Extraction**: Extract text content from Word documents for analysis
4. **Integrity Verification**: Verify file integrity and create checksums for validation

### Usage:

#### Step 1: Load Document
- Read .doc or .docx files from specified paths
- Validate file format and integrity

#### Step 2: Extract Metadata
- Extract document properties (title, author, created date, modified date)
- Store metadata in structured format

#### Step 3: Extract Content
- Extract plain text content from document
- Preserve formatting information where possible
- Generate content summary

#### Step 4: Create Backup
- Create timestamped backup copies in `output/<current_date>/doc_backups/`
- Generate checksum for integrity verification

#### Step 5: Save Report
- Save document preservation report as JSON in `output/<current_date>/doc_report_<current_timestamp>.json`
- Include metadata, content summary, and backup location

### Output Structure:
```
output/<current_date>/
├── doc_backups/
│   └── <filename>_<timestamp>.docx
└── doc_report_<current_timestamp>.json
```
