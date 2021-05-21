#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Merge
Version  : 0.08
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/J/JS/JSMITH/Algorithm-Merge-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JS/JSMITH/Algorithm-Merge-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libalgorithm-merge-perl/libalgorithm-merge-perl_0.08-3.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Algorithm-Merge-license = %{version}-%{release}
Requires: perl-Algorithm-Merge-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Algorithm::Diff)

%description
NAME
Algorithm::Merge - Three-way merge and diff
SYNOPSIS
use Algorithm::Merge qw(merge diff3 traverse_sequences3);

%package dev
Summary: dev components for the perl-Algorithm-Merge package.
Group: Development
Provides: perl-Algorithm-Merge-devel = %{version}-%{release}
Requires: perl-Algorithm-Merge = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-Merge package.


%package license
Summary: license components for the perl-Algorithm-Merge package.
Group: Default

%description license
license components for the perl-Algorithm-Merge package.


%package perl
Summary: perl components for the perl-Algorithm-Merge package.
Group: Default
Requires: perl-Algorithm-Merge = %{version}-%{release}

%description perl
perl components for the perl-Algorithm-Merge package.


%prep
%setup -q -n Algorithm-Merge-0.08
cd %{_builddir}
tar xf %{_sourcedir}/libalgorithm-merge-perl_0.08-3.debian.tar.xz
cd %{_builddir}/Algorithm-Merge-0.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Algorithm-Merge-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Algorithm-Merge
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Algorithm-Merge/19b171f4bdfdc6d15da5234a3c915c887decf9ab
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::Merge.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Algorithm-Merge/19b171f4bdfdc6d15da5234a3c915c887decf9ab

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Algorithm/Merge.pm
