"""sum of all views

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext


def main():
    """main function"""

    sc = SparkContext("local", "WordCountExample")

    file_path = "data/youtube.txt"
    # prepare data
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 9)

    # mapper
    rdd = rdd.map(lambda x: (x[3], int(x[5])))

    rdd = rdd.reduceByKey(lambda x, y: x + y)

    result = rdd.collect()

    for x in result:
        print(x)


if __name__ == "__main__":
    main()
