# test_local.py
import json
from functions.get_item import lambda_handler

# Simular el event de API Gateway
mock_event = {
    "httpMethod": "GET",
    "path": "/items/test123",
    "pathParameters": {
        "id": "5"
    },
    "headers": {
        "Content-Type": "application/json"
    },
    "requestContext": {
        "requestId": "test-request-id"
    }
}

mock_context = None  # Context puede ser None para pruebas simples

# Ejecutar la función
try:
    result = lambda_handler(mock_event, mock_context)
    print("✅ Resultado:")
    print(json.dumps(result, indent=2))
except Exception as e:
    print("❌ Error:")
    print(str(e))