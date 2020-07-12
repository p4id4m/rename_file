import os
from dotenv import load_dotenv

load_dotenv()
FOLDER = os.getenv("FOLDER")

def main():
    # If more key phrases are needed add them to this list
    key_phrases = ["%20", "%27", "%5"]
    for (_root, _dirs, files) in os.walk(FOLDER):
        for file in files:
            if file.endswith(".pdf"):
                for key in key_phrases:
                    if key in file:
                        os.rename(file, file.replace(key, "_"))
                        print(file)

if __name__ == "__main__":
    main()
