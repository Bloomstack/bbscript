import click
import ujson
import bbscript

@click.group()
def cli():
	pass

@cli.command()
@click.option("--path", help="A bbscript json file to run")
def run(path):
	with open(path) as f:
		data = ujson.load(f)
		bbscript.run(data, {})

if __name__ == '__main__':
    cli()