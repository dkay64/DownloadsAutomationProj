# -*- coding: utf-8 -*-
"""DownloadsAutomationProject

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M1rPIbCeA-PR9zLk5bAHMA4H_2ey_IeS
"""

# File uplaoded from local (some file paths not specified)

#!pip install watchdog

import os
from os import scandir, rename

from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import shutil

source_dir = "" # specify source filepath

dest_dir_sfx = "" # filepath for SFX sounds (not long songs or music/audio files)
dest_dir_music = "" # filepath for long songs/music/audio files
dest_dir_video = "" # filepath for videos
dest_dir_image = "" # filepath for images
dest_dir_documents = "" # filepath for documents
dest_dir_applications = "" # filepath for applications

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".svgz"]
video_extensions = [".webm", ".mpg", ".mpeg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov"]
audio_extensions = [".m4a", "mp3", ".wav", ".wma", ".mid", ".midi"]
document_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".html", ".tex", ".log"]
application_extensions = [".dmg", ".exe", ".iso"]

def makeUnique(dest, name):
    filename, extension = os.splitext(name)
    counter = 1
    exists = os.exists(f"{dest}/{name}")
    while exists:
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move(dest, entry, name):
    fileExists = os.path.exists(dest + "/" + name)
    if fileExists:
        uniqueName = makeUnique(name)
        os.rename(entry, uniqueName)
    shutil.move(entry, dest)

class MovingEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_image_files(entry, name)
                self.check_video_files(entry, name)
                self.check_audio_files(entry, name)
                self.check_document_files(entry, name)
                self.check_application_files(entry, name)

    def check_image_files(self, entry, name):
        for imageExtens in image_extensions:
            if name.endswith(imageExtens) or name.endswith(imageExtens.upper()):
                move(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_video_files(self, entry, name):
        for videoExtens in video_extensions:
            if name.endswith(videoExtens) or name.endswith(videoExtens.upper()):
                move(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_audio_files(self, entry, name):
        for audioExtens in audio_extensions:
            if name.endswith(audioExtens) or name.endswith(audioExtens.upper()):
                if entry.stat().st_size < 25000000 or "SFX" in name:
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_document_files(self, entry, name):
        for documentExtens in document_extensions:
            if name.endswith(documentExtens) or name.endswith(documentExtens.upper()):
                move(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_application_files(self, entry, name):
        for applicationExtens in document_extensions:
            if name.endswith(applicationExtens) or name.endswith(applicationExtens.upper()):
                move(dest_dir_applications, entry, name)
                logging.info(f"Moved application file: {name}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MovingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()