%define upstream_name    Inline-Python
%define upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    Easy implementation of Python extensions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Inline/Inline-Python-%{upstream_version}.tar.gz

BuildRequires: perl(CGI)
BuildRequires: perl(Inline)
BuildRequires: perl-devel
BuildRequires: python-devel

%description
The 'Inline::Python' module allows you to put Python source code directly
"inline" in a Perl script or module. It sets up an in-process Python
interpreter, runs your code, and then examines Python's symbol table for
things to bind to Perl. The process of interrogating the Python interpreter
for globals only occurs the first time you run your Python code. The
namespace is cached, and subsequent calls use the cached version.

This document describes 'Inline::Python', the Perl package which gives you
access to a Python interpreter. For lack of a better place to keep it, it
also gives you instructions on how to use 'perlmodule', the Python package
which gives you access to the Perl interpreter.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
%makeinstall_std

%clean

%files
%doc README Changes
%{_mandir}/man3/*
%perl_vendorarch/Inline
%perl_vendorarch/auto/Inline


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.390.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.390.0-1
+ Revision: 644752
- update to new version 0.39

* Sun Mar 06 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.380.0-1
+ Revision: 642271
- remove check section for build success
- new version

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 0.37

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Thu Jul 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-2mdv2011.0
+ Revision: 556776
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2011.0
+ Revision: 552374
- update to 0.36

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 0.350.0-1mdv2010.1
+ Revision: 530433
- update to 0.35

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2010.1
+ Revision: 518483
- update to 0.34

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.1
+ Revision: 510095
- update to 0.33

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.320.0-1mdv2010.1
+ Revision: 498988
- update to 0.32

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.1
+ Revision: 474664
- update to 0.31

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.1
+ Revision: 472251
- update to 0.30

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2010.0
+ Revision: 410094
- rebuild using %%perl_convert_version

* Wed Jul 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2010.0
+ Revision: 393526
- update to new version 0.29

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.28-2mdv2009.1
+ Revision: 320142
- rebuild for new python

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2009.1
+ Revision: 315108
- update to new version 0.28

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2009.1
+ Revision: 305727
- update to new version 0.27

* Fri Nov 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2009.1
+ Revision: 305400
- reintroduction, as this new version works
- create perl-Inline-Python


* Mon Sep 19 2005 Pascal Terjan <pterjan@mandriva.org> 0.22-2mdk
- fix file list

* Tue Jan 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.22-1mdk
- 0.22
- Don't include Python.pod twice

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.21-3mdk
- Rebuild for new python

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.21-2mdk
- Rebuild for new perl

* Mon Aug 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.21-1mdk
- New version 0.21
- Add make test

* Mon Mar 01 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.20-7mdk
- rebuild
- own dir

* Fri Aug 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.20-6mdk
- rebuild for new python
- disable test

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.20-5mdk
- Use %%makeinstall_std now that it works on klama

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 0.20-4mdk
- Forgot DESTDIR on %%makeinstall

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 0.20-3mdk
- Fix install for new perl
- Macrofication
- Fix man path
- Unpackaged perllocal.pod

* Wed Jul 09 2003 Austin Acton <aacton@yorku.ca> 0.20-2mdk
- add some buildrequires and enable test

* Tue Jul 08 2003 Austin Acton <aacton@yorku.ca> 0.20-1mdk
- disable test until we can figure out why it fails
- from andi payn <payn@myrealbox.com> :
  - first specfile, based loosely on perl-Inline.spec



