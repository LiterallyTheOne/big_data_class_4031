"""PySpark example"""

from pyspark import SparkContext


def main():
    """main function"""
    sc = SparkContext("local", "WordCountExample")

    file_path = "pyspark/example_2.txt"
    rdd = sc.textFile(file_path)

    rdd = rdd.map(lambda x: (x, 1))

    rdd = rdd.reduceByKey(lambda x, y: x + y)
    rdd = rdd.filter(lambda x: x[1] > 1)

    rdd = rdd.map(lambda x: (x[0].split(" ")[0], x[1]))
    rdd = rdd.map(lambda x: (x[0], 1))

    rdd = rdd.reduceByKey(lambda x, y: x + y)

    result = rdd.collect()

    for x in result:
        print(x)

    sc.stop()


if __name__ == "__main__":
    main()
