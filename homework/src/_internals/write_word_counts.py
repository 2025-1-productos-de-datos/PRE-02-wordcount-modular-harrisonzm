import os

import homework.src.utils.data as IO


def write_count_words(counter, output_folder):
    # create the directory output/ if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_name = "wordcount.tsv"
    file_path = os.path.join(IO.data_output, output_name)
    # save the results using tsv format
    with open(file_path, "w", encoding="utf-8") as f:
        for word, count in counter.items():
            # write the word and count to the file
            f.write(f"{word}\t{count}\n")
