"""

Example Commands to interface with:
- docker run --name redis -p 6379:6379 --restart=always -d redis:alpine
"""

import os
import bottle
import docker

# key to secure requests (TODO: make decorator for bottle to use)
key = os.getenv("HASH")

# TODO: run this periodically
client = docker.from_env()
client.ping()  # check if docker client is there
containers = {o.name: o for o in client.containers.list(all=True)}

# Travis handler
@bottle.route('/dabbler/0.0.0/travis/<slug>')
def index(slug):
    if key and ('hash' not in bottle.request.query or key != bottle.request.query['hash']):
        bottle.abort(403, "Invalid Hash Query")
    if slug not in containers:
        bottle.abort(417, "Invalid Container: {}".format(slug))

    # TODO: PARSE THE TRAVIS PAYLOAD AND GET THE VERSION TO DEPLOY

    return "Done!"


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080, dev=True)
