import os

from google.cloud import bigquery

def update(name, age, category):
    # simple non parameterized query
    client = bigquery.Client()
    query = """
        UPDATE `ikala-cloud-sandbox-sammy.ikala_newbie.staff`
        SET age = @age, category = @category
        WHERE name = @name
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