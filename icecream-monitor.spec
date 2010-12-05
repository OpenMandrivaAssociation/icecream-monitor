Name: icecream-monitor
Version: 1.0
Release: %mkrel 7
Summary: KDE4 GUI Monitor for icecream distributed compiled system
License: GPL
Url: http://en.opensuse.org/Icecream
Group: Graphical desktop/KDE
# Using Suse tarball
Source0: icemon.tar.bz2
Patch0: icemon.dif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: icecream-devel
BuildRequires: kdevplatform4-devel
BuildRequires: kde4-macros
Provides: icemon = %version-%release
Provides: icecream4-monitor = %version-%release
Obsoletes: icemon < 1.0-2

%description
KDE 4 GUI Monitor for icecream distributed compiled system

%files
%defattr(-,root,root,-)
%_kde_bindir/*
%_kde_appsdir/icemon
%_kde_iconsdir/*/*/*/icemon.*
%_kde_datadir/applications/kde4/icemon.desktop
%_kde_docdir/*/*/icemon
%_kde_appsdir/cmake/modules/FindIcecream.cmake

#-----------------------------------------------------------------

%prep
%setup -q -n %name
%patch0 -p0 -b .orig

%build
%cmake_kde4

%make

%install
rm -rf %buildroot

%makeinstall_std -C build

%clean
rm -rf %buildroot

