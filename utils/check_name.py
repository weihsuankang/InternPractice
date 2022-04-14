import os

from google.cloud import bigquery

def check_name(name):
    # simple non parameterized query
    client = bigquery.Client()
    query = """
        SELECT name
        FROM `ikala-cloud-sandbox-sammy.ikala_newbie.staff`
        WHERE name = @name
    """

    query_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("name", "STRING", name),
        ]
    )

    query_res = client.query(query, job_config=query_config)  # Make an API request.

    output = {}
    # to print in the console
    for row in query_res:
        output["name"] = row.name

    return bool(output)