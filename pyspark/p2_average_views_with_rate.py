"""average views of rate >= 3 and rate < 3

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext


def main():
    """main function"""

    sc = SparkContext("local", "p2")

    file_path = "data/youtube.txt"
    # prepare data
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 6)

    # mapper
    rdd = rdd.map(lambda x: (float(x[6]), int(x[5])))

    above_3 = rdd.filter(lambda x: x[0] >= 3)
    above_3 = above_3.map(lambda x: x[1])

    below_3 = rdd.filter(lambda x: x[0] < 3)
    below_3 = below_3.map(lambda x: x[1])

    result_above_3 = above_3.sum() / above_3.count()
    result_below_3 = below_3.sum() / below_3.count()

    above_3 = above_3.collect()

    print(result_above_3)
    print(result_below_3)


if __name__ == "__main__":
    main()
