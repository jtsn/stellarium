%define name	stellarium
%define version	0.9.0
%define release	%mkrel 1
%define title	Stellarium

Name:		%{name} 
Summary:	Stellarium is a desktop planetarium 
Version:	%{version} 
Release:	%{release} 
Source:		http://stellarium.sourceforge.net/download/%{name}-%{version}.tar.bz2
Source10:	%{name}.16.png.bz2
Source11:	%{name}.32.png.bz2
Source12:	%{name}.48.png.bz2
Patch0:		stellarium-0.8.2-manpage.diff
URL:		http://www.stellarium.org
Group:		Sciences/Astronomy
Buildrequires:	mesaglu-devel 
Buildrequires:	SDL-devel
Buildrequires:	SDL_mixer-devel
Buildrequires:	png-devel
Buildrequires:	jpeg-devel
Buildrequires:	freetype2-devel
Buildrequires:	qt4-devel
BuildRequires:	boost-devel
BuildRequires:	gettext-devel
Buildrequires:	cmake

BuildRoot:	%{_tmppath}/%{name}-buildroot 
License:	GPLv2 

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.


%prep 
%setup -q
%patch0 -p1 -b .manpage 

%build 
export QTDIR=/usr/lib/qt4
export PATH=$QTDIR/bin:$PATH
%cmake
%make


%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{_bindir}/install -c -p"

# Icons
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
bzcat %{SOURCE10} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE11} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE12} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=Desktop planetarium
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Science;Astronomy;
EOF
%find_lang %{name}

%clean 
rm -rf $RPM_BUILD_ROOT 


%files -f build/%{name}.lang
%defattr(-,root,root,0755) 
%doc README COPYING AUTHORS 
%{_bindir}/%{name} 
%{_datadir}/%{name}/
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus}



