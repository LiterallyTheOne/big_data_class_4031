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

    rdd = rdd.map(lambda x: (x[3], float(x[5]) * float(x[6])))

    rdd = rdd.groupByKey()

    sum_rdd = rdd.mapValues(sum)
    len_rdd = rdd.mapValues(len)  # type: ignore

    result_sum = sum_rdd.collect()
    result_len = len_rdd.collect()

    for x, y in zip(result_sum, result_len):
        print(x[0], x[1] / y[1])


if __name__ == "__main__":
    main()
