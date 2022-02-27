#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%define		pdir	Algorithm
%define		pnam	SVM
Summary:	Perl bindings for the libsvm Support Vector Machine library
Summary(pl.UTF-8):	Dowiązania Perla do biblioteki libsvm (Support Vector Machine)
Name:		perl-Algorithm-SVM
Version:	0.13
Release:	15
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	276ec1b341e05aa4c0353685f32ea4d5
URL:		http://search.cpan.org/dist/Algorithm-SVM/
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm::SVM implements a Support Vector Machine for Perl. Support
Vector Machines provide a method for creating classification functions
from a set of labeled training data, from which predictions can be
made for subsequent data sets.

%description -l pl.UTF-8
Moduł Algorithm::SVM jest implementacją Support Vector Machine dla
Perla. Support Vector Machines udostępniają sposób tworzenia funkcji
klasyfikujących ze zbioru oznaczonych danych treningowych, z których
można dokonywać przewidywań co do kolejnych zbiorów danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e 's/#include <errno.h>/#include <errno.h>\n#include <stdlib.h>\n#include <string.h>/g' bindings.cpp

%build
%{__perl} Makefile.PL \
	CCFLAGS="%{rpmcflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" \
	INSTALLDIRS=vendor

# cc1plus: warning: command line option "-Wdeclaration-after-statement" is valid for C/ObjC but not for C++
%{__sed} -i -e 's/-Wdeclaration-after-statement//' Makefile

%{__make} \
	CC="%{__cxx}" \
	OPTIMIZE="%{rpmcxxflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Algorithm/SVM/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Algorithm/*.pm
%{perl_vendorarch}/Algorithm/SVM
%dir %{perl_vendorarch}/auto/Algorithm/SVM
%{perl_vendorarch}/auto/Algorithm/SVM/*.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Algorithm/SVM/*.so
%{_mandir}/man3/*
