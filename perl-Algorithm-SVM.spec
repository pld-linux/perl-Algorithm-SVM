#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Algorithm
%define		pnam	SVM
Summary:	Perl bindings for the libsvm Support Vector Machine library
Summary(pl):	-
Name:		perl-Algorithm-SVM
Version:	0.06
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9f0f648ea626c7912682cf3bd8d6411
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
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
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
%{perl_sitearch}/Algorithm/*.pm
%{perl_sitearch}/Algorithm/SVM
%dir %{perl_sitearch}/auto/Algorithm/SVM
%{perl_sitearch}/auto/Algorithm/SVM/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Algorithm/SVM/*.so
%{_mandir}/man3/*
