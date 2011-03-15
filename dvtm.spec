%define name    dvtm 
%define version 0.6
%define release %mkrel 1
%define Summary Tiling window management for the console
Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        MIT
Group:          Terminals
URL:            http://www.brain-dump.org/projects/dvtm/
Source0:        http://www.brain-dump.org/projects/dvtm/%{name}-%{version}.tar.gz
BuildRoot:      %_tmppath/%name-buildroot
BuildRequires:	libncurses-devel libncursesw-devel
%description
dvtm brings the concept of tiling window management, popularized by
X11-window managers like dwm to the console. As a console window manager
it tries to make it easy to work with multiple console based programs
like vim, mutt, cmus or irssi.

%prep
%setup

%build
sed -i 's/PREFIX.*local*/PREFIX\ =\ \/usr\//' config.mk
%make

%install
%{__rm} -Rf %{buildroot}
%make DESTDIR=%buildroot install

%clean
%{__rm} -rf %buildroot

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-status
%{_mandir}/man1/%{name}.1*

