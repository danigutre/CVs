"""
Script to merge Spanish and English CV Word documents into a single file.
"""
from docxcompose.composer import Composer
from docx import Document
import os


def merge_cv_docx():
    """Merge Spanish and English CV Word documents into a single file."""

    script_dir = os.path.dirname(os.path.abspath(__file__))

    spanish_cv = os.path.join(script_dir, "DanielGutierrezCV_Esp.docx")
    english_cv = os.path.join(script_dir, "DanielGutierrezCV_Eng.docx")
    output_file = os.path.join(script_dir, "DanielGutierrezCV_Combined.docx")

    for path in [spanish_cv, english_cv]:
        if not os.path.exists(path):
            print(f"Error: {path} not found!")
            return

    try:
        print("Merging Word documents...")
        print(f"  - Base: {os.path.basename(spanish_cv)}")
        master = Document(spanish_cv)
        composer = Composer(master)

        print(f"  - Appending: {os.path.basename(english_cv)}")
        composer.append(Document(english_cv))

        print(f"Writing merged document to: {output_file}")
        composer.save(output_file)

        print(f"\nSuccessfully merged CVs!")
        print(f"  Output: {output_file}")

    except Exception as e:
        print(f"Error during merge: {e}")


if __name__ == "__main__":
    merge_cv_docx()
