from utils.check_id import check_id

from google.cloud import bigquery

def delete(user_id):
    # check if parameter is complete
    if not user_id:
        return "status:failed, \n message:need to enter user_id for completeness"
    # check if user exist
    if check_id(user_id) == False:
        return f"status:failed, \n do not found user {user_id}"

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

    return "status:sucess"