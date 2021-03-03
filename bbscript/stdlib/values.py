from ..meta import bbmeta
from .utils import flt, cint

def var_resolver(ctx, var, field):
	return "unknown"

@bbmeta(
	description="Returns a variable value or its field value if the variable is a document",
	inputs=[
		dict(
			name="var",
			type="str"
		),
		dict(
			name="field",
			type="str",
			optional=True
		)
	],
	outputs=dict(
		name="result",
		type="dynamic",
		type_resolver=var_resolver
	)
)
def cmd_var(ctx, var, field=None):
	if not field:
		return ctx.get("${}".format(var))
	
	return ctx.get("${}".format(var)).get(field, None)

def cmd_doc(ctx, var, meta=None):
	return ctx.get("${}".format(var))

def cmd_array(ctx, *args):
	return list(args)

@bbmeta(
	inputs=[
		dict(
			name="var",
			type="str"
		),
		dict(
			name="value",
			type=dict(
				union=["int", "float", "bool", "string", "doc"]
			)
		)
	],
	outputs=dict(
		name="result",
		type=dict(
			union=["int", "float", "bool", "string", "doc"],
			match=["value"]
		)
	)
)
def cmd_set(ctx, var, value):
	ctx.update({"${}".format(var): value})
	return value
