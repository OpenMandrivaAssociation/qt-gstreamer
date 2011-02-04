Name: qt-gstreamer
Summary: C++ bindings for GStreamer with a Qt-style API
Version: 0.10.1
Release: %mkrel 1
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/wiki/QtGStreamer
Group: Development/KDE and Qt
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: automoc
BuildRequires: boost-devel
BuildRequires: libgstreamer0.10-plugins-base-devel
BuildRequires: bison flex
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.bz2
Patch0: qt-gstreamer-0.10.1-libdir.patch

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

%files
%defattr(-,root,root)
%_libdir/gstreamer-0.10/libgstqwidgetvideosink.so

#-------------------------------------------------------------------

%define major 0
%define libname %mklibname %name %{major}

%package -n %{libname}
Summary: C++ bindings for GStreamer with a Qt-style API
Group: System/Libraries

%description -n %{libname}
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

%files -n %{libname}
%defattr(-,root,root)
%_libdir/*.so.%{major}
%_libdir/*.so.%{major}.*

#--------------------------------------------------------------------

%define develname %mklibname -d %name

%package -n %{develname}
Summary: Development files for QtGstreamer
Group: Development/KDE and Qt
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %{develname}
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

This package contains files for developing applications using 
QtGstreamer.

%files -n %{develname}
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_libdir/QtGStreamer/*.cmake
%_includedir/QtGStreamer

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .libdir

%build
%cmake_qt4 -DQTGSTREAMER_TESTS=ON -DLIB_INSTALL_DIR=%{_libdir}
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%check
pushd build
ctest
popd

%clean
rm -rf %buildroot
