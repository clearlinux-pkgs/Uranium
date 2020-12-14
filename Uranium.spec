#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Uranium
Version  : 4.8
Release  : 26
URL      : https://github.com/Ultimaker/Uranium/archive/4.8/Uranium-4.8.tar.gz
Source0  : https://github.com/Ultimaker/Uranium/archive/4.8/Uranium-4.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: Uranium-data = %{version}-%{release}
Requires: Uranium-license = %{version}-%{release}
Requires: Uranium-python = %{version}-%{release}
Requires: Uranium-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : gettext-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qttools-dev

%description
Uranium
=======
Uranium is a Python framework for building 3D printing related applications.

%package data
Summary: data components for the Uranium package.
Group: Data

%description data
data components for the Uranium package.


%package license
Summary: license components for the Uranium package.
Group: Default

%description license
license components for the Uranium package.


%package python
Summary: python components for the Uranium package.
Group: Default
Requires: Uranium-python3 = %{version}-%{release}
Provides: uranium-python

%description python
python components for the Uranium package.


%package python3
Summary: python3 components for the Uranium package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Uranium package.


%prep
%setup -q -n Uranium-4.8
cd %{_builddir}/Uranium-4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606009353
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1606009353
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Uranium
cp %{_builddir}/Uranium-4.8/LICENSE %{buildroot}/usr/share/package-licenses/Uranium/b0285d2a104d4e90b17a2db8a713bd441745b793
pushd clr-build
%make_install
popd
## install_append content
for src in %{buildroot}/usr/lib64/python*/site-packages; do dest=$(sed 's!/usr/lib64/!/usr/lib/!' <<< ${src}); mkdir -p $(dirname ${dest}); mv ${src} $(dirname ${dest}); done
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/uranium/plugins/ConsoleLogger/ConsoleLogger.py
/usr/lib64/uranium/plugins/ConsoleLogger/__init__.py
/usr/lib64/uranium/plugins/ConsoleLogger/plugin.json
/usr/lib64/uranium/plugins/FileHandlers/OBJReader/OBJReader.py
/usr/lib64/uranium/plugins/FileHandlers/OBJReader/__init__.py
/usr/lib64/uranium/plugins/FileHandlers/OBJReader/plugin.json
/usr/lib64/uranium/plugins/FileHandlers/OBJReader/tests/TestOBJReader.py
/usr/lib64/uranium/plugins/FileHandlers/OBJReader/tests/sphere.obj
/usr/lib64/uranium/plugins/FileHandlers/OBJWriter/OBJWriter.py
/usr/lib64/uranium/plugins/FileHandlers/OBJWriter/__init__.py
/usr/lib64/uranium/plugins/FileHandlers/OBJWriter/plugin.json
/usr/lib64/uranium/plugins/FileHandlers/STLReader/STLReader.py
/usr/lib64/uranium/plugins/FileHandlers/STLReader/__init__.py
/usr/lib64/uranium/plugins/FileHandlers/STLReader/plugin.json
/usr/lib64/uranium/plugins/FileHandlers/STLReader/tests/TestStlReader.py
/usr/lib64/uranium/plugins/FileHandlers/STLReader/tests/simpleTestCubeASCII.stl
/usr/lib64/uranium/plugins/FileHandlers/STLReader/tests/simpleTestCubeBinary.stl
/usr/lib64/uranium/plugins/FileHandlers/STLWriter/STLWriter.py
/usr/lib64/uranium/plugins/FileHandlers/STLWriter/__init__.py
/usr/lib64/uranium/plugins/FileHandlers/STLWriter/plugin.json
/usr/lib64/uranium/plugins/FileLogger/FileLogger.py
/usr/lib64/uranium/plugins/FileLogger/__init__.py
/usr/lib64/uranium/plugins/FileLogger/plugin.json
/usr/lib64/uranium/plugins/LocalContainerProvider/LocalContainerProvider.py
/usr/lib64/uranium/plugins/LocalContainerProvider/__init__.py
/usr/lib64/uranium/plugins/LocalContainerProvider/plugin.json
/usr/lib64/uranium/plugins/LocalFileOutputDevice/LocalFileOutputDevice.py
/usr/lib64/uranium/plugins/LocalFileOutputDevice/LocalFileOutputDevicePlugin.py
/usr/lib64/uranium/plugins/LocalFileOutputDevice/__init__.py
/usr/lib64/uranium/plugins/LocalFileOutputDevice/plugin.json
/usr/lib64/uranium/plugins/Tools/CameraTool/CameraTool.py
/usr/lib64/uranium/plugins/Tools/CameraTool/__init__.py
/usr/lib64/uranium/plugins/Tools/CameraTool/plugin.json
/usr/lib64/uranium/plugins/Tools/CameraTool/tests/TestCameraTool.py
/usr/lib64/uranium/plugins/Tools/MirrorTool/MirrorTool.py
/usr/lib64/uranium/plugins/Tools/MirrorTool/MirrorToolHandle.py
/usr/lib64/uranium/plugins/Tools/MirrorTool/__init__.py
/usr/lib64/uranium/plugins/Tools/MirrorTool/plugin.json
/usr/lib64/uranium/plugins/Tools/RotateTool/RotateTool.py
/usr/lib64/uranium/plugins/Tools/RotateTool/RotateTool.qml
/usr/lib64/uranium/plugins/Tools/RotateTool/RotateToolHandle.py
/usr/lib64/uranium/plugins/Tools/RotateTool/__init__.py
/usr/lib64/uranium/plugins/Tools/RotateTool/plugin.json
/usr/lib64/uranium/plugins/Tools/RotateTool/tests/TestRotateTool.py
/usr/lib64/uranium/plugins/Tools/ScaleTool/ScaleTool.py
/usr/lib64/uranium/plugins/Tools/ScaleTool/ScaleTool.qml
/usr/lib64/uranium/plugins/Tools/ScaleTool/ScaleToolHandle.py
/usr/lib64/uranium/plugins/Tools/ScaleTool/__init__.py
/usr/lib64/uranium/plugins/Tools/ScaleTool/plugin.json
/usr/lib64/uranium/plugins/Tools/ScaleTool/tests/TestScaleTool.py
/usr/lib64/uranium/plugins/Tools/SelectionTool/SelectionTool.py
/usr/lib64/uranium/plugins/Tools/SelectionTool/__init__.py
/usr/lib64/uranium/plugins/Tools/SelectionTool/plugin.json
/usr/lib64/uranium/plugins/Tools/TranslateTool/TranslateTool.py
/usr/lib64/uranium/plugins/Tools/TranslateTool/TranslateTool.qml
/usr/lib64/uranium/plugins/Tools/TranslateTool/TranslateToolHandle.py
/usr/lib64/uranium/plugins/Tools/TranslateTool/__init__.py
/usr/lib64/uranium/plugins/Tools/TranslateTool/plugin.json
/usr/lib64/uranium/plugins/Tools/TranslateTool/tests/TestTranslateTool.py
/usr/lib64/uranium/plugins/UpdateChecker/UpdateChecker.py
/usr/lib64/uranium/plugins/UpdateChecker/UpdateCheckerJob.py
/usr/lib64/uranium/plugins/UpdateChecker/__init__.py
/usr/lib64/uranium/plugins/UpdateChecker/plugin.json
/usr/lib64/uranium/plugins/UpdateChecker/tests/TestUpdateCheckerJob.py
/usr/lib64/uranium/plugins/Views/SimpleView/SimpleView.py
/usr/lib64/uranium/plugins/Views/SimpleView/__init__.py
/usr/lib64/uranium/plugins/Views/SimpleView/plugin.json

