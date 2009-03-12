%define	module	Pod-POM
%define	name	perl-%{module}
%define	version	0.18
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	POD Object Model
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Pod/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module implements a parser to convert Pod documents into a simple object
model form known hereafter as the Pod Object Model. The object model is
generated as a hierarchical tree of nodes, each of which represents a different
element of the original document. The tree can be walked manually and the nodes
examined, printed or otherwise manipulated. In addition, Pod::POM supports and
provides view objects which can automatically traverse the tree, or section
thereof, and generate an output representation in one form or another.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

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


