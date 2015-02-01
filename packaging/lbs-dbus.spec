Name:		lbs-dbus
Summary:	Dbus interface for Location based service
Version:	0.3.0
Release:	1
Group:		System/Libraries
License:	Apache
Source0:	lbs-dbus-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:	cmake
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(dlog)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(capi-appfw-app-manager)
BuildRequires:	pkgconfig(capi-appfw-package-manager)
BuildRequires:	pkgconfig(pkgmgr-info)
BuildRequires:	python
BuildRequires:	python-xml

%description
LBS dbus interface

%package -n	liblbs-dbus
Summary:	LBS dbus library
Group:	TO_BE/FILLED_IN
Requires(post): sys-assert

%description -n liblbs-dbus
LBS client API library

%package -n	liblbs-dbus-devel
Summary:	Telephony client API (devel)
Group:		Development/Libraries
Requires:	liblbs-dbus = %{version}-%{release}

%description -n liblbs-dbus-devel
LBS client API library (devel)


%prep
%setup -q


%build
export CFLAGS+=" -Wno-unused-local-typedefs "
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -n liblbs-dbus
%manifest liblbs-dbus.manifest
%defattr(-,root,root,-)
#%doc COPYING
%{_libdir}/*.so.*
%{_prefix}/etc/dbus-1/system.d/*

%files -n liblbs-dbus-devel
%defattr(-,root,root,-)
%{_includedir}/lbs-dbus/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
