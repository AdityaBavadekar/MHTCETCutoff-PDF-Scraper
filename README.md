# MHT CET College, Branch, Cutoff PDF Scraper
Extremely simple python script that reads the MHT CET Cap Cutoff PDF and saves the same to `cleaned.json`.

One PDF is provided but anyway the script will work irrespective of the year mentioned on the pdf. If you want to use it with another year's pdf, just change the `TARGET_FILE` in run.py that's it.

To run navigate to this directory in Terminal and execute `python run.py`

## Output (Example):
This is part of the output generated with the provided pdf. Script will generate similar structure for each University mentioned in PDF.
```json
[
  "COEP Technological University": {
    "branches": [
      {
        "branch": "Civil Engineering",
        "cutoff": "98.0804777"
      },
      {
        "branch": "Computer Engineering",
        "cutoff": "99.9145785"
      },
      {
        "branch": "Electrical Engineering",
        "cutoff": "99.2817892"
      },
      {
        "branch": "Electronics and Telecommunication Engg",
        "cutoff": "99.7062307"
      },
      {
        "branch": "Instrumentation and Control Engineering",
        "cutoff": "99.1350380"
      },
      {
        "branch": "Mechanical Engineering",
        "cutoff": "98.8504095"
      },
      {
        "branch": "Manufacturing Science and Engineering",
        "cutoff": "97.6728754"
      },
      {
        "branch": "Metallurgy and Material Technology",
        "cutoff": "96.6135363"
      }
    ]
  },
]
```