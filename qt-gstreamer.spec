%define api 0.10
%define glibapi 2.0
%define major 0

Summary:	C++ bindings for GStreamer with a Qt-style API
Name:		qt-gstreamer
Version:	0.10.2
Release:	4
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		http://gstreamer.freedesktop.org/wiki/QtGStreamer
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	qt4-qmlviewer
BuildRequires:	boost-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

%files
%{_libdir}/gstreamer-0.10/libgstqtvideosink.so
%{_qt_importdir}/QtGStreamer/

#----------------------------------------------------------------------------

%define libqtglib %mklibname QtGLib %{glibapi} %{major}

%package -n %{libqtglib}
Summary:	C++/Qt bindings for parts of the GLib and GObject APIs
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0 < 0.10.2
Conflicts:	%{_lib}qtglib0.10.2 < 0.10.2-4
Obsoletes:	%{_lib}qtglib0.10.2 < 0.10.2-4
Conflicts:	%{_lib}qtglib2.0_0.10.2 < 0.10.2-4
Obsoletes:	%{_lib}qtglib2.0_0.10.2 < 0.10.2-4

%description -n %{libqtglib}
Library providing C++/Qt bindings for parts of the GLib and GObject
APIs, a base on which QtGStreamer is built.

%files -n %{libqtglib}
%{_libdir}/libQtGLib-%{glibapi}.so.%{major}*

#----------------------------------------------------------------------------

%define libqtgstreamer %mklibname QtGStreamer %{api} %{major}

%package -n %{libqtgstreamer}
Summary:	C++/Qt bindings for GStreamer
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0 < 0.10.2
Conflicts:	%{_lib}qtgstreamer0.10.2 < 0.10.2-4
Obsoletes:	%{_lib}qtgstreamer0.10.2 < 0.10.2-4

%description -n %{libqtgstreamer}
Library providing C++/Qt bindings for GStreamer

%files -n %{libqtgstreamer}
%{_libdir}/libQtGStreamer-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libqtgstreamerui %mklibname QtGStreamerUi %{api} %{major}

%package -n %{libqtgstreamerui}
Summary:	Library providing integration with QtGui
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0 < 0.10.2
Conflicts:	%{_lib}qtgstreamerui0.10.2 < 0.10.2-4
Obsoletes:	%{_lib}qtgstreamerui0.10.2 < 0.10.2-4

%description -n %{libqtgstreamerui}
Library providing integration with QtGui.

%files -n %{libqtgstreamerui}
%{_libdir}/libQtGStreamerUi-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define libqtgstreamerutils %mklibname QtGStreamerUtils %{api} %{major}

%package -n %{libqtgstreamerutils}
Summary:	Library providing some high level utility classes
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0 < 0.10.2
Conflicts:	%{_lib}qtgstreamerutils0.10.2 < 0.10.2-4
Obsoletes:	%{_lib}qtgstreamerutils0.10.2 < 0.10.2-4

%description -n %{libqtgstreamerutils}
Library providing some high level utility classes.

%files -n %{libqtgstreamerutils}
%{_libdir}/libQtGStreamerUtils-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%define devname %mklibname -d %{name}

%package -n %{devname}
Summary:	Development files for QtGstreamer
Group:		Development/KDE and Qt
Requires:	%{libqtglib} = %{EVRD}
Requires:	%{libqtgstreamer} = %{EVRD}
Requires:	%{libqtgstreamerui} = %{EVRD}
Requires:	%{libqtgstreamerutils} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

This package contains files for developing applications using 
QtGstreamer.

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/QtGStreamer/*.cmake
%{_includedir}/QtGStreamer

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4 -DQTGSTREAMER_TESTS=ON -DLIB_INSTALL_DIR=%{_libdir}
%make

%install
%makeinstall_std -C build
