#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ffmpegthumbs
Version  : 20.08.2
Release  : 18
URL      : https://download.kde.org/stable/release-service/20.08.2/src/ffmpegthumbs-20.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.2/src/ffmpegthumbs-20.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.2/src/ffmpegthumbs-20.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: ffmpegthumbs-data = %{version}-%{release}
Requires: ffmpegthumbs-lib = %{version}-%{release}
Requires: ffmpegthumbs-license = %{version}-%{release}
Requires: ffmpegthumbs-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavdevice)
BuildRequires : pkgconfig(libavfilter)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libswscale)
BuildRequires : qtbase-dev mesa-dev

%description
FFmpegthumbnailer is a lightweight video thumbnailer that can be used by file
managers to create thumbnails for your video files. The thumbnailer uses ffmpeg
o decode frames from the video files, so supported videoformats depend on the
configuration flags of ffmpeg.

%package data
Summary: data components for the ffmpegthumbs package.
Group: Data

%description data
data components for the ffmpegthumbs package.


%package lib
Summary: lib components for the ffmpegthumbs package.
Group: Libraries
Requires: ffmpegthumbs-data = %{version}-%{release}
Requires: ffmpegthumbs-license = %{version}-%{release}

%description lib
lib components for the ffmpegthumbs package.


%package license
Summary: license components for the ffmpegthumbs package.
Group: Default

%description license
license components for the ffmpegthumbs package.


%package locales
Summary: locales components for the ffmpegthumbs package.
Group: Default

%description locales
locales components for the ffmpegthumbs package.


%prep
%setup -q -n ffmpegthumbs-20.08.2
cd %{_builddir}/ffmpegthumbs-20.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602629859
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602629859
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ffmpegthumbs
cp %{_builddir}/ffmpegthumbs-20.08.2/COPYING %{buildroot}/usr/share/package-licenses/ffmpegthumbs/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/ffmpegthumbs-20.08.2/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/ffmpegthumbs/77976f406ba34009d9ba5a43b882fe6de68e5175
pushd clr-build
%make_install
popd
%find_lang ffmpegthumbs

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/ffmpegthumbnailersettings5.kcfg
/usr/share/kservices5/ffmpegthumbs.desktop
/usr/share/metainfo/org.kde.ffmpegthumbs.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/ffmpegthumbs.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ffmpegthumbs/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/ffmpegthumbs/77976f406ba34009d9ba5a43b882fe6de68e5175

%files locales -f ffmpegthumbs.lang
%defattr(-,root,root,-)

