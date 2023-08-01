#!/usr/bin/env python3

import argparse
import sys
from typing import Sequence
from xdsl.dialects import gpu

from xdsl.interpreters.experimental.wgsl_printer import WGSLPrinter
from xdsl.ir import MLContext
from xdsl.tools.command_line_tool import CommandLineTool


class WGSLTranslate(CommandLineTool):
    def __init__(
        self,
        description: str = "xDSL WGSL translation demo tool",
        args: Sequence[str] | None = None,
    ):
        self.available_frontends = {}

        self.ctx = MLContext()
        self.register_all_dialects()
        self.register_all_frontends()
        # arg handling
        arg_parser = argparse.ArgumentParser(description=description)
        self.register_all_arguments(arg_parser)
        self.args = arg_parser.parse_args(args=args)

        self.ctx.allow_unregistered = self.args.allow_unregistered_dialect

    def run(self):
        input, file_extension = self.get_input_stream()
        try:
            module = self.parse_chunk(input, file_extension)
            if module is not None:
                module.verify()
                printer = WGSLPrinter()
                for op in module.ops:
                    if isinstance(op, gpu.ModuleOp):
                        printer.print(op, sys.stdout)
        finally:
            if input is not sys.stdin:
                input.close()


def main():
    return WGSLTranslate().run()


if __name__ == "__main__":
    main()
