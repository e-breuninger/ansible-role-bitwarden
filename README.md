# Ansible Role: Bitwarden

[![CI](https://github.com/e-breuninger/ansible-role-bitwarden/actions/workflows/ci.yml/badge.svg)](https://github.com/e-breuninger/ansible-role-bitwarden/actions/workflows/ci.yml)

Deploy Bitwarden with Docker and Docker-Compose following the steps provided by Bitwardens setup.sh.

The setup script is not fully automatabel, so this role uses it as a blueprint.
Instead of doing every step via Ansible the Bitwarden Setup container is used.

Use the official docs as reference: https://bitwarden.com/help/article/install-on-premise/

Install and configure bitwarden on premise in docker-compose fashion.

## Table of content

* [Default Variables](#default-variables)
  * [bitwarden_domain_name](#bitwarden_domain_name)
  * [bitwarden_global_env](#bitwarden_global_env)
  * [bitwarden_nginx_cert_path](#bitwarden_nginx_cert_path)
  * [bitwarden_nginx_key_path](#bitwarden_nginx_key_path)
  * [bitwarden_setup_config](#bitwarden_setup_config)
  * [bitwarden_version](#bitwarden_version)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### bitwarden_domain_name

Domain name witch used for hole bitwarden setup

#### Default value

```YAML
bitwarden_domain_name: localhost
```

### bitwarden_global_env

Map of global Bitwarden environment variables. Each entire is mapped to the global.override.env. See https://bitwarden.com/help/article/environment-variables/

#### Default value

```YAML
bitwarden_global_env: {}
```

#### Example usage

```YAML
bitwarden_global_env:
  globalSettings__mail__smtp__host: localhost
  globalSettings__mail__smtp__port: 25
```

### bitwarden_nginx_cert_path

Path of the certificate file used for the Nginx container (required). The user of the role is responsible for providing a valid certificate file. File is copied from the provided location to Bitwardens user home in order to garantue the correct mapping inside the container.

#### Default value

```YAML
bitwarden_nginx_cert_path:
```

### bitwarden_nginx_key_path

Path of the key file used for the Nginx container (required). The user of the role is responsible for providing a valid key file. File is copied from the provided location to Bitwardens user home in order to garantue the correct mapping inside the container.

#### Default value

```YAML
bitwarden_nginx_key_path:
```

### bitwarden_setup_config

Map of Bitwarden setup configuration values to override. Use this to change values in the generated config.yml file from Bitwarden.

#### Default value

```YAML
bitwarden_setup_config: {}
```

#### Example usage

```YAML
bitwarden_setup_config:
  database_docker_volume: true
```

### bitwarden_version

#### Default value

```YAML
bitwarden_version: 1.43.0
```

## Dependencies

None.

## License

MIT

## Author

Marco Frese <marco.frese@breuninger.de>
