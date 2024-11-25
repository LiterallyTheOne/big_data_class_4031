"""PySpark example"""

from pyspark import SparkContext


def main():
    """main function"""
    sc = SparkContext("local", "WordCountExample")

    file_path = "pyspark/example.txt"
    rdd = sc.textFile(file_path)

    rdd = rdd.flatMap(lambda x: x.split(" "))
    rdd = rdd.map(lambda x: (x, 1))
    rdd = rdd.reduceByKey(lambda x, y: (x + y))
    result = rdd.collect()
    print(result)

    sc.stop()


if __name__ == "__main__":
    main()
