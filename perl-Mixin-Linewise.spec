%define upstream_name    Mixin-Linewise

Name:		perl-%{upstream_name}
Version:	0.111
Release:	1

Summary:	Get linewise writers for strings and filenames
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Mixin::Linewise
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Mixin-Linewise-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(PerlIO::utf8_strict)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
It's boring to deal with opening files for IO, converting strings to
handle-like objects, and all that. With the Mixin::Linewise::Readers
manpage and the Mixin::Linewise::Writers manpage, you can just write a
method to handle handles, and methods for handling strings and filenames
are added for you.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*
