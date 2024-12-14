"""
Join

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext, SparkConf


def main():
    """main function"""

    conf = (
        SparkConf()
        .setAppName("p8")
        .set("spark.executor.memory", "4g")
        .set("spark.driver.memory", "4g")
    )

    sc = SparkContext(
        "local",
        conf=conf,
    )

    # prepare data
    file_path = "pyspark/example_3.txt"
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 1)

    rdd_1 = rdd.map(
        lambda x: (
            x[0],
            int(x[1]),
        ),
    )

    rdd_2 = rdd.map(
        lambda x: (
            x[0],
            int(x[2]),
        )
    )

    result = rdd_2.join(rdd_1)
    result = result.distinct()

    result = result.collect()  # type: ignore

    for x in result:
        print(x)

    sc.stop()


if __name__ == "__main__":
    main()
