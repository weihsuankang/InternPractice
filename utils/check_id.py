import os

from google.cloud import bigquery

def check_id(user_id):
    # simple non parameterized query
    client = bigquery.Client()
    query = """
        SELECT id
        FROM `ikala-cloud-sandbox-sammy.ikala_newbie.staff`
        WHERE id = @id
    """

    query_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("id", "STRING", user_id),
        ]
    )

    query_res = client.query(query, job_config=query_config)  # Make an API request.

    output = {}
    # to print in the console
    for row in query_res:
        output["user_id"] = row.id

    return bool(output)