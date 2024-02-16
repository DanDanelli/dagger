import sys

import anyio
import dagger
from dagger import dag


async def main(args: list[str]):
    async with dagger.connection():
        # build container with cowsay entrypoint
        ctr = (
            dag.container()
            .from_("python:alpine")
            .with_exec(["pip", "install", "cowsay"])
            .with_entrypoint(["cowsay"])
        )

        # run cowsay with requested message
        result = await ctr.with_exec(args).stdout()

    print(result)


anyio.run(main, sys.argv[1:])
