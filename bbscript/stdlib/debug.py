import re
import pprint

from termcolor import colored
from ..meta import bbmeta

DBUG_PP = pprint.PrettyPrinter(indent=2, depth=2)

def cmd_dbug(ctx, id, cmd, label=None):
	"""
		Parameters:
		-----------
		id:
		cmd:
		label:

		returns: command
	"""
	print(colored("[{}] {}".format(id, label if label else " Debug:"), "yellow", attrs=['bold']))
	for line in cmd:
		print("  ", DBUG_PP.pformat(line))
	return cmd