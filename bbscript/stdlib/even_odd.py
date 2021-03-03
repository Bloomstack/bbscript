from ..meta import bbmeta
from .utils import flt

@bbmeta(
	description="Returns true when the value provided is an even number, else false.",
	inputs=[
		dict(name="val", type=dict(union=["int", "float"]))
	], 
	outputs=dict(name="result", type="boolean")
)
def cmd_is_even(ctx, val):
	return flt(val) % 2 == 0

@bbmeta(
	description="Returns true when the value provided is an odd number, else false.",
	inputs=[
		dict(name="val", type=dict(union=["int", "float"]))
	], 
	outputs=dict(name="result", type="boolean")
)
def cmd_is_odd(ctx, val):
	return flt(val) % 2 != 0
