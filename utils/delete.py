import os

from google.cloud import bigquery

def delete(user_id):
    # simple non parameterized query
    client = bigquery.Client()
    query = """
        DELETE FROM `ikala-cloud-sandbox-sammy.ikala_newbie.staff`
        WHERE id = @id
    """

    query_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("id", "STRING", user_id),
        ]
    )

    query_res = client.query(query, job_config=query_config)  # Make an API request.

    return "done"