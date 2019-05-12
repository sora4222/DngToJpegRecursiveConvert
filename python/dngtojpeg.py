"""
This uses a location to recursively enter subdirectories and find all
the DNG files and converting them to a JPEG.
"""
import logging
from pathlib import Path
from typing import Union

import numpy as np
import rawpy
from PIL import Image

from python.config.yaml import Config


class DngToJpeg():
    def __init__(self, location: Union[Path, str]):
        self.root_location: Path = Path(location)

    def convert_all_dngs_to_jpegs(self) -> None:
        """
        This will recursively convert all jpeg files located underneath the root
        directory to dng files leaving the remaining dng files
        :return:
        """
        subdirectory_or_file: Path
        for subdirectory_or_file in self.root_location.rglob("*"):
            if subdirectory_or_file.is_dir() or subdirectory_or_file.suffix.lower() != ".dng":
                continue
            location_of_file = self._convert_dng(subdirectory_or_file)
            if location_of_file:
                logging.info(f"Saved image {location_of_file}")
            else:
                logging.warning(f"An image has not saved: {subdirectory_or_file.resolve()}")

    def _convert_dng(self, file: Path) -> Union[bool, str]:
        """
        Converts a single DNG file and saves it to
        a jpeg file
        :param file: The path to the file to be converted.
        :return:
        """
        try:
            with rawpy.imread(str(file.resolve())) as dng_file:
                image_unprocessed: np.ndarray = dng_file.postprocess()

                # Convert to PIL image
                image = Image.fromarray(image_unprocessed)
                image_reshaped = image.resize((image.size[0] // 4, image.size[1] // 4))
                location_to_save = str(self.root_location.joinpath(file.name)) + ".jpg"
                image_reshaped.save(location_to_save, format="JPEG", quality=73)
                return location_to_save
        except FileNotFoundError or FileExistsError:
            return False


if __name__ == '__main__':
    config = Config("config.yaml")
    dng_to_jpeg = DngToJpeg(config.get_root_location())
    dng_to_jpeg.convert_all_dngs_to_jpegs()
