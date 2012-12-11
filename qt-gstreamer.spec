%define major 0
%define oldlibname %mklibname qt-gstreamer 0

Name: qt-gstreamer
Summary: C++ bindings for GStreamer with a Qt-style API
Version: 0.10.2
Release: 1
License: LGPLv2+
Url: http://gstreamer.freedesktop.org/wiki/QtGStreamer
Group: Development/KDE and Qt

#BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(QtGui) < 5.0.0
BuildRequires: pkgconfig(QtCore) < 5.0.0
BuildRequires: pkgconfig(QtTest) < 5.0.0
BuildRequires: pkgconfig(QtDeclarative) < 5.0.0
BuildRequires: pkgconfig(QtOpenGL) < 5.0.0
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires: qt4-qmlviewer
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: doxygen
Source0: http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.bz2

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

%files
%_libdir/gstreamer-0.10/libgstqtvideosink.so
%_qt_importdir/QtGStreamer/

#-------------------------------------------------------------------
%define libqtglib %mklibname qtglib %{version}

%package -n %{libqtglib}
Summary: C++/Qt bindings for parts of the GLib and GObject APIs
Group: System/Libraries
Conflicts: %{oldlibname} < 0.10.2
%description -n %{libqtglib}
Library providing C++/Qt bindings for parts of the GLib and GObject 
APIs, a base on which QtGStreamer is built.

%files -n %{libqtglib}
%_libdir/libQtGLib-2.0.so.%{major}*

#-------------------------------------------------------------------
%define libqtgstreamer %mklibname qtgstreamer %{version}

%package -n %{libqtgstreamer}
Summary: C++/Qt bindings for GStreamer
Group: System/Libraries
Conflicts: %{oldlibname} < 0.10.2
%description -n %{libqtgstreamer}
Library providing C++/Qt bindings for GStreamer

%files -n %{libqtgstreamer}
%_libdir/libQtGStreamer-0.10.so.%{major}*

#-------------------------------------------------------------------
%define libqtgstreamerui %mklibname qtgstreamerui %{version}

%package -n %{libqtgstreamerui}
Summary: Library providing integration with QtGui
Group: System/Libraries
Conflicts: %{oldlibname} < 0.10.2
%description -n %{libqtgstreamerui}
Library providing integration with QtGui.

%files -n %{libqtgstreamerui}
%_libdir/libQtGStreamerUi-0.10.so.%{major}*

#-------------------------------------------------------------------
%define libqtgstreamerutils %mklibname qtgstreamerutils %{version}

%package -n %{libqtgstreamerutils}
Summary: Library providing some high level utility classes
Group: System/Libraries
Conflicts: %{oldlibname} < 0.10.2
%description -n %{libqtgstreamerutils}
Library providing some high level utility classes.

%files -n %{libqtgstreamerutils}
%_libdir/libQtGStreamerUtils-0.10.so.%{major}*

#--------------------------------------------------------------------
%define develname %mklibname -d %name

%package -n %{develname}
Summary: Development files for QtGstreamer
Group: Development/KDE and Qt
Requires: %libqtglib = %version-%release
Requires: %libqtgstreamer = %version-%release
Requires: %libqtgstreamerui = %version-%release
Requires: %libqtgstreamerutils = %version-%release

Provides: %name-devel = %version-%release

%description -n %{develname}
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

This package contains files for developing applications using 
QtGstreamer.

%files -n %{develname}
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_libdir/QtGStreamer/*.cmake
%_includedir/QtGStreamer

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4 -DQTGSTREAMER_TESTS=ON -DLIB_INSTALL_DIR=%{_libdir}
%make

%install
%makeinstall_std -C build
