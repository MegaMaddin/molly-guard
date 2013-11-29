molly-guard
===========

Protects machines from accidental shutdowns/reboots - now even for el6.
This repository includes the spec file and a patch to rebuild molly-guard
for el6 distributions like RHEL, CentOS or Scientific-Linux.

molly-guard description
=======================

The package installs a shell script that overrides the existing
shutdown/reboot/halt/poweroff commands and first runs a set of scripts, which
all have to exit successfully, before molly-guard invokes the real command.

One of the scripts checks for existing SSH sessions. If any of the four
commands are called interactively over an SSH session, the shell script
prompts you to enter the name of the host you wish to shut down. This should
adequately prevent you from accidental shutdowns and reboots.

This shell script passes through the commands to the respective binaries in
/sbin and should thus not get in the way if called non-interactively, or
locally.
