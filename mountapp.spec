Summary:	A Window Maker dock app which simplies managing mountable devices
Summary(pl):	Aplikacja dokowalna dla Window Makera do zarz±dzania urz±dzeniami mountowalnymi
Name:		mountapp
Version:	2.7
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://download.sourceforge.net/pub/sourceforge/%{name}-%{version}.tar.gz
URL:		http://mountapp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libPropList-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	MountApp


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
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README THANKS AUTHORS NEWS ChangeLog SMB-Notes
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mount.app
