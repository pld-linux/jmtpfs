Summary:	FUSE based MTP filesystem
Name:		jmtpfs
Version:	0.5
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://github.com/JasonFerrara/jmtpfs/archive/v%{version}.tar.gz
# Source0-md5:	501e51530d3c04d63e9ac96d794bf5c5
URL:		https://github.com/JasonFerrara/jmtpfs
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel
BuildRequires:	libmtp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUSE based MTP filesystem designed to make exchanging files between
Android devices and Linux work as well as it did with using USB Mass
Storage.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/jmtpfs
