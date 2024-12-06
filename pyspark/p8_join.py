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
    file_path = "data/youtube.txt"
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 6)

    rdd = rdd.filter(lambda x: x[3].strip() == "Entertainment")

    rdd_1 = rdd.map(
        lambda x: (
            x[3],
            (
                int(x[5]),
                float(x[6]),
            ),
        ),
    )

    rdd_2 = rdd.map(
        lambda x: (
            x[3],
            (
                int(x[2]),
                int(x[8]),
            ),
        )
    )

    result = rdd_2.leftOuterJoin(rdd_1)

    result = result.top(10)  # type: ignore

    for x in result:
        print(x)

    sc.stop()


if __name__ == "__main__":
    main()
