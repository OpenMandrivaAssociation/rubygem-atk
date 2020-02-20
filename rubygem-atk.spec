# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	gem_name	atk

Summary:	Ruby binding of ATK-1.0.x
Name:		rubygem-%{gem_name}

Version:	3.4.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	rubygems-devel
BuildRequires:  rubygem(glib2)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(atk)
BuildRequires:	rubygem-native-package-installer
BuildRequires:  rubygem-gobject-introspection
Obsoletes:      ruby-atk

%description
Ruby binding of ATK-1.0.x.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_extdir_mri}

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

%files
%{gem_instdir}/lib/*.rb
%{gem_spec}
%{gem_cache}
%{gem_instdir}/[A-Z]*
%{gem_instdir}/dependency-check/*
%{gem_instdir}/*.gemspec
%{gem_instdir}/test/*.rb

%files doc
%doc %{gem_docdir}


