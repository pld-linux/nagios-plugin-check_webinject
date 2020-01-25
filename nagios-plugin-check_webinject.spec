%define		plugin	check_webinject
Summary:	Nagios plugin for testing web services
Name:		nagios-plugin-%{plugin}
Version:	1.84
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	https://labs.consol.de/assets/downloads/%{plugin}-%{version}.tar.gz
# Source0-md5:	bbf409153bb46e6beb25b4b3395c911e
Source1:	%{plugin}.cfg
URL:		https://labs.consol.de/nagios/check_webinject/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
check_webinject is a Nagios check plugin based on the Webinject Perl
Module available on CPAN which is now part of the Webinject project.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
