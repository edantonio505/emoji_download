# emoji_download
Emoji download is a script that will automate the task of downloading emojis (gif, png, jpg) images onto your local computer. The emojis can be uploaded to the slack channel to make your slack conversations more fun!. 

The emojis are being downloaded from 2 sources: *https://emojipacks.com* and *https://slackmojis.com/*


### Prerequisites

* [Python3](https://www.python.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/en/master/)


### Usage
```

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source 1 'slackmojis.com', source 2 'emojipacks.com'.
                        Default 1
  -c CATEGORY, --category CATEGORY
                        Enter any category from Emojipacks
                        https://emojipacks.com/packs/${CATEGORY}. This option
                        only works with source 2.

```


### Examples
To download emojis from *https://slackmojis.com* use this command.
* `python get_emojis.py -s 1`

To download specific emojis with a category option from *https://emojipacks.com* use this option. The CATEGORY option can be found by navigating to the emojicpacks url and clicking on any of the categories shown on the landing page. "emojipacks.com/packs/[CATEGORY]"
* `python get_emojis.py -s 2 -c rick-and-morty`
