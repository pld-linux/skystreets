Summary:	Remake of SkyRoads game
Summary(pl):	Remake gry SkyRoads
Name:		skystreets
Version:	0.2.1
Release:	1
License:	Open Software License
Group:		Applications/Games
Source0:	http://skystreets.kaosfusion.com/%{name}_src_%{version}.tar.bz2
# Source0-md5:	-
Source1:	http://skystreets.kaosfusion.com/%{name}_data_%{version}.tar.bz2
# Source1-md5:	-
Patch0:		%{name}-Makefile.patch
URL:		http://skystreets.kaosfusion.com/
BuildRequires:	SDL-devel
BuildRequires:	OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remake of classic DOS game SkyRoads.

%description -l pl
Remake starej DOSowej gry SkyRoads.

%prep
%setup -q -n %{name} -b 1
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
   DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING CREDITS ChangeLog EDITOR LevelFormat README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
