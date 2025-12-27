import os
import shutil
import sys

def make_pack(series_name):
    # This is a stub for the packaging logic.
    # In a full version, this would zip up the 'out' folder and include the README.
    print(f"Packaging series: {series_name}...")
    # ... logic to zip files ...
    print("Done. (Stub)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python make_prompt_pack.py <series_name>")
        sys.exit(1)
    make_pack(sys.argv[1])
