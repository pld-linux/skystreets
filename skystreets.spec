Summary:	Remake of SkyRoads game
Summary(pl):	Remake gry SkyRoads
Name:		skystreets
Version:	0.2.4
Release:	1
License:	Open Software License
Group:		Applications/Games
Source0:	http://skystreets.kaosfusion.com/%{name}-%{version}.tar.bz2
# Source0-md5:	63b572fef1b14590f3bb7b301787b6bc
URL:		http://skystreets.kaosfusion.com/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remake of classic DOS game SkyRoads.

%description -l pl
Remake starej DOS-owej gry SkyRoads.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO AUTHORS CODE NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
