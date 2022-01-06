# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define  _empty_manifest_terminate_build 0
Summary:	Ruby binding of ATK-1.0.x
Name:		rubygem-atk
Version:	3.4.9
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/atk-%{version}.gem
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(atk)
BuildRequires:	rubygem-native-package-installer
BuildRequires:	rubygem-rake
BuildRequires:  rubygem-pkg-config

Obsoletes:      ruby-atk

%description
Ruby binding of ATK-1.0.x.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
%gem_build

%install
%gem_install

%files
%{gem_files}

