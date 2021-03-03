from ..meta import bbmeta
from ..flags import StopExecutionNoRecover

def flt(val):
	try:
		return float(val)
	except:
		return 0

def cint(val):
	try:
		return int(val)
	except:
		return 0

def cmd_unsupported_function(ctx, cmd):
	print("UNSUPPORTED FUNCTION: ", cmd)
	ctx.update({
		"error": "Unsupported command: {}".format(cmd)
	})
	return StopExecutionNoRecover()

@bbmeta(
	description="Logs values",
	inputs=[
		dict(
			dynamic=True,
			type=dict(
				union=["int", "float", "str", "bool", "doc", "undefined"]
			)
		)
	]
)	
def cmd_log(ctx, *args):
	print(*args)