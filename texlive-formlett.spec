Name:		texlive-formlett
Version:	21480
Release:	1
Summary:	Letters to multiple recipients
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/formlett
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/formlett.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for multiple letters from the same basic source; the
package offers parametrisation of the letters actually sent.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/formlett/formlett.sty
%doc %{_texmfdistdir}/doc/generic/formlett/prog_manual.pdf
%doc %{_texmfdistdir}/doc/generic/formlett/prog_manual.tex
%doc %{_texmfdistdir}/doc/generic/formlett/user_manual.pdf
%doc %{_texmfdistdir}/doc/generic/formlett/user_manual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
