import os

from google.cloud import bigquery

def insert(name, age, category):
    # simple non parameterized query
    client = bigquery.Client()
    query = """
        INSERT INTO `ikala-cloud-sandbox-sammy.ikala_newbie.staff`
        VALUES(88, @name, @age, @category, "2023-01-02")
    """

    query_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("name", "STRING", name),
            bigquery.ScalarQueryParameter("age", "INTEGER", age),
            bigquery.ScalarQueryParameter("category", "STRING", category),
        ]
    )

    query_res = client.query(query, job_config=query_config)  # Make an API request.

    return "done"