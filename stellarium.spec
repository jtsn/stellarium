
%define title	Stellarium

Name:		stellarium 
Version:	0.11.4a
Release:	2
Summary:	Desktop planetarium 
Group:		Sciences/Astronomy
License:	GPLv2+
URL:		http://www.stellarium.org
Source0:	http://downloads.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glu) 
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	qt4-devel >= 3:4.4.1
BuildRequires:	gettext-devel
BuildRequires:	cmake
BuildRequires:	imagemagick

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.


%prep 
%setup -q -n %{name}-0.11.4

%build 
%cmake_qt4
%make

%install
cd build
make install DESTDIR=%{buildroot} INSTALL="%{_bindir}/install -c -p"
cd -

mkdir -p %{buildroot}%{_datadir}/applications

install -d -m 755 %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[1] \
    %{buildroot}%{_liconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[2] \
    %{buildroot}%{_iconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[4] \
    %{buildroot}%{_miconsdir}/stellarium.png

%find_lang %{name} %{name}-skycultures %{name}.lang

%files -f %{name}.lang 
#%{name}-skycultures.lang
%defattr(-,root,root,0755) 
%doc README COPYING AUTHORS 
%{_bindir}/%{name} 
%{_datadir}/%{name}
%{_mandir}/man1/*.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/stellarium.xpm
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
