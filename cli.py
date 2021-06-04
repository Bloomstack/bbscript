import click
import ujson
import bbscript
from bbscript.flags import RepeatStatement

def test_input(ctx):
	"""
		To get custom user input!
		input: Yes/No
		
		If yes
		it stores value in user_input of context
				
	"""
	if ctx.get("user_input"):
		print("We got: ", ctx.get("user_input"))
		return

	val = input("Say yes: ")
	if val == "yes":
		ctx["user_input"] = val
	
	return RepeatStatement()

@click.group()
def cli():
	pass

@cli.command()
@click.option("--path", help="A bbscript json file to run")
def run(path):
	"""
		Runs as main function:
		input: it takes json file as input
	"""
	with open(path) as f:
		data = ujson.load(f)
		rt = bbscript.Runtime({
			"input": test_input
		}, data)
		for l in rt.exec():
			pass

@cli.command()
def docs():
	"""
		It creates a document of the runtime
	"""
	rt = bbscript.Runtime()
	print(rt.docs())

if __name__ == '__main__':
    cli()