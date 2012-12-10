%define name	horgand
%define version	1.14
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	FM organ synthesizer
Version: 	%{version}
Release: 	%{release}
Source0:		%{name}-%{version}.tar.bz2
Patch0:		horgand-1.14-adopt-fltk.patch
URL:		http://horgand.berlios.de
License:	GPL
Group:		Sound
BuildRequires:	libalsa-devel jackit-devel fltk-devel pkgconfig(sndfile)
BuildRequires:	alsa-utils xpm-devel
buildrequires:	pkgconfig(cairo)
buildrequires:	pkgconfig(pixman-1)

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

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/%name
%{_datadir}/%name
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.14-7mdv2011.0
+ Revision: 611098
- rebuild

* Thu Jan 21 2010 Jérôme Brenier <incubusss@mandriva.org> 1.14-6mdv2010.1
+ Revision: 494769
- rebuild for new fltk

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 1.14-4mdv2009.1
+ Revision: 314146
- adopt to fltk dirname
- use configure2_5x

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.14-3mdv2009.0
+ Revision: 246881
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 15 2007 Emmanuel Andry <eandry@mandriva.org> 1.14-1mdv2008.1
+ Revision: 120410
- New version

* Tue Sep 04 2007 Emmanuel Andry <eandry@mandriva.org> 1.11-1mdv2008.0
+ Revision: 79479
- buildrequires xpm-devel
- buildrequires alsa-utils
- New version
- drop old menu
- Import horgand



* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 1.07-4mdv2007.0
- forgot xdg tag

* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 1.07-3mdv2007.0
- xdg menu

* Fri Jan 13 2006 Emmanuel Andry <eandry@free.fr> 1.07-2mdk
- rebuild
- %%mkrel

* Sat Mar 25 2005 Austin Acton <austin@mandrake.org> 1.07-1mdk
- from Emmanuel Andry <eandry@free.fr> :
  - 1.07

* Sun Jun 6 2004 Austin Acton <austin@mandrake.org> 1.06-2mdk
- rebuild

* Fri Feb 13 2004 Austin Acton <austin@mandrake.org> 1.06-1mdk
- 1.06

* Tue Jan 27 2004 Austin Acton <austin@mandrake.org> 1.05-2mdk
- new URL

* Mon Jan 19 2004 Austin Acton <austin@mandrake.org> 1.05-1mdk
- 1.05
- fix buildrequires for lib64
- buildrequires sndfile

* Sat Dec 27 2003 Austin Acton <austin@linx.ca> 1.04-1mdk
- 1.04

* Mon Jul 7 2003 Austin Acton <aacton@yorku.ca> 1.02-1mdk
- 1.02

* Mon Jun 23 2003 Austin Acton <aacton@yorku.ca> 1.01-1mdk
- 1.01
- use configure
- use makeinstall

* Thu Jun 19 2003 Austin Acton <aacton@yorku.ca> 1.0-1mdk
- 1.0

* Fri Jun 13 2003 Austin Acton <aacton@yorku.ca> 0.92-1mdk
- 0.92
- decapitalize name
- don't use compile.sh
- add manpage

* Wed Jun 4 2003 Austin Acton <aacton@yorku.ca> 0.91-1mdk
- initial package
