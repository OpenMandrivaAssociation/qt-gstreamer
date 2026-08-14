%define api 1.0
%define glibapi 2.0
%define major 0
%define qt6_name qt6-gstreamer
%define oldlibqt5glib %mklibname qt5glib 2.0 %{major}
%define oldlibqt5gstreamer %mklibname qt5gstreamer %{api} %{major}
%define oldlibqt5gstreamerquick %mklibname qt5gstreamerquick %{api} %{major}
%define oldlibqt5gstreamerui %mklibname qt5gstreamerui %{api} %{major}
%define oldlibqt5gstreamerutils %mklibname qt5gstreamerutils %{api} %{major}
%define olddevnameQt5 %mklibname -d qt5-gstreamer

Summary:	C++ bindings for GStreamer with a Qt-style API
Name:		qt-gstreamer
Version:	1.2.0
Release:	20
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://gstreamer.freedesktop.org/wiki/QtGStreamer
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.xz
Source100:	qt-gstreamer.rpmlintrc
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
# CMake 4: get_target_property() on a missing target is an error
Patch103:	qt-gstreamer-cmake4-doxygen.patch
Patch104:	qt-gstreamer-qt6.patch

BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	boost-devel
BuildRequires:	qmake6
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api})
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6OpenGLWidgets)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)

%description
QtGStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt
applications.

#-------------------------------------------------------------------
%package -n %{qt6_name}
Summary: C++ bindings for GStreamer with a Qt6-style API
Group:   Development/KDE and Qt
Obsoletes: qt5-gstreamer < %{EVRD}

%description -n %{qt6_name}
Qt6GStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt6
applications.

%files -n %{qt6_name}
%{_libdir}/gstreamer-%{api}/libgstqt6videosink.so
%{_libdir}/qt6/qml/QtGStreamer/

#-------------------------------------------------------------------
%define libqt6glib %mklibname qt6glib 2.0 %{major}

%package -n %{libqt6glib}
Summary: C++/Qt6 bindings for parts of the GLib and GObject APIs
Group:   System/Libraries
Obsoletes: %{oldlibqt5glib} < %{EVRD}

%description -n %{libqt6glib}
Library providing C++/Qt6 bindings for parts of the GLib and GObject
APIs, a base on which Qt6GStreamer is built.

%files -n %{libqt6glib}
%{_libdir}/libQt6GLib-2.0.so.%{major}*
%{_libdir}/libQt6GLib-2.0.so.%{version}

#-------------------------------------------------------------------
%define libqt6gstreamer %mklibname qt6gstreamer %{api} %{major}

%package -n %{libqt6gstreamer}
Summary: C++/Qt6 bindings for GStreamer
Group:   System/Libraries
Obsoletes: %{oldlibqt5gstreamer} < %{EVRD}

%description -n %{libqt6gstreamer}
Library providing C++/Qt6 bindings for GStreamer

%files -n %{libqt6gstreamer}
%{_libdir}/libQt6GStreamer-%{api}.so.%{major}*
%{_libdir}/libQt6GStreamer-%{api}.so.%{version}

#-------------------------------------------------------------------
%define libqt6gstreamerquick %mklibname qt6gstreamerquick %{api} %{major}

%package -n %{libqt6gstreamerquick}
Summary: C++/Qt6 bindings for GStreamer
Group: System/Libraries
Obsoletes: %{oldlibqt5gstreamerquick} < %{EVRD}
%description -n %{libqt6gstreamerquick}
Library providing C++/Qt6 bindings for GStreamer

%files -n %{libqt6gstreamerquick}
%{_libdir}/libQt6GStreamerQuick-%{api}.so.%{major}*
%{_libdir}/libQt6GStreamerQuick-%{api}.so.%{version}

#-------------------------------------------------------------------
%define libqt6gstreamerui %mklibname qt6gstreamerui %{api} %{major}

%package -n %{libqt6gstreamerui}
Summary: Library providing integration with Qt6Gui
Group:   System/Libraries
Obsoletes: %{oldlibqt5gstreamerui} < %{EVRD}

%description -n %{libqt6gstreamerui}
Library providing integration with Qt6Gui.

%files -n %{libqt6gstreamerui}
%{_libdir}/libQt6GStreamerUi-%{api}.so.%{major}*
%{_libdir}/libQt6GStreamerUi-%{api}.so.%{version}

#-------------------------------------------------------------------
%define libqt6gstreamerutils %mklibname qt6gstreamerutils %{api} %{major}

%package -n %{libqt6gstreamerutils}
Summary: Library providing some high level utility classes
Group:   System/Libraries
Obsoletes: %{oldlibqt5gstreamerutils} < %{EVRD}

%description -n %{libqt6gstreamerutils}
Library providing some high level utility classes.

%files -n %{libqt6gstreamerutils}
%{_libdir}/libQt6GStreamerUtils-%{api}.so.%{major}*
%{_libdir}/libQt6GStreamerUtils-%{api}.so.%{version}

#--------------------------------------------------------------------
%define develnameQt6 %mklibname -d %{qt6_name}

%package -n %{develnameQt6}
Summary: Development files for Qt6Gstreamer
Group:   Development/KDE and Qt

Requires: %{libqt6glib} = %{EVRD}
Requires: %{libqt6gstreamer} = %{EVRD}
Requires: %{libqt6gstreamerquick} = %{EVRD}
Requires: %{libqt6gstreamerui} = %{EVRD}
Requires: %{libqt6gstreamerutils} = %{EVRD}
Requires: boost-devel
Provides: qt6-gstreamer-devel = %{EVRD}
Obsoletes: qt5-gstreamer-devel < %{EVRD}
Obsoletes: %{olddevnameQt5} < %{EVRD}

%description -n %{develnameQt6}
Qt6GStreamer provides C++ bindings for GStreamer with a Qt-style API,
plus some helper classes for integrating GStreamer better in Qt6
applications.

This package contains files for developing applications using
Qt6Gstreamer.

%files -n %{develnameQt6}
%doc %{_docdir}/%{name}/html
%{_includedir}/Qt6GStreamer
%{_libdir}/cmake/Qt6GStreamer/*.cmake
%{_libdir}/libQt6GLib-2.0.so
%{_libdir}/libQt6GStreamer-%{api}.so
%{_libdir}/libQt6GStreamerQuick-%{api}.so
%{_libdir}/libQt6GStreamerUi-%{api}.so
%{_libdir}/libQt6GStreamerUtils-%{api}.so
%{_libdir}/pkgconfig/Qt6GLib-2.0.pc
%{_libdir}/pkgconfig/Qt6GStreamer-%{api}.pc
%{_libdir}/pkgconfig/Qt6GStreamerQuick-%{api}.pc
%{_libdir}/pkgconfig/Qt6GStreamerUi-%{api}.pc
%{_libdir}/pkgconfig/Qt6GStreamerUtils-%{api}.pc

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
# C++17 removed the register keyword; clang treats remaining uses as errors.
export CXXFLAGS="%{optflags} -Wno-register"
%cmake -DQT_VERSION=6 -DQTGSTREAMER_EXAMPLES=OFF
%make_build
%make_build doc

%install
%make_install -C build
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a build/doc/html %{buildroot}%{_docdir}/%{name}/
