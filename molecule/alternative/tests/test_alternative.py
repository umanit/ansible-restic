import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_binary(host):
    binary = host.file("/usr/local/bin/restic")
    assert binary.exists
    assert binary.is_file
    assert binary.mode == 0o750


def test_cronfiles(host):
    cronfiles = [
        "/etc/cron.d/restic-backblaze-example",
        "/etc/cron.d/restic-s3-example"
    ]
    for file in cronfiles:
        f = host.file(file)
        assert f.exists
        assert f.is_file
        assert f.mode == 0o640
        # assert f.contains('RESTIC_PASSWORD="correcthorsebatterystaple"')
#       # with host.sudo():
#            assert f.contains('RESTIC_PASSWORD="correcthorsebatterystaple"')
#
#
# def test_logdir(host):
#     logdir = host.file("/var/log/restic")
#     assert logdir.is_directory
#     assert logdir.exists
