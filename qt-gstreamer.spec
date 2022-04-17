%define api 1.0
%define glibapi 2.0
%define major 0
%define qt5_name qt5-gstreamer

Summary:	C++ bindings for GStreamer with a Qt-style API
Name:		qt-gstreamer
Version:	1.2.0
Release:	15
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		http://gstreamer.freedesktop.org/wiki/QtGStreamer
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.xz
## upstream patches
Patch0:		0001-gstqtvideosink-fix-memory-leak-and-synchronization-i.patch
Patch1:		0002-CMakeLists.txt-actually-require-GStreamer-1.2.0.patch
Patch2:		0003-qtglvideosinkbase-don-t-use-variable-name-interface-.patch
Patch3:		0004-when-built-against-1.4-the-unit-test-fails-because-i.patch
Patch4:		0005-gstreamer-now-supports-animated-PNGs-so-PNG-is-now-a.patch
Patch5:		0006-tests-auto-taglisttest.cpp-it-appears-tag-lists-remo.patch
Patch6:		0007-Create-an-empty-structure-to-pass-to-gst_message_new.patch
Patch7:		0008-ElementMessage-also-needs-a-valid-structure.patch
Patch8:		0009-Add-pbutils-include-directory-to-include-paths.patch
Patch9:		0010-Workaround-build-failures-with-boost-1.57-and-moc.patch
Patch10:	0011-Fix-compilation-with-GStreamer-1.5.1.patch
Patch11:	0012-whitespace-cleanup.patch
Patch12:	0013-By-GStreamer-1.6-the-audio-codec-name-for-FLAC-chang.patch
Patch13:	0014-It-appears-there-is-only-one-attachement.patch
Patch14:	0015-The-geometry-must-never-be-set-to-0-once-the-node-is.patch
Patch15:	0016-Fix-build-with-Clang-3.8.patch
Patch16:	0017-gst_message_new_application-fails-when-passed-a-NULL.patch
Patch17:	0018-Set-default-empty-structure-on-Application-and-Eleme.patch
Patch18:	0019-Fix-crash-when-the-VideoItem-moves-in-the-SceneGraph.patch
Patch19:	0020-Fix-QGst-Memory-bug-on-case-insensitive-fs.patch
Patch20:	0021-Fix-QtGStreamer-lookup-on-Qt5.patch
Patch21:	0022-QGst-Pad-strong-ref-the-event-in-sendEvent.patch
Patch22:	0023-qt5glvideosink-fix-of-too-much-red-value-in-video.patch
Patch23:	0024-Fix-cmake-with-Qt-5.11_beta3-dropping-qt5_use_module.patch
Patch24:	0025-openglsurfacepainter.cpp-remove-1-for-right-and-bott.patch
Patch25:	0026-videomaterial.cpp-Prevent-the-use-of-uninitialized-t.patch
Patch26:	0027-FindGLIB2-Do-not-use-REQUIRED-to-find-PkgConfig-and-.patch
Patch27:	0028-FindGStreamer-Do-not-search-for-plugin-dir-if-gstrea.patch
Patch28:	0029-FindGStreamer-Fix-cases-where-gst.h-and-gstconfig.h-.patch
Patch29:	0030-Use-GSTREAMER_INCLUDE_DIRS-instead-of-GSTREAMER_INCL.patch
Patch30:	0031-Device-DeviceMonitor-support.patch
Patch31:	0032-DeviceMonitor-example.patch
Patch32:	0033-Fix-discoverer-test.patch
Patch33:	0034-Fix-QUIET-flag-in-FindGStreamer-and-FindGStreamerPlu.patch
Patch34:	0035-README-add-maintenance-notice.patch
Patch35:	0036-QGst-caps-compilation-fix-from-https-bugs.kde.org-sh.patch
## uptreamable patches
#Patch100:	qt-gstreamer-1.2.0-boost_160.patch
Patch101:	qt-gstreamer-1.2.0-compile.patch
Patch102:	qt-gstreamer-glib.patch

BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	boost-devel
BuildRequires:	qmake5
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api})
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

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
%autosetup -p1

%build
%cmake -DQT_VERSION=5
%make_build

%install
%make_install -C build
