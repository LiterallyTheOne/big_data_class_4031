"""Entertainment videos with more than 90 days of age,
and show top 10 data with the most views.


0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext


def main():
    """main function"""

    sc = SparkContext("local", "q5")

    # prepare data
    file_path = "data/youtube.txt"
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 6)

    rdd_1 = rdd.filter(lambda x: x[3].strip() == "Entertainment")
    rdd_1 = rdd_1.filter(lambda x: float(x[2]) > 90)
    rdd_1 = rdd_1.map(lambda x: float(x[6]))
    result_1 = rdd_1.max()  # type: ignore

    print(result_1)

    rdd_2 = rdd.map(lambda x: (int(x[5]), x[1]))

    result_2 = rdd_2.top(10)  # type: ignore

    for x in result_2:
        print(x)


if __name__ == "__main__":
    main()
