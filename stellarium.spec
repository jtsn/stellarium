%define name stellarium
%define version 0.8.2
%define release %mkrel 2
%define title Stellarium

Name: %{name} 
Summary: Stellarium is a desktop planetarium 
Version: %{version} 
Release: %{release} 
Source: http://stellarium.sourceforge.net/download/%{name}-%{version}.tar.bz2
Source10: %{name}.16.png.bz2
Source11: %{name}.32.png.bz2
Source12: %{name}.48.png.bz2
#Patch0:   stellarium-0.8.0-gcc41.patch.bz2		
Patch0: stellarium-0.8.2-manpage.diff
Patch1: stellarium-0.8.2-opengl_context_init.diff
Patch2: stellarium-0.8.2-64bit_fix.diff
URL: http://stellarium.sourceforge.net/
Group: Sciences/Astronomy
#Buildrequires: libxorg-x11-devel 
Buildrequires: mesaglu-devel 
Buildrequires: SDL-devel
Buildrequires: SDL_mixer-devel
Buildrequires: png-devel
Buildrequires: freetype2-devel
BuildRoot: %{_tmppath}/%{name}-buildroot 
License: GPL 

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.


%prep 
%setup -q
#%patch0 
%patch0 -p1 -b .manpage 
%patch1 -p1 -b .glcontext 
%patch2 -p1 -b .64bit 

%build 
%configure 
%make


%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall

# Icons
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}
bzcat %{SOURCE10} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE11} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE12} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

# Menu entry
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/%{name}" icon="stellarium.png" needs="X11" \
section="Applications/Sciences/Astronomy" title="Stellarium" longtitle="3D Planetarium" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title}
Comment=%{longtitle}
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Science;Astronomy;X-MandrivaLinux-MoreApplications-Sciences-Astronomy;
EOF

%find_lang %{name}

%clean 
rm -rf $RPM_BUILD_ROOT 


%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc README COPYING AUTHORS 
%{_bindir}/%{name} 
%{_datadir}/%{name}/
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/%{name}
%_mandir/man1/*

%post
%{update_menus}

%postun
%{clean_menus}



