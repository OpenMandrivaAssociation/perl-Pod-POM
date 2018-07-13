%define	modname	Pod-POM
%define modver 2.01

Summary:	POD Object Model
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-POM-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes TODO
%{_bindir}/*
%{perl_vendorlib}/Pod
%{_mandir}/man1/*
%{_mandir}/man3/*