%files data
%defattr(-,root,root,-)
/usr/share/cmake-3.19/Modules/UraniumTranslationTools.cmake
/usr/share/uranium/resources/bundled_packages/uranium.json
/usr/share/uranium/resources/i18n/cs_CZ/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/cs_CZ/uranium.po
/usr/share/uranium/resources/i18n/de_DE/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/de_DE/uranium.po
/usr/share/uranium/resources/i18n/es_ES/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/es_ES/uranium.po
/usr/share/uranium/resources/i18n/fi_FI/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/fi_FI/uranium.po
/usr/share/uranium/resources/i18n/fr_FR/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/fr_FR/uranium.po
/usr/share/uranium/resources/i18n/hu_HU/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/hu_HU/uranium.po
/usr/share/uranium/resources/i18n/it_IT/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/it_IT/uranium.po
/usr/share/uranium/resources/i18n/ja_JP/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/ja_JP/uranium.po
/usr/share/uranium/resources/i18n/ko_KR/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/ko_KR/uranium.po
/usr/share/uranium/resources/i18n/nl_NL/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/nl_NL/uranium.po
/usr/share/uranium/resources/i18n/pl_PL/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/pl_PL/uranium.po
/usr/share/uranium/resources/i18n/pt_BR/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/pt_BR/uranium.po
/usr/share/uranium/resources/i18n/pt_PT/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/pt_PT/uranium.po
/usr/share/uranium/resources/i18n/ru_RU/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/ru_RU/uranium.po
/usr/share/uranium/resources/i18n/tr_TR/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/tr_TR/uranium.po
/usr/share/uranium/resources/i18n/uranium.pot
/usr/share/uranium/resources/i18n/zh_CN/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/zh_CN/uranium.po
/usr/share/uranium/resources/i18n/zh_TW/LC_MESSAGES/uranium.mo
/usr/share/uranium/resources/i18n/zh_TW/uranium.po
/usr/share/uranium/resources/shaders/color.shader
/usr/share/uranium/resources/shaders/composite.shader
/usr/share/uranium/resources/shaders/default.shader
/usr/share/uranium/resources/shaders/object.shader
/usr/share/uranium/resources/shaders/platform.shader
/usr/share/uranium/resources/shaders/select_face.shader
/usr/share/uranium/resources/shaders/selection.shader
/usr/share/uranium/resources/shaders/toolhandle.shader

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Uranium/b0285d2a104d4e90b17a2db8a713bd441745b793

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
