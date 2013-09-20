Summary:	FUSE based MTP filesystem
Name:		jmtpfs
Version:	0.4
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	http://research.jacquette.com/wp-content/uploads/2012/05/%{name}-%{version}.tar.gz
# Source0-md5:	e6bcade86da701a5d2b6f6bbc9b24e39
Patch0:		gcc.patch
URL:		http://research.jacquette.com/jmtpfs-exchanging-files-between-android-devices-and-linux/
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
%patch0 -p1

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
