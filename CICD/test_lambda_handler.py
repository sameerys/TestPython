import unittest
import json
import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CICD.lambda_handler import lambda_handler


class TestLambdaHandler(unittest.TestCase):
    """Integration tests for Lambda handler function."""

    def setUp(self):
        """Set up test context."""
        self.context = type('Context', (), {
            'function_name': 'test-prime-checker',
            'memory_limit_in_mb': 128,
            'invoked_function_arn': 'arn:aws:lambda:us-east-1:123456789012:function:test-prime-checker',
            'aws_request_id': 'test-request-id-123'
        })()

    def create_api_gateway_event(self, body):
        """Helper method to create API Gateway event structure."""
        return {
            'httpMethod': 'POST',
            'path': '/prime',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(body) if isinstance(body, dict) else body,
            'isBase64Encoded': False
        }

    def test_prime_number_17(self):
        """Test with a prime number (17)."""
        event = self.create_api_gateway_event({'number': 17})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['number'], 17)
        self.assertTrue(body['is_prime'])

    def test_composite_number_100(self):
        """Test with a composite number (100)."""
        event = self.create_api_gateway_event({'number': 100})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertEqual(body['number'], 100)
        self.assertFalse(body['is_prime'])

    def test_edge_case_zero(self):
        """Test with zero."""
        event = self.create_api_gateway_event({'number': 0})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertFalse(body['is_prime'])

    def test_edge_case_one(self):
        """Test with one."""
        event = self.create_api_gateway_event({'number': 1})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertFalse(body['is_prime'])

    def test_edge_case_two(self):
        """Test with two (smallest prime)."""
        event = self.create_api_gateway_event({'number': 2})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertTrue(body['is_prime'])

    def test_negative_number(self):
        """Test with a negative number."""
        event = self.create_api_gateway_event({'number': -5})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertFalse(body['is_prime'])

    def test_large_prime(self):
        """Test with a larger prime number (997)."""
        event = self.create_api_gateway_event({'number': 997})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 200)
        body = json.loads(response['body'])
        self.assertTrue(body['is_prime'])

    def test_missing_number_field(self):
        """Test with missing 'number' field in request."""
        event = self.create_api_gateway_event({'value': 17})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)
        self.assertIn('number', body['error'].lower())

    def test_invalid_json(self):
        """Test with invalid JSON in request body."""
        event = {
            'httpMethod': 'POST',
            'path': '/prime',
            'headers': {'Content-Type': 'application/json'},
            'body': '{invalid json}',
            'isBase64Encoded': False
        }
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_string_input(self):
        """Test with string input instead of integer."""
        event = self.create_api_gateway_event({'number': '17'})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_float_input(self):
        """Test with float input instead of integer."""
        event = self.create_api_gateway_event({'number': 17.5})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_boolean_input(self):
        """Test with boolean input (should be rejected)."""
        event = self.create_api_gateway_event({'number': True})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_null_input(self):
        """Test with null input."""
        event = self.create_api_gateway_event({'number': None})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_missing_body(self):
        """Test with missing request body."""
        event = {
            'httpMethod': 'POST',
            'path': '/prime',
            'headers': {'Content-Type': 'application/json'},
            'isBase64Encoded': False
        }
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_response_has_cors_headers(self):
        """Test that response includes CORS headers."""
        event = self.create_api_gateway_event({'number': 17})
        response = lambda_handler(event, self.context)

        self.assertIn('headers', response)
        self.assertIn('Access-Control-Allow-Origin', response['headers'])
        self.assertIn('Content-Type', response['headers'])
        self.assertEqual(response['headers']['Content-Type'], 'application/json')

    def test_response_structure(self):
        """Test that successful response has correct structure."""
        event = self.create_api_gateway_event({'number': 17})
        response = lambda_handler(event, self.context)

        # Check response structure
        self.assertIn('statusCode', response)
        self.assertIn('headers', response)
        self.assertIn('body', response)

        # Check body structure
        body = json.loads(response['body'])
        self.assertIn('number', body)
        self.assertIn('is_prime', body)
        self.assertIsInstance(body['is_prime'], bool)

    def test_very_large_number(self):
        """Test with a very large number (should handle ValueError)."""
        event = self.create_api_gateway_event({'number': 10**100})
        response = lambda_handler(event, self.context)

        # Should either succeed or return 400 with error
        self.assertIn(response['statusCode'], [200, 400])

    def test_array_input(self):
        """Test with array input instead of number."""
        event = self.create_api_gateway_event({'number': [17]})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)

    def test_object_input(self):
        """Test with object input instead of number."""
        event = self.create_api_gateway_event({'number': {'value': 17}})
        response = lambda_handler(event, self.context)

        self.assertEqual(response['statusCode'], 400)
        body = json.loads(response['body'])
        self.assertIn('error', body)


if __name__ == '__main__':
    unittest.main()
