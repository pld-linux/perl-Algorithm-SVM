#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Algorithm
%define		pnam	SVM
Summary:	Perl bindings for the libsvm Support Vector Machine library
Summary(pl.UTF-8):	Dowiązania Perla do biblioteki libsvm (Support Vector Machine)
Name:		perl-Algorithm-SVM
Version:	0.11
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95a77fc32f958c745d596940a50b7682
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/auto/Algorithm/SVM/*.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Algorithm/SVM/*.so
%{_mandir}/man3/*
