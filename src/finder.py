"""
In this file we implement the code in order to find memes, musics, etc...
"""
from pathlib import Path
from uuid import uuid4
from PIL import Image
from bs4 import BeautifulSoup

import requests
import json
import os

class MemeFinder(object):
    """This class finds the trending memes and downloads it"""
    TIMES = ["day", "week", "month", "year"]
    
    def __init__(self, time: str = "week", category: str | None = None, debugging: bool = False):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        
        self.memes_path = Path(__file__).parent / "memes"
        self.memes_path.mkdir(parents=True, exist_ok=True)
        self.db = Path(__file__).parent / "db.json"
        
        time = time if time in self.TIMES else "week"
        if not category or category == "top-memes":
            self.category = "top-memes"
            self.memes_link = f"https://ifunny.co/top-memes/{time}"
        else:
            self.category = category
            self.memes_link = f"https://ifunny.co/{category}?filter=meme"
            if not self.check_page(self.memes_link):
                self.category = "top-memes"
                self.memes_link = f"https://ifunny.co/top-memes/{time}"

        self.known_memes = self.load_from_json()
        self.debugging = debugging

        
    def check_page(self, page: str):
        response = requests.get(page, headers=self.headers)
        return response.status_code == 200
    
    def _download_img(self, src: str):
        response = requests.get(src)
        if response.status_code == 200:
            file_name = src.split('/')[-1]
            path = self.memes_path / f"{file_name}"
            if file_name not in self.known_memes:
                with open(path, 'wb') as f:
                    f.write(response.content)
                self.known_memes.append(file_name.split(".")[0])
                new_path = self.convert2jpg(path)
                return new_path
            else:
                print(f"{file_name} alreafy exists. skipping...")
        return None

    def convert2jpg(self, path: str | Path):
        if not isinstance(path, Path):
            path = Path(path)
        if path.suffix == ".jpg":
            return path
        img = Image.open(path).convert("RGB")
        img.save(f"{path.with_suffix('.jpeg')}", "jpeg")
        os.remove(path)
        return path.with_suffix(".jpeg")

    def get_images_link(self):
        response = requests.get(self.memes_link, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text)
            images = soup.findAll('img')
            data = [{"src": image["data-src"],
                     "alt": image["alt"],
                     "category": self.category} for image in images if image["src"] != '/stub.svg' and image.get("data-src", False)]
            return list(map(self.process_link, data))
        return []
    
    def filter(self, img: dict[str, str]):
        return img["src"].startswith("https://imageproxy.ifunny.co")
    
    def process_link(self, img: dict[str, str]):
        if self.filter(img):
            img["src"] = f"https://imageproxy.ifunny.co/,/user_photos{img['src'].split('user_photos')[-1]}"
        return img

    def get_memes(self):
        links = self.get_images_link()
        for i, img in enumerate(links):
            src = self._download_img(img["src"])
            links[i]["src"] = str(src)
        self.add2db(links)
    
    def add2db(self, imgs: list[dict[str, str]]):
        if self.db.exists():
            with self.db.open("r") as jf:
                db = json.load(jf)
            db.extend(imgs)
            db = self.filter_dict(db)
        else: 
            self.db.touch(exist_ok=True)
            db = imgs
        with self.db.open("w") as jf:
            json.dump(db, 
                      jf,
                      indent=4)
    
    def load_from_json(self):
        if self.db.exists():
            with self.db.open("r") as f:
                data = json.load(f)
                return [dt["src"].split("/")[-1].split(".")[0] for dt in data]
        else:
            return []
    
    def filter_dict(self, jsondb: list[dict[str, str]]):
        return list(
            {
                dictionary['src']: dictionary
                for dictionary in jsondb
            }.values()
        )

            
        
    
if __name__ == "__main__":
    src = "https://img.ifunny.co/images/395acdb80d883fbccba84e2755ea9fa6b7c56db184b953ec17ecc4b5259257cb_1.webp"
    finder = MemeFinder(time="month", category="science-tech")
    links = finder.get_images_link()
    finder.get_memes()    
