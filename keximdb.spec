# TODO: rethink Name
Summary:	Kexi MDB plugin
Summary(pl.UTF-8):   Wtyczka MDB do Kexi
Name:		keximdb
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/database/%{name}-%{version}.tar.gz
# Source0-md5:	93db33e0d7d488694166e53f41192f38
URL:		http://www.kexi-project.org/
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	kdelibs-devel
BuildRequires:	kexi-devel >= 0.9-4
BuildRequires:	pkgconfig >= 1:0.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kexi MDB plugin.

%description -l pl.UTF-8
Wtyczka MDB do Kexi.

%prep
%setup -q

%build
%configure \
	--with-kexidb-includes=%{_includedir}/kexidb \
	--with-kexidb-libraries=%{_libdir} \
	--with-qt-libraries=%{_libdir} \
	--without-arts \
	--enable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/kde3/keximigrate_mdb.la
%attr (755,root,root) %{_libdir}/kde3/keximigrate_mdb.so
%{_datadir}/services/keximigrate_mdb.desktop
