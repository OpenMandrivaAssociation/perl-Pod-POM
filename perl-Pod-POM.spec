%define	upstream_name	 Pod-POM
%define upstream_version 0.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	POD Object Model
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(YAML::Any)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements a parser to convert Pod documents into a simple object
model form known hereafter as the Pod Object Model. The object model is
generated as a hierarchical tree of nodes, each of which represents a different
element of the original document. The tree can be walked manually and the nodes
examined, printed or otherwise manipulated. In addition, Pod::POM supports and
provides view objects which can automatically traverse the tree, or section
thereof, and generate an output representation in one form or another.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot} 
%{makeinstall_std}

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README TODO
%{_bindir}/*
%{perl_vendorlib}/Pod
%{_mandir}/*/*
