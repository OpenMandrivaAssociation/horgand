%define name	horgand
%define version	1.14
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	FM organ synthesizer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://horgand.berlios.de
License:	GPL
Group:		Sound
BuildRequires:	libalsa-devel jackit-devel fltk-devel libsndfile-devel
BuildRequires:	alsa-utils xpm-devel

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
%{_datadir}/applications/mandriva-%{name}.desktop

