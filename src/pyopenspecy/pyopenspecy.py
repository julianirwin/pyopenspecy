from importlib.resources import files
import pandas as pd
import pyopenspecy

def random_raman_spectrum():
    metadata = random_raman_metadata()
    df = _raman_data_df()
    return df[df.sample_name == metadata["sample_name"]]


def random_ftir_spectrum():
    metadata = random_ftir_metadata()
    df = _ftir_data_df()
    return df[df.sample_name == metadata["sample_name"]]


def random_ftir_metadata():
    metadata_row = _ftir_metadata_df().sample(n=1)
    return {
        "sample_name": metadata_row.sample_name.iloc[0],
        "spectrum_identity": metadata_row.spectrum_identity.iloc[0],
        "spectrum_id": metadata_row.spectrum_id.iloc[0],
        "other_information": metadata_row.other_information.iloc[0],
    }


def random_raman_metadata():
    metadata_row = _raman_metadata_df().sample(n=1)
    return {
        "sample_name": metadata_row.sample_name.iloc[0],
        "spectrum_identity": metadata_row.spectrum_identity.iloc[0],
        "spectrum_id": metadata_row.spectrum_id.iloc[0],
        "other_information": metadata_row.other_information.iloc[0],
    }


def _raman_data_df():
    data_filepath = files(pyopenspecy) / "data/raman_library.csv"
    return pd.read_csv(data_filepath)


def _ftir_data_df():
    metadata_filepath = files(pyopenspecy) / "data/ftir_library.csv"
    return pd.read_csv(metadata_filepath)


def _raman_metadata_df():
    metadata_filepath = files(pyopenspecy) / "data/raman_metadata.csv"
    return pd.read_csv(metadata_filepath)


def _ftir_metadata_df():
    metadata_filepath = files(pyopenspecy) / "data/ftir_metadata.csv"
    return pd.read_csv(metadata_filepath)


def raman_spectrum_by_id(id):
    df = _raman_data_df()
    return df[df.sample_name == id]


def fuzzy_search_raman():
    pass