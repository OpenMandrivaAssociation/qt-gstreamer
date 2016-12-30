%define api 1.0
%define glibapi 2.0
%define major 0
%define qt5_name qt5-gstreamer

Summary:	C++ bindings for GStreamer with a Qt-style API
Name:		qt-gstreamer
Version:	1.2.0
Release:	8
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		http://gstreamer.freedesktop.org/wiki/QtGStreamer
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.xz
## upstream patches
Patch0:		0000-gstqtvideosink-fix-memory-leak-and-synchronization-i.patch
Patch1:		0001-CMakeLists.txt-actually-require-GStreamer-1.2.0.patch
Patch2:		0002-qtglvideosinkbase-don-t-use-variable-name-interface-.patch
Patch3:		0003-when-built-against-1.4-the-unit-test-fails-because-i.patch
Patch4:		0004-gstreamer-now-supports-animated-PNGs-so-PNG-is-now-a.patch
Patch5:		0005-tests-auto-taglisttest.cpp-it-appears-tag-lists-remo.patch
Patch6:		0006-Create-an-empty-structure-to-pass-to-gst_message_new.patch
Patch7:		0007-ElementMessage-also-needs-a-valid-structure.patch
Patch8:		0008-Add-pbutils-include-directory-to-include-paths.patch
Patch9:		0009-Workaround-build-failures-with-boost-1.57-and-moc.patch
Patch10:	0010-Fix-compilation-with-GStreamer-1.5.1.patch
Patch11:	0011-whitespace-cleanup.patch
Patch12:	0012-By-GStreamer-1.6-the-audio-codec-name-for-FLAC-chang.patch
Patch13:	0013-It-appears-there-is-only-one-attachement.patch
Patch14:	0014-The-geometry-must-never-be-set-to-0-once-the-node-is.patch
Patch15:	0015-Fix-build-with-Clang-3.8.patch
Patch16:	0016-gst_message_new_application-fails-when-passed-a-NULL.patch

## uptreamable patches
Patch100:	qt-gstreamer-1.2.0-boost_160.patch

BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	qt4-qmlviewer
BuildRequires:	boost-devel
BuildRequires:	qt4-devel
BuildRequires:	qmake5
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api})
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

%files
%{_libdir}/gstreamer-%{api}/libgstqtvideosink.so
%{_qt_importdir}/QtGStreamer/

#----------------------------------------------------------------------------

%define libqtglib %mklibname QtGLib %{glibapi} %{major}

%package -n %{libqtglib}
Summary:	C++/Qt bindings for parts of the GLib and GObject APIs
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0
Conflicts:	%{_lib}qtglib0.10.2
Obsoletes:	%{_lib}qtglib0.10.2
Conflicts:	%{_lib}qtglib2.0_0.10.2
Obsoletes:	%{_lib}qtglib2.0_0.10.2
Conflicts:      %{_lib}QtGLib2.0_2
Obsoletes:      %{_lib}QtGLib2.0_2

%description -n %{libqtglib}
Library providing C++/Qt bindings for parts of the GLib and GObject
APIs, a base on which QtGStreamer is built.

%files -n %{libqtglib}
%{_libdir}/libQtGLib-%{glibapi}.so.%{major}*
%{_libdir}/libQtGLib-%{glibapi}.so.%{version}

#----------------------------------------------------------------------------

%define libqtgstreamer %mklibname QtGStreamer %{api} %{major}

%package -n %{libqtgstreamer}
Summary:	C++/Qt bindings for GStreamer
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0
Conflicts:	%{_lib}qtgstreamer0.10.2
Conflicts:	%{_lib}QtGStreamer0.10_0
Obsoletes:	%{_lib}qtgstreamer0.10.2
Obsoletes:	%{_lib}QtGStreamer0.10_0

%description -n %{libqtgstreamer}
Library providing C++/Qt bindings for GStreamer

%files -n %{libqtgstreamer}
%{_libdir}/libQtGStreamer-%{api}.so.%{major}*
%{_libdir}/libQtGStreamer-%{api}.so.%{version}

#----------------------------------------------------------------------------

%define libqtgstreamerui %mklibname QtGStreamerUi %{api} %{major}

%package -n %{libqtgstreamerui}
Summary:	Library providing integration with QtGui
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0
Conflicts:	%{_lib}qtgstreamerui0.10.2
Conflicts:	%{_lib}QtGStreamerUi0.10_0
Obsoletes:	%{_lib}qtgstreamerui0.10.2
Obsoletes:	%{_lib}QtGStreamerUi0.10_0

%description -n %{libqtgstreamerui}
Library providing integration with QtGui.

%files -n %{libqtgstreamerui}
%{_libdir}/libQtGStreamerUi-%{api}.so.%{major}*
%{_libdir}/libQtGStreamerUi-%{api}.so.%{version}

#----------------------------------------------------------------------------

%define libqtgstreamerutils %mklibname QtGStreamerUtils %{api} %{major}

%package -n %{libqtgstreamerutils}
Summary:	Library providing some high level utility classes
Group:		System/Libraries
Conflicts:	%{_lib}qt-gstreamer0
Conflicts:	%{_lib}qtgstreamerutils0.10.2
Conflicts:	%{_lib}QtGStreamerUtils0.10_0
Obsoletes:	%{_lib}qtgstreamerutils0.10.2
Obsoletes:	%{_lib}QtGStreamerUtils0.10_0

%description -n %{libqtgstreamerutils}
Library providing some high level utility classes.

