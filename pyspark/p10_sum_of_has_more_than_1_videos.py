"""
Sum of has more than 1 videos

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

    rdd = rdd.map(
        lambda x: (
            (
                x[3],
                x[1],
            ),
            1,
        )
    )

    rdd = rdd.groupByKey()
    rdd = rdd.mapValues(sum)

    rdd = rdd.filter(lambda x: x[1] > 1)

    rdd = rdd.map(lambda x: (x[0][0], x[0][1]))
    rdd = rdd.groupByKey()
    rdd = rdd.mapValues(len)  # type: ignore

    result = rdd.collect()

    for x in result:
        print(x)

    sc.stop()


if __name__ == "__main__":
    main()
