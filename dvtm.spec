%global debug_package %{nil}

Name:		dvtm
Version:	0.15
Release:	1
Summary:	Tiling window management for the console
License:	MIT
Group:		Terminals
URL:		http://www.brain-dump.org/projects/dvtm/
Source0:	http://www.brain-dump.org/projects/dvtm/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)

%description
dvtm brings the concept of tiling window management, popularized by
X11-window managers like dwm to the console. As a console window manager
it tries to make it easy to work with multiple console based programs
like vim, mutt, cmus or irssi.

%prep
%setup -q

%build
sed -i 's/PREFIX.*local*/PREFIX\ =\ \/usr\//' config.mk
%make_build

%install
%__rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root)
%doc README* LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-status
%{_mandir}/man1/%{name}.1*



%changelog
* Sun Sep 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.8-1mdv2012.0
+ Revision: 816599
- update to 0.8

* Wed Dec 21 2011 Andrey Bondrov <abondrov@mandriva.org> 0.7-1
+ Revision: 744095
- New version 0.7, spec cleanup

* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.6-1
+ Revision: 645168
- update to new version 0.6

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-2mdv2011.0
+ Revision: 617916
- the mass rebuild of 2010.0 packages

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.2-1mdv2010.0
+ Revision: 402539
- update to new version 0.5.2

* Wed Feb 18 2009 Nicolas Vigier <nvigier@mandriva.com> 0.5.1-1mdv2009.1
+ Revision: 342550
- update to version 0.5.1

* Thu Oct 16 2008 Nicolas Vigier <nvigier@mandriva.com> 0.4.1-1mdv2009.1
+ Revision: 294198
- fix release tag, files list, requires, indentation
- import dvtm


* Wed Jul 10 2008 Sebastien Bocahu <zecrazytux@zecrazytux.net> 0.4.1-1mdv2008.1
- First realease of dvtm mandriva rpm package

