#
Summary:	Kexi MDB
Summary(pl):	Kexi MDB
Name:		keximdb
Version:	0.9
Release:	0.1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://sunsite.icm.edu.pl/pub/unix/kde/stable/apps/KDE3.x/database/%{name}-%{version}.tar.gz
# Source0-md5:	93db33e0d7d488694166e53f41192f38
URL:		http://www.kexi-project.org/
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kexi-devel
BuildRequires:	kexi
BuildRequires:	pkgconfig
Requires:	kexi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}-%{version}

%build

%configure --with-kexidb-includes=%{_includedir}/kexidb \
	--with-kexidb-libraries=%{_libdir} \
	--with-qt-libraries=%{_libdir} \
	--without-arts \
	--enable-debug
	
#  --with-extra-includes=DIR
#  --with-extra-libs=DIR
#  --with-qt-dir=DIR
#  --with-qt-includes=DIR.
#  --with-libiconv-prefix=DIR

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

#%attr(755,root,root) %{_bindir}/*

#%{_datadir}/%{name}

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
