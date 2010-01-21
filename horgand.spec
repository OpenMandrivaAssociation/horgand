%define name	horgand
%define version	1.14
%define release %mkrel 6

Name: 	 	%{name}
Summary: 	FM organ synthesizer
Version: 	%{version}
Release: 	%{release}
Source:		%{name}-%{version}.tar.bz2
Patch0:		horgand-1.14-adopt-fltk.patch
URL:		http://horgand.berlios.de
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libalsa-devel jackit-devel fltk-devel libsndfile-devel
BuildRequires:	alsa-utils xpm-devel

%description
Horgand is a jack capable organ client with presets and some effects
incorporated. Horgand generates the sound in real time like a FM synthesizer.
You can change the frecuency of all the drawars and add some special effects.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
perl -p -i -e "s|-O6|$RPM_OPT_FLAGS||g" Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
%makeinstall_std PREFIX=%_prefix
rm -fr $RPM_BUILD_ROOT/%_docdir/%name

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Horgand
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Sequencer;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/%name
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
