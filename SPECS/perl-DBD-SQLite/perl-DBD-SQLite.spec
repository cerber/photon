# Got the intial spec from Fedora and modified it
Summary:        SQLite DBI Driver
Name:           perl-DBD-SQLite
Version:        1.48
Release:        1%{?dist}
Group:          Development/Libraries
License:        (GPL+ or Artistic) and Public Domain
URL:            http://search.cpan.org/dist/DBD-SQLite/
Source0:        http://search.cpan.org/CPAN/authors/id/I/IS/ISHIGAKI/DBD-SQLite-%{version}.tar.gz
%define sha1 DBD-SQLite=d2baa78384b0a05fb331c1873822263a2b04c0d8
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:  sqlite-autoconf
BuildRequires:  perl
BuildRequires:	perl-DBI
Requires:	perl-DBI
Requires:	perl

%description
SQLite is a public domain RDBMS database engine that you can find at
http://www.hwaci.com/sw/sqlite/.

This module provides a SQLite RDBMS module that uses the system SQLite 
libraries.

%prep
%setup -q -n DBD-SQLite-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f \( -name .packlist -o \
     -name '*.bs' -size 0 \) -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/DBD/
%{_mandir}/man3/*

%changelog
*	Thu Jan 21 2016 Anish Swaminathan <anishs@vmware.com> 1.48-1
-	Upgrade version
*	Fri Apr 3 2015 Divya Thaluru <dthaluru@vmware.com> 1.46-1
-	Initial version.
