import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_apache_service_running(host):
    apache = host.service('apache2')

    assert apache.is_running
    assert apache.is_enabled


@pytest.fixture(params=[
    'apache2',
    'curl',
    'php7.0-gd',
    'libapache2-mod-php',
    'php7.0-mbstring',
    'php7.0-mcrypt',
    'php7.0-mysql',
    'php7.0-xml',
    'php7.0-zip'
])
def test_packages_installed(host):
    assert host.package(host.param).is_installed
