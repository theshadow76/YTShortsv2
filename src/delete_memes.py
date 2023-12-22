from pathlib import Path

import os

def delete():
    root_path= Path(__file__).parent
    paths = (root_path / "memes").glob("*.*")
    for path in paths:
        os.remove(path)
    if (root_path / "db.json").exists:
        print(f"{root_path / 'db.json'} exists")
        os.remove(root_path / "db.json")
        
if __name__=="__main__":
    delete()