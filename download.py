#!/usr/bin/python
#-*- coding: utf-8 -*-

from urllib.parse import urljoin
from pathlib import Path
import requests
import json

from pyquery import PyQuery

__author__ = 'michelecafagna26'

MAX_TRIES = 100

class PascalSentenceDataSet():

    DATASET_DIR = 'images/'
    ANNOTATION_OUTPUT_PATH = "pascal_sentences.json"
    PASCAL_SENTENCE_DATASET_URL = 'http://vision.cs.uiuc.edu/pascal-sentences/'

    def __init__(self):
        self.url = PascalSentenceDataSet.PASCAL_SENTENCE_DATASET_URL

    def annotations(self):
        dom = PyQuery(self.url)

        sentences = {}
        for tr in dom('body>table>tr').items():
            img_src = tr('img').attr['src']
            category, img_file_name = img_src.split("/")
            caps = [td.text() for td in tr('table tr td').items()]

            sentences[img_file_name] = { "category": category,
                                         "captions": caps }

        with open(self.ANNOTATION_OUTPUT_PATH, "w") as fp:
            json.dump(sentences, fp)
        
        print(f"Annotations saved in {self.ANNOTATION_OUTPUT_PATH}")


    def images(self):
        dom = PyQuery(self.url)
        for img in dom('img').items():
            img_src = img.attr['src']
            img_file_name = img_src.split("/")[1]

            # download image
            output = Path(self.DATASET_DIR, img_file_name)

            if img_src.startswith('http'):
                img_url = img_src
            else:
                img_url = urljoin(self.url, img_src)
            if output.is_file():
                print(f"Already downloaded, Skipping: {output}")
                continue
            print(f"Downloading: {output}")
            with open(output,'wb') as f:
                for _ in range(MAX_TRIES):
                    result = requests.get(img_url)
                    raw = result.content
                    if result.status_code == 200:
                        f.write(raw)
                        break
                    print("error occurred while fetching img")
                    print("retry...")

if __name__=="__main__":

    downloader = PascalSentenceDataSet()

    #downloader.images()
    downloader.annotations()
