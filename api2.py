import requests


access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IlJFRzEyMzQ3IiwibmFtZSI6IkpvaG4gRG9lIiwiZW1haWwiOiJqb2huQGV4YW1wbGUuY29tIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYxMjIzLCJleHAiOjE3NDY5NjIxMjN9.wp2ktnzkYYznzU-hqNi-YVtXwErFX80mlbpbGu5f6KY"


final_sql_query = """
SELECT 
    p.AMOUNT AS SALARY,
    e.FIRST_NAME || ' ' || e.LAST_NAME AS NAME,
    CAST((julianday('2025-05-11') - julianday(e.DOB)) / 365.25 AS INTEGER) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE 
    CAST(strftime('%d', p.PAYMENT_TIME) AS INTEGER) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
""".strip()


url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"


headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

body = {
    "finalQuery": final_sql_query
}

try:
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    print("Query submitted successfully!")
    print("Response:", response.json())
except Exception as e:
    print("Submission failed:", e)
    print("Response content:", response.text)
