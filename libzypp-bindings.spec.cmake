#
# spec file for package libzypp-bindings
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           @PACKAGE@
Version:        @VERSION@
Release:        0
License:        GPL
Group:          Development/Languages/Ruby
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake gcc-c++ ruby-devel swig
BuildRequires:  libzypp-devel >= 3.0.0
Requires:       libzypp >= 3.0.0
Source:         %{name}-%{version}.tar.bz2
Summary:        Language Bindings for libzypp
%description
Language Bindings for libzypp

 Authors:
----------
    Duncan Mac-Vicar P. <dmacvicar@suse.de>
    Klaus Kaempf <kkaempf@suse.de>

%prep
%setup -q

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DLIB=%{_lib} \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      ..
make %{?jobs:-j %jobs}

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/%{rb_ver}/%{rb_arch}/rzypp.so

%changelog -n ruby-zypp
