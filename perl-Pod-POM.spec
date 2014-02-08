%define	upstream_name	 Pod-POM
%define upstream_version 0.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	POD Object Model
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(YAML::Any)
BuildRequires:	perl-devel

BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README TODO
%{_bindir}/*
%{perl_vendorlib}/Pod
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.270.0-4mdv2012.0
+ Revision: 765599
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.270.0-3
+ Revision: 764127
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.270.0-2
+ Revision: 667296
- mass rebuild

* Tue Apr 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.270.0-1mdv2011.0
+ Revision: 532159
- update to 0.27

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 404294
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2010.0
+ Revision: 371729
- update to new version 0.25
- update to new version 0.22

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.1
+ Revision: 354175
- update to new version 0.18

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.17-6mdv2009.0
+ Revision: 223999
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.17-5mdv2008.1
+ Revision: 180532
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-4mdv2007.0
+ Revision: 134335
- rebuild
- Import perl-Pod-POM

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-3mdk
- spec cleanup
- fix directory ownership
- %%mkrel
- better summary, description and url
- rpmbuildupdate aware
- enable test

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.17-2mdk
- rebuild for new perl

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.17-1mdk
- 0.17

