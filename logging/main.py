from sanic import Sanic, response
from sys import argv
import os

import loggingg

app = Sanic("LoggingApp")


@app.post("/upload")
async def upload(request):
    loggingg.loggingUpload(request.json)
    return response.json({})


@app.post("/query")
async def query(request):
    res = loggingg.loggingQuery(request.json)
    return response.json(res)


if __name__ == "__main__":
    if not os.path.exists('./logging/logs'):
        os.mkdir('./logging/logs')
    app.run(host="0.0.0.0", port=8001)
