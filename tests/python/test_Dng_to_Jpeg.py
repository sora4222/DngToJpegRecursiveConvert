import pathlib

from python.dngtojpeg import DngToJpeg


def test_dng_to_jpeg_conversion():
    location_of_image: pathlib.PurePath = pathlib.PurePath(__file__) \
        .parents[1].joinpath("resources")

    converter = DngToJpeg(pathlib.Path(location_of_image))

    location_saved = converter._convert_dng(pathlib.Path(location_of_image.joinpath("IMGP2661.DNG")))
    assert str(pathlib.Path(location_of_image.joinpath("IMGP2661.DNG.jpg"))) == location_saved

    pathlib.Path(location_of_image.joinpath("IMGP2661.DNG.jpg")).unlink()


def test_dng_to_jpeg_and_all_folders():
    location_of_image: pathlib.PurePath = pathlib.PurePath(__file__) \
        .parents[1].joinpath("resources")

    converter = DngToJpeg(pathlib.Path(location_of_image))

    converter.convert_all_dngs_to_jpegs()
