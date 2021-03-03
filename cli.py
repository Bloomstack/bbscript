import click
import ujson
import bbscript
from bbscript.flags import RepeatStatement

def test_input(ctx):
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
	with open(path) as f:
		data = ujson.load(f)
		rt = bbscript.Runtime({
			"input": test_input
		}, data)
		for l in rt.exec():
			pass

@cli.command()
def docs():
	rt = bbscript.Runtime()
	print(rt.docs())

if __name__ == '__main__':
    cli()