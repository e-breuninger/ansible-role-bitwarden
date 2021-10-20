# Ansible Role: Bitwarden

[![CI](https://github.com/e-breuninger/ansible-role-bitwarden/actions/workflows/ci.yml/badge.svg)](https://github.com/e-breuninger/ansible-role-bitwarden/actions/workflows/ci.yml)

Deploy Bitwarden with Docker and Docker-Compose using the `bitwarden.sh`.

This role is an automated wrapper around the Bitwarden setup scripts. 
It makes heavy use of handlers to trigger reconfigure and update tasks. 

If you need any task not covered by the role it's totally fine to use the setup script on the machine directly.
Use the official docs as reference: https://bitwarden.com/help/article/install-on-premise/

## Usage

The role is currently not in Ansible Galaxy due to an issue of connecting out Github organisation with Galaxy.
As soon this is fixed you will be able to use it via Galaxy. 

Add the following to your `requirements.yml`

    roles:
      - src: git+https://github.com/e-breuninger/ansible-role-bitwarden.git
        name: breuninger.bitwarden
        version: 0.1.0

Add the role to your playbook:

    - hosts: server
      roles:
        - { role: breuninger.bitwarden }


## Known issues

### Certbot

We currently only support static TLS certificates for Nginx. The Certbot integration is not configured.
Feel free to add this feature as a PR if needed. 

### Bitwarden version

Bitwarden has a different version in the setup files than in the tagged version of the repo may indicates.
This is due to their release strategy, which always increases the actual version only in the master. We are already in talks with Bitwarden and hope for a different mode of release.
