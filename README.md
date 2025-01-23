# Downloads Automation Project

## Overview

A Python script that automatically organizes files from a downloads folder by sorting them into specific directories based on file type.

## Features

- Automatically moves files to designated folders
- Supports multiple file types:
 - Images
 - Videos
 - Audio (differentiates between short SFX and music files)
 - Documents
 - Applications

## Prerequisites

- Python 3.x
- Watchdog library (`pip install watchdog`)

## Setup

1. Clone the repository
2. Install dependencies: `pip install watchdog`
3. Configure file paths in the script
  - Set `source_dir` to your downloads folder
  - Set destination directories for each file type

## Configuration

Modify these variables in the script:
- `source_dir`: Path to your downloads folder
- `dest_dir_sfx`: Directory for short sound files
- `dest_dir_music`: Directory for music files
- `dest_dir_video`: Directory for video files
- `dest_dir_image`: Directory for image files
- `dest_dir_documents`: Directory for document files
- `dest_dir_applications`: Directory for application files

## Usage

Run the script:
```bash
python downloads_automation.py```

The script will continuously monitor the source directory and organize files in real-time.

## Supported File Extensions

* Images: .jpg, .jpeg, .png, .gif, .webp, .svg
* Videos: .webm, .mpg, .mpeg, .mp4, .avi, .wmv, .mov
* Audio: .m4a, .mp3, .wav, .wma, .mid
* Documents: .doc, .docx, .pdf, .xls, .xlsx, .ppt, .pptx
* Applications: .dmg, .exe, .iso

## Logging

The script provides logging information about moved files, including timestamps.

## Notes

* Files with existing names are automatically renamed to avoid overwriting
* Audio files < 25MB are considered SFX, others are moved to music folder
* Uses file extension to determine file type (case-insensitive)
