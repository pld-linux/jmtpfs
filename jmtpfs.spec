Summary:	FUSE based MTP filesystem
Summary(pl.UTF-8):	System plików MTP oparty na FUSE
Name:		jmtpfs
Version:	0.5
Release:	1
License:	GPL v3
Group:		Applications/System
#Source0Download: https://github.com/JasonFerrara/jmtpfs/tags
# TODO: use
#Source0:	https://github.com/JasonFerrara/jmtpfs/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/JasonFerrara/jmtpfs/archive/v%{version}.tar.gz
# Source0-md5:	501e51530d3c04d63e9ac96d794bf5c5
URL:		https://github.com/JasonFerrara/jmtpfs
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libmagic-devel
BuildRequires:	libmtp-devel >= 1.1.0
BuildRequires:	libstdc++-devel >= 6:4.3
Requires:	libfuse-tools >= 2.6
Requires:	libmtp >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FUSE based MTP filesystem designed to make exchanging files between
Android devices and Linux work as well as it did with using USB Mass
Storage.

%description -l pl.UTF-8
Oparty na FUSE system plików MTP, zaprojektowany tak, żeby wymiana
plików między urządzeniami z Androidem a Linuksem działała tak dobrze,
ajk przy użyciu USB Mass Storage.

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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/jmtpfs
