# Dabbler
An apprentice to the orchestrator

Dabbler is a tool that exposes some REST APIs that allow the dynamic reloading of docker processes based on CI Web Hooks.

## Usage
```
docker run -d --name=dabbler \
  --restart=always \
  -p <exposed_port_here>:8080 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  bign8/dabbler
```

## Triggers

* `POST /dabbler/0.0.0/travis/<meta-data-here>` for travis CI targets


## Build
<!-- TODO: setup virtualenv -->

```
pip install -Ur requirements.txt
docker build -t bign8/dabbler .
```
