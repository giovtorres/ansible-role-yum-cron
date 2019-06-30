import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_yum_cron_is_installed(host):
    assert host.package("yum-cron").is_installed


def test_yum_cron_service(host):
    s = host.service("yum-cron")
    assert not s.is_enabled
    assert not s.is_running


def test_yum_cron_config(host):
    if host.system_info.release.startswith('7'):
        f = host.file("/etc/yum/yum-cron.conf")
        assert f.user == "root"
        assert f.group == "root"
        assert f.mode == 0o644
        assert f.contains("apply_updates = no")
    elif host.system_info.release.startswith('6'):
        f = host.file("/etc/sysconfig/yum-cron")
        assert f.user == "root"
        assert f.group == "root"
        assert f.mode == 0o644
        assert f.contains("DOWNLOAD_ONLY=yes")
