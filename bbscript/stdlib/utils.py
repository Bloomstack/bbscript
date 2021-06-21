from ..meta import bbmeta
from ..flags import StopExecutionNoRecover

def flt(val):
	"""
		Returns
		-------
			returns a float value
	"""
	try:
		return float(val)
	except:
		return float(0)

def cint(val):
	"""
		Returns
		-------
			returns an int value
	"""
	try:
		return int(val)
	except:
		return int(0)

def cmd_unsupported_function(ctx, cmd):
	"""
		To validate unsupported commands
	"""
	ctx.update({
		"$error": "Unsupported command: {}".format(cmd)
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
	"""
		logs the args
	"""
	print(*args)