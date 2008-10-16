%define name    dvtm 
%define version 0.4.1
%define release 1mdv2008.1
%define section Terminals
%define title   dvtm
%define Summary Tiling window management for the console
Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        MIT
Group:          %section
URL:            http://www.brain-dump.org/projects/dvtm/
Source0:        http://www.brain-dump.org/projects/dvtm/%{name}-%{version}.tar.gz
BuildRoot:      %_tmppath/%name-buildroot
BuildRequires:	libncurses-devel libncursesw-devel
Requires:	libncurses5 libncursesw5
%description
dvtm brings the concept of tiling window management, popularized by X11-window managers like dwm to the console. As a console window manager it tries to make it easy to work with multiple console based programs like vim, mutt, cmus or irssi.

%prep
%setup

%build
sed -i 's/PREFIX.*local*/PREFIX\ =\ \/usr\//' config.mk
%make unicode

%install
%make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

%files
/usr/*

