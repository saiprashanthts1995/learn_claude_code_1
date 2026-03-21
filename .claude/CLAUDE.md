# Claude Instructions for Sai

## Personal Preferences
- Always address the user as **Sai** in all communications
- Be direct, concise, and action-oriented
- Provide working code with minimal explanation unless asked
- Prioritize practical solutions over theoretical discussions

## PySpark Code Standards

### PEP8 Compliance
- Follow [PEP 8](https://pep8.org/) strictly for all Python code
- Line length: maximum 79 characters (88 for comments)
- Use 4 spaces for indentation (never tabs)
- Two blank lines between top-level definitions
- One blank line between method definitions
- Variable naming: `snake_case` for variables and functions, `PascalCase` for classes
- Import statements: standard library → third-party → local modules
- All imports must be listed alphabetically within groups

### Type Hints & Documentation
- Add type hints to all function signatures
- Use docstrings in Google/NumPy format
- Document parameters, return types, and exceptions
- Include inline comments for complex logic

## PySpark Best Practices

### DataFrame Operations
- Always cache intermediate DataFrames if reused multiple times
- Partition data strategically based on query patterns
- Use columnar operations instead of UDFs when possible
- Broadcast small DataFrames in joins (<200MB)
- Avoid wide transformations (shuffle operations) when unnecessary
- Use `coalesce()` before writing to reduce small files

### Performance Optimization
- Enable adaptive query execution: `spark.sql.adaptive.enabled=true`
- Use dynamic partition pruning for large tables
- Leverage columnar format (Parquet) for storage
- Minimize data shuffling with proper join strategies
- Use bucketing for frequently joined tables
- Profile with Spark UI before optimization

### Memory Management
- Understand executor memory allocation (heap vs overhead)
- Set appropriate `spark.sql.shuffle.partitions` (default 200)
- Use `persist()` with appropriate storage levels
- Clear unused DataFrames with `unpersist()`

## Data Engineering Practices

### File Organization
```
project/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extractors/
│   ├── transformers/
│   ├── loaders/
│   └── utils/
├── tests/
├── requirements.txt
├── setup.py
└── README.md
```

### Configuration Management
- Use external config files (YAML/JSON) for parameters
- Never hardcode credentials or paths
- Support environment-specific configurations
- Use environment variables for sensitive data

### Error Handling
- Implement try-except blocks with specific exceptions
- Log errors with context information
- Gracefully handle empty DataFrames
- Validate input data schema before processing
- Implement retry logic for transient failures

### Testing
- Write unit tests for transformations
- Test edge cases (empty data, nulls, duplicates)
- Use pytest for test framework
- Mock external dependencies
- Aim for 80%+ code coverage

## Code Template Structure

### Minimal PySpark Application
```python
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, when, sum as spark_sum
import logging


def create_spark_session(app_name: str) -> SparkSession:
    """Create and configure Spark session."""
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .getOrCreate()


def extract_data(spark: SparkSession, path: str) -> DataFrame:
    """Extract data from source."""
    return spark.read.parquet(path)


def transform_data(df: DataFrame) -> DataFrame:
    """Apply business logic transformations."""
    return df.filter(col("active") == True) \
        .withColumn("new_col", when(col("value") > 0, col("value")).otherwise(0))


def load_data(df: DataFrame, path: str) -> None:
    """Write transformed data to target."""
    df.coalesce(1) \
        .write \
        .mode("overwrite") \
        .parquet(path)


def main() -> None:
    """Main execution flow."""
    spark = create_spark_session("DataPipeline")
    try:
        df = extract_data(spark, "input/path")
        transformed = transform_data(df)
        load_data(transformed, "output/path")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
```

## Logging Standards
- Use built-in `logging` module
- Set appropriate log levels (DEBUG, INFO, WARNING, ERROR)
- Include contextual information in log messages
- Avoid logging at high frequency in loops

## Git & Version Control
- Commit frequently with descriptive messages
- Include issue numbers in commits
- Use feature branches for new work
- Write meaningful pull request descriptions

## Dependencies
- Pin exact versions in requirements.txt
- Keep dependencies minimal
- Use virtual environments (venv or Poetry)
- Document Python version requirements (3.8+)

## Performance Monitoring
- Use Spark UI (http://localhost:4040) to analyze jobs
- Profile execution plans with `explain()`
- Monitor JVM metrics and garbage collection
- Track job duration and data volumes

---

**Last Updated:** March 2026
**Version:** 1.0
