#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Algorithm
%define	pnam	SVM
Summary:	Perl bindings for the libsvm Support Vector Machine library
Summary(pl):	-
Name:		perl-Algorithm-SVM
Version:	0.06
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm::SVM implements a Support Vector Machine for Perl. Support
Vector Machines provide a method for creating classifcation functions
from a set of labeled training data, from which predictions can be
made for subsequent data sets.

%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

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
