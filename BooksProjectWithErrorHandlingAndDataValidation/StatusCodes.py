# Status Codes

# What are Status Codes ?

# An HTTP Status Code is used to help the Client (the user or the
# system submitting data to the server) to understand what happened
# on the server side application.

# Status Codes:

# 1xx =============> Information Response: Request Processing.
# 2xx =============> Success: Request successfully complete.
# 3xx =============> Redirection: Further action must be complete.
# 4xx =============> Client Errors: An error was caused by the client.
# 5xx =============> Server Errors: An error occurred on the server.

# 2xx Successful Status Codes:

# 200: OK =========================> It is a standard response for a successful
# request. It is commonly used for successful GET requests when the data is
# being returned.

# 201: Created =====================> The request has been successful, which
# creates a new resource. It is used when a POST request creates an entity.


# 204: No Content ==================> The request has been successful, did not
# create an entity nor return anything. It is commonly used with POST requests.

# 4xx Client Errors Status Codes:

# 400: Bad Request ====> The request cannot be processed due to the client error.
# It is commonly used for invalid request methods.

# 401: Unauthorized =====> Client does not have valid authentication for the
# target resource.

# 404: Not Found =====> The clients requested resource can not be found.

# 422: Unprocessable Entity =====> Semantic Errors in the Client Errors (ex: Parameter
# Validation Errors and Field Validation Errors)

# 5xx Server Errors Status Codes:

# 500: Internal Server Error =====> This is a generic error message. It
# appears when an unexpected issue on the server happened.
