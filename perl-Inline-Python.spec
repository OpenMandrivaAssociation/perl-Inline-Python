%define realname   Inline-Python
%define version    0.28
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Easy implementation of Python extensions
Source:     http://www.cpan.org/modules/by-module/Inline/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRequires: perl-devel
BuildRequires: python-devel
BuildRequires: perl(CGI)
BuildRequires: perl(Inline)
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorarch/Inline
%perl_vendorarch/auto/Inline
