Summary:	A Window Maker dock app which simplies managing mountable devices
Summary(pl):	Aplikacja dokowalna dla Window Makera do zarz±dzania urz±dzeniami mountowalnymi
Name:		mountapp
Version:	2.7
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/%{name}-%{version}.tar.gz
URL:		http://mountapp.sourceforge.net/
BuildRequires:	libPropList-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	MountApp

%define		_prefix		/usr/X11R6

%description
This is a Window Maker dock app which allows you to browse all your
mount points and to mount/unmount devices in a simple point and click
manner. Double clicking on the background will bring up a
configuration app written with GTK+.

%description -l pl
MountApp to aplikacja dokowalna Window Makera, pozwalaj±ca przegl±daæ
punkty montowania i w prosty sposób (wska¿ i kliknij) montowaæ i
odmontowywaæ je. Podwójne klikniêcie w tle wywo³a aplikacje
konfiguruj±c± napisana w GTK+.

%prep
%setup -q

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf TODO README THANKS AUTHORS NEWS ChangeLog SMB-Notes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mount.app
