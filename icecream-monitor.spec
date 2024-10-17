Name: icecream-monitor
Version: 1.0
Release: 8
Summary: KDE4 GUI Monitor for icecream distributed compiled system
License: GPL
Url: https://en.opensuse.org/Icecream
Group: Graphical desktop/KDE
# Using Suse tarball
Source0: icemon.tar.bz2
Patch0: icemon.dif
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
export LDFLAGS="-lQtNetwork -ldl"
%cmake_kde4

%make

%install

%makeinstall_std -C build



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2011.0
+ Revision: 611170
- rebuild

* Sun Jan 17 2010 Anssi Hannula <anssi@mandriva.org> 1.0-6mdv2010.1
+ Revision: 492676
- fix icon (refresh icemon.dif from opensuse)
- fix buildrequires on kdevplatform4-devel

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - old directory, without matching package

  + Helio Chissini de Castro <helio@mandriva.com>
    - Raise release to crush old debug packages
    - New version to match current main icecream package
    - Back to original official name
    - New upstream tarball to match current icecream
    - Rebuild to cover missing package

* Tue Aug 26 2008 Helio Chissini de Castro <helio@mandriva.com> 0.1.svn852735-1mdv2009.0
+ Revision: 276218
- New kde4 version of icecream monitor
- import icemon


* Mon Sep 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-09-04 18:52:57 (59878)
- Old package based on icecream had 2 as epoch number, so needed raise epoch to 3

* Mon Sep 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-09-04 15:51:09 (59809)
- import icecream-monitor-0.1-1mdv2007.0

* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
- First separated package from main icecream

