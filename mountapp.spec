Summary:	A Window Maker dock app which simplies managing mountable devices
Summary(pl):	Aplikacja dokowalna dla Window Makera do zarz±dzania urz±dzeniami mountowalnymi
Name:		mountapp
Version:	3.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/mountapp/%{name}-%{version}.tar.gz
# Source0-md5:	5e507a88e9144ce241a0d7261d4a1d68
Patch0:		%{name}-WINGs.patch
URL:		http://mountapp.sourceforge.net/
BuildRequires:	WindowMaker-devel >= 0.80
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
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
%patch0 -p1

%build
rm -f missing
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
%doc TODO README THANKS AUTHORS NEWS ChangeLog 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mount.app
