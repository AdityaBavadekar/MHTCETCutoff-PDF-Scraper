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

## Script 2: summarise.py
On execution, the asks the user to enter names of cities seperated with a comma and prints the names of colleges that mention the city in their name.
> ℹ️ Note: It will show colleges that mention the city in their name. It is obvious that some instutites that don't mention the city name will be missed out so be careful.
### Output
Example excution:
```
Enter cities (Delim : ','):
Cities: Pune, Mumbai


****************************************
Pune
****************************************
- TSSMS's Pd. Vasantdada Patil Institute of Technology, Bavdhan, Pune
- Marathwada Mitra Mandal's College of Engineering, Karvenagar, Pune
... MORE WILL BE SHOWN

****************************************
 Mumbai
****************************************
- Institute of Chemical Technology, Mumbai Marathwada off campus, Jalna
- Veermata Jijabai Technological Institute(VJTI), Matunga, Mumbai
... MORE WILL BE SHOWN
```
