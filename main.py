"""The Excuse That Almost Works — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The excuse: car broke down, mechanic says Friday — and Vice City sends its regards.
TEXT = "Boss, my car broke down on the way in. The mechanic says Friday, maybe. Vice City sends its regards."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
