import math
from ..meta import bbmeta
from ..errors import InvalidOperation
from .utils import flt, cint
from jsonschema import validate


schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/product.schema.json",
  "title": "Math",
  "type": "object",
  "properties": {
    "op": {
      "description": "Math Operation to perform",
      "type": "string",
    },
    "left": {
      "description": "left value of the operation",
      "type": "number"
    },
	"right": {
      "description": "left value of the operation",
      "type": "number"
    }
  },
  "required": [ "op", "left", "right" ]
}
def cmd_math(ctx, op: str, left, right):
	"""
			To perform math operations.

			Parameters:
			-----------
			op: Math operation to perform
			left: left value
			right: right value

			Returns:
			--------
			value of the left and right parameter with respect to the op.

	"""
	try:
		math_json = {
			"op": op,
			"left": left, 
			"right": right,
		}
		validate(instance=math_json, schema=schema)
		type_fn = flt
		if isinstance(left, int):
			type_fn = cint
			left = type_fn(left)
		if isinstance(right, int):
			type_fn = cint
			right = type_fn(right)


		if op == "+":
			return left + right
		elif op == "-":
			return left - right
		elif op == "*":
			return left * right
		elif op == "/":
			return left / right
		elif op == "%":
			return left * (right / 100)
		elif op == "MOD":
			return math.fmod(left, right)
		elif op == "WRAP":
			return left % right

		raise InvalidOperation("op must be one of +, -, *, /, %, MOD")

	except Exception as err:
		raise ValueError(err)
