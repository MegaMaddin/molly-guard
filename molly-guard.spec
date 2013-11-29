Name:           molly-guard
Version:        0.4.5
Release:        2%{?dist}
Summary:        Protects machines from accidental shutdowns/reboots

Group:          Applications/System
License:        Artistic 2.0
URL:            http://packages.qa.debian.org/m/molly-guard.html
Source0:        %{name}_%{version}.orig.tar.gz
Patch0:         molly-guard_0.4.5-rhel.diff.gz

BuildArch:      noarch
BuildRequires:  libxslt docbook-style-xsl

%description
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

%prep
%setup -q
%patch0 -p1

%build
%{__make} prefix=/usr etc_prefix=


%install
%{__rm} -rf %{buildroot}
%{__make} install DEST=%{buildroot} prefix=/usr etc_prefix=

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/run.d
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%{_sysconfdir}/%{name}/run.d/10-print-message
%{_sysconfdir}/%{name}/run.d/30-query-hostname
%{_mandir}/man8/molly-guard.8.gz
%{_datarootdir}/%{name}/shutdown
%{_datarootdir}/%{name}/reboot
%{_datarootdir}/%{name}/halt
%{_datarootdir}/%{name}/poweroff

%changelog
* Fri Nov 29 2013 Mega Maddin <github@megamaddin.org> 0.4.5-2
- changed spec commands to rpm macros
* Sat Apr 19 2013 Martin Probst <maddin@megamaddin.org> 0.4.5-1
- initial rpm release for Red Hat based distribution
- changed calling of guarded executables for Red Hat based systems to aliases, because RHEL does not provide the path ordering needed by molly-guard
- revised man page
