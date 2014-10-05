# 
# spec file for package libzypp-bindings
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
# 
# nodebuginfo
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%if 0%{?suse_version}
%{!?ruby_vendorarch: %define ruby_vendorarch %(ruby -rrbconfig -e 'puts Config::CONFIG["vendorarchdir"] ')}
%else
%{!?ruby_vendorarch: %define ruby_vendorarch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"] ')}
%endif

Name:           libzypp-bindings
Version:        0.5.9.1
Release:        1.3
License:        GPL v2 or later
Summary:        Bindings for libzypp
Group:          Development/Sources
%if 0%{?suse_version}  
Vendor:    openSUSE  
%endif 
Source:         %{name}-%{version}.tar.gz
Patch1:         remove-perl-binding.patch
Patch2:         support-armv7-architectures.patch
Patch3:         Capabilities-iterator.patch
Patch4:         meego-add-more-class.patch

BuildRequires:  cmake gcc-c++ python-devel
BuildRequires:  swig >= 1.3.40
%if 0%{?suse_version} == 1140
BuildRequires:  libzypp-devel >= 8.13.2
%else
%if 0%{?suse_version} == 1130
BuildRequires:  libzypp-devel >= 7.9.11
%else
BuildRequires:  libzypp-devel
%endif
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides bindings for libzypp, the library for package management.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DPYTHON_SITEDIR=%{python_sitearch} \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      ..
make -j1

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean

%package -n python-zypp
Summary:        Python bindings for libzypp
Group:          Development/Languages/Python
%if 0%{?suse_version} == 1140
Requires:  libzypp >= 8.13.2
%else
%if 0%{?suse_version} == 1130
Requires:  libzypp >= 7.9.11
%endif
%endif
%description -n python-zypp
Python bindings of libzypp

%files -n python-zypp
%defattr(-,root,root,-)
%{python_sitearch}/_zypp.so
%{python_sitearch}/zypp.py*
