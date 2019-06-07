#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ffmpegthumbs
Version  : 19.04.2
Release  : 4
URL      : https://download.kde.org/stable/applications/19.04.2/src/ffmpegthumbs-19.04.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.2/src/ffmpegthumbs-19.04.2.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.2/src/ffmpegthumbs-19.04.2.tar.xz.sig
Summary  : FFmpeg-based thumbnail creator for video files
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: ffmpegthumbs-data = %{version}-%{release}
Requires: ffmpegthumbs-lib = %{version}-%{release}
Requires: ffmpegthumbs-license = %{version}-%{release}
Requires: ffmpegthumbs-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
%setup -q -n ffmpegthumbs-19.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559880612
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1559880612
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ffmpegthumbs
cp COPYING %{buildroot}/usr/share/package-licenses/ffmpegthumbs/COPYING
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/ffmpegthumbs/cmake_COPYING-CMAKE-SCRIPTS
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/ffmpegthumbs.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ffmpegthumbs/COPYING
/usr/share/package-licenses/ffmpegthumbs/cmake_COPYING-CMAKE-SCRIPTS

%files locales -f ffmpegthumbs.lang
%defattr(-,root,root,-)

