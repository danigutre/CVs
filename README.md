# Daniel Gutierrez — CV Repository

Personal CV repository containing résumés in both English and Spanish, along with a utility script to merge them into a single PDF.

## Files

| File | Description |
|------|-------------|
| `DanielGutierrezCVEng.pdf` | CV in English (PDF) |
| `DanielGutierrezCVEsp.pdf` | CV in Spanish (PDF) |
| `DanielGutierrezCV.pdf` | CV (PDF) |
| `CV 08_25 Eng.docx` | CV in English (Word) |
| `CV 08_25 Esp.docx` | CV in Spanish (Word) |
| `merge_cvs.py` | Script to merge English and Spanish PDFs into one file |

## Merging the CVs

The `merge_cvs.py` script combines the English and Spanish PDFs into a single file (`DanielGutierrezCV_Combined.pdf`).

### Requirements

- Python 3
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Install the dependency with:

```bash
pip install PyPDF2
```

### Usage

```bash
python merge_cvs.py
```

The merged output will be saved as `DanielGutierrezCV_Combined.pdf` in the same directory.