%files -n %{libqtgstreamerutils}
%{_libdir}/libQtGStreamerUtils-%{api}.so.%{major}*
%{_libdir}/libQtGStreamerUtils-%{api}.so.%{version}

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
%{_libdir}/libQtGLib-2.0.so
%{_libdir}/libQtGStreamer-%{api}.so
%{_libdir}/libQtGStreamerUi-%{api}.so
%{_libdir}/libQtGStreamerUtils-%{api}.so
%{_libdir}/pkgconfig/QtGStreamerUtils-%{api}.pc
%{_libdir}/pkgconfig/QtGStreamerUi-%{api}.pc
%{_libdir}/pkgconfig/QtGStreamer-%{api}.pc
%{_libdir}/pkgconfig/QtGLib-2.0.pc
%{_libdir}/cmake/QtGStreamer/*.cmake
%{_includedir}/QtGStreamer

#-------------------------------------------------------------------
%package -n %{qt5_name}
Summary: C++ bindings for GStreamer with a Qt5-style API
Group:   Development/KDE and Qt

%description -n %{qt5_name}
Qt5GStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt5
applications.

%files -n %{qt5_name}
%{_libdir}/gstreamer-%{api}/libgstqt5videosink.so
%{_libdir}/qt5/qml/QtGStreamer/

#-------------------------------------------------------------------
%define libqt5glib %mklibname qt5glib 2.0 %{major}

%package -n %{libqt5glib}
Summary: C++/Qt5 bindings for parts of the GLib and GObject APIs
Group:   System/Libraries

%description -n %{libqt5glib}
Library providing C++/Q5t bindings for parts of the GLib and GObject 
APIs, a base on which Qt5GStreamer is built.

%files -n %{libqt5glib}
%{_libdir}/libQt5GLib-2.0.so.%{major}*
%{_libdir}/libQt5GLib-2.0.so.%{version}

#-------------------------------------------------------------------
%define libqt5gstreamer %mklibname qt5gstreamer %{api} %{major}

%package -n %{libqt5gstreamer}
Summary: C++/Qt5 bindings for GStreamer
Group:   System/Libraries

%description -n %{libqt5gstreamer}
Library providing C++/Qt5 bindings for GStreamer

%files -n %{libqt5gstreamer}
%{_libdir}/libQt5GStreamer-%{api}.so.%{major}*
%{_libdir}/libQt5GStreamer-%{api}.so.%{version}

#-------------------------------------------------------------------
%define libqt5gstreamerquick %mklibname qt5gstreamerquick %{api} %{major}

%package -n %{libqt5gstreamerquick}
Summary: C++/Qt5 bindings for GStreamer
Group: System/Libraries
%description -n %{libqt5gstreamerquick}
Library providing C++/Qt5 bindings for GStreamer

%files -n %{libqt5gstreamerquick}
%{_libdir}/libQt5GStreamerQuick-%{api}.so.%{major}*
%{_libdir}/libQt5GStreamerQuick-%{api}.so.%{version}

#-------------------------------------------------------------------
%define libqt5gstreamerui %mklibname qt5gstreamerui %{api} %{major}

%package -n %{libqt5gstreamerui}
Summary: Library providing integration with Qt5Gui
Group:   System/Libraries

%description -n %{libqt5gstreamerui}
Library providing integration with Qt5Gui.

%files -n %{libqt5gstreamerui}
%{_libdir}/libQt5GStreamerUi-%{api}.so.%{major}*
%{_libdir}/libQt5GStreamerUi-%{api}.so.%{version}

#-------------------------------------------------------------------
%define libqt5gstreamerutils %mklibname qt5gstreamerutils %{api} %{major}

%package -n %{libqt5gstreamerutils}
Summary: Library providing some high level utility classes
Group:   System/Libraries

%description -n %{libqt5gstreamerutils}
Library providing some high level utility classes.

%files -n %{libqt5gstreamerutils}
%{_libdir}/libQt5GStreamerUtils-%{api}.so.%{major}*
%{_libdir}/libQt5GStreamerUtils-%{api}.so.%{version}

#--------------------------------------------------------------------
%define develnameQt5 %mklibname -d %{qt5_name}

%package -n %{develnameQt5}
Summary: Development files for Qt5Gstreamer
Group:   Development/KDE and Qt

Requires: %libqt5glib = %{EVRD}
Requires: %libqt5gstreamer = %{EVRD}
Requires: %libqt5gstreamerquick = %{EVRD}
Requires: %libqt5gstreamerui = %{EVRD}
Requires: %libqt5gstreamerutils = %{EVRD}
Requires: boost-devel
Provides: qt5-gstreamer-devel = %{EVRD}

%description -n %{develnameQt5}
Qt5GStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt5
applications.

This package contains files for developing applications using 
Qt5Gstreamer.

%files -n %{develnameQt5}
%_includedir/Qt5GStreamer
%{_libdir}/cmake/Qt5GStreamer/*.cmake
%{_libdir}/libQt5GLib-2.0.so
%{_libdir}/libQt5GStreamer-%{api}.so
%{_libdir}/libQt5GStreamerQuick-%{api}.so
%{_libdir}/libQt5GStreamerUi-%{api}.so
%{_libdir}/libQt5GStreamerUtils-%{api}.so
%{_libdir}/pkgconfig/Qt5GLib-2.0.pc
%{_libdir}/pkgconfig/Qt5GStreamer-%{api}.pc
%{_libdir}/pkgconfig/Qt5GStreamerQuick-%{api}.pc
%{_libdir}/pkgconfig/Qt5GStreamerUi-%{api}.pc
%{_libdir}/pkgconfig/Qt5GStreamerUtils-%{api}.pc

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
mkdir -p qt4

pushd qt4
%cmake -DQT_VERSION=4 ../../
%make
popd

mkdir -p qt5

pushd qt5
%cmake -DQT_VERSION=5 ../../
%make
popd

%install
%makeinstall_std -C qt4/build
%makeinstall_std -C qt5/build
