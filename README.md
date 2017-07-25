# Ansible Role: yum-cron

Installs and configures yum-cron which runs yum updates as a cron job.
Supported on EL6 and 7.

## Requirements

None.

## Role Variables

> Note: The configuration for yum-cron differs between EL6 and 7.  Therefore, a
> different group of variables are used depending on your distribution version.

### EL 7 Options

Enable or disable the yum-cron service:

    yum_cron_service_enabled: True

What kind of update to use.  Options are:

- `default`                            = yum upgrade
- `security`                           = yum --security upgrade
- `security-severity:Critical`         = yum --sec-severity=Critical upgrade
- `minimal`                            = yum --bugfix update-minimal
- `minimal-security`                   = yum --security update-minimal
- `minimal-security-severity:Critical` =  --sec-severity=Critical update-minimal

    yum_cron_update_cmd: "default"

Whether a message should be emitted when updates are available, were
downloaded, or applied:

    yum_cron_update_messages: "yes"

Whether updates should be downloaded when they are available:

    yum_cron_download_updates: "yes"

Whether updates should be applied when they are available.  Note that
download_updates must also be yes for the update to be applied:

    yum_cron_apply_updates: "yes"

Maximum amout of time to randomly sleep, in minutes:

    yum_cron_random_sleep: 360

Name to use for this system in messages that are emitted.  If system_name is
None, the hostname will be used:

    yum_cron_system_name: "None"

How to send messages.  Valid options are `stdio` and `email`.  If emit_via includes
stdio, messages will be sent to stdout; this is useful to have cron send the
messages.  If emit_via includes email, this program will send email itself
according to the configured options.  If emit_via is None or left blank, no
messages will be sent.

    yum_cron_emit_via: "stdio"

The width, in characters, that messages that are emitted should be formatted to:

    yum_cron_output_width: 80

The address to send email messages from. NOTE: 'localhost' will be replaced
with the value of system_name.

    yum_cron_email_from: "root@localhost"

List of addresses to send messages to:

    yum_cron_email_to: "root"

Name of the host to connect to to send email messages:

    yum_cron_email_host: "localhost"

Use this to filter Yum core messages:

- `-4`: critical
- `-3`: critical+errors
- `-2`: critical+errors+warnings (default)

    yum_cron_debuglevel: "-2"

### EL6 Options

Pass parameters to yum:

    yum_cron_yum_parameter: ""

Don't install, just check:

    yum_cron_check_only: "no"

Check to see if you can reach the repos before updating:

    yum_cron_check_first: "no"

Don't install, just check and download:

    yum_cron_download_only: "no"

Print error ranging from level 0 thru 10.  0 means print only critical errors:

    yum_cron_error_level: "0"

Set the debug level from 0 thru 10, higher number means more output:

    yum_cron_debug_level: "0"

Tell yum to wait a random time:

    yum_cron_randomwait: "60"

Mail the output to this email address:

    yum_cron_mailto: ""

Tag the yum emails when sent:

    yum_cron_systemname: "{{ ansible_fqdn }}"

Days of the week you want to run yum-cron:

    yum_cron_days_of_week: "0123456"

Do clean up on this day.  Defaults to `0` (Sunday):

    yum_cron_cleanday: "0"

Make yum-cron service wait for transactions to complete:

    yum_cron_service_waits: "yes"

Set the time period, in seconds. for the yum-cron service to wait for
transactions to complete:

    yum_cron_service_wait_time: "300"

## Dependencies

None.

## Example Playbook

    - hosts: servers
      roles:
         - ansible-role-yum-cron

## License

BSD.
