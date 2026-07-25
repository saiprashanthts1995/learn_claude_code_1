# doc_skill - Document Preservation Skill

A Claude Code skill for preserving, managing, and extracting data from Microsoft Word documents (.doc and .docx files).

## Features

- **Metadata Extraction**: Extract document properties (author, creation date, modification date, etc.)
- **Content Extraction**: Extract and summarize text content from Word documents
- **Automatic Backups**: Create timestamped backup copies of documents
- **Integrity Verification**: Generate checksums to verify file integrity
- **Structured Reports**: Generate JSON reports with complete preservation information

## Installation

### Prerequisites

Install the required Python package:

```bash
pip install python-docx
```

## Usage

### Using the Skill

Invoke the doc_skill in Claude Code:

```
/doc_skill
```

### Programmatic Usage

```python
from assets.doc_helper import DocPreserver

# Initialize the preserver
preserver = DocPreserver(output_base="output")

# Preserve a single document
result = preserver.preserve_document("path/to/document.docx")

# Save the report
report_path = preserver.save_report(result)
print(f"Report saved to: {report_path}")
```

## Output

The skill generates the following outputs:

```
output/<YYYY-MM-DD>/
├── doc_backups/
│   └── <filename>_<timestamp>.docx    # Backup copy
└── doc_report_<timestamp>.json         # Preservation report
```

## Report Structure

The JSON report includes:

```json
{
  "status": "success",
  "timestamp": "2026-04-06T10:30:45.123456",
  "metadata": {
    "filename": "document.docx",
    "file_path": "/path/to/document.docx",
    "file_size_bytes": 12345,
    "author": "Author Name",
    "created": "2026-01-01 10:00:00",
    "modified": "2026-04-06 09:00:00",
    "title": "Document Title",
    "paragraphs_count": 42,
    "tables_count": 3
  },
  "content_summary": {
    "text_content": "Full text content...",
    "paragraph_count": 42,
    "table_count": 3,
    "summary": {
      "word_count": 5000,
      "character_count": 28000
    }
  },
  "backup": {
    "backup_path": "output/2026-04-06/doc_backups/document_20260406_103045.docx",
    "backup_filename": "document_20260406_103045.docx"
  },
  "checksum": "a1b2c3d4e5f6..."
}
```

## Methods

### `DocPreserver`

#### `extract_metadata(file_path: str) -> Dict`
Extracts document metadata including author, creation date, modification date, title, subject, and document structure info.

#### `extract_content(file_path: str) -> Dict`
Extracts all text content and tables from the document, with word and character count summaries.

#### `create_backup(file_path: str) -> Dict`
Creates a timestamped backup copy of the document in the backup directory.

#### `preserve_document(file_path: str) -> Dict`
Performs the complete preservation workflow: metadata extraction, content extraction, backup creation, and checksum generation.

#### `save_report(preservation_data: Dict, filename: Optional[str] = None) -> str`
Saves the preservation data as a JSON report file.

## Requirements

- Python 3.7+
- `python-docx` package

## Notes

- The skill reuses existing helper files and virtual environments
- All backups are created with timestamp versioning to prevent overwrites
- Checksums are generated for integrity verification
- Reports are stored in JSON format for easy parsing and archival

---

Created for preserving important document collections and maintaining audit trails.
