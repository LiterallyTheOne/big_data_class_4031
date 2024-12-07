"""Count of being referenced

0  | 1        | 2   | 3        | 4      | 5     | 6    | 7       | 8        | 9
id | uploader | age | category | length | views | rate | ratings | comments | related_ids

"""

from pyspark import SparkContext


def mapper(x):
    """mapper

    :param x: _description_
    :type x: _type_
    :return: _description_
    :rtype: _type_
    """
    result = []
    for r in x[9:]:
        result.append((r, x[0]))

    return result


def main():
    """main function"""

    sc = SparkContext("local", "p3")

    file_path = "data/youtube.txt"
    # prepare data
    rdd = sc.textFile(file_path)
    rdd = rdd.map(lambda x: x.split("\t"))
    rdd = rdd.filter(lambda x: len(x) > 9)

    # mapper
    rdd = rdd.flatMap(mapper)
    rdd = rdd.groupByKey()

    rdd = rdd.mapValues(len)  # type: ignore
    rdd = rdd.sortBy(lambda x: x[1], ascending=False)  # type: ignore

    result = rdd.collect()

    print(result[:20])

    # for x in result[:20]:
    #     print(x[0], end="\t")
    #     for y in x[1]:
    #         print(y, end="\t")

    #     print()


if __name__ == "__main__":
    main()
