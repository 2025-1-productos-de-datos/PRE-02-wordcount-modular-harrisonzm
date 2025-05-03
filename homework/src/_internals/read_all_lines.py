import os

import homework.src.utils.data as IO


def read_all_lines(input_folder):
    lines = []
    input_file_list = os.listdir(input_folder)
    for filename in input_file_list:
        filepath = os.path.join(input_folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            lines.extend(lines)
    return lines
