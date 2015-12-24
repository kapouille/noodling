import asyncio
from aiohttp import web
from os.path import abspath, join, dirname
from mimetypes import guess_type


_HERE = dirname(abspath(__file__))


def get_static(relative_path):
    try:
        full_path = join(_HERE, "web", relative_path)
        mime_type, encoding = guess_type(full_path)
        with open(full_path) as file:
            return web.Response(
                    body=file.read().encode(encoding or "utf-8"),
                    content_type=mime_type
            )
    except (FileNotFoundError, IsADirectoryError) as error:
        return web.Response(text="404: {}".format(error), status=404)


async def handle_static(request):
    return get_static(request.match_info["relative_path"])


async def index(request):
    return get_static("index.html")


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    app.router.add_route("GET", r"/{relative_path:.+}", handle_static)

    srv = await loop.create_server(app.make_handler(), "0.0.0.0", 8888)
    print("Server started at http://0.0.0.0:8888")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
