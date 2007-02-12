Summary:	A Window Maker dock app which simplies managing mountable devices
Summary(pl.UTF-8):   Aplikacja dokowalna dla Window Makera do zarządzania urządzeniami mountowalnymi
Name:		mountapp
Version:	3.0
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/mountapp/%{name}-%{version}.tar.gz
# Source0-md5:	5e507a88e9144ce241a0d7261d4a1d68
Source1:	%{name}.desktop
Patch0:		%{name}-WINGs.patch
URL:		http://mountapp.sourceforge.net/
BuildRequires:	WindowMaker-devel >= 0.80
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
Obsoletes:	MountApp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Window Maker dock app which allows you to browse all your
mount points and to mount/unmount devices in a simple point and click
manner. Double clicking on the background will bring up a
configuration app written with GTK+.

%description -l pl.UTF-8
MountApp to aplikacja dokowalna Window Makera, pozwalająca przeglądać
punkty montowania i w prosty sposób (wskaż i kliknij) montować i
odmontowywać je. Podwójne kliknięcie wywoła w tle aplikację
konfigurującą napisaną w GTK+.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README THANKS AUTHORS NEWS ChangeLog 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mount.app
%{_desktopdir}/docklets/*.desktop
