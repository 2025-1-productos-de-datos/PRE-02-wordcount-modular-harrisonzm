import os

from homework.src.wordcount import main


def test_migracion():
    if not os.path.exists("data/output/wordcount.tsv"):
        main()

    results = {}
    with open("data/output/wordcount.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            pey, value = line.strip().split("\t")
            results[pey] = value

    assert results.get("computational", 0) == "3"
    assert results.get("analytics", 0) == "5"
