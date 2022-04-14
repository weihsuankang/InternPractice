from utils.check_id import check_id

from google.cloud import bigquery

def profile(user_id):
    # check if parameter is complete
    if not user_id:
        return "status:failed, \n message:need to enter user_id(STRING) for completeness"
    # check if user exist
    if check_id(user_id) == False:
        return f"status:failed, \n do not found user {user_id}"

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

    return output