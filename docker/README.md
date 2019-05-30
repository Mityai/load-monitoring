# Grafana / Graphite with Docker

## Setup

### Using docker-compose

See the `docker-compose.yml` file for an configuration to use with `docker-compose`
```
sudo pip install -U docker-compose
docker-compose up -d -f docker-compose.yml
```

#### Grafana

* Web interface: `http://[hostname]:3000`
* Login: `admin`
* Password: `admin`

More about Docker Image for Grafana: https://grafana.com/docs/installation/docker/

#### Graphite

The container exposes the following ports for Graphite:
* `80`: Front-End Dashboard
* `2003`: Carbon's plaintext receiver
* `2004`: Carbon's pickle receiver
* `8080`: Graphite internal gunicorn port (without Nginx proxying)
* `8125`: statsd
* `8126`: statsd admin

More about Docker Image for Graphite: https://github.com/graphite-project/docker-graphite-statsd
