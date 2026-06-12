from lambda_function import lambda_handler

event = {
    "name": "Keerthi"
}

output = lambda_handler(event, None)

print(output)
