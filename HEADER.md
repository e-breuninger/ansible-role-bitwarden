# Ansible Role: Bitwarden

[![CI](https://github.com/e-breuninger/ansible-role-bitwarden/actions/workflows/ci.yml/badge.svg)](https://github.com/e-breuninger/ansible-role-bitwarden/actions/workflows/ci.yml)

Deploy Bitwarden with Docker and Docker-Compose following the steps provided by Bitwardens setup.sh.

The setup script is not fully automatabel, so this role uses it as a blueprint.
Instead of doing every step via Ansible the Bitwarden Setup container is used.

Use the official docs as reference: https://bitwarden.com/help/article/install-on-premise/
