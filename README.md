# nba-headshot-downloader
`nba-headshot-downloader` is a package for downloading headshots of all nba players from [the official NBA website](https://www.nba.com/). This package uses ID's from the `nba_api` package to get the latest available photos of NBA players from media day.
# Getting Started
`nba-headshot-downloader` requires Python version 3.8 or higher as well as the `requests` package.
```
pip install nba-headshot-downloader
```
## Downloading Headshots
```python
from nba_headshot_downloader import headshots

headshots.getHeadshotById(2544) # download to root directory
headshots.getHeadshotById(2544, "./assets") # downloads to specified directory
```