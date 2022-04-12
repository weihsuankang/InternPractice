import os

from google.cloud import bigquery

def insert(name, age, category):
    # simple non parameterized query
    client = bigquery.Client()
    query = """
        INSERT INTO `ikala-cloud-sandbox-sammy.ikala_newbie.staff`
        VALUES(GENERATE_UUID(), @name, @age, @category, CURRENT_DATETIME())
    """

    query_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("name", "STRING", name),
            bigquery.ScalarQueryParameter("age", "INTEGER", age),
            bigquery.ScalarQueryParameter("category", "STRING", category),
        ]
    )

    query_res = client.query(query, job_config=query_config)  # Make an API request.

    output = {}
    for row in query_res:
        output["name"] = row.name
        output["age"] = row.age
        output["category"] = row.category

    return output