"""
Script to merge English and Spanish CV PDFs into a single document.
"""
from PyPDF2 import PdfMerger
import os

def merge_cv_pdfs():
    """Merge English and Spanish CV PDFs into a single file."""
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define input files
    english_cv = os.path.join(script_dir, "DanielGutierrezCVEng.pdf")
    spanish_cv = os.path.join(script_dir, "DanielGutierrezCVEsp.pdf")
    
    # Define output file
    output_file = os.path.join(script_dir, "DanielGutierrezCV_Combined.pdf")
    
    # Check if input files exist
    if not os.path.exists(english_cv):
        print(f"Error: {english_cv} not found!")
        return
    
    if not os.path.exists(spanish_cv):
        print(f"Error: {spanish_cv} not found!")
        return
    
    # Create PDF merger
    merger = PdfMerger()
    
    try:
        print("Merging PDFs...")
        print(f"  - Adding: {os.path.basename(english_cv)}")
        merger.append(english_cv)
        
        print(f"  - Adding: {os.path.basename(spanish_cv)}")
        merger.append(spanish_cv)
        
        # Write merged PDF
        print(f"Writing merged PDF to: {output_file}")
        merger.write(output_file)
        merger.close()
        
        print(f"\n✓ Successfully merged CVs!")
        print(f"  Output: {output_file}")
        
    except Exception as e:
        print(f"Error during merge: {e}")
        merger.close()

if __name__ == "__main__":
    merge_cv_pdfs()
