Name:           irssi
Version:        1.0
Release:        1%{?dist}
Summary:        Client irssi

License:        GPLv2
URL:            https://irssi.org/
Source0:        https://github.com/Grallistrix/irssi/releases/download/%{version}/irssi-%{version}.tar.gz


BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  perl-ExtUtils-Embed
BuildRequires:  utf8proc-devel
BuildRequires:  cmake
BuildRequires:  openssl-devel
Requires:       glib2
Requires:       openssl-devel
Requires:       perl
Requires:       ncurses-libs

%description
The client of the future


%prep
%setup -n irssi


%build
meson Build
ninja -C %{_builddir}/irssi/Build


%install
DESTDIR=%{buildroot} ninja -C Build install
mkdir -p %{buildroot}/usr/local/share/licenses/%{name}/
cp %{_builddir}/irssi/COPYING %{buildroot}/usr/local/share/licenses/%{name}/


%files
%license /usr/local/share/licenses/%{name}/COPYING
/usr/local/bin/%{name}
/usr/local/share/%{name}/
/usr/local/share/doc 
/usr/local/share/man
/usr/local/include/
/usr/local/lib64/
/usr/local/bin/openssl

%changelog
* Tue May 14 2024 Andrzej Piotrowski <apiotrow@student.agh.edu.pl> - 1-1
- 1 version 1 release
