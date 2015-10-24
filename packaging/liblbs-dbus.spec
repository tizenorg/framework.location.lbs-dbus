Name:		liblbs-dbus
Summary:	Dbus interface for Location based service
Version:	0.3.3
Release:	1
Group:		Framework/Location
License:	Apache-2.0
Source0:    %{name}-%{version}.tar.gz
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

%description
LBS dbus interface

%package devel
Summary:	Telephony client API (devel)
Group:		Development/Libraries
Requires:	liblbs-dbus = %{version}-%{release}

%description devel
LBS client API library (devel)


%prep
%setup -q


%build
export CFLAGS="$CFLAGS -DTIZEN_DEBUG_ENABLE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_DEBUG_ENABLE"
export FFLAGS="$FFLAGS -DTIZEN_DEBUG_ENABLE"

export CFLAGS+=" -Wno-unused-local-typedefs "
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest liblbs-dbus.manifest
%defattr(-,root,root,-)
#%doc COPYING
%{_libdir}/*.so.*
%{_prefix}/etc/dbus-1/system.d/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/lbs-dbus/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
