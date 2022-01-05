"""Role testing files using testinfra."""

import pytest


def test_bitwarden_user(host):
    """Validate bitwarden user is exists"""
    u = host.user("bitwarden")
    assert u.name
    assert u.exists
    assert u.group == "bitwarden"
    assert u.home == "/opt/bitwarden"


@pytest.mark.parametrize(
    "container_name",
    [
        ("bitwarden-nginx"),
        ("bitwarden-admin"),
        ("bitwarden-mssql"),
        ("bitwarden-web"),
        ("bitwarden-api"),
        ("bitwarden-notifications"),
        ("bitwarden-attachments"),
        ("bitwarden-identity"),
        ("bitwarden-icons"),
        ("bitwarden-events"),
        ("bitwarden-sso"),
    ],
)
def test_containers_are_runing(host, container_name):
    """"Validate Bitwarden container is running """
    container = host.docker(container_name)
    assert container.is_running


def test_nginx_container_http_exposed_port(host):
    """"Validate exposed http port from nginx container """
    assert host.socket("tcp://0.0.0.0:%s" % "80").is_listening


def test_nginx_container_https_exposed_port(host):
    """"Validate exposed https port from nginx container """
    assert host.socket("tcp://0.0.0.0:%s" % "443").is_listening


def test_host_certificate_exists(host):
    """Validare host certificate in Bitwarden certificate directory"""
    cert_file = host.file("/opt/bitwarden/bwdata/ssl/localhost/certificate.crt")
    assert cert_file.is_file
    assert cert_file.exists
    assert cert_file.mode == 0o600
    assert cert_file.user == "bitwarden"
    assert cert_file.group == "bitwarden"


def test_host_certificate_key_exists(host):
    """Validare host certificate key in Bitwarden certificate directory"""
    cert_file = host.file("/opt/bitwarden/bwdata/ssl/localhost/private.key")
    assert cert_file.is_file
    assert cert_file.exists
    assert cert_file.mode == 0o600
    assert cert_file.user == "bitwarden"
    assert cert_file.group == "bitwarden"


def test_web_entry_point(host):
    """Validate bitwarden responce on web ports """
    resp = host.ansible(
        "uri", "url=https://localhost/alive validate_certs=False", check=False
    )
    print(resp)
    assert resp["status"] == 200


def test_global_env_(host):
    """Validate if global variables are set"""
    file = host.file("/opt/bitwarden/bwdata/env/global.override.env")
    assert file.exists
    assert file.contains("adminSettings__admins=root@localhost")
    assert file.contains("globalSettings__mail__smtp__host=localhost")
    assert file.contains("globalSettings__mail__smtp__port=25")
