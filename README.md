# python-monitoring
A simple script to monitor HTTP

## DOMAIN LISTS
Update `domains.yaml`, follow these format
```yaml
project:
  - name: bing.com
    url: https://bing.com
open-source:
  - name: debian.org
    url: https://www.debian.org
  - name: ubuntu.com
    url: https://ubuntu.com/
```


## BUILD DOCKER
To build a docker image
```sh
docker build -t jaranguda/python-monitoring
```
