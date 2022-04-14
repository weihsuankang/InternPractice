from utils.check_name import check_name

from google.cloud import bigquery

def update(name, age, category):
    # check if parameter is complete
    if not name or not age or not category:
        return "status:failed, \n message:need to enter name, age, category for completeness"
    # check if user exist
    if check_name(name) == False:
        return f"status:failed, \n do not found user {name}"

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

    return "status:sucess"