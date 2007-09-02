%define name	horgand
%define version	1.07
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	FM organ synthesizer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://horgand.berlios.de
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libalsa-devel jackit-devel fltk-devel libsndfile-devel

%description
Horgand is a jack capable organ client with presets and some effects
incorporated. Horgand generates the sound in real time like a FM synthesizer.
You can change the frecuency of all the drawars and add some special effects.

%prep
%setup -q

%build
%configure
perl -p -i -e "s|-O6|$RPM_OPT_FLAGS||g" Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
cp man/%name.1 $RPM_BUILD_ROOT/%_mandir/man1
bzip2 $RPM_BUILD_ROOT/%_mandir/man1/%name.1
mkdir -p $RPM_BUILD_ROOT/%_bindir
%makeinstall_std PREFIX=%_prefix
rm -fr $RPM_BUILD_ROOT/%_docdir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="Horgand" longtitle="FM Organ Synthesizer" section="Multimedia/Sound"\
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Horgand
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Sequencer;
Encoding=UTF-8
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/%name
%{_datadir}/%name
%{_mandir}/man1/*
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
