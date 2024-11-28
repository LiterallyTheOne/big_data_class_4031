# Install Pyspark

To install `PySpark` with `conda` we can use the steps below:

## Create a conda environment

First we need to create an virtual environment and activate it.

```shell
conda create --name pyspark_312 python=3.12
conda activate pyspark_312

```

## Install OpenJDK on conda environment

Then we sould have a running `Java` in our machine.
If you don't have, we can install it on our `conda environment`
with the code below:

```shell
conda install conda-forge::openjdk
```

## Install Pyspark

There are different verions of `Pyspark`,
but we need the standard version of it becasue
we are not connecting to `SQL` or `HDFS`.

```shell
pip install pyspark
```

**_NOTE:_** to see the full list of options you can see this [link](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)   

## Install psutil (optional)

To enhance the performance of `PySpark` you can isntall
`psutil`

```shell
pip install psutil
```

## Example

Here is an code as an example (example_1.py):

```py
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

```

If the content of `pyspark/example.txt` would be like below:

```text
apple orange
orange banana
apple grape
orange peach
```

the output of this code would be:

```text
[('apple', 2), ('orange', 3), ('banana', 1), ('grape', 1), ('peach', 1)]
```
