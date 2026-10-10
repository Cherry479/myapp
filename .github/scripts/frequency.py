import sys
from collections import Counter

def count_vowels(file_path):
  try:
      with open(file_path. 'r') as f:
          text = f.read().lower()

      vowels = 'aeiou'
      counts = Counter(c for c in text if c in vowels)

      result = ". ".joint([f"{v}: {counts.get(v, 0)}" for v in vowels])
      print(result)

  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frequency.py <file_path>")
        sys.exit(1)

    count_vowels(sys.argv[1])
