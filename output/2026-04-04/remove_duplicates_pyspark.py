from pyspark.sql import SparkSession

def fn_removeDuplicates(df):
    """Remove duplicates from a PySpark DataFrame.

    Args:
        df: PySpark DataFrame

    Returns:
        PySpark DataFrame with duplicates removed
    """
    return df.dropDuplicates()


def fn_removeDuplicatesSubset(df, subset_cols):
    """Remove duplicates based on specific columns.

    Args:
        df: PySpark DataFrame
        subset_cols: List of column names to consider for duplicates

    Returns:
        PySpark DataFrame with duplicates removed based on subset columns
    """
    return df.dropDuplicates(subset_cols)


if __name__ == "__main__":
    # Create SparkSession
    spark = SparkSession.builder.appName("RemoveDuplicates").getOrCreate()

    # Sample data with duplicates
    data = [
        ("John", 25, "Engineer"),
        ("Jane", 30, "Manager"),
        ("John", 25, "Engineer"),  # Duplicate
        ("Bob", 28, "Analyst"),
        ("Jane", 30, "Manager"),   # Duplicate
    ]

    columns = ["name", "age", "position"]
    df = spark.createDataFrame(data, columns)

    print("Original DataFrame:")
    df.show()

    print("\nAfter removing all duplicates:")
    df_no_duplicates = fn_removeDuplicates(df)
    df_no_duplicates.show()

    print("\nAfter removing duplicates based on 'name' column only:")
    df_no_duplicates_name = fn_removeDuplicatesSubset(df, ["name"])
    df_no_duplicates_name.show()

    spark.stop()
