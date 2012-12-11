%define upstream_name    Mixin-Linewise
%define upstream_version 0.003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Get linewise writeers for strings and filenames
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mixin/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Sub::Exporter)

BuildArch:	noarch

%description
It's boring to deal with opening files for IO, converting strings to
handle-like objects, and all that. With the Mixin::Linewise::Readers
manpage and the Mixin::Linewise::Writers manpage, you can just write a
method to handle handles, and methods for handling strings and filenames
are added for you.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.3.0-2mdv2011.0
+ Revision: 655047
- rebuild for updated spec-helper

* Mon Feb 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 506245
- update to 0.003

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.002-2mdv2010.0
+ Revision: 375941
- rebuild

* Wed Mar 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.002-1mdv2009.1
+ Revision: 360983
- import perl-Mixin-Linewise


* Tue Mar 24 2009 cpan2dist 0.002-1mdv
- initial mdv release, generated with cpan2dist

