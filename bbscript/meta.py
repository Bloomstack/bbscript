def bbmeta(inputs, outputs=None, errors=None, description=None):
	def wrapper(fn):
		fn.bbmeta = dict(inputs=inputs, outputs=outputs, errors=errors, description=description)
		return fn

	return wrapper