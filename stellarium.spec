
%define title	Stellarium

Name:		stellarium 
Version:	0.10.6 
Release:	%mkrel 1
Summary:	Desktop planetarium 
Group:		Sciences/Astronomy
License:	GPLv2+
URL:		http://www.stellarium.org
Source:		http://downloads.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
Buildrequires:	mesaglu-devel 
Buildrequires:	SDL-devel
Buildrequires:	SDL_mixer-devel
Buildrequires:	png-devel
Buildrequires:	jpeg-devel
Buildrequires:	freetype2-devel
Buildrequires:	qt4-devel >= 3:4.4.1
BuildRequires:	gettext-devel
Buildrequires:	cmake
Buildrequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.


%prep 
%setup -q

%build 
%cmake_qt4
%make

%install
rm -rf %{buildroot}
cd build
make install DESTDIR=%{buildroot} INSTALL="%{_bindir}/install -c -p"
cd -

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=Desktop planetarium
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Science;Astronomy;Qt;
EOF

install -d -m 755 %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[1] \
    %{buildroot}%{_liconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[2] \
    %{buildroot}%{_iconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[4] \
    %{buildroot}%{_miconsdir}/stellarium.png

%find_lang %{name} %{name} stellarium-skycultures

%clean 
rm -rf %{buildroot} 

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc README COPYING AUTHORS 
%{_bindir}/%{name} 
%{_datadir}/%{name}
%{_mandir}/man1/*.1.*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
