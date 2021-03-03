from ..meta import bbmeta
from .utils import flt, cint

@bbmeta(
	description="Converts any input into an integer",
	inputs=[
		dict(name="val", type=dict(union=["int", "float", "bool", "str"]))
	],
	outputs=dict(
		name="result",
		type="int"
	)
)
def cmd_int(ctx, val):
	return cint(val)

@bbmeta(
	description="Converts any input into an float",
	inputs=[
		dict(name="val", type=dict(union=["int", "float", "bool", "str"]))
	],
	outputs=dict(
		name="result",
		type="float"
	)
)
def cmd_float(ctx, val):
	return flt(val)

@bbmeta(
	description="Converts any input into an string",
	inputs=[
		dict(name="val", type=dict(union=["int", "float", "bool", "str"]))
	],
	outputs=dict(
		name="result",
		type="str"
	)
)
def cmd_string(ctx, val):
	return str(val)

@bbmeta(
	description="Converts any input into an boolean",
	inputs=[
		dict(name="val", type=dict(union=["int", "float", "bool", "str"]))
	],
	outputs=dict(
		name="result",
		type="bool"
	)
)
def cmd_bool(ctx, val):
	return bool(val)

@bbmeta(
	description="Provides an undefined value. Usually used to reset or remove values of objects",
	inputs=[],
	outputs=dict(
		name="result",
		type="undefined"
	)
)
def cmd_undefined(ctx):
	return None