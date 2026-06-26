def handle_json_error(e, response):
    return {
        "status": "error",
        "message": str(e),
        "raw_response": response
    }