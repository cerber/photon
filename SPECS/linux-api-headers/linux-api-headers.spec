Summary:	Linux API header files
Name:		linux-api-headers
Version:	4.2.0
Release:	1%{?dist}
License:	GPLv2
URL:		http://www.kernel.org/
Group:		System Environment/Kernel
Vendor:		VMware, Inc.
Distribution: Photon
Source0:	http://www.kernel.org/pub/linux/kernel/v4.x/linux-4.2.tar.xz
%define sha1 linux=5e65d0dc94298527726fcd7458b6126e60fb2a8a
BuildArch:	noarch
%description
The Linux API Headers expose the kernel's API for use by Glibc.
%prep
%setup -q -n linux-4.2
%build
make mrproper
make headers_check
%install
cd %{_builddir}/linux-4.2
make INSTALL_HDR_PATH=%{buildroot}%{_prefix} headers_install
find /%{buildroot}%{_includedir} \( -name .install -o -name ..install.cmd \) -delete
%files
%defattr(-,root,root)
%{_includedir}/*
%changelog
*   Wed Dec 16 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 4.2.0-1
-   Upgrading kernel version to 4.2.0.
*   Wed Aug 12 2015 Sharath George <sharathg@vmware.com> 4.0.9-1
-   Upgrading kernel version.
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 3.13.3-1
-	Initial build. First version
