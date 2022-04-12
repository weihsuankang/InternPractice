import os

from google.cloud import bigquery

def profile(user_id):
    # simple non parameterized query
    client = bigquery.Client()
    query = """
        SELECT id, name, age, category 
        FROM `ikala-cloud-sandbox-sammy.ikala_newbie.staff*` 
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
        output["name"] = row.name
        output["age"] = row.age
        output["category"] = row.category

    if output == {}:
        return f"User_id: {user_id} could not found"
    else:
        return output