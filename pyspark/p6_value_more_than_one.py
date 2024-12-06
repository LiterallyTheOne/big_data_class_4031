"""
Sum value more than one
"""

from pyspark import SparkContext


def main():
    """main function"""

    sc = SparkContext("local", "p6")

    # prepare data
    file_path = "pyspark/example_3.txt"
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 1)

    rdd = rdd.map(
        lambda x: (x[0], (int(x[1]), int(x[2]))),
    )

    rdd = rdd.repartition(2)

    rdd = rdd.reduceByKey(
        lambda x, y: (x[0] + y[0], x[1] + y[1]),
    )

    result = rdd.collect()

    for x in result:
        print(x)


if __name__ == "__main__":
    main()
