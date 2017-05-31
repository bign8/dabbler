# Dabbler
An apprentice to the orchestrator

Dabbler is a tool that exposes some REST APIs that allow the dynamic reloading of docker processes based on CI Web Hooks.

## Usage
```
docker run -d --name=dabbler \
  --restart=always \
  -p <exposed_port_here>:80 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  bign8/dabbler
```

## Triggers

* `POST /dabbler/0.0.0/travis/<meta-data-here>` for travis CI targets
