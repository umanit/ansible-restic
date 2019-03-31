import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_binary(host):
    binary = host.file("/usr/local/bin/restic")
    assert binary.exists
    assert binary.is_file
    assert binary.mode == 0o750
