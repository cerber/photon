Summary:        Python cryptography library
Name:           python-cryptography
Version:        1.2.1
Release:        1%{?dist}
Url:            https://cryptography.io
License:        ASL 2.0
Group:          Development/Languages/Python
Source0:        https://pypi.python.org/packages/source/c/cryptography/cryptography-%{version}.tar.gz
%define sha1 cryptography=e6f0b8907588e972bb7e7c0541fa5c1d5451068d

BuildRequires: python2
BuildRequires: python2-libs
BuildRequires: python2-devel
BuildRequires: python-setuptools
Requires:      python-cffi
BuildRequires: python-cffi
BuildRequires: openssl-devel
Requires:      openssl

Requires:       python2
Requires:       python2-libs

%description
Cryptography is a Python library which exposes cryptographic recipes and primitives.


%prep
%setup -q -n cryptography-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
*	Thu Jan 21 2016 Anish Swaminathan <anishs@vmware.com> 1.2.1-1
-	Upgrade version
* 	Wed Nov 18 2015 Divya Thaluru <dthaluru@vmware.com> 1.1-1
- 	Initial packaging for Photon
