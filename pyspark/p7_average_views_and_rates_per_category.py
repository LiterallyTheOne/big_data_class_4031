"""
Average of views and rates per category


0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext


def main():
    """main function"""

    sc = SparkContext("local", "p7")

    # prepare data
    file_path = "data/youtube.txt"
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 6)

    rdd = rdd.map(
        lambda x: (x[3], (int(x[5]), float(x[6]))),
    )

    rdd = rdd.repartition(2)

    rdd_1 = rdd.reduceByKey(
        lambda x, y: (x[0] + y[0], x[1] + y[1]),
    )

    rdd_2 = rdd.groupByKey()
    rdd_2 = rdd_2.mapValues(len)  # type: ignore

    result = rdd_1.collect()
    result_2 = rdd_2.collect()

    for x, y in zip(result, result_2):
        print(
            f"category: {x[0]}\n\t average_view: {x[1][0]/ y[1]}\n\t average_rate: {x[1][1]/ y[1]}"
        )


if __name__ == "__main__":
    main()
