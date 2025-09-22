# ANVO Scraper (Python Version)

A multi-source animal vocalization scraper that downloads bird and wildlife sound recordings from various online databases with flexible filtering and organized file management.

---

## ✨ Features

- **Multi-source support**: Xeno-Canto, YouTube, Macaulay Library, TBC ...
- **Flexible search**: Common or scientific name
- **Quality filtering**: Source-specific quality ratings (A–E for Xeno-Canto, resolution for YouTube)  
- **Duration limits**: Filter recordings by length  
- **Smart organization**: Automatic directory structure by `source/species/quality`  
- **Progress tracking**: Real-time download progress and summary  
- **Cross-platform**: Works on Windows, macOS, and Linux  
- **Rate limiting**: Respects API limits with built-in delays  

---

## 📂 File Structure

---

## ⚙️ Installation

### Prerequisites
- Python **3.6+**
- Internet connection  

### Dependencies
```bash
pip install requests yt-dlp
```

### Setup
```bash
git clone https://github.com/laelume/anvo.git
```
```bash
cd anvo/utils/scraper
```

### 🚀 Usage
#### Command Line Interface
##### Basic Syntax:
```bash
python scrap.py [SOURCE] [SPECIES] [OPTIONS]
```
### Examples
#### Download 10 A-quality kiwi sounds from Xeno-Canto
```bash
python scrap.py xenocanto "kiwi" -q A -l 10
```
#### Download audio from 5 owl videos on YouTube
```bash
python scrap.py youtube "owl sounds" --quality 720p --limit 5
```
#### Download B-quality robin recordings with no limit on number of recordings (watch out!!)
```bash
python scrap.py xenocanto "robin" -l unlimited -q B
```
#### Download recordings of cardinals with a duration less than 0.5 minutes
```bash
python scrap.py xenocanto "cardinal" -d 0.5
```
#### Scientific name search
```bash
python scrap.py xenocanto "Corvus" -q A -l 20
```
#### Custom organization
```bash
python scrap.py xenocanto "eagle" -o "raptors" -q B
```

#### 🛠️ Help Commands
```bash
python scrap.py --help       # Detailed help
python scrap.py --examples   # Usage examples
python scrap.py --sources    # Available sources
python scrap.py --qualities  # Quality rating info
```

#### 📁 Output Structure
```bash
scraped_sounds/
├── xenocanto/
│   ├── kiwi/A/
│   │   ├── XC123456 - Brown Kiwi - Apteryx mantelli.mp3
│   │   └── XC789012 - Little Spotted Kiwi - Apteryx owenii.mp3
│   └── owl/B/
│       └── XC345678 - Barn Owl - Tyto alba.mp3
├── youtube/
│   └── owl_sounds/720p/
│       └── YT_abc123 - Great Horned Owl Calls.mp3
└── macaulay/
    └── robin/A/
        └── ML456789 - American Robin - Turdus migratorius.mp3
```
