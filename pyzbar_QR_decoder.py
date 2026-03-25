#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from pyzbar.pyzbar import decode as pyZbarDecode

from PIL import Image

import cooked_input as ci

from sys import stdin
from pathlib import Path

from logzero import logger
from logzero import formatter as logzero_formatter
from logzero import setup_default_logger as logzero_sdf

from tkinter import filedialog as tkFileDialog
from tkinter import Tk as Tk
from urllib.parse import unquote
import base64

my_formatter = logzero_formatter(formatter="%Y-%m-%d %H:%M:%S %z")
logzero_sdf(formatter=my_formatter)

def test_base64_functionality():
    base64_string = " R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")

    print(f"Decoded string: {sample_string}")


def main():
    startdir = False
    while not startdir:  # sourcery skip
        if stdin.isatty():
            startdir = ci.get_string(
                prompt="Enter Starting Path, ** to exit: ",
                default=Path(r"~\Downloads").expanduser(),
            )
        else:
            startdir = tkFileDialog.askdirectory(
                title="Default Directory for Processing Files...",
                initialdir=r"~\Downloads",
                mustexist=True,
            )
        if "**" in startdir:
            startdir = False
            return startdir
        startPath = Path(startdir)
        if not startPath.is_dir():
            startdir = False
            return startdir
    else:
        ...
        logger.debug("Else in while reached.")
    logger.debug("Exited while.")
    if not startdir:
        return False
    imageName = tkFileDialog.askopenfilename()
    if not imageName:
        return False
    img = Image.open(imageName)
    decodedData = pyZbarDecode(img)
    logger.debug(f"{decodedData=}")
    for result in decodedData:
        attempt = result.data.decode("utf-8")
        logger.debug(f"{attempt=}")

        attempt = unquote(attempt)
        logger.debug(attempt)
        google_auth_bkup = "otpauth-migration://offline?data="
        prefix_attempt = attempt.removeprefix(google_auth_bkup)
        if prefix_attempt != attempt:
            b64_attempt = prefix_attempt.encode("utf-8")
            logger.debug(F"{b64_attempt=}")
            logger.debug(F"{base64.b64decode(b64_attempt)=}")
    return True


if __name__ == "__main__":
    nextRun = True
    if not stdin.isatty():
        root = Tk()
        #    root.hide()
        #    root.iconify()
        root.withdraw()
        while nextRun:
            nextRun = main()
            ...
        root.destroy()
        #    root.update()
        #    root.deiconify()
    else:
        while nextRun:
            nextRun = main()
            ...
