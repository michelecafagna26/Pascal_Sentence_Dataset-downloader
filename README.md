# Pascal_Sentence_Dataset-downloader
Utility to downlaod the Pascal Sentence Dataset in json-format.

This script is inspired by https://github.com/rupy/PascalSentenceDataset.

## Get started
```
git clone https://github.com/michelecafagna26/Pascal_Sentence_Dataset-downloader.git
```

## Installaton

```
pip install -r requirements.txt
```

## Run

```
python download.py
```

A json file named 'pascal_sentences.json' will be created and the images will be saved in 'images/'

## Data format

```
{"2008_000716.jpg": 
    {"category": "aeroplane", 
    "captions": 
        ["One jet lands at an airport while another takes off next to it.", 
         "Two airplanes parked in an airport.", 
         "Two jets taxi past each other.", 
         "Two parked jet airplanes facing opposite directions.", 
          "two passenger planes on a grassy plain"]
    },
  ...
}
```

## Reference

Pascal Sentence Dataset : https://vision.cs.uiuc.edu/pascal-sentences/

