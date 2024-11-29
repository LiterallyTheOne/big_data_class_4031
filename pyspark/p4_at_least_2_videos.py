"""average views of rate >= 3 and rate < 3

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext


def main():
    """main function"""

    sc = SparkContext("local", "p4")

    # prepare data
    file_path = "data/youtube.txt"
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 6)

    rdd = rdd.map(lambda x: (f"{x[3]}\t{x[1]}", 1))
    rdd = rdd.reduceByKey(lambda x, y: x + y)

    rdd = rdd.filter(lambda x: x[1] > 1)

    rdd = rdd.map(lambda x: (x[0].split("\t")[0], 1))
    rdd = rdd.reduceByKey(lambda x, y: x + y)

    result = rdd.collect()

    for x in result[:20]:
        print(x)


if __name__ == "__main__":
    main()
