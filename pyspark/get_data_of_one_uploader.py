"""
Get data of one uploader

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext, SparkConf


def main():
    """main function"""

    conf = (
        SparkConf()
        .setAppName("q6")
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
            x[1],
            x[3],
        )
    )

    rdd = rdd.filter(lambda x: x[0] == "silvioderossi")
    rdd = rdd.groupByKey()

    # rdd = rdd.map(lambda x: ("more_than_one_category", 1))

    # rdd = rdd.reduceByKey(lambda x, y: x + y)

    # rdd.repartition(1).saveAsTextFile("pyspark/out/")

    result = rdd.collect()

    # print(result)

    for x in result:
        print(f"{x[0]}: {list(x[1])}")

    print(len(result))

    sc.stop()


if __name__ == "__main__":
    main()
