#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Algorithm
%define		pnam	SVM
Summary:	Perl bindings for the libsvm Support Vector Machine library
Summary(pl):	Dowi±zania Perla do biblioteki libsvm (Support Vector Machine)
Name:		perl-Algorithm-SVM
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8524c3a26866460e8b7505d242f9b3d2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm::SVM implements a Support Vector Machine for Perl. Support
Vector Machines provide a method for creating classification functions
from a set of labeled training data, from which predictions can be
made for subsequent data sets.

%description -l pl
Modu³ Algorithm::SVM jest implementacj± Support Vector Machine dla
Perla. Support Vector Machines udostêpniaj± sposób tworzenia funkcji
klasyfikuj±cych ze zbioru oznaczonych danych treningowych, z których
mo¿na dokonywaæ przewidywañ co do kolejnych zbiorów danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Algorithm/*.pm
%{perl_vendorarch}/Algorithm/SVM
%dir %{perl_vendorarch}/auto/Algorithm/SVM
%{perl_vendorarch}/auto/Algorithm/SVM/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Algorithm/SVM/*.so
%{_mandir}/man3/*
