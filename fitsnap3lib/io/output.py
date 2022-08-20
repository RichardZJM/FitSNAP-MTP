from fitsnap3lib.io.outputs.output_factory import output_factory
from fitsnap3lib.io.input import Config


config = Config()


if __name__.split(".")[-1] == "output":
    #self.config = Config()
    output = output_factory(config.sections["OUTFILE"].output_style)
