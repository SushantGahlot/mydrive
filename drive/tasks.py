import logging
import os
from mydrive.celery import app

@app.task
def delete_files(files):
    if files:
        for file in files:
            try:
                os.remove(file)
            except FileExistsError:
                pass