%define	modname	Pod-POM

Summary:	POD Object Model
Name:		perl-%{modname}
Version:	2.01
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Pod::POM
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-POM-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Slurper)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(YAML::Any)
BuildRequires:	perl-devel

%description
This module implements a parser to convert Pod documents into a simple object
model form known hereafter as the Pod Object Model. The object model is
generated as a hierarchical tree of nodes, each of which represents a different
element of the original document. The tree can be walked manually and the nodes
examined, printed or otherwise manipulated. In addition, Pod::POM supports and
provides view objects which can automatically traverse the tree, or section
thereof, and generate an output representation in one form or another.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes TODO
%{_bindir}/*
%{perl_vendorlib}/Pod
%{_mandir}/man1/*
%{_mandir}/man3/*
