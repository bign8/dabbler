"""
Example Commands to interface with:
- docker run --name redis -p 6379:6379 --restart=always -d redis:alpine

Travis - https://docs.travis-ci.com/user/notifications/#Configuring-webhook-notifications
Circle CI - https://circleci.com/docs/1.0/configuration/
"""

import os
import json
import bottle
import docker

# key to secure requests (TODO: make decorator for bottle to use)
key = os.getenv("HASH")

# TODO: run this periodically
client = docker.from_env()
client.ping()  # check if docker client is there
containers = {o.name: o for o in client.containers.list(all=True)}

# Travis handler
@bottle.route('/dabbler/0.0.0/travis/<slug>', method="POST")
def index(slug):
    if key and ('hash' not in bottle.request.query or key != bottle.request.query['hash']):
        bottle.abort(403, "Invalid Hash Query")

    print 'Debug Headers:' + json.dumps(dict(bottle.request.headers))
    print 'Debug Body:' + ''.join(bottle.request.body.readlines())

    if slug not in containers:
        bottle.abort(417, "Invalid Container: {}".format(slug))

    # TODO: PARSE THE TRAVIS PAYLOAD AND GET THE VERSION TO DEPLOY

    return "Done!"

# Docker Hub Handler
"""
{
  "push_data": {
    "pushed_at": 1496812349,
    "images": [

    ],
    "tag": "latest",
    "pusher": "bign8"
  },
  "callback_url": "https:\/\/registry.hub.docker.com\/u\/bign8\/helvetictoc\/hook\/224aiaejagi5f44bcfebjj2ac514g02cj\/",
  "repository": {
    "status": "Active",
    "description": "builds from GitHub",
    "is_trusted": true,
    "full_description": <truncated>,
    "repo_url": "https:\/\/hub.docker.com\/r\/bign8\/helvetictoc",
    "owner": "bign8",
    "is_official": false,
    "is_private": false,
    "name": "helvetictoc",
    "namespace": "bign8",
    "star_count": 0,
    "comment_count": 0,
    "date_created": 1496807188,
    "dockerfile": "FROM pierrezemb\/gostatic:latest\nMAINTAINER Nate Woods <me@bign8.info>\nADD static\/ \/srv\/http\n",
    "repo_name": "bign8\/helvetictoc"
  }
}
"""
@bottle.route('/dabbler/hub/<slug>', method="POST")
def hub(slug):
    print 'TODO'

if __name__ == "__main__":
    bottle.run(host='0.0.0.0', port=8080, dev=True)
