from pandas import read_csv
from format import clean_str, shuffle_both


def read_train_data(file_name, x_col, y_col, separator='\t', with_cleaning=True, with_header=False, with_shuffle=True):
    with open(file_name) as pos_src:
        if not with_header:
            # skips 0-th row, because it contains only header
            out = read_csv(pos_src, sep=separator, skiprows=[0], header=None)
        else:
            out = read_csv(pos_src, sep=separator, header=None)

    x_text = _read_unicode_lines(out[x_col].tolist(), with_cleaning)
    y_text = out[y_col].tolist()

    if with_shuffle:
        return shuffle_both(x_text, y_text)
    else:
        return x_text, y_text


def read_test_data(file_name, x_col, with_cleaning=True):
    x_text = read_csv(file_name, skiprows=[0], header=None)

    return _read_unicode_lines(x_text[x_col], with_cleaning)


def _read_unicode_lines(lines, with_cleaning=True):
    if with_cleaning:
        return [clean_str(sentence.decode('utf-8')) for sentence in lines]
    else:
        return [sentence.decode('utf-8') for sentence in lines]
